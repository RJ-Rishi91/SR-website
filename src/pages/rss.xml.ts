import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context: any) {
  const API_URL = import.meta.env.PUBLIC_API_URL || process.env.PUBLIC_API_URL || 'http://localhost:8000';
  let items: any[] = [];

  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 2000);
    const res = await fetch(`${API_URL}/api/posts`, { signal: controller.signal });
    clearTimeout(timeoutId);
    if (res.ok) {
      const apiPosts = await res.json();
      if (Array.isArray(apiPosts) && apiPosts.length > 0) {
        items = apiPosts.map((p) => ({
          title: p.title,
          pubDate: p.published_at ? new Date(p.published_at) : new Date(),
          description: p.excerpt,
          link: `/blog/${p.slug}/`,
        }));
      }
    }
  } catch {
    // Fallback
  }

  if (items.length === 0) {
    const posts = await getCollection('blog');
    items = posts.map((post) => ({
      title: post.data.title,
      pubDate: new Date(post.data.date),
      description: post.data.description,
      link: `/blog/${post.slug}/`,
    }));
  }

  return rss({
    title: 'Studio Ravya - Web Design & Engineering Insights',
    description: 'Practical advice on websites, web design costs, and digital products from Studio Ravya.',
    site: context.site || 'https://studioravya.onerishi.in',
    items,
    customData: `<language>en-us</language>`,
  });
}
