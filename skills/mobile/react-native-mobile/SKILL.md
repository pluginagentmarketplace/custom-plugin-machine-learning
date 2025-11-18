---
name: react-native-mobile
description: Build cross-platform mobile apps with React Native.
---

# React Native Mobile Development

## Quick Start

### React Native Component
```javascript
import { View, Text, StyleSheet } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Hello Mobile!</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    fontSize: 24,
  },
});
```

## Key Topics

- **Core Components**: View, Text, ScrollView, FlatList
- **Navigation**: React Navigation stack, tab, drawer
- **State Management**: Redux, Context API, Zustand
- **Networking**: Fetch, axios, real-time APIs
- **Platform-Specific Code**: .ios.js, .android.js, Platform.select
- **Native Modules**: Bridging to native code
- **Performance**: FlatList optimization, Hermes engine
- **Testing**: Testing Library, Detox

## Best Practices

✅ Use FlatList for long lists
✅ Optimize images and assets
✅ Handle platform differences
✅ Test on real devices
✅ Use native modules wisely
✅ Monitor performance
✅ Implement proper error handling

