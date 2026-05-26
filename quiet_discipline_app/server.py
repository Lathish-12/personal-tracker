import http.server
import socketserver
import json
import urllib.request
import urllib.parse
import sys

PORT = 8000

class QuietDisciplineHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Clean logging
        sys.stderr.write("%s - - [%s] %s\n" % (self.address_string(), self.log_date_time_string(), format%args))

    def do_POST(self):
        if self.path == '/api/github/token':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                # Parse client request body
                req_data = json.loads(post_data.decode('utf-8'))
                code = req_data.get('code', '').strip()
                client_id = req_data.get('client_id', '').strip()
                client_secret = req_data.get('client_secret', '').strip()
                
                if not code or not client_id or not client_secret:
                    self.send_error_response(400, "Missing required parameters (code, client_id, client_secret)")
                    return

                print(f"[OAuth] Received request: Client ID: '{client_id}' (len: {len(client_id)}), Secret len: {len(client_secret)}")

                # 1. Exchange OAuth code for an access token with GitHub
                token_url = "https://github.com/login/oauth/access_token"
                token_payload = urllib.parse.urlencode({
                    'client_id': client_id,
                    'client_secret': client_secret,
                    'code': code
                }).encode('utf-8')
                
                token_request = urllib.request.Request(
                    token_url,
                    data=token_payload,
                    headers={
                        'Accept': 'application/json',
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }
                )
                
                with urllib.request.urlopen(token_request) as response:
                    token_res = json.loads(response.read().decode('utf-8'))
                    
                access_token = token_res.get('access_token')
                if not access_token:
                    err_desc = token_res.get('error_description', 'Invalid client credentials or code expired')
                    print(f"[OAuth Error] Token exchange failed: {token_res}")
                    self.send_error_response(400, f"GitHub OAuth Error: {err_desc}")
                    return

                print("[OAuth] Access token received successfully from GitHub.")

                # 2. Fetch user profile information
                user_url = "https://api.github.com/user"
                user_request = urllib.request.Request(
                    user_url,
                    headers={
                        'Authorization': f'Bearer {access_token}',
                        'User-Agent': 'Quiet-Discipline-App',
                        'Accept': 'application/json'
                    }
                )
                
                with urllib.request.urlopen(user_request) as response:
                    user_profile = json.loads(response.read().decode('utf-8'))

                print(f"[OAuth] User profile fetched for username: {user_profile.get('login')}")

                # 3. Fetch private/verified user emails (in case profile email is empty)
                emails_url = "https://api.github.com/user/emails"
                emails_request = urllib.request.Request(
                    emails_url,
                    headers={
                        'Authorization': f'Bearer {access_token}',
                        'User-Agent': 'Quiet-Discipline-App',
                        'Accept': 'application/json'
                    }
                )
                
                try:
                    with urllib.request.urlopen(emails_request) as response:
                        emails = json.loads(response.read().decode('utf-8'))
                        
                    # Locate the primary email address
                    primary_email = None
                    for email_obj in emails:
                        if email_obj.get('primary'):
                            primary_email = email_obj.get('email')
                            break
                    
                    if primary_email:
                        user_profile['email'] = primary_email
                        print(f"[OAuth] Syncing primary email: {primary_email}")
                except Exception as e:
                    print(f"[OAuth Warning] Could not fetch private emails: {e}")

                # Send success response back to frontend client
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(user_profile).encode('utf-8'))

            except Exception as e:
                print(f"[OAuth Exception] Error occurred: {e}")
                self.send_error_response(500, f"Internal Server Exchange Error: {str(e)}")
        else:
            self.send_error_response(404, "Endpoint not found")

    def send_error_response(self, code, message):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({"error": message}).encode('utf-8'))

    def end_headers(self):
        # Support CORS pre-flight checks if required
        super().end_headers()

# Set up socket server reuse to avoid 'address already in use' errors on quick restarts
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    handler = QuietDisciplineHandler
    print(f"==================================================")
    print(f"[SERVER] QUIET DISCIPLINE WEB SERVER ACTIVATED")
    print(f"[URL] Local application hosted on: http://localhost:{PORT}")
    print(f"[API] Proxy token endpoint: http://localhost:{PORT}/api/github/token")
    print(f"==================================================")
    
    with ThreadedTCPServer(("", PORT), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server gracefully...")
            httpd.server_close()
            sys.exit(0)
