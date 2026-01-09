# Google Material Design 3 (Material You) - Comprehensive Guide

> Last updated: January 2026
> Material Design 3 version: 1.4.0 (Jetpack Compose)

## Table of Contents

1. [Overview](#overview)
2. [Core Concepts](#core-concepts)
3. [Color System](#color-system)
4. [Typography Scale](#typography-scale)
5. [Shape System](#shape-system)
6. [Motion Principles](#motion-principles)
7. [Components](#components)
8. [Design Tokens](#design-tokens)
9. [Implementation](#implementation)
10. [Accessibility](#accessibility)
11. [Official Documentation](#official-documentation)

---

## Overview

Material Design 3 (M3), also known as Material You, is Google's latest design system that emphasizes personalization, accessibility, and cross-platform consistency. It introduces dynamic color extraction, refined typography, and an updated component library.

### Key Features

- **Dynamic Color**: Automatically generates color schemes from user wallpaper or content
- **Tonal Palettes**: Color system based on tonal values for better accessibility
- **Simplified Typography**: 15 type styles organized into 5 categories
- **Updated Components**: 30+ components with improved accessibility
- **Design Tokens**: 141+ system tokens for consistent theming

---

## Core Concepts

### Dynamic Color (Material You)

Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme automatically.

**Key Points:**
- Fully supported on Android 12+
- WCAG contrast standards met by default
- Available across web and Flutter
- Use Material Theme Builder for previewing

### Five Key Color Types

| Type | Purpose |
|------|---------|
| **Primary** | Prominent components (buttons, active states, elevated surfaces) |
| **Secondary** | Less prominent components (filter chips, secondary actions) |
| **Tertiary** | Contrasting accents balancing primary/secondary |
| **Neutral** | Surface and background tones |
| **Neutral Variant** | Additional emphasis levels |

---

## Color System

### Color Roles

Material 3 defines comprehensive color roles for consistent application:

#### Primary Roles
- `primary` - Primary brand color
- `on-primary` - Content color on primary
- `primary-container` - Container using primary
- `on-primary-container` - Content on primary container

#### Secondary Roles
- `secondary` - Secondary brand color
- `on-secondary` - Content color on secondary
- `secondary-container` - Container using secondary
- `on-secondary-container` - Content on secondary container

#### Tertiary Roles
- `tertiary` - Tertiary accent color
- `on-tertiary` - Content color on tertiary
- `tertiary-container` - Container using tertiary
- `on-tertiary-container` - Content on tertiary container

#### Surface Roles
- `surface` - Default surface color
- `surface-dim` - Dimmed surface variant
- `surface-bright` - Brightened surface variant
- `surface-container` - Standard container surface
- `surface-container-low` - Lower emphasis container
- `surface-container-high` - Higher emphasis container
- `on-surface` - Content on surface
- `on-surface-variant` - Secondary content on surface

#### Additional Roles
- `background` / `on-background` - App background
- `error` / `on-error` / `error-container` / `on-error-container` - Error states
- `outline` / `outline-variant` - Borders and dividers

### Dynamic Color Implementation (Android)

```kotlin
val dynamicColor = Build.VERSION.SDK_INT >= Build.VERSION_CODES.S
val colors = when {
    dynamicColor && darkTheme -> dynamicDarkColorScheme(LocalContext.current)
    dynamicColor && !darkTheme -> dynamicLightColorScheme(LocalContext.current)
    darkTheme -> DarkColorScheme
    else -> LightColorScheme
}
```

---

## Typography Scale

Material 3 simplifies typography into 5 categories with 3 sizes each (15 total styles):

### Display (Short, Important Text)

| Style | Size | Weight |
|-------|------|--------|
| Display Large | 57sp | Regular |
| Display Medium | 45sp | Regular |
| Display Small | 36sp | Regular |

### Headline (Short, High-Emphasis)

| Style | Size | Weight |
|-------|------|--------|
| Headline Large | 32sp | Regular |
| Headline Medium | 28sp | Regular |
| Headline Small | 24sp | Regular |

### Title (Medium-Emphasis)

| Style | Size | Weight |
|-------|------|--------|
| Title Large | 22sp | SemiBold |
| Title Medium | 16sp | Medium |
| Title Small | 14sp | Medium |

### Body (Main Content)

| Style | Size | Weight |
|-------|------|--------|
| Body Large | 16sp | Regular |
| Body Medium | 14sp | Regular (default) |
| Body Small | 12sp | Regular |

### Label (Buttons, Tabs)

| Style | Size | Weight |
|-------|------|--------|
| Label Large | 14sp | Medium |
| Label Medium | 12sp | Medium |
| Label Small | 11sp | Medium |

### Font Families

- **Display & Headline**: Google Sans
- **Body & Title**: Google Sans Text
- **Code**: Google Sans Mono
- **Web Fallback**: Roboto

### Implementation

```kotlin
val AppTypography = Typography(
    displayLarge = TextStyle(
        fontFamily = fontFamily,
        fontWeight = FontWeight.Normal,
        fontSize = 57.sp,
        lineHeight = 64.sp,
        letterSpacing = (-0.25).sp
    ),
    bodyMedium = TextStyle(
        fontFamily = fontFamily,
        fontWeight = FontWeight.Normal,
        fontSize = 14.sp,
        lineHeight = 20.sp,
        letterSpacing = 0.25.sp
    ),
    labelLarge = TextStyle(
        fontFamily = fontFamily,
        fontWeight = FontWeight.Medium,
        fontSize = 14.sp,
        lineHeight = 20.sp,
        letterSpacing = 0.1.sp
    )
)
```

---

## Shape System

### Corner Radius Scale

| Size | Radius | Use Case |
|------|--------|----------|
| Extra Small | 4dp | Small components (checkboxes) |
| Small | 8dp | Chips, small cards |
| Medium | 12dp | Cards, dialogs |
| Large | 16dp | Large cards, sheets |
| Extra Large | 28dp | FABs, large containers |

### Extended Sizes

- **Large Increased**: 20dp
- **Extra Large Increased**: 32dp
- **Full**: Circular (pill shapes)

### Implementation

```kotlin
val AppShapes = Shapes(
    extraSmall = RoundedCornerShape(4.dp),
    small = RoundedCornerShape(8.dp),
    medium = RoundedCornerShape(12.dp),
    large = RoundedCornerShape(16.dp),
    extraLarge = RoundedCornerShape(28.dp)
)
```

---

## Motion Principles

### Duration Guidelines

| Context | Duration |
|---------|----------|
| Mobile (larger animations) | 300-400ms |
| Mobile (smaller animations) | 150-200ms |
| Desktop | 150-200ms |

### Easing System (7 Curves)

1. **Standard**: Utility animations (start and end on-screen)
2. **Standard Accelerate**: Elements entering screen
3. **Standard Decelerate**: Elements exiting screen
4. **Emphasized**: M3-styled animations (start and end on-screen)
5. **Emphasized Accelerate**: M3-styled entering animations
6. **Emphasized Decelerate**: M3-styled exiting animations
7. **Custom**: Brand-specific with arc motion paths

### Transition Patterns

1. **Container Transform**: Seamless element-to-element transitions
2. **Shared Axis**: Navigation transitions
3. **Fade Through**: Unrelated element transitions
4. **Fade**: Simple opacity transitions

---

## Components

Material 3 includes 30+ major components:

### Buttons (5 Emphasis Levels)

| Button Type | Emphasis | Use Case |
|-------------|----------|----------|
| Filled | Highest | Primary actions (Save, Confirm) |
| Filled Tonal | Medium-High | Secondary actions with emphasis |
| Elevated | Medium | Actions needing background separation |
| Outlined | Medium | Important non-primary actions |
| Text | Lowest | Auxiliary actions |

```kotlin
// Filled (highest emphasis)
Button(onClick = { }) { Text("Save") }

// Tonal (medium emphasis)
FilledTonalButton(onClick = { }) { Text("Next") }

// Outlined (secondary)
OutlinedButton(onClick = { }) { Text("Cancel") }

// Text (lowest emphasis)
TextButton(onClick = { }) { Text("Learn more") }
```

### Navigation Components

| Component | Device | Destinations |
|-----------|--------|--------------|
| Navigation Bar | Mobile | 3-5 |
| Navigation Rail | Tablet/Landscape | 3-7 + optional FAB |
| Navigation Drawer | Large screens | Unlimited |

### Input Components

- **Text Fields**: Filled and Outlined variants
- **Checkboxes**: Multi-select options
- **Radio Buttons**: Single-select options
- **Switches**: Toggle on/off states
- **Sliders**: Value selection
- **Chips**: Assist, Filter, Input, Suggestion

### Container Components

- **Cards**: Elevated, Filled, Outlined
- **Dialogs**: Modal windows for decisions
- **Sheets**: Bottom sheets, side sheets
- **Menus**: Dropdown, context menus

### Feedback Components

- **Progress Indicators**: Linear, Circular
- **Snackbars**: Brief messages
- **Badges**: Notification counts

---

## Design Tokens

### Token Architecture (4 Levels)

1. **Reference Tokens**: Base values (colors, measurements)
2. **System Tokens**: Abstract semantic roles (~141 tokens)
3. **Component Tokens**: Component-specific values (800+ tokens)
4. **Theme Tokens**: Implementation-specific overrides

### Color Design Tokens

```css
/* System Color Tokens */
--md-sys-color-primary: #6442d6;
--md-sys-color-on-primary: #ffffff;
--md-sys-color-primary-container: #e9ddff;
--md-sys-color-surface: #fffbfe;
--md-sys-color-on-surface: #1c1b1f;
--md-sys-color-outline: #79747e;
```

### Typography Design Tokens

```css
/* System Typography Tokens */
--md-sys-typescale-display-large-font-family: "Google Sans";
--md-sys-typescale-display-large-font-size: 57px;
--md-sys-typescale-display-large-font-weight: 400;
--md-sys-typescale-display-large-line-height: 64px;
```

### Elevation Tokens

Material 3 uses **tonal elevation** (color overlays) instead of shadows:

```css
/* Shadow values (when needed) */
--md-sys-elevation-level1: 0px 1px 2px rgba(0,0,0,0.3), 0px 1px 3px 1px rgba(0,0,0,0.15);
--md-sys-elevation-level2: 0px 1px 2px rgba(0,0,0,0.3), 0px 2px 6px 2px rgba(0,0,0,0.15);
--md-sys-elevation-level3: 0px 1px 3px rgba(0,0,0,0.3), 0px 4px 8px 3px rgba(0,0,0,0.15);
```

---

## Implementation

### Android (Jetpack Compose)

**Dependencies (v1.4.0)**:

```kotlin
dependencies {
    implementation("androidx.compose.material3:material3:1.4.0")
    implementation("androidx.compose.material3:material3-window-size-class:1.4.0")
    implementation("androidx.compose.material3:material3-adaptive-navigation-suite:1.5.0-alpha11")
}
```

**Theme Setup**:

```kotlin
@Composable
fun AppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    dynamicColor: Boolean = true,
    content: @Composable () -> Unit
) {
    val colorScheme = when {
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
            val context = LocalContext.current
            if (darkTheme) dynamicDarkColorScheme(context)
            else dynamicLightColorScheme(context)
        }
        darkTheme -> DarkColorScheme
        else -> LightColorScheme
    }

    MaterialTheme(
        colorScheme = colorScheme,
        typography = AppTypography,
        shapes = AppShapes,
        content = content
    )
}
```

### Flutter

```dart
MaterialApp(
  theme: ThemeData(
    useMaterial3: true,
    colorScheme: ColorScheme.fromSeed(
      seedColor: Colors.blue,
      brightness: Brightness.light,
    ),
  ),
  home: MyHomePage(),
)
```

### Web (Material Web Components)

**Installation**:
```bash
npm install @material/web
```

**Usage**:
```html
<script src="https://cdn.jsdelivr.net/npm/@material/web"></script>

<md-filled-button>Primary Action</md-filled-button>
<md-outlined-button>Secondary Action</md-outlined-button>
<md-text-button>Tertiary Action</md-text-button>
```

---

## Accessibility

### WCAG Compliance

Material 3 maintains WCAG 2.1 compliance:

| Standard | Requirement |
|----------|-------------|
| Normal Text | 4.5:1 contrast (AA), 7:1 (AAA) |
| Large Text (24px+) | 3:1 contrast (AA), 4.5:1 (AAA) |
| UI Components | 3:1 minimum |

### Built-in Features

- **Dynamic Color**: Automatically meets contrast standards
- **Color Role Pairing**: Proper contrast ensured (primary/on-primary, etc.)
- **Touch Targets**: Minimum 48x48dp
- **Focus Indicators**: Clear, visible focus states
- **Screen Reader Support**: Semantic labels for TalkBack/VoiceOver

### Best Practices

```kotlin
// Screen reader support
IconButton(
    onClick = { },
    modifier = Modifier.semantics {
        contentDescription = "Add to favorites"
    }
) {
    Icon(Icons.Default.Favorite, contentDescription = null)
}

// Proper color usage
Text(
    "Important message",
    color = MaterialTheme.colorScheme.onSurface,
    style = MaterialTheme.typography.bodyLarge
)
```

---

## Official Documentation

### Primary Resources

| Resource | URL |
|----------|-----|
| Material Design 3 Home | https://m3.material.io/ |
| Get Started | https://m3.material.io/get-started |
| Foundations | https://m3.material.io/foundations |

### Style Guides

| Topic | URL |
|-------|-----|
| Color Roles | https://m3.material.io/styles/color/roles |
| Color System | https://m3.material.io/styles/color/the-color-system |
| Dynamic Color | https://m3.material.io/styles/color/dynamic/user-generated-source |
| Typography | https://m3.material.io/styles/typography/overview |
| Typography Tokens | https://m3.material.io/styles/typography/type-scale-tokens |
| Shape | https://m3.material.io/styles/shape/corner-radius-scale |
| Elevation | https://m3.material.io/styles/elevation/overview |
| Motion | https://m3.material.io/styles/motion/easing-and-duration |

### Components

| Component | URL |
|-----------|-----|
| All Components | https://m3.material.io/components |
| Buttons | https://m3.material.io/components/all-buttons |
| Navigation Bar | https://m3.material.io/components/navigation-bar/overview |
| Cards | https://m3.material.io/components/cards/guidelines |
| Dialogs | https://m3.material.io/components/dialogs |
| FAB | https://m3.material.io/components/floating-action-button/overview |
| Text Fields | https://m3.material.io/components/text-fields/accessibility |

### Platform Implementation

| Platform | URL |
|----------|-----|
| Android (Compose) | https://developer.android.com/develop/ui/compose/designsystems/material3 |
| Compose Material3 Releases | https://developer.android.com/jetpack/androidx/releases/compose-material3 |
| Web Components | https://material-web.dev/ |
| Material Web GitHub | https://github.com/material-components/material-web |
| Flutter Material | https://flutter.dev/design/material |

### Tools

| Tool | URL |
|------|-----|
| Material Theme Builder | https://m3.material.io/theme-builder |
| Theme Builder GitHub | https://github.com/material-foundation/material-theme-builder |
| Material Tokens (DSP) | https://github.com/material-foundation/material-tokens |

### Accessibility

| Topic | URL |
|-------|-----|
| Accessibility Overview | https://m3.material.io/foundations/overview/assistive-technology |
| Color Contrast | https://m3.material.io/foundations/designing/color-contrast |
| Accessible Design | https://m3.material.io/foundations/designing/structure |

---

## Version History

### v1.4.0 (September 2025)
- SecureTextField and OutlinedSecureTextField
- TextFieldState-based TextField
- AutoSize behavior for Text
- HorizontalCenteredHeroCarousel
- TimePicker with picker/input mode switching

### Performance Metrics
- 23% higher user engagement vs Material 2
- 15% better accessibility scores vs Material 2
