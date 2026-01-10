# IMPROVMENTS_ROADMAP

This roadmap turns the modern UI/UX improvement points into concrete, trackable work. It is organized into phases with clear outputs and acceptance criteria.

---

## Phase 0 — Foundations and Audit

**Goals**
- Establish baseline quality, design tokens, and platform parity.
- Identify gaps in the current skill data and docs.

**Tasks**
- Inventory existing guidance and data coverage (styles, components, navigation, accessibility, performance).
- Define token taxonomy: primitive → semantic → component.
- Decide platform scopes: iOS (SwiftUI/Liquid Glass), Android (Compose/Material 3), cross‑platform.

**Deliverables**
- Token taxonomy outline.
- Coverage matrix of current vs desired guidance.

**Acceptance Criteria**
- All domains mapped to token and component coverage.
- Clear list of missing rules and missing CSV entries.

---

## Phase 1 — Design Tokens + Theming

**Goals**
- Consistent dynamic theming across platforms.
- Semantic tokens drive UI decisions.

**Tasks**
- Add/extend token guidance in docs and CSVs (color, typography, spacing, elevation).
- Define dark mode + dynamic color strategy (Material 3 + iOS system colors).
- Provide token usage examples for SwiftUI and Compose.

**Deliverables**
- Updated tokens CSV entries.
- Token guidance section in `docs/MODERN-MOBILE-UIUX.md`.

**Acceptance Criteria**
- Token names are consistent across platforms.
- Dynamic color rules documented for Android 12+ and iOS system colors.

---

## Phase 2 — Motion and Interaction

**Goals**
- Motion feels intentional and accessible.
- Interactions are platform‑native.

**Tasks**
- Add motion rules: durations, easing, reduce‑motion fallback.
- Add gesture rules and alternatives (tap, swipe, long‑press).
- Add haptics guidance for key actions.

**Deliverables**
- New animation and gesture CSV entries.
- Motion guidance section in docs.

**Acceptance Criteria**
- All interactive components list a reduce‑motion alternative.
- Gesture‑only actions have button alternatives.

---

## Phase 3 — Information Hierarchy and Layout

**Goals**
- Faster comprehension and fewer steps.
- Clear primary/secondary actions.

**Tasks**
- Add hierarchy rules (glanceable → tappable → detailed).
- Add layout guidance for tabs, rails, and split panes.
- Ensure thumb‑zone placement for primary actions.

**Deliverables**
- Navigation and component CSV entries updated.
- Doc section on hierarchy and progressive disclosure.

**Acceptance Criteria**
- Primary action is always reachable in thumb zone.
- Larger screens use adaptive layouts (rail/split).

---

## Phase 4 — Accessibility and Input Efficiency

**Goals**
- Meet AA contrast, targets, and screen reader usability.
- Faster data entry and fewer errors.

**Tasks**
- Add a11y rules for charting, form validation, focus order.
- Add input guidance: autofill, keyboard types, inline validation.
- Add error recovery rules.

**Deliverables**
- Accessibility and forms CSV entries updated.
- Doc updates for a11y + input patterns.

**Acceptance Criteria**
- All interactive elements have labels.
- Touch targets are 44pt/48dp minimum.
- Forms validate inline with clear error recovery.

---

## Phase 5 — Loading, Empty States, and Trust

**Goals**
- Keep users oriented and confident during latency.
- Clear next steps for empty states.

**Tasks**
- Add loading patterns: skeleton, streaming, progressive.
- Add empty state rules with action.
- Add permission priming and privacy messaging guidance.

**Deliverables**
- Loading and error CSV entries updated.
- Doc section on trust + privacy cues.

**Acceptance Criteria**
- Every loading state has a fallback.
- Empty states always include a next action.

---

## Phase 6 — Performance and Quality

**Goals**
- Smooth scrolling, fast UI feedback, minimal jank.

**Tasks**
- Add performance rules: lazy lists, stable keys, memory‑safe images.
- Add profiling tips for iOS and Android.

**Deliverables**
- Performance CSV entries updated.
- Doc section on performance UX.

**Acceptance Criteria**
- Lists use lazy rendering with stable keys.
- Image loading guidance exists for both platforms.

---

## Implementation Checklist

- [ ] Update CSV datasets (tokens, components, navigation, accessibility, animation, loading, performance).
- [ ] Update `docs/MODERN-MOBILE-UIUX.md` with new sections.
- [ ] Update platform rules in `SKILL.md`.
- [ ] Mirror changes into `cli/assets` skill copies.
- [ ] Add version entry in `cli/src/commands/versions.ts`.

---

## Suggested Order of Execution

1. Tokens + theming
2. Motion + interaction
3. Hierarchy + layout
4. Accessibility + input
5. Loading + trust
6. Performance + polish
