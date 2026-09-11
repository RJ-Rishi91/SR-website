from datetime import datetime
from slugify import slugify
from sqlalchemy import desc
from sqlalchemy.orm import Session

from . import models, schemas


def get_published_posts(db: Session, category: str | None = None) -> list[models.Post]:
    q = db.query(models.Post).filter(models.Post.status == "published")
    if category:
        q = q.filter(models.Post.category == category)
    return q.order_by(desc(models.Post.published_at), desc(models.Post.created_at)).all()


def get_post_by_slug(db: Session, slug: str) -> models.Post | None:
    return db.query(models.Post).filter(models.Post.slug == slug).first()


def get_all_posts(db: Session) -> list[models.Post]:
    return db.query(models.Post).order_by(desc(models.Post.updated_at)).all()


def get_post_by_id(db: Session, post_id: int) -> models.Post | None:
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def create_post(db: Session, post_in: schemas.PostCreate) -> models.Post:
    raw_slug = post_in.slug or slugify(post_in.title)
    final_slug = raw_slug
    counter = 1
    while db.query(models.Post).filter(models.Post.slug == final_slug).first():
        final_slug = f"{raw_slug}-{counter}"
        counter += 1

    post_data = post_in.model_dump(exclude={"slug"})
    post_data["slug"] = final_slug
    if post_in.status == "published" and not post_data.get("published_at"):
        post_data["published_at"] = datetime.utcnow()

    db_post = models.Post(**post_data)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post(db: Session, db_post: models.Post, updates: schemas.PostUpdate) -> models.Post:
    update_data = updates.model_dump(exclude_unset=True)

    if "title" in update_data and "slug" not in update_data and not db_post.slug:
        update_data["slug"] = slugify(update_data["title"])

    if update_data.get("status") == "published" and not db_post.published_at:
        update_data["published_at"] = datetime.utcnow()

    for field, val in update_data.items():
        setattr(db_post, field, val)

    db_post.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: Session, db_post: models.Post) -> None:
    db.delete(db_post)
    db.commit()


# Inquiries CRUD
def create_inquiry(db: Session, inq_in: schemas.InquiryCreate) -> models.Inquiry:
    db_inq = models.Inquiry(**inq_in.model_dump())
    db.add(db_inq)
    db.commit()
    db.refresh(db_inq)
    return db_inq


def get_all_inquiries(db: Session) -> list[models.Inquiry]:
    return db.query(models.Inquiry).order_by(desc(models.Inquiry.created_at)).all()


def get_inquiry_by_id(db: Session, inq_id: int) -> models.Inquiry | None:
    return db.query(models.Inquiry).filter(models.Inquiry.id == inq_id).first()
