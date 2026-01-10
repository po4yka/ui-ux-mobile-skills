# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

UI/UX Mobile is an AI-powered design intelligence toolkit providing searchable databases of mobile UI styles, color systems, typography scales, components, navigation patterns, gestures, accessibility guidelines, animations, onboarding patterns, forms, responsive layouts, error handling, design tokens, spacing systems, loading states, and performance patterns. It works as a skill for Claude Code and OpenAI Codex.

Supports:
- **iOS**: SwiftUI with iOS 26 Liquid Glass
- **Android**: Jetpack Compose with Material Design 3
- **Cross-platform**: Flutter, React Native, Kotlin Multiplatform (KMP)

## Search Command

```bash
python3 .claude/skills/ui-ux-mobile/scripts/search.py "<query>" --domain <domain> [-n <max_results>] [--platform <platform>] [--format <format>]
```

**Search options:**
- `--domain, -d` - Search domain(s), comma-separated for multi-domain
- `--platform, -p` - Filter by platform: `ios`, `android`, `cross-platform`
- `--format, -f` - Output format: `markdown`, `json`, `code-only`, `summary`
- `--max-results, -n` - Maximum results (default: 3)

**Available domains (16):**
- `style` - Visual styles by platform (Material You, Liquid Glass, minimal)
- `color` - Color palettes and systems (dynamic color, tonal palette)
- `typography` - Type scales and fonts (display, headline, body)
- `component` - UI components cross-platform (button, card, sheet)
- `navigation` - Navigation patterns (bottom nav, tab bar, drawer)
- `gesture` - Touch interactions (swipe, tap, haptic)
- `accessibility` - A11y guidelines (WCAG, VoiceOver, TalkBack)
- `animation` - Motion design (spring, ease, reduce motion)
- `onboarding` - User onboarding patterns (walkthrough, coach marks, progressive)
- `forms` - Form validation and inputs (validation, error state, multi-step)
- `responsive` - Tablet/foldable layouts (breakpoint, adaptive, grid)
- `errors` - Error handling patterns (retry, recovery, offline)
- `tokens` - Design token architecture (primitive, semantic, component)
- `spacing` - Spacing and sizing systems (padding, baseline grid, density)
- `loading` - Loading state patterns (skeleton, shimmer, progress)
- `performance` - UI performance optimization (lazy loading, caching)

**Stack search:**
```bash
python3 .claude/skills/ui-ux-mobile/scripts/search.py "<query>" --stack <stack>
```
Available stacks: `swiftui`, `jetpack-compose`, `flutter`, `react-native`, `kmp-compose`, `material3`, `liquid-glass`

## Architecture

```
ui-ux-mobile-skills/
├── .claude/skills/ui-ux-mobile/    # Claude Code skill
│   ├── SKILL.md                     # Skill definition
│   ├── scripts/
│   │   ├── search.py                # CLI entry point
│   │   └── core.py                  # BM25 search engine
│   └── data/                        # CSV databases (16 domains + 7 stacks)
├── .codex/skills/ui-ux-mobile/     # OpenAI Codex skill (mirror of Claude)
│   ├── SKILL.md
│   ├── scripts/
│   └── data/
├── cli/                            # Installation CLI tool
│   ├── src/                         # TypeScript source
│   └── assets/                      # Distribution assets
├── docs/                           # Research documentation
│   ├── MATERIAL3.md
│   ├── IOS26-LIQUID-GLASS.md
│   ├── KMP-UNIFIED-UI.md
│   └── MODERN-MOBILE-UIUX.md
├── CLAUDE.md                       # This file
└── README.md                       # Project overview
```

The search engine uses BM25 ranking. Domain auto-detection is available when `--domain` is omitted.

## Sync Rules

When modifying files, keep Claude and Codex skills in sync:

- **Data & Scripts**: Changes in `.claude/skills/ui-ux-mobile/` must be copied to:
  - `.codex/skills/ui-ux-mobile/`
  - `cli/assets/.claude/skills/ui-ux-mobile/`
  - `cli/assets/.codex/skills/ui-ux-mobile/`
- **SKILL.md**: Update both Claude and Codex versions (paths differ)

## Prerequisites

- Python 3.x (no external dependencies required for search)
- Node.js 18+ (for CLI tool development)

## Git Workflow

Never push directly to `main`. Always:

1. Create a new branch: `git checkout -b feat/...` or `fix/...`
2. Commit changes
3. Push branch: `git push -u origin <branch>`
4. Create PR: `gh pr create`
