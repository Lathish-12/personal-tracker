---
name: Serene Habit
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#45464d'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#006b5f'
  on-secondary: '#ffffff'
  secondary-container: '#62fae3'
  on-secondary-container: '#007165'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#191c1e'
  on-tertiary-container: '#818486'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#62fae3'
  secondary-fixed-dim: '#3cddc7'
  on-secondary-fixed: '#00201c'
  on-secondary-fixed-variant: '#005047'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-max-width: 1120px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  stack-sm: 4px
  stack-md: 12px
  stack-lg: 24px
---

## Brand & Style

The design system is centered on the concept of "Quiet Discipline." It targets individuals seeking a focused, distraction-free environment to cultivate personal growth. The aesthetic is rooted in **Minimalism** with a **Modern Corporate** polish, emphasizing clarity over clutter to reduce cognitive load.

The interface should evoke a sense of calm, privacy, and steady progress. By using generous whitespace and a restricted color palette, the UI steps back to let the user’s data—their habits and streaks—take center stage. The emotional response should be one of quiet encouragement rather than frantic gamification.

## Colors

The palette is designed to be grounded and refreshing. 
- **Primary (Deep Slate):** Used for primary text, headers, and core brand elements to provide a professional, authoritative foundation.
- **Secondary (Soft Mint/Teal):** Reserved exclusively for positive actions, successful completions, and streak indicators. This color acts as the "reward" signal within the system.
- **Tertiary (Cloud White):** Used for surface backgrounds and container fills to maintain an airy, open feel.
- **Neutral (Slate Gray):** Used for secondary text, borders, and inactive states.

Backgrounds should remain predominantly white (#FFFFFF) to maximize the "breathability" of the interface.

## Typography

This design system utilizes **Hanken Grotesk** for headlines to provide a sharp, contemporary character that feels both architectural and approachable. **Inter** is used for all functional body text and UI labels due to its exceptional legibility and systematic feel.

Vertical rhythm is strictly enforced through a baseline grid. Large display sizes use tighter letter spacing to maintain visual cohesion, while smaller labels use increased tracking for better readability in metadata-heavy areas (like date pickers or streak counts).

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy on desktop to create a sense of focused containment, centering the user's focus on a single column or a simple dashboard layout. 

- **Desktop:** 12-column grid with a narrow 1120px max-width to prevent line lengths from becoming unreadable.
- **Tablet:** 8-column fluid grid with 24px margins.
- **Mobile:** Single column with 16px horizontal margins.

Spacing follows an 8px linear scale. Large sections of content (e.g., different habit categories) should be separated by substantial vertical padding (64px+) to reinforce the minimalist aesthetic and give the user's mind "room to breathe."

## Elevation & Depth

To maintain a clean and secure feel, this design system avoids heavy shadows. Depth is communicated primarily through **Tonal Layers** and **Low-Contrast Outlines**.

- **Level 0 (Background):** Pure white (#FFFFFF).
- **Level 1 (Cards/Containers):** Tertiary color (#F8FAFC) fill or a 1px border in a very light neutral (#E2E8F0).
- **Interactive Elevation:** On hover, cards may use an "Ambient Shadow"—a very soft, 10% opacity slate tint with a large 20px blur and no offset—to feel as if they are subtly lifting off the page.
- **Modals:** Use a heavy backdrop blur (12px) with a semi-transparent slate overlay (20% opacity) to maintain focus and imply a secure, private space.

## Shapes

The shape language is **Rounded**, balancing the professional tone of the typography with a friendly, encouraging feel.

- **Standard Buttons & Inputs:** 0.5rem (8px) corner radius.
- **Habit Cards:** 1rem (16px) corner radius for a softer, more protective appearance.
- **Streak Chips:** 1.5rem (24px) for a full-pill shape, making them feel like distinct, collectible badges of progress.

## Components

### Buttons
- **Primary:** Deep Slate background with white text. High-contrast and decisive.
- **Success (Completion):** Soft Mint background. Used for the daily "Check-off" action.
- **Ghost:** No background, slate border. Used for secondary actions like "Edit" or "Archive."

### Habit Cards
Cards should be "flat" by default with a subtle border. When a habit is marked complete, the card border should transition to Soft Mint, and a subtle Mint tint should fill the background to provide immediate visual satisfaction.

### Streak Indicators
Use a horizontal row of "Pill" shapes. Completed days are filled with Soft Mint; future days are a light neutral outline. Current day is Deep Slate to indicate focus.

### Input Fields
Inputs use a minimal bottom-border only or a very light 4-sided border. On focus, the border transitions to Deep Slate with a subtle 2px Mint "glow" (outer shadow) to indicate active engagement.

### Progress Bars
Thin, 4px height bars. The track is light gray (#F1F5F9) and the indicator is Soft Mint. No rounded ends on the progress fill to maintain a clean, precision-instrument look.