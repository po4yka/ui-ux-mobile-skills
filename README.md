# UI/UX Mobile - Design Intelligence for Mobile Apps

AI-powered design intelligence toolkit for mobile UI/UX development. Provides searchable databases of styles, colors, typography, components, navigation, gestures, accessibility, animations, onboarding, forms, responsive layouts, errors, design tokens, spacing, loading states, and performance patterns.

## Supported AI Assistants

- **Claude Code** - Full skill support
- **OpenAI Codex** - Full skill support

## Supported Platforms

- **iOS**: SwiftUI with iOS 26 Liquid Glass
- **Android**: Jetpack Compose with Material Design 3
- **Cross-platform**: Flutter, React Native, Kotlin Multiplatform (KMP)

## Features

- **16 Search Domains**: style, color, typography, component, navigation, gesture, accessibility, animation, onboarding, forms, responsive, errors, tokens, spacing, loading, performance
- **7 Stack Guides**: SwiftUI, Jetpack Compose, Flutter, React Native, KMP, Material 3, Liquid Glass
- **Multi-domain Search**: Search across multiple domains with comma-separated values
- **Platform Filtering**: Filter results by ios, android, or cross-platform
- **Output Formats**: markdown, json, code-only, summary
- **Zero Dependencies**: Pure Python with BM25 search algorithm
- **CLI Installer**: Easy installation for Claude and Codex

## Installation

### Using CLI (Recommended)

```bash
# Install globally
npm install -g uipro-mobile

# Or use npx
npx uipro-mobile init

# Install for specific AI
uipro-mobile init --ai claude
uipro-mobile init --ai codex
uipro-mobile init --ai all
```

### Manual Installation

Copy the appropriate skill folder to your project:

```bash
# For Claude Code
cp -r .claude/skills/ui-ux-mobile /path/to/your/project/.claude/skills/

# For OpenAI Codex
cp -r .codex/skills/ui-ux-mobile /path/to/your/project/.codex/skills/
```

## Quick Start

### Search by Domain

```bash
# Search mobile styles
python3 .claude/skills/ui-ux-mobile/scripts/search.py "liquid glass" --domain style

# Search color systems
python3 .claude/skills/ui-ux-mobile/scripts/search.py "dynamic color" --domain color

# Search components
python3 .claude/skills/ui-ux-mobile/scripts/search.py "bottom sheet" --domain component

# Search accessibility
python3 .claude/skills/ui-ux-mobile/scripts/search.py "screen reader" --domain accessibility

# Search onboarding patterns
python3 .claude/skills/ui-ux-mobile/scripts/search.py "walkthrough" --domain onboarding

# Search responsive layouts
python3 .claude/skills/ui-ux-mobile/scripts/search.py "tablet" --domain responsive
```

### Advanced Search

```bash
# Multi-domain search
python3 .claude/skills/ui-ux-mobile/scripts/search.py "button" --domain component,animation

# Platform filtering
python3 .claude/skills/ui-ux-mobile/scripts/search.py "navigation" --domain navigation --platform ios

# Code-only output
python3 .claude/skills/ui-ux-mobile/scripts/search.py "glass" --stack swiftui --format code-only

# JSON output
python3 .claude/skills/ui-ux-mobile/scripts/search.py "validation" --domain forms --format json
```

### Search by Stack

```bash
# SwiftUI + Liquid Glass
python3 .claude/skills/ui-ux-mobile/scripts/search.py "glass effect" --stack swiftui

# Jetpack Compose + Material 3
python3 .claude/skills/ui-ux-mobile/scripts/search.py "state navigation" --stack jetpack-compose

# Flutter
python3 .claude/skills/ui-ux-mobile/scripts/search.py "theme provider" --stack flutter

# KMP Compose
python3 .claude/skills/ui-ux-mobile/scripts/search.py "expect actual" --stack kmp-compose
```

## Available Domains

| Domain | Description |
|--------|-------------|
| `style` | Visual styles by platform (Material You, Liquid Glass, minimal) |
| `color` | Color palettes and systems (dynamic color, tonal palette) |
| `typography` | Type scales and fonts (display, headline, body) |
| `component` | UI components cross-platform (button, card, sheet) |
| `navigation` | Navigation patterns (bottom nav, tab bar, drawer) |
| `gesture` | Touch interactions (swipe, tap, haptic) |
| `accessibility` | A11y guidelines (WCAG, VoiceOver, TalkBack) |
| `animation` | Motion design (spring, ease, reduce motion) |
| `onboarding` | User onboarding (walkthrough, coach marks, progressive) |
| `forms` | Form validation (error states, multi-step, submit) |
| `responsive` | Tablet/foldable layouts (breakpoint, adaptive, grid) |
| `errors` | Error handling (retry, recovery, offline, graceful degradation) |
| `tokens` | Design tokens (primitive, semantic, component, alias) |
| `spacing` | Spacing systems (padding, margin, baseline grid, density) |
| `loading` | Loading states (skeleton, shimmer, progress, streaming) |
| `performance` | UI optimization (lazy loading, caching, virtualization) |

## Available Stacks

| Stack | Focus |
|-------|-------|
| `swiftui` | iOS 26+, Liquid Glass, NavigationStack, @State |
| `jetpack-compose` | Material 3, NavHost, StateFlow, remember |
| `flutter` | Material/Cupertino, Navigator 2.0, Provider |
| `react-native` | React Navigation, FlatList, StyleSheet |
| `kmp-compose` | expect/actual, StateFlow, shared UI |
| `material3` | Color roles, typography, shape, elevation |
| `liquid-glass` | glassEffect, GlassEffectContainer, tinting |

## Documentation

Detailed research documentation available in `docs/`:

- **[Material Design 3](docs/MATERIAL3.md)** - Complete Material 3 guide
- **[iOS 26 Liquid Glass](docs/IOS26-LIQUID-GLASS.md)** - Liquid Glass design system
- **[KMP Unified UI](docs/KMP-UNIFIED-UI.md)** - Kotlin Multiplatform guide
- **[Modern Mobile UX](docs/MODERN-MOBILE-UIUX.md)** - Best practices guide

## Project Structure

```
ui-ux-mobile-skills/
├── .claude/skills/ui-ux-mobile/    # Claude Code skill
│   ├── SKILL.md                     # Skill definition
│   ├── scripts/                     # Search engine
│   └── data/                        # CSV databases
├── .codex/skills/ui-ux-mobile/     # OpenAI Codex skill
│   ├── SKILL.md
│   ├── scripts/
│   └── data/
├── cli/                            # CLI installer tool
│   ├── src/                         # TypeScript source
│   └── assets/                      # Distribution assets
└── docs/                           # Research documentation
```

## Requirements

- Python 3.x (for running search scripts)
- Node.js 18+ (for CLI tool, optional)

## License

MIT
