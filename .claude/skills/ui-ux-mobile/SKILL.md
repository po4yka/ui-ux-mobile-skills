---
name: ui-ux-mobile
description: "Mobile UI/UX design intelligence. Material Design 3, iOS 26 Liquid Glass, KMP Compose. 7 stacks (SwiftUI, Jetpack Compose, Flutter, React Native, KMP, Material 3, Liquid Glass). Actions: plan, build, create, design, implement, review, fix, improve, optimize mobile UI/UX code. Platforms: iOS, Android, cross-platform, KMP. Elements: button, navigation, tab bar, bottom sheet, card, list, form, dialog. Styles: Material You, Liquid Glass, minimal, dark mode, glassmorphism, adaptive. Topics: color palette, accessibility, animation, gesture, typography, spacing, haptic feedback, dynamic color."
---

# UI/UX Mobile - Design Intelligence for Mobile Apps

Searchable database of mobile UI styles, color systems, typography scales, components, navigation patterns, gestures, accessibility guidelines, and animations for iOS (SwiftUI, Liquid Glass), Android (Jetpack Compose, Material 3), and cross-platform (Flutter, React Native, KMP).

## Prerequisites

Check if Python is installed:

```bash
python3 --version || python --version
```

If Python is not installed, install it based on user's OS:

**macOS:**
```bash
brew install python3
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install python3
```

**Windows:**
```powershell
winget install Python.Python.3.12
```

---

## How to Use This Skill

When user requests mobile UI/UX work (design, build, create, implement, review, fix, improve), follow this workflow:

### Step 1: Analyze User Requirements

Extract key information from user request:
- **Platform**: iOS, Android, cross-platform, KMP
- **Design system**: Material 3, Liquid Glass, custom
- **Style keywords**: minimal, dark mode, glassmorphism, adaptive
- **Stack**: SwiftUI, Jetpack Compose, Flutter, React Native, KMP

### Step 2: Search Relevant Domains

Use `search.py` multiple times to gather comprehensive information. Search until you have enough context.

```bash
python3 .claude/skills/ui-ux-mobile/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

**Recommended search order:**

1. **Style** - Get visual style recommendations for the platform
2. **Component** - Get cross-platform component implementations
3. **Typography** - Get platform-specific type scales
4. **Color** - Get color palette (with dynamic color support info)
5. **Navigation** - Get navigation pattern recommendations
6. **Gesture** - Get touch interaction guidelines
7. **Animation** - Get motion design patterns
8. **Accessibility** - Get a11y requirements and implementations
9. **Stack** - Get stack-specific guidelines

### Step 3: Stack Guidelines

Search stack-specific best practices and implementation patterns.

```bash
python3 .claude/skills/ui-ux-mobile/scripts/search.py "<keyword>" --stack <stack>
```

Available stacks:
- `swiftui` - iOS 26+ with Liquid Glass
- `jetpack-compose` - Android with Material 3
- `flutter` - Cross-platform Flutter
- `react-native` - React Native patterns
- `kmp-compose` - Kotlin Multiplatform Compose
- `material3` - Material Design 3 reference
- `liquid-glass` - iOS 26 Liquid Glass reference

---

## Search Reference

### Available Domains

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `style` | Visual styles by platform | Material You, Liquid Glass, minimal, dark mode |
| `color` | Color palettes and systems | dynamic color, tonal palette, iOS system colors |
| `typography` | Type scales and fonts | display, headline, body, SF Pro, Roboto |
| `component` | UI components cross-platform | button, card, navigation bar, bottom sheet |
| `navigation` | Navigation patterns | bottom navigation, tab bar, drawer, stack |
| `gesture` | Touch interactions | swipe, tap, long press, pinch, haptic |
| `accessibility` | A11y guidelines | WCAG, VoiceOver, TalkBack, contrast, focus |
| `animation` | Motion design | spring, ease, transition, reduce motion |

### Available Stacks

| Stack | Focus |
|-------|-------|
| `swiftui` | iOS 26+, Liquid Glass, NavigationStack, @State |
| `jetpack-compose` | Material 3, NavHost, StateFlow, remember |
| `flutter` | Material/Cupertino, Navigator 2.0, Provider |
| `react-native` | React Navigation, FlatList, StyleSheet |
| `kmp-compose` | expect/actual, StateFlow, shared UI |
| `material3` | Color roles, typography, shape, elevation |
| `liquid-glass` | glassEffect, GlassEffectContainer, tinting |

---

## Example Workflows

### iOS App with Liquid Glass

```bash
# 1. Search style for iOS 26
python3 .claude/skills/ui-ux-mobile/scripts/search.py "liquid glass iOS" --domain style

# 2. Search navigation patterns
python3 .claude/skills/ui-ux-mobile/scripts/search.py "bottom navigation iOS" --domain navigation

# 3. Search components
python3 .claude/skills/ui-ux-mobile/scripts/search.py "button sheet dialog" --domain component

# 4. Search Liquid Glass stack guidelines
python3 .claude/skills/ui-ux-mobile/scripts/search.py "glass effect grouping" --stack liquid-glass

# 5. Search SwiftUI implementation
python3 .claude/skills/ui-ux-mobile/scripts/search.py "state navigation" --stack swiftui
```

### Android App with Material 3

```bash
# 1. Search Material 3 style
python3 .claude/skills/ui-ux-mobile/scripts/search.py "material you dynamic" --domain style

# 2. Search color system
python3 .claude/skills/ui-ux-mobile/scripts/search.py "dynamic color android" --domain color

# 3. Search typography
python3 .claude/skills/ui-ux-mobile/scripts/search.py "headline body" --domain typography

# 4. Search Material 3 stack guidelines
python3 .claude/skills/ui-ux-mobile/scripts/search.py "color button" --stack material3

# 5. Search Jetpack Compose implementation
python3 .claude/skills/ui-ux-mobile/scripts/search.py "state navigation" --stack jetpack-compose
```

### Cross-Platform KMP App

```bash
# 1. Search adaptive style
python3 .claude/skills/ui-ux-mobile/scripts/search.py "adaptive cross-platform" --domain style

# 2. Search components
python3 .claude/skills/ui-ux-mobile/scripts/search.py "button navigation" --domain component

# 3. Search KMP implementation
python3 .claude/skills/ui-ux-mobile/scripts/search.py "expect actual" --stack kmp-compose

# 4. Search accessibility
python3 .claude/skills/ui-ux-mobile/scripts/search.py "screen reader" --domain accessibility
```

---

## Platform-Specific Rules

### iOS (SwiftUI + Liquid Glass)

| Rule | Do | Don't |
|------|----|----- |
| **Glass usage** | Use glass for navigation and controls | Apply glass to content layers |
| **Glass grouping** | Use GlassEffectContainer for related elements | Let glass sample other glass |
| **Tab bar** | Use system TabView (floating in iOS 26) | Force custom bottom navigation |
| **State** | Use @State, @StateObject, @ObservedObject correctly | Use @ObservedObject to create objects |
| **Animation** | Use spring animations with reduce motion check | Ignore prefers-reduced-motion |

### Android (Jetpack Compose + Material 3)

| Rule | Do | Don't |
|------|----|----- |
| **Color** | Use MaterialTheme.colorScheme roles | Hardcode hex colors |
| **Dynamic color** | Check SDK >= 31 for dynamic color | Force dynamic color on older devices |
| **Typography** | Use MaterialTheme.typography tokens | Define custom text sizes |
| **State** | Use remember, rememberSaveable, StateFlow | Use remember for data that must survive rotation |
| **Lists** | Use LazyColumn with stable keys | Use Column with items for long lists |

### Cross-Platform

| Rule | Do | Don't |
|------|----|----- |
| **Touch targets** | 48dp minimum on Android, 44pt on iOS | Smaller touch targets |
| **Accessibility** | Test with TalkBack AND VoiceOver | Test on one platform only |
| **Navigation** | Use platform navigation patterns | Force same navigation on all platforms |
| **Gestures** | Provide button alternatives for gestures | Require gestures without alternatives |

---

## Pre-Delivery Checklist

### Platform Consistency
- [ ] Uses platform design language (Material 3 / Liquid Glass)
- [ ] Typography follows platform type scale
- [ ] Color system uses platform color roles
- [ ] Navigation follows platform patterns

### Accessibility
- [ ] All interactive elements have accessibility labels
- [ ] Minimum 4.5:1 color contrast for text
- [ ] Touch targets are 48dp (Android) / 44pt (iOS) minimum
- [ ] Reduce motion preference respected
- [ ] Tested with VoiceOver (iOS) / TalkBack (Android)

### Animation
- [ ] Spring animations for natural feel
- [ ] Reduce motion alternative provided
- [ ] Durations: 150-200ms for small, 300-400ms for large
- [ ] No flashing content (seizure risk)

### Performance
- [ ] Lazy loading for long lists
- [ ] Memoization for expensive computations
- [ ] Stable keys for list items
- [ ] Minimal state scope

---

## Tips for Better Results

1. **Specify platform** - "iOS button" > "button" for platform-specific results
2. **Search multiple domains** - Style + Component + Stack = Complete implementation
3. **Check accessibility** - Always search accessibility for any interactive element
4. **Use stack search** - Get implementation-specific code patterns
5. **Combine results** - Synthesize multiple searches for complete guidance
