from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .database import SessionLocal
from .models import Post


def check_and_publish_scheduled_posts():
    db = SessionLocal()
    try:
        now = datetime.utcnow()
        scheduled_posts = (
            db.query(Post)
            .filter(Post.status == "scheduled")
            .filter(Post.scheduled_at <= now)
            .all()
        )
        for post in scheduled_posts:
            post.status = "published"
            post.published_at = now
            db.commit()
            print(f"[Scheduler] Auto-published scheduled post: {post.title} (slug: {post.slug})")
    except Exception as e:
        print(f"[Scheduler] Error checking scheduled posts: {e}")
    finally:
        db.close()


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_and_publish_scheduled_posts, "interval", minutes=1)
    scheduler.start()
    return scheduler
