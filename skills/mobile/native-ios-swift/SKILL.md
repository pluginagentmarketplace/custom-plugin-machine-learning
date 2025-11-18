---
name: native-ios-swift
description: Develop native iOS apps using Swift and SwiftUI.
---

# Native iOS Development with Swift

## Quick Start

### SwiftUI View
```swift
import SwiftUI

struct ContentView: View {
    @State private var count = 0

    var body: some View {
        VStack {
            Text("Count: \(count)")
                .font(.headline)

            Button(action: { count += 1 }) {
                Text("Increment")
            }
        }
        .padding()
    }
}

#Preview {
    ContentView()
}
```

## Key Topics

- **SwiftUI**: Declarative UI framework
- **State Management**: @State, @Binding, @ObservedObject
- **Navigation**: NavigationStack, NavigationSplitView
- **Networking**: URLSession, Combine, async/await
- **Core Data**: Local data persistence
- **AsyncAwait**: Modern concurrency model
- **Performance**: View optimization, memory management
- **Testing**: XCTest, UI testing

## Best Practices

✅ Use SwiftUI for new projects
✅ Leverage Swift's type safety
✅ Use @State and @Binding properly
✅ Handle optionals carefully
✅ Test UI thoroughly
✅ Monitor memory usage
✅ Use async/await for concurrency

