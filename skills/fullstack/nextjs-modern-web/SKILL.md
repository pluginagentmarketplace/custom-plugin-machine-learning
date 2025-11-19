---
name: nextjs-modern-web
description: Master Next.js for production-ready full-stack applications.
---

# Next.js & Modern Web Development

## Quick Start

### App Router (Next.js 13+)
```typescript
// app/page.tsx
export default function Home() {
  return <h1>Welcome</h1>;
}

// app/api/users/route.ts
export async function GET() {
  return Response.json({ users: [] });
}
```

### Server Components
```typescript
// Server component by default
export default async function Posts() {
  const posts = await fetchPosts();
  return (
    <ul>
      {posts.map(post => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

## Key Features

- **App Router**: File-based routing, server components
- **SSR/SSG**: Server-side rendering and static generation
- **API Routes**: Backend endpoints in the same project
- **Image Optimization**: Automatic image optimization
- **Dynamic Routes**: [id], [...slug] patterns
- **Middleware**: Request interception
- **Database Integration**: Prisma, ORMs
- **Deployment**: Vercel, Docker

## Best Practices

✅ Use Server Components by default
✅ Implement proper error boundaries
✅ Optimize images and assets
✅ Use dynamic imports for large components
✅ Implement proper caching
✅ Secure API endpoints
✅ Use TypeScript for type safety

