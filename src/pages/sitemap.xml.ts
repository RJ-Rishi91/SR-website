import { getCollection } from 'astro:content';

export async function GET(context: any) {
  const siteUrl = context.site?.toString().replace(/\/$/, '') || 'https://studioravya.onerishi.in';
  const API_URL = import.meta.env.PUBLIC_API_URL || process.env.PUBLIC_API_URL || 'http://localhost:8000';

  const staticPages = [
    '',
    'services',
    'services/website-design-development',
    'services/landing-pages',
    'services/ecommerce-websites',
    'services/brand-and-web-identity',
    'services/custom-web-apps',
    'work',
    'work/vesper-ai',
    'work/aura-living',
    'work/monolith-protocol',
    'work/lumina-architecture',
    'work/kinetix-launch',
    'process',
    'pricing',
    'about',
    'blog',
    'contact',
    'faq',
    'privacy-policy',
    'terms-of-service',
  ];

  let blogPosts: Array<{ slug: string; lastmod?: string }> = [];

  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 2000);
    const res = await fetch(`${API_URL}/api/posts`, { signal: controller.signal });
    clearTimeout(timeoutId);
    if (res.ok) {
      const apiPosts = await res.json();
      if (Array.isArray(apiPosts) && apiPosts.length > 0) {
        blogPosts = apiPosts.map((p) => ({
          slug: p.slug,
          lastmod: p.published_at ? new Date(p.published_at).toISOString().split('T')[0] : undefined,
        }));
      }
    }
  } catch {
    // Fallback
  }

  if (blogPosts.length === 0) {
    const localPosts = await getCollection('blog');
    blogPosts = localPosts.map((post) => ({
      slug: post.slug,
      lastmod: new Date().toISOString().split('T')[0],
    }));
  }

  const latestDate = new Date().toISOString().split('T')[0];
  const urls: Array<{ loc: string; lastmod?: string; changefreq: string; priority: string }> = [];

  staticPages.forEach((page) => {
    let priority = '0.8';
    let changefreq = 'monthly';

    if (page === '') {
      priority = '1.0';
      changefreq = 'weekly';
    } else if (['services', 'work', 'contact'].includes(page)) {
      priority = '0.9';
      changefreq = 'weekly';
    } else if (page.startsWith('services/') || page.startsWith('work/')) {
      priority = '0.85';
      changefreq = 'monthly';
    } else if (['privacy-policy', 'terms-of-service'].includes(page)) {
      priority = '0.3';
      changefreq = 'yearly';
    }

    urls.push({
      loc: page ? `${siteUrl}/${page}/` : `${siteUrl}/`,
      lastmod: latestDate,
      changefreq,
      priority,
    });
  });

  blogPosts.forEach((post) => {
    urls.push({
      loc: `${siteUrl}/blog/${post.slug}/`,
      lastmod: post.lastmod || latestDate,
      changefreq: 'monthly',
      priority: '0.75',
    });
  });

  const sitemapXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls
  .map((u) => {
    const lines = [
      '  <url>',
      `    <loc>${u.loc}</loc>`,
      u.lastmod ? `    <lastmod>${u.lastmod}</lastmod>` : null,
      `    <changefreq>${u.changefreq}</changefreq>`,
      `    <priority>${u.priority}</priority>`,
      '  </url>',
    ].filter(Boolean);
    return lines.join('\n');
  })
  .join('\n')}
</urlset>`;

  return new Response(sitemapXml, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
    },
  });
}
