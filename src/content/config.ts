import { defineCollection, z } from 'astro:content';

const blogCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    category: z.string(),
    date: z.string(),
    readTime: z.string(),
    coverImage: z.string().optional(),
    featured: z.boolean().optional(),
  }),
});

export const collections = {
  blog: blogCollection,
};
