---
name: testing-qa
description: Master testing strategies and quality assurance practices.
---

# Testing & Quality Assurance

## Testing Pyramid

```
    △ E2E
   ▲▲▲ Integration
  ▲▲▲▲▲ Unit
```

Most tests at bottom, fewer at top.

## Test Types

### Unit Testing
```javascript
test('adds two numbers', () => {
  expect(add(2, 3)).toBe(5);
});
```

### Integration Testing
```javascript
test('user signup flow', async () => {
  const response = await signupUser(userData);
  expect(response.status).toBe(201);
});
```

### End-to-End Testing
```javascript
test('user can login and view dashboard', async () => {
  await page.goto('/login');
  await page.fill('[name=email]', 'user@test.com');
  // ... more steps
});
```

## Testing Frameworks

- **JavaScript**: Jest, Vitest, Testing Library
- **Python**: pytest, unittest
- **Java**: JUnit, Mockito
- **Go**: testing, testify

## QA Practices

- **Test-Driven Development**: Write tests first
- **Continuous Testing**: Automated test runs
- **Code Coverage**: Measure test coverage
- **Performance Testing**: Load, stress tests
- **Security Testing**: Vulnerability scanning

## Best Practices

✅ Test behavior, not implementation
✅ Aim for high coverage
✅ Automate repetitive tests
✅ Test edge cases
✅ Keep tests maintainable
✅ Run tests frequently
✅ Document test strategy

