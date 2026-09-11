from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Text
from .database import Base

CATEGORIES = [
    "Pricing & Planning",
    "Web Design & UX",
    "Development & Engineering",
    "Strategy & Business",
    "Case Studies",
]


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    excerpt = Column(String, nullable=False)
    body = Column(Text, nullable=False)  # Markdown
    cover_image = Column(String, nullable=True)
    read_time_minutes = Column(Integer, nullable=False, default=5)
    status = Column(String, nullable=False, default="draft")  # draft | scheduled | published
    scheduled_at = Column(DateTime, nullable=True)

    meta_title = Column(String, nullable=True)
    meta_description = Column(String, nullable=True)
    meta_keywords = Column(String, nullable=True)
    og_image = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published_at = Column(DateTime, nullable=True)

    @property
    def effective_meta_title(self) -> str:
        return self.meta_title or self.title

    @property
    def effective_meta_description(self) -> str:
        return self.meta_description or self.excerpt

    @property
    def effective_og_image(self) -> str | None:
        return self.og_image or self.cover_image


class Inquiry(Base):
    __tablename__ = "inquiries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    company = Column(String, nullable=True)
    project_type = Column(String, nullable=False, default="Website Design & Dev")
    budget_range = Column(String, nullable=False, default="$5,000 – $10,000")
    timeline = Column(String, nullable=True)
    message = Column(Text, nullable=False)
    status = Column(String, nullable=False, default="new")  # new | contacted | archived
    created_at = Column(DateTime, default=datetime.utcnow)
