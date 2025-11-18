---
name: html-css-design
description: Master semantic HTML5, advanced CSS layouts, responsive design, animations, and modern CSS techniques including Flexbox, Grid, and custom properties.
---

# 🎨 HTML, CSS & Modern Design

**Production-Ready HTML/CSS Development with Modern Layout Techniques**

## Quick Start

### Semantic HTML5 Structure
```html
<!-- ✅ GOOD: Semantic, accessible structure -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Product page for e-commerce">
  <title>Product | E-Shop</title>
</head>
<body>
  <header role="banner">
    <nav aria-label="Main navigation">
      <a href="/" aria-current="page">Home</a>
      <a href="/products">Products</a>
      <a href="/contact">Contact</a>
    </nav>
  </header>

  <main>
    <article>
      <h1>Product Name</h1>
      <section>
        <h2>Description</h2>
        <p>Product details...</p>
      </section>
      <section>
        <h2>Reviews</h2>
        <ul role="list">
          <li>Review 1</li>
          <li>Review 2</li>
        </ul>
      </section>
    </article>
  </main>

  <footer role="contentinfo">
    <p>&copy; 2024 E-Shop. All rights reserved.</p>
  </footer>
</body>
</html>
```

### Modern CSS Grid Layout
```css
/* ✅ GOOD: Responsive grid system */
:root {
  --spacing-unit: 1rem;
  --max-width: 1200px;
  --grid-gap: var(--spacing-unit);
}

.container {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 var(--spacing-unit);
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--grid-gap);
  align-items: start;
}

/* Mobile-first responsive */
@media (min-width: 640px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

### CSS Animations & Transitions
```css
/* ✅ GOOD: Performant animations */
@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.card {
  animation: slideIn 0.3s ease-out;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}
```


## Production Code Examples

```html
<!-- 🔥 Modern HTML5 with Semantic Elements & Accessibility -->
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Production-ready semantic HTML5">
    <title>E-Commerce Product Page</title>
    <link rel="preload" href="styles.css" as="style">
</head>
<body>
    <header role="banner">
        <nav aria-label="Main">
            <a href="/" aria-current="page">Home</a>
        </nav>
    </header>

    <main>
        <article>
            <h1>Premium Product</h1>
            <img src="product.jpg" alt="Product image showing features" loading="lazy">
            <section>
                <h2>Details</h2>
                <dl>
                    <dt>Price</dt>
                    <dd>$99.99</dd>
                </dl>
            </section>
        </article>
    </main>

    <footer role="contentinfo">
        <p>&copy; 2024 Company</p>
    </footer>
</body>
</html>
```

```css
/* 🎨 Modern CSS with Grid, Flexbox, and Animation */
:root {
    --color-primary: #007bff;
    --spacing-unit: 1rem;
    --font-sans: system-ui, -apple-system, sans-serif;
}

html {
    scroll-behavior: smooth;
    -webkit-font-smoothing: antialiased;
}

body {
    font-family: var(--font-sans);
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

header {
    display: flex;
    align-items: center;
    padding: var(--spacing-unit);
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

nav {
    display: flex;
    gap: var(--spacing-unit);
}

main {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

article {
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

article:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 20px rgba(0,0,0,0.15);
}

img {
    width: 100%;
    height: auto;
    display: block;
}

/* Responsive Typography */
h1 {
    font-size: clamp(1.5rem, 5vw, 3rem);
    line-height: 1.2;
    margin: 0;
}

/* Accessibility Focus */
a:focus {
    outline: 2px solid var(--color-primary);
    outline-offset: 2px;
}

/* Print Styles */
@media print {
    header, footer { display: none; }
    article { box-shadow: none; }
}

/* Dark Mode Support */
@media (prefers-color-scheme: dark) {
    body { background: #1a1a1a; color: #fff; }
    article { background: #2a2a2a; }
}
```
        


### Advanced Patterns
- **CSS Grid Masonry**: Create flexible gallery layouts
- **Container Queries**: Responsive design without media queries
- **CSS-in-JS**: BEM naming convention, atomic CSS approach
- **Web Components**: Custom elements with Shadow DOM
- **Accessibility First**: WCAG 2.1 AA compliance checklist
        


### Real-World Projects
1. **Responsive E-Commerce Product Page** (Level: Intermediate)
   - Multi-image gallery with lazy loading
   - Responsive product specs and pricing
   - Filter and sort functionality
   - Accessibility compliance testing
   - Performance: <1s LCP, <100ms FID

2. **Design System Component Library** (Level: Advanced)
   - 50+ reusable components
   - Token-based theming (light/dark/custom)
   - Storybook documentation
   - Performance monitoring
   - Test coverage: >95%

3. **Marketing Website** (Level: Intermediate)
   - Hero sections with parallax
   - Customer testimonials carousel
   - Contact forms with validation
   - Email integration
   - Analytics tracking
        

## Key Topics

### 🏗️ Semantic HTML5
- Article, Section, Nav, Aside, Header, Footer
- Main, Details, Summary elements
- ARIA attributes for accessibility
- Form accessibility (labels, descriptions)
- Microdata and structured data

### 🎨 Advanced CSS
- Flexbox for alignment & distribution
- CSS Grid for complex layouts
- Subgrid for nested grids
- Custom Properties (CSS Variables)
- CSS Functions: calc(), clamp(), min(), max()
- Logical properties (inline, block)

### 📱 Responsive Design
- Mobile-first approach
- Breakpoint strategy
- Flexible images & media
- Container queries
- Fluid typography

### ⚡ Performance
- Critical CSS
- Font loading strategies
- Image optimization
- CSS minification
- CSS-in-JS considerations

### ♿ Accessibility (a11y)
- Color contrast (WCAG AA/AAA)
- Keyboard navigation
- Focus management
- Screen reader optimization
- ARIA roles & attributes

## Advanced Concepts

### CSS Grid Advanced Pattern
```css
/* Complex layout with named grid areas */
.layout {
  display: grid;
  grid-template-areas:
    "header header header"
    "sidebar main main"
    "footer footer footer";
  grid-template-columns: 200px 1fr 1fr;
  grid-template-rows: auto 1fr auto;
  gap: 1rem;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }

@media (max-width: 768px) {
  .layout {
    grid-template-areas:
      "header"
      "main"
      "sidebar"
      "footer";
    grid-template-columns: 1fr;
  }
}
```

### Custom Properties System
```css
/* Design token system */
:root {
  /* Colors */
  --color-primary: #0066cc;
  --color-primary-dark: #0052a3;
  --color-primary-light: #e6f0ff;

  /* Typography */
  --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-size-base: 1rem;
  --font-size-lg: 1.25rem;
  --font-size-sm: 0.875rem;
  --line-height-base: 1.5;

  /* Spacing */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);

  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-base: 200ms ease;
  --transition-slow: 300ms ease;
}

.button {
  background-color: var(--color-primary);
  padding: var(--spacing-md) var(--spacing-lg);
  font-family: var(--font-family);
  transition: background-color var(--transition-base);
}

.button:hover {
  background-color: var(--color-primary-dark);
}
```

## Best Practices ✅

### HTML
✅ Always use semantic HTML first
✅ Validate HTML structure
✅ Use proper heading hierarchy
✅ Include alt text for images
✅ Use aria-label for icons
✅ Test with screen readers

### CSS
✅ Use CSS Custom Properties for tokens
✅ Follow mobile-first approach
✅ Minimize CSS in HTML
✅ Use CSS Grid for layouts
✅ Avoid inline styles
✅ Use CSS class selectors (avoid ID)
✅ Keep specificity low

### Accessibility
✅ Test with keyboard only
✅ Test with screen readers (NVDA, JAWS)
✅ Check color contrast
✅ Ensure focus indicators visible
✅ Use meaningful alt text
✅ Test with real users

### Performance
✅ Minify CSS for production
✅ Use CSS containment
✅ Avoid expensive selectors
✅ Optimize critical CSS path
✅ Use font-display: swap
✅ Lazy load non-critical CSS

## Real-World Projects

### 1. Responsive E-Commerce Product Page
**Technologies:** HTML5, CSS3, CSS Grid, Flexbox
**Duration:** 8-12 hours
**Skills:** Semantic markup, responsive design, component styling
**Deliverables:**
- Product showcase with images
- Variant selector
- Reviews section
- Related products
- Responsive across devices

### 2. Design System Component Library
**Technologies:** HTML5, CSS, CSS Custom Properties
**Duration:** 20-30 hours
**Skills:** Design tokens, component styling, accessibility
**Deliverables:**
- Color system
- Typography scale
- Spacing system
- Component styles
- Documentation

### 3. Marketing Website
**Technologies:** Semantic HTML, CSS Grid, animations
**Duration:** 15-20 hours
**Skills:** Layout, typography, animations, accessibility
**Deliverables:**
- Hero section
- Feature sections
- Testimonials
- CTA sections
- Mobile responsive

## Tools & Technologies

- **Design:** Figma, Adobe XD
- **CSS Tools:** PostCSS, Sass/SCSS
- **Validators:** W3C HTML, CSS validators
- **Accessibility:** WAVE, Lighthouse, Axe DevTools
- **Performance:** Lighthouse, WebPageTest
- **DevTools:** Browser DevTools, CSS Grid inspector

## Career Path Integration

**Skills:** HTML/CSS Design → JavaScript → React → TypeScript → Full Stack

**Next Steps:**
1. Master semantic HTML
2. Learn CSS Flexbox & Grid
3. Build responsive layouts
4. Implement accessibility
5. Move to JavaScript for interactivity

---

**Start building beautiful, accessible, responsive websites today!** 🚀
