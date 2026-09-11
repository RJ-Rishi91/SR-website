import os
from datetime import datetime
from app.database import Base, SessionLocal, engine
from app.models import Post

Base.metadata.create_all(bind=engine)


def seed_posts():
    db = SessionLocal()
    try:
        count = db.query(Post).count()
        if count >= 9:
            print(f"[Seed] Database already has {count} posts.")
            return

        try:
            from app.articles import ARTICLES
        except ImportError:
            from .articles import ARTICLES

        for idx, art in enumerate(ARTICLES, 1):
            slug = art["slug"]
            existing = db.query(Post).filter(Post.slug == slug).first()
            if not existing:
                post = Post(
                    slug=slug,
                    title=art["title"],
                    category=art["category"],
                    excerpt=art["excerpt"],
                    body=art["body"],
                    cover_image=f"/images/{slug}.jpg",
                    read_time_minutes=art["read_time_minutes"],
                    status="published",
                    published_at=datetime.utcnow(),
                    meta_title=art["meta_title"],
                    meta_description=art["meta_description"],
                )
                db.add(post)
        db.commit()
        print(f"[Seed] Successfully ensured 9 articles seeded in database.")
    except Exception as e:
        print(f"[Seed] Error seeding posts: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    seed_posts()
