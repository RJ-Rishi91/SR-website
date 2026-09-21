import { getCollection } from 'astro:content';

export async function GET(context: any) {
  const siteUrl = context.site?.toString().replace(/\/$/, '') || 'https://studioravya.onerishi.in';
  const latestDate = new Date().toISOString().split('T')[0];

  const caseStudyImages: Record<string, { image: string; title: string }> = {
    'work/vesper-ai': {
      image: `${siteUrl}/images/showcase-saas-platform.png`,
      title: 'Vesper AI Flagship Web Platform Case Study',
    },
    'work/aura-living': {
      image: `${siteUrl}/images/showcase-ecommerce.png`,
      title: 'Aura Living Editorial E-Commerce Storefront Case Study',
    },
    'work/monolith-protocol': {
      image: `${siteUrl}/images/showcase-fintech.png`,
      title: 'Monolith Protocol Fintech Web Application Case Study',
    },
    'work/lumina-architecture': {
      image: `${siteUrl}/images/showcase-architecture.png`,
      title: 'Lumina Architecture Minimalist Portfolio Case Study',
    },
    'work/kinetix-launch': {
      image: `${siteUrl}/images/showcase-landing.png`,
      title: 'Kinetix Launch High-Converting Campaign Page Case Study',
    },
  };

  const staticPages = [
    { path: '', priority: '1.0', changefreq: 'weekly', image: `${siteUrl}/images/studio-workspace.png`, imageTitle: 'Studio Ravya Web Design and Digital Product Studio' },
    { path: 'services', priority: '0.9', changefreq: 'weekly' },
    { path: 'services/website-design-development', priority: '0.85', changefreq: 'monthly' },
    { path: 'services/landing-pages', priority: '0.85', changefreq: 'monthly' },
    { path: 'services/ecommerce-websites', priority: '0.85', changefreq: 'monthly' },
    { path: 'services/brand-and-web-identity', priority: '0.85', changefreq: 'monthly' },
    { path: 'services/custom-web-apps', priority: '0.85', changefreq: 'monthly' },
    { path: 'work', priority: '0.9', changefreq: 'weekly' },
    { path: 'work/vesper-ai', priority: '0.85', changefreq: 'monthly' },
    { path: 'work/aura-living', priority: '0.85', changefreq: 'monthly' },
    { path: 'work/monolith-protocol', priority: '0.85', changefreq: 'monthly' },
    { path: 'work/lumina-architecture', priority: '0.85', changefreq: 'monthly' },
    { path: 'work/kinetix-launch', priority: '0.85', changefreq: 'monthly' },
    { path: 'process', priority: '0.8', changefreq: 'monthly' },
    { path: 'pricing', priority: '0.85', changefreq: 'monthly' },
    { path: 'about', priority: '0.8', changefreq: 'monthly' },
    { path: 'blog', priority: '0.85', changefreq: 'weekly' },
    { path: 'contact', priority: '0.9', changefreq: 'weekly' },
    { path: 'faq', priority: '0.7', changefreq: 'monthly' },
    { path: 'privacy-policy', priority: '0.3', changefreq: 'yearly' },
    { path: 'terms-of-service', priority: '0.3', changefreq: 'yearly' },
  ];

  const localPosts = await getCollection('blog');
  const urls: Array<{
    loc: string;
    lastmod: string;
    changefreq: string;
    priority: string;
    image?: string;
    imageTitle?: string;
  }> = [];

  // Add static pages
  staticPages.forEach((item) => {
    const loc = item.path ? `${siteUrl}/${item.path}/` : `${siteUrl}/`;
    const caseImg = caseStudyImages[item.path];
    const image = caseImg ? caseImg.image : item.image;
    const imageTitle = caseImg ? caseImg.title : item.imageTitle;

    urls.push({
      loc,
      lastmod: latestDate,
      changefreq: item.changefreq,
      priority: item.priority,
      image,
      imageTitle,
    });
  });

  // Add blog posts with image metadata
  localPosts.forEach((post) => {
    const rawCover = post.data.coverImage || '';
    const cleanCover = rawCover
      .replace(/^https?:\/\/(localhost|127\.0\.0\.1):8000/, '')
      .replace(/^https?:\/\/studioravya-backend\.onrender\.com/, '');
    const fullImageUrl = cleanCover.startsWith('http')
      ? cleanCover
      : `${siteUrl}${cleanCover.startsWith('/') ? '' : '/'}${cleanCover}`;

    urls.push({
      loc: `${siteUrl}/blog/${post.slug}/`,
      lastmod: latestDate,
      changefreq: 'monthly',
      priority: '0.75',
      image: cleanCover ? fullImageUrl : undefined,
      imageTitle: post.data.title,
    });
  });

  const sitemapXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
${urls
  .map((u) => {
    const lines = [
      '  <url>',
      `    <loc>${u.loc}</loc>`,
      `    <lastmod>${u.lastmod}</lastmod>`,
      `    <changefreq>${u.changefreq}</changefreq>`,
      `    <priority>${u.priority}</priority>`,
    ];

    if (u.image) {
      lines.push('    <image:image>');
      lines.push(`      <image:loc>${u.image.replace(/&/g, '&amp;')}</image:loc>`);
      if (u.imageTitle) {
        lines.push(`      <image:title>${u.imageTitle.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')}</image:title>`);
      }
      lines.push('    </image:image>');
    }

    lines.push('  </url>');
    return lines.join('\n');
  })
  .join('\n')}
</urlset>`;

  return new Response(sitemapXml, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
      'X-Content-Type-Options': 'nosniff',
      'Cache-Control': 'public, max-age=3600',
    },
  });
}
