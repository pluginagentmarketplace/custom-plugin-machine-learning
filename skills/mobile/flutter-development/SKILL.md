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

