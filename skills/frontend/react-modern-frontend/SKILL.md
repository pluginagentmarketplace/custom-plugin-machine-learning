---
name: react-modern-frontend
description: Master react & modern frontend. Production-ready code examples, best practices, and real-world applications.
---

# React & Modern Frontend

**Production-Quality Guide with Real Code Examples**

## Quick Start

```jsx
import { useState, useEffect, useCallback } from 'react';

// Functional component with hooks
function Counter() {
  const [count, setCount] = useState(0);
  const [loading, setLoading] = useState(false);

  // Side effects
  useEffect(() => {
    document.title = `Count: ${count}`;
  }, [count]);

  // Memoized callback
  const increment = useCallback(() => {
    setCount(prev => prev + 1);
  }, []);

  // Loading state
  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
    </div>
  );
}

// Custom hook pattern
function useFetch(url) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(setData)
      .catch(setError);
  }, [url]);

  return { data, error };
}

// Using custom hook
function App() {
  const { data: users } = useFetch('/api/users');
  return <div>{users && users.map(u => <p key={u.id}>{u.name}</p>)}</div>;
}
```


## Production Code Examples

```jsx
// 🔥 Production-Grade React Patterns

import React, {
  useState, useEffect, useCallback, useMemo, useRef,
  useReducer, useContext, createContext
} from 'react';

// 1. Custom Hook with Error Handling
export const useFetch = (url, options = {}) => {
  const [state, dispatch] = useReducer(
    (state, action) => {
      switch(action.type) {
        case 'LOADING': return { ...state, loading: true, error: null };
        case 'SUCCESS': return { loading: false, error: null, data: action.payload };
        case 'ERROR': return { loading: false, error: action.payload, data: null };
        default: return state;
      }
    },
    { loading: false, error: null, data: null }
  );

  useEffect(() => {
    const controller = new AbortController();

    (async () => {
      dispatch({ type: 'LOADING' });
      try {
        const res = await fetch(url, {
          ...options,
          signal: controller.signal
        });
        if (!res.ok) throw new Error(\`HTTP \${res.status}\`);
        const data = await res.json();
        dispatch({ type: 'SUCCESS', payload: data });
      } catch (error) {
        if (error.name !== 'AbortError') {
          dispatch({ type: 'ERROR', payload: error });
        }
      }
    })();

    return () => controller.abort();
  }, [url, options]);

  return state;
};

// 2. Context for State Management
const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('light');

  const toggleTheme = useCallback(() => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  }, []);

  const value = useMemo(() => ({ theme, toggleTheme }), [theme]);

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
};

// 3. Memoized Components
const UserCard = React.memo(({ user, onSelect }) => {
  const handleClick = useCallback(() => {
    onSelect(user.id);
  }, [user.id, onSelect]);

  return (
    <article onClick={handleClick}>
      <h3>{user.name}</h3>
      <p>{user.email}</p>
    </article>
  );
}, (prev, next) => {
  return prev.user.id === next.user.id;
});

// 4. Advanced State Management
const useAsync = (asyncFunction, immediate = true) => {
  const [state, dispatch] = useReducer(
    (state, action) => ({ ...state, ...action }),
    { loading: immediate, error: null, data: null }
  );

  const execute = useCallback(async () => {
    dispatch({ loading: true, error: null });
    try {
      const response = await asyncFunction();
      dispatch({ loading: false, data: response });
    } catch (error) {
      dispatch({ loading: false, error });
    }
  }, [asyncFunction]);

  useEffect(() => {
    if (immediate) execute();
  }, [execute, immediate]);

  return { ...state, execute };
};

// 5. Error Boundary
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, info) {
    console.error('Error caught:', error, info);
  }

  render() {
    if (this.state.hasError) {
      return <div>Something went wrong. Please refresh.</div>;
    }
    return this.props.children;
  }
}

// 6. Compound Component Pattern
const Tabs = ({ children }) => {
  const [activeTab, setActiveTab] = useState(0);

  return React.Children.map(children, (child, index) =>
    React.cloneElement(child, { activeTab, setActiveTab, index })
  );
};

Tabs.Tab = ({ label, index, activeTab, setActiveTab, children }) => (
  <div hidden={activeTab !== index}>
    <button onClick={() => setActiveTab(index)}>{label}</button>
    {activeTab === index && children}
  </div>
);
```
        


### Advanced Patterns
- **Render Props Pattern**: Flexible component composition
- **Higher-Order Components (HOC)**: Component enhancement
- **Concurrent Features**: useTransition, useDeferredValue
- **Suspense Boundaries**: Code splitting integration
- **Server Components**: SSR patterns with React Server Components
        



## Key Topics

- Functional components and hooks
- useState, useEffect, useCallback, useRef
- Custom hooks
- Component composition patterns
- Performance optimization (React.memo, useMemo)
- Error boundaries
- Suspense and code splitting

## Advanced Concepts

### Best Practices
- ✅ Production-ready code patterns
- ✅ Performance optimization
- ✅ Testing strategies
- ✅ Error handling
- ✅ Security considerations
- ✅ Scalability patterns
- ✅ Maintainability and documentation

### Common Pitfalls
- ❌ Avoid inefficient patterns
- ❌ Don't skip testing
- ❌ Don't ignore error handling
- ❌ Don't optimize prematurely
- ❌ Don't hardcode values
- ❌ Don't skip documentation

## Real-World Projects

- Build an e-commerce product page
- Create a real-time chat interface
- Develop a dashboard with data visualization

## Resources

- Official documentation
- Recommended tutorials
- Best practices guides
- Community forums

## Career Integration

This skill connects to:
- Related technologies
- Career paths
- Interview preparation
- Portfolio building

---

**Master React & Modern Frontend today!** 🚀
