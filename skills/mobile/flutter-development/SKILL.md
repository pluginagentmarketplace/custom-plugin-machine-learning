---
name: flutter-development
description: Master Flutter for beautiful, high-performance mobile apps.
---

# Flutter & Dart Development

## Quick Start

### Flutter Widget
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Flutter')),
        body: const Center(child: Text('Hello Flutter!')),
      ),
    );
  }
}
```


## Production Code Examples

```bash
# Command line examples for quick start
# Replace with language-specific code
echo "Production code examples will be customized per skill"
```
        


### Advanced Patterns
- Pattern 1: Industry best practices
- Pattern 2: Error handling strategies
- Pattern 3: Performance optimization
- Pattern 4: Testing approaches
- Pattern 5: Deployment strategies
        


### Real-World Projects
1. **Beginner Project** (Level: Beginner)
   - Core concepts application
   - Basic requirements
   - Expected duration: 1-2 weeks

2. **Intermediate Project** (Level: Intermediate)
   - Multiple integrations
   - Advanced concepts
   - Expected duration: 3-4 weeks

3. **Advanced Project** (Level: Advanced)
   - Production-grade application
   - Complex architecture
   - Expected duration: 6-8 weeks
        

## Key Topics

- **Widgets**: StatelessWidget, StatefulWidget, CustomPaint
- **Flutter Architecture**: Widget tree, rendering pipeline
- **State Management**: Provider, Riverpod, GetX, BLoC
- **Navigation**: Navigator, GoRouter, deep linking
- **Networking**: HTTP, WebSockets, API integration
- **Performance**: Profiling, optimization, frame rates
- **Testing**: Unit tests, widget tests, integration tests
- **Deployment**: iOS and Android release process

## Best Practices

✅ Use const constructors
✅ Separate business logic from UI
✅ Use proper state management
✅ Optimize rebuilds
✅ Test thoroughly
✅ Use design patterns
✅ Handle errors gracefully

