---
name: react-modern-frontend
description: Master React with hooks, functional components, state management, and modern best practices.
---

# React & Modern Frontend

## Quick Start

### Functional Components with Hooks
```jsx
import { useState, useEffect } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Count: ${count}`;
  }, [count]);

  return (
    <button onClick={() => setCount(count + 1)}>
      Clicked {count} times
    </button>
  );
}
```

### Custom Hooks
```javascript
function useWindowWidth() {
  const [width, setWidth] = useState(window.innerWidth);

  useEffect(() => {
    const handleResize = () => setWidth(window.innerWidth);
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return width;
}
```

## Key Topics

- **React Hooks**: useState, useEffect, useContext, useReducer
- **Component Patterns**: Composition, render props, compound components
- **State Management**: Context API, Redux, Zustand
- **Performance**: React.memo, useMemo, useCallback
- **Server Components**: RSC, Next.js, streaming
- **Testing**: React Testing Library, Jest
- **Best Practices**: Key props, avoiding prop drilling, composition

## Best Practices

✅ Use functional components and hooks
✅ Memoize expensive computations
✅ Avoid prop drilling with Context
✅ Use proper key props in lists
✅ Handle loading and error states
✅ Test user interactions, not implementation
✅ Optimize bundle size

