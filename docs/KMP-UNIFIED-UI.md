# Kotlin Multiplatform (KMP) Unified Interface Approaches

> Last updated: January 2026
> Compose Multiplatform version: 1.9.x
> Kotlin version: 2.3.x

## Table of Contents

1. [Overview](#overview)
2. [Compose Multiplatform](#compose-multiplatform)
3. [Architecture Patterns](#architecture-patterns)
4. [State Management](#state-management)
5. [UI Components](#ui-components)
6. [Platform Integration](#platform-integration)
7. [Design System Implementation](#design-system-implementation)
8. [Shared UI vs Shared Logic](#shared-ui-vs-shared-logic)
9. [Performance Considerations](#performance-considerations)
10. [Testing Strategies](#testing-strategies)
11. [Best Practices](#best-practices)
12. [Official Documentation](#official-documentation)

---

## Overview

Kotlin Multiplatform (KMP) with Compose Multiplatform represents a production-ready solution for cross-platform UI development. It enables code sharing across Android, iOS, Desktop, and Web while maintaining flexibility for platform-specific implementations.

### Key Milestones (2025)

| Date | Milestone |
|------|-----------|
| May 2025 | Compose Multiplatform 1.8.0 - iOS reaches Stable |
| September 2025 | Compose Multiplatform 1.9.0 - Web reaches Beta |

### Code Sharing Statistics

Production apps demonstrate impressive reuse:
- **Logic sharing**: Up to 90% between Android and iOS
- **UI + Logic sharing**: 60-90% of total application code
- **Real-world examples**: Respawn (96% shared), Markaz, Wrike, Physics Wallah

---

## Compose Multiplatform

### Platform Support Status

| Platform | Status | Notes |
|----------|--------|-------|
| Android | Stable | Since inception |
| iOS | Stable | Since May 2025 (v1.8.0) |
| Desktop | Stable | Windows, macOS, Linux |
| Web | Beta | Since September 2025 (v1.9.0) |

### iOS-Specific Features

- Native scrolling physics matching iOS behavior
- Text editing with native selection and RTL support
- Drag-and-drop integration with system
- Accessibility (VoiceOver, AssistiveTouch, Full Keyboard Access)
- Native navigation gestures
- Adaptive UI respecting system settings

### Desktop Extensions

- Menu systems
- Keyboard shortcuts
- Window manipulation
- Notification management
- Hardware-accelerated UI rendering

### Web Capabilities (Beta)

- HTML interoperability
- Type-safe navigation with deep linking
- Accessibility for assistive technologies
- Cross-browser compatibility

---

## Architecture Patterns

### MVVM (Model-View-ViewModel)

**Characteristics:**
- Separate publishers for each piece of data
- Lower boilerplate compared to MVI
- Familiar to Android developers
- Works well with LiveData and StateFlow

**Best For:**
- Simpler UI components
- Teams transitioning from traditional Android development
- Moderate complexity applications

```kotlin
class MyViewModel : ViewModel() {
    private val _name = MutableStateFlow("")
    val name: StateFlow<String> = _name.asStateFlow()

    private val _email = MutableStateFlow("")
    val email: StateFlow<String> = _email.asStateFlow()

    fun updateName(value: String) { _name.value = value }
    fun updateEmail(value: String) { _email.value = value }
}
```

### MVI (Model-View-Intent)

**Core Components:**
1. **Model (State)**: Immutable UI state representation
2. **View (UI)**: Renders UI based on current state
3. **Intent**: Represents user actions

**Key Advantages:**
- Predictable state management
- Single source of truth
- Better scalability
- Prevents inconsistent states

**Best For:**
- Complex UIs with many state combinations
- Apps requiring strict state management
- Teams familiar with reactive programming

```kotlin
// State
data class MyState(
    val isLoading: Boolean = false,
    val data: List<Item> = emptyList(),
    val error: String? = null
)

// Intent
sealed class MyIntent {
    object LoadData : MyIntent()
    data class ItemClicked(val id: String) : MyIntent()
}

// ViewModel with MVI
class MyViewModel : ViewModel() {
    private val _state = MutableStateFlow(MyState())
    val state: StateFlow<MyState> = _state.asStateFlow()

    fun processIntent(intent: MyIntent) {
        when (intent) {
            is MyIntent.LoadData -> loadData()
            is MyIntent.ItemClicked -> handleItemClick(intent.id)
        }
    }

    private fun loadData() {
        viewModelScope.launch {
            _state.update { it.copy(isLoading = true) }
            try {
                val data = repository.fetchData()
                _state.update { it.copy(isLoading = false, data = data) }
            } catch (e: Exception) {
                _state.update { it.copy(isLoading = false, error = e.message) }
            }
        }
    }
}
```

### MVI Libraries for KMP

| Library | Description | Repository |
|---------|-------------|------------|
| Orbit MVI | Simple MVI framework | https://github.com/orbit-mvi/orbit-mvi |
| Fluxo | Supports MVI, MVVM+, Redux, TEA | https://github.com/fluxo-kt/fluxo |

---

## State Management

### StateFlow

A hot flow that holds and emits a read-only state with a single updatable value.

**Characteristics:**
- Always has a value (requires initial)
- Replay cache of size 1
- Hot flow (active independently of collectors)

**Usage:**

```kotlin
// ViewModel
class MyViewModel {
    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()

    fun loadData() {
        viewModelScope.launch {
            _uiState.value = UiState.Loading
            try {
                val data = repository.fetch()
                _uiState.value = UiState.Success(data)
            } catch (e: Exception) {
                _uiState.value = UiState.Error(e.message)
            }
        }
    }
}

// Compose UI
@Composable
fun MyScreen(viewModel: MyViewModel) {
    val state by viewModel.uiState.collectAsState()

    when (val currentState = state) {
        is UiState.Loading -> LoadingIndicator()
        is UiState.Success -> DataList(currentState.data)
        is UiState.Error -> ErrorMessage(currentState.message)
    }
}
```

### SharedFlow

A hot flow for broadcasting events to multiple consumers.

**Characteristics:**
- No initial value required
- Configurable replay cache
- Multiple collectors observe same values

**Usage:**

```kotlin
class MyViewModel {
    private val _events = MutableSharedFlow<UiEvent>()
    val events: SharedFlow<UiEvent> = _events.asSharedFlow()

    fun onButtonClick() {
        viewModelScope.launch {
            _events.emit(UiEvent.NavigateToDetails)
        }
    }
}
```

### Comparison

| Aspect | StateFlow | SharedFlow |
|--------|-----------|------------|
| State Holding | Always has value | No inherent state |
| Initial Value | Required | Not required |
| Replay Cache | Size 1 (latest) | Configurable |
| Use Case | UI state | One-time events |

---

## UI Components

### Material 3 in Compose Multiplatform

**Available Components:**
- Button, Checkbox, RadioButton, Switch
- TextField, OutlinedTextField
- Card, Surface
- Navigation components
- Dialog, AlertDialog
- AppBar (TopAppBar, BottomAppBar)

**Usage:**

```kotlin
@Composable
fun App() {
    MaterialTheme(
        colorScheme = lightColorScheme(),
        typography = Typography(),
        shapes = Shapes()
    ) {
        // App content
    }
}
```

### Platform-Specific Adaptations

#### iOS Text Input (1.9.0+)

```kotlin
// Platform-specific text input options
TextField(
    value = text,
    onValueChange = { text = it },
    modifier = Modifier.platformImeOptions(
        imeOptions = PlatformImeOptions(
            keyboardType = KeyboardType.Email,
            autoCorrection = AutoCorrection.No
        )
    )
)
```

#### Android-Only Components

Use `androidMain` source set for Android-specific UI:

```kotlin
// androidMain/kotlin/PlatformSpecific.kt
@Composable
actual fun PlatformSpecificView() {
    AndroidView(factory = { context ->
        // Create Android-specific view
    })
}
```

### Adaptive Layouts

```kotlin
@Composable
fun AdaptiveLayout() {
    val windowSizeClass = calculateWindowSizeClass()

    when (windowSizeClass.widthSizeClass) {
        WindowWidthSizeClass.Compact -> PhoneLayout()
        WindowWidthSizeClass.Medium -> TabletLayout()
        WindowWidthSizeClass.Expanded -> DesktopLayout()
    }
}
```

**Library:** `chrisbanes/material3-windowsizeclass-multiplatform`

---

## Platform Integration

### Expect/Actual Mechanism

Kotlin's approach to compile-time safe platform-specific implementations.

**Structure:**

```kotlin
// commonMain - Contract
expect fun getPlatformName(): String

expect class PlatformFile {
    fun readText(): String
}

// androidMain - Android Implementation
actual fun getPlatformName(): String = "Android"

actual class PlatformFile(private val file: File) {
    actual fun readText(): String = file.readText()
}

// iosMain - iOS Implementation
actual fun getPlatformName(): String = "iOS"

actual class PlatformFile(private val path: String) {
    actual fun readText(): String = NSString.stringWithContentsOfFile(path)
}
```

**When to Use:**
- Simple platform API wrappers
- Native code access with performance requirements
- Platform-specific constants

**When NOT to Use:**
- Complex UI logic
- When interfaces + DI would be clearer
- Large implementations

### SwiftUI Interop

#### Compose in SwiftUI

```swift
// SwiftUI wrapper for Compose content
struct ComposeView: UIViewControllerRepresentable {
    func makeUIViewController(context: Context) -> UIViewController {
        MainViewControllerKt.MainViewController()
    }

    func updateUIViewController(_ uiViewController: UIViewController, context: Context) {}
}

// Usage
struct ContentView: View {
    var body: some View {
        ComposeView()
            .ignoresSafeArea(.keyboard)
    }
}
```

#### SwiftUI in Compose

```kotlin
@Composable
fun SwiftUIMapView() {
    UIKitViewController(
        factory = {
            // Create UIHostingController with SwiftUI view
            SwiftUIMapViewControllerKt.createMapViewController()
        },
        update = { controller ->
            // Update if needed
        }
    )
}
```

### Android Native Views Integration

```kotlin
@Composable
fun WebViewContainer(url: String) {
    AndroidView(
        factory = { context ->
            WebView(context).apply {
                webViewClient = WebViewClient()
                loadUrl(url)
            }
        },
        update = { webView ->
            webView.loadUrl(url)
        }
    )
}
```

### WebView Libraries

| Library | Platforms | Repository |
|---------|-----------|------------|
| compose-webview-multiplatform | Android, iOS, Desktop | https://github.com/KevinnZou/compose-webview-multiplatform |
| compose-webview | Android, iOS, Desktop, Web | https://github.com/parkwoocheol/compose-webview |

---

## Design System Implementation

### Theme Architecture

```kotlin
// Common theme definition
@Composable
fun AppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
    val colorScheme = if (darkTheme) DarkColorScheme else LightColorScheme

    MaterialTheme(
        colorScheme = colorScheme,
        typography = AppTypography,
        shapes = AppShapes,
        content = content
    )
}

// Color schemes
private val LightColorScheme = lightColorScheme(
    primary = Color(0xFF6200EE),
    secondary = Color(0xFF03DAC6),
    background = Color(0xFFFFFFFF),
    surface = Color(0xFFFFFFFF),
    onPrimary = Color.White,
    onSecondary = Color.Black,
    onBackground = Color.Black,
    onSurface = Color.Black,
)

private val DarkColorScheme = darkColorScheme(
    primary = Color(0xFFBB86FC),
    secondary = Color(0xFF03DAC6),
    background = Color(0xFF121212),
    surface = Color(0xFF121212),
    onPrimary = Color.Black,
    onSecondary = Color.Black,
    onBackground = Color.White,
    onSurface = Color.White,
)
```

### Typography

```kotlin
val AppTypography = Typography(
    displayLarge = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 57.sp,
        lineHeight = 64.sp
    ),
    headlineMedium = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 28.sp,
        lineHeight = 36.sp
    ),
    bodyLarge = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 16.sp,
        lineHeight = 24.sp
    ),
    labelMedium = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Medium,
        fontSize = 12.sp,
        lineHeight = 16.sp
    )
)
```

### Custom Font Integration

```kotlin
// commonMain
expect val appFontFamily: FontFamily

// androidMain
actual val appFontFamily: FontFamily = FontFamily(
    Font(R.font.app_font_regular, FontWeight.Normal),
    Font(R.font.app_font_medium, FontWeight.Medium),
    Font(R.font.app_font_bold, FontWeight.Bold)
)

// iosMain
actual val appFontFamily: FontFamily = FontFamily(
    // iOS font loading
)
```

### CompositionLocal for Design Tokens

```kotlin
// Define dimension tokens
data class AppDimensions(
    val paddingSmall: Dp = 8.dp,
    val paddingMedium: Dp = 16.dp,
    val paddingLarge: Dp = 24.dp,
    val cornerRadius: Dp = 12.dp
)

val LocalAppDimensions = staticCompositionLocalOf { AppDimensions() }

// Provide in theme
@Composable
fun AppTheme(content: @Composable () -> Unit) {
    CompositionLocalProvider(
        LocalAppDimensions provides AppDimensions()
    ) {
        MaterialTheme(/* ... */) {
            content()
        }
    }
}

// Usage
@Composable
fun MyCard() {
    val dimensions = LocalAppDimensions.current
    Card(
        modifier = Modifier.padding(dimensions.paddingMedium),
        shape = RoundedCornerShape(dimensions.cornerRadius)
    ) {
        // Content
    }
}
```

---

## Shared UI vs Shared Logic

### Shared Logic Architecture (Recommended Start)

Share 60-90% of business logic, keep UI platform-specific.

**Module Structure:**

```
project/
  shared/
    src/
      commonMain/kotlin/
        domain/          # Entities, Use Cases
        data/            # Repositories, Data Sources
        network/         # API Clients
        util/            # Extensions, Helpers
      androidMain/kotlin/
      iosMain/kotlin/

  androidApp/            # Android UI (Jetpack Compose)
  iosApp/               # iOS UI (SwiftUI)
```

**What to Share (100%):**
- Domain models/entities
- Repository interfaces
- Use cases/business logic
- Network clients
- Database operations
- Validation logic

### Shared UI Architecture (Compose Multiplatform)

Maximum code reuse with consistent UX.

**Module Structure:**

```
project/
  shared/
    src/
      commonMain/kotlin/
        domain/
        data/
        ui/              # Shared Compose UI
          screens/
          components/
          theme/

  composeApp/           # Shared Compose entry point
  iosApp/               # iOS wrapper
  androidApp/           # Android wrapper
  desktopApp/           # Desktop wrapper
```

**Best For:**
- Apps with standard UI
- Startup/prototyping phase
- Consistency > native feel

### Hybrid Approach

Share what makes sense, keep the rest native.

```
project/
  shared/
    src/
      commonMain/kotlin/
        domain/
        data/
        ui/
          common/       # Shared simple screens

  composeApp/
    src/
      commonMain/kotlin/
        ui/
          shared/      # Compose UI for simple screens

  iosApp/
    SwiftUI/
      NativeScreens/   # Complex native iOS screens

  androidApp/
    compose/
      NativeScreens/   # Complex native Android screens
```

### Decision Framework

| Factor | Shared UI | Native UI |
|--------|-----------|-----------|
| UI Complexity | Standard | Complex platform-specific |
| Time to Market | Fast | Slower |
| Team Expertise | Kotlin | iOS/Android specialists |
| Native Feel | Acceptable | Critical |
| Code Reuse | 70-90% | 50-70% (logic only) |

---

## Performance Considerations

### Rendering Architecture

- **Graphics Engine**: Skia (2D graphics library)
- **iOS**: Skia with Metal or Core Graphics
- **Desktop**: Hardware-accelerated via Skia
- **Web**: Kotlin/Wasm compilation

### Performance Characteristics

- App startup comparable to pure native
- Scrolling on par with SwiftUI
- Binary size overhead: ~9 MB for Compose Multiplatform

### Optimization Best Practices

```kotlin
// Use remember for expensive calculations
@Composable
fun ExpensiveScreen(items: List<Item>) {
    val sortedItems = remember(items) {
        items.sortedBy { it.name }
    }
    // Use sortedItems
}

// Minimize recomposition with derivedStateOf
@Composable
fun SearchScreen(items: List<Item>, query: String) {
    val filteredItems by remember(items, query) {
        derivedStateOf {
            items.filter { it.name.contains(query) }
        }
    }
}

// Use stable keys for lists
LazyColumn {
    items(items, key = { it.id }) { item ->
        ItemRow(item)
    }
}
```

### Profiling Tools

| Platform | Tool |
|----------|------|
| Android | Android Profiler (Compose layout inspector) |
| iOS | Xcode Instruments (Metal debugging) |
| Desktop | Native OS profilers |
| Web | Browser DevTools |

---

## Testing Strategies

### Test Architecture

```
shared/src/
  commonTest/kotlin/    # Shared tests
  androidTest/kotlin/   # Android instrumented tests
  iosTest/kotlin/       # iOS-specific tests
```

### Unit Testing

```kotlin
// commonTest
class RepositoryTest {
    @Test
    fun `fetchData returns expected results`() = runTest {
        val repository = Repository(FakeDataSource())
        val result = repository.fetchData()
        assertEquals(expected, result)
    }
}
```

### Flow Testing with Turbine

```kotlin
@Test
fun `state updates correctly on load`() = runTest {
    val viewModel = MyViewModel()

    viewModel.state.test {
        assertEquals(UiState.Loading, awaitItem())

        viewModel.loadData()

        assertEquals(UiState.Success(data), awaitItem())
    }
}
```

### Compose UI Testing

```kotlin
@Test
fun buttonClickUpdatesState() {
    composeTestRule.setContent {
        MyScreen(viewModel)
    }

    composeTestRule
        .onNodeWithText("Click Me")
        .performClick()

    composeTestRule
        .onNodeWithText("Clicked!")
        .assertIsDisplayed()
}
```

### Key Testing Libraries

| Library | Purpose |
|---------|---------|
| `kotlin.test` | Core multiplatform testing |
| `kotlinx-coroutines-test` | Coroutine testing |
| `Turbine` | Flow testing |
| `Mockk` / `Mockative` | Mocking |

---

## Best Practices

### Project Architecture

1. **Clear Separation of Concerns**
   - Domain logic in shared module
   - Platform-specific code isolated
   - Dependency injection for flexibility

2. **Gradual Adoption**
   - Start with shared business logic
   - Add Compose UI incrementally
   - Transition one screen at a time

### State Management

1. **Use StateFlow for UI State**
   - Single source of truth
   - Works with `collectAsState()`

2. **Use SharedFlow for Events**
   - One-time events (navigation, dialogs)
   - Broadcasting to multiple observers

3. **Implement MVI or MVVM consistently**
   - MVI for complex state flows
   - MVVM for simpler logic

### Code Sharing Guidelines

| Category | Share? | Notes |
|----------|--------|-------|
| Domain Models | Yes (100%) | Always share |
| Business Logic | Yes (100%) | Always share |
| Network Code | Yes (100%) | Always share |
| Validation | Yes (100%) | Always share |
| UI Components | Consider | Use Compose or go native |
| Platform APIs | Partial | Use expect/actual |
| Hardware Access | No | Keep platform-specific |

### Dependency Injection

**Recommended:** Koin (easy multiplatform setup)

```kotlin
// commonMain
val appModule = module {
    single { Repository(get()) }
    factory { UseCase(get()) }
}

// Platform-specific modules
val platformModule = module {
    single<DataSource> { PlatformDataSource() }
}

// Usage
class MyViewModel(
    private val useCase: UseCase = get()
) : ViewModel() {
    // ...
}
```

---

## Official Documentation

### Core KMP Documentation

| Resource | URL |
|----------|-----|
| KMP Overview | https://kotlinlang.org/docs/multiplatform/kmp-overview.html |
| Quickstart | https://kotlinlang.org/docs/multiplatform/quickstart.html |
| Get Started | https://kotlinlang.org/docs/multiplatform/get-started.html |
| Project Wizard | https://kmp.jetbrains.com/ |
| Compatibility Guide | https://kotlinlang.org/docs/multiplatform/multiplatform-compatibility-guide.html |

### Compose Multiplatform

| Resource | URL |
|----------|-----|
| Create First App | https://kotlinlang.org/docs/multiplatform/compose-multiplatform-create-first-app.html |
| Official Site | https://www.jetbrains.com/compose-multiplatform/ |
| GitHub | https://github.com/JetBrains/compose-multiplatform |
| Releases | https://github.com/JetBrains/compose-multiplatform/releases |
| Platform Specifics | https://kotlinlang.org/docs/multiplatform/compose-platform-specifics.html |

### Advanced Topics

| Topic | URL |
|-------|-----|
| Expect/Actual | https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-expect-actual.html |
| Platform APIs | https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-connect-to-apis.html |
| SwiftUI Integration | https://kotlinlang.org/docs/multiplatform/compose-swiftui-integration.html |
| iOS Touch Handling | https://kotlinlang.org/docs/multiplatform/compose-ios-touch.html |
| Adaptive Layouts | https://kotlinlang.org/docs/multiplatform/compose-adaptive-layouts.html |
| Material 3 API | https://kotlinlang.org/api/compose-multiplatform/material3/ |

### Android Developers

| Resource | URL |
|----------|-----|
| KMP Guide | https://developer.android.com/kotlin/multiplatform |
| KMP Codelab | https://developer.android.com/codelabs/kmp-get-started |
| Material 3 Adaptive | https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive |

### State Management

| Resource | URL |
|----------|-----|
| StateFlow/SharedFlow | https://developer.android.com/kotlin/flow/stateflow-and-sharedflow |
| StateFlow API | https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-state-flow/ |

### Learning Resources

| Resource | URL |
|----------|-----|
| Learning Resources | https://kotlinlang.org/docs/multiplatform/kmp-learning-resources.html |
| Use Cases | https://kotlinlang.org/docs/multiplatform/use-cases-examples.html |
| Reasons to Try | https://kotlinlang.org/docs/multiplatform/multiplatform-reasons-to-try.html |

---

## IDE Requirements

| IDE | Version |
|-----|---------|
| IntelliJ IDEA | 2025.2.2+ |
| Android Studio | Otter 2025.2.1+ |
| Kotlin Plugin | Bundled or latest |

---

## Summary

Kotlin Multiplatform with Compose Multiplatform offers:

1. **Stability**: iOS stable (May 2025), Web in Beta (September 2025)
2. **Flexibility**: Share UI, logic, or both
3. **Performance**: Native-level with Skia rendering
4. **Ecosystem**: Rich library support, excellent tooling
5. **Production-Ready**: Proven by major companies

**Success Factors:**
- Clear architectural boundaries
- Appropriate code-sharing decisions
- Team experience with reactive programming
- Proper testing strategies
- Gradual adoption approach
