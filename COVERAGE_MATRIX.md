# COVERAGE_MATRIX

Inventory of current guidance coverage in the skill data and docs.

---

## Data Domains (CSV)

| Domain | File | Rows | Platform Coverage Notes |
|--------|------|------|--------------------------|
| Accessibility | `accessibility.csv` | 52 | Unspecified platform tags (all rows lack Platform values) |
| Animation | `animations.csv` | 70 | Mostly Cross‑platform; some Material 3 and iOS 26 |
| Color | `colors.csv` | 50 | Cross‑platform with Android and iOS variants |
| Components | `components.csv` | 73 | Heavily Cross‑platform; minimal iOS/Android‑only |
| Errors | `errors.csv` | 32 | Cross‑platform only |
| Forms | `forms.csv` | 41 | Cross‑platform only |
| Gestures | `gestures.csv` | 41 | Cross‑platform with iOS/iPadOS variants |
| Loading | `loading.csv` | 29 | Mostly Cross‑platform; minimal iOS/Android |
| Navigation | `navigation.csv` | 37 | Mixed; many Cross‑platform + some platform‑specific |
| Onboarding | `onboarding.csv` | 30 | Cross‑platform only |
| Performance | `performance.csv` | 30 | Cross‑platform only |
| Responsive | `responsive.csv` | 35 | Cross‑platform with Android/iOS variants |
| Spacing | `spacing.csv` | 39 | Cross‑platform with Android/iOS variants |
| Styles | `styles.csv` | 43 | Mostly Cross‑platform; some iOS/Android and platform families |
| Tokens | `tokens.csv` | 45 | Cross‑platform only; semantic level |
| Typography | `typography.csv` | 61 | iOS + Material 3 dominant; some Android, Cross‑platform |

---

## Stack Guides (CSV)

| Stack | File | Rows |
|-------|------|------|
| SwiftUI | `stacks/swiftui.csv` | 35 |
| Jetpack Compose | `stacks/jetpack-compose.csv` | 33 |
| Material 3 | `stacks/material3.csv` | 33 |
| Flutter | `stacks/flutter.csv` | 19 |
| React Native | `stacks/react-native.csv` | 18 |
| KMP Compose | `stacks/kmp-compose.csv` | 18 |
| Liquid Glass | `stacks/liquid-glass.csv` | 18 |

---

## Documentation Coverage

- `docs/MATERIAL3.md` — Material Design 3 guide and tokens
- `docs/IOS26-LIQUID-GLASS.md` — iOS 26 Liquid Glass system
- `docs/KMP-UNIFIED-UI.md` — KMP architecture and UI
- `docs/MODERN-MOBILE-UIUX.md` — broad UX best practices

---

## Gaps to Address (Phase 1+)

- Accessibility domain lacks platform tagging; add iOS/Android specifics.
- Components skew cross‑platform; add platform‑specific entries for camera, sheets, navigation.
- Tokens are semantic only; add primitive + component tokens.
- Errors, forms, onboarding, performance are cross‑platform only; add platform specifics.
