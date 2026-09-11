import os
from datetime import datetime
from app.database import Base, SessionLocal, engine
from app.models import Post

Base.metadata.create_all(bind=engine)


def seed_posts():
    db = SessionLocal()
    try:
        slug = "how-much-does-a-website-cost"
        existing = db.query(Post).filter(Post.slug == slug).first()
        if existing:
            print(f"[Seed] Post '{slug}' already exists in database.")
            return

        # Find sample markdown file
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        md_file = os.path.join(root_dir, "studioravya-sample-blog-post.md")

        body_content = ""
        if os.path.exists(md_file):
            with open(md_file, "r", encoding="utf-8") as f:
                raw = f.read()
                # Split frontmatter if exists
                if raw.startswith("---"):
                    parts = raw.split("---", 2)
                    if len(parts) >= 3:
                        body_content = parts[2].strip()
                if not body_content:
                    body_content = raw.strip()
        else:
            body_content = """# How Much Does a Website Cost in 2026? A Practical Breakdown

"How much does a website cost?" is one of the first questions every business owner asks, and it's also one of the hardest to answer honestly — because the real answer is "it depends."

## What actually drives the price
- **Page count and complexity.**
- **Custom design vs. template.**
- **E-commerce and functionality.**
- **Content and copywriting.**
- **Timeline.**
"""

        post = Post(
            slug=slug,
            title="How Much Does a Website Cost in 2026? A Practical Breakdown",
            category="Pricing & Planning",
            excerpt="A practical breakdown of what actually drives website pricing — from simple landing pages to custom web apps — so you know what to budget before you reach out.",
            body=body_content,
            cover_image="/images/showcase-saas-platform.png",
            read_time_minutes=6,
            status="published",
            published_at=datetime.utcnow(),
            meta_title="How Much Does a Website Cost in 2026? [Pricing Guide]",
            meta_description="A practical breakdown of what actually drives website pricing — from simple landing pages to custom web apps — so you know what to budget before you reach out.",
        )
        db.add(post)
        db.commit()
        print(f"[Seed] Successfully seeded initial article: '{post.title}'")
    except Exception as e:
        print(f"[Seed] Error seeding posts: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    seed_posts()
