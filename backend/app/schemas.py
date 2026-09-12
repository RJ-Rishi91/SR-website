from datetime import datetime
from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    title: str
    category: str
    excerpt: str
    body: str
    cover_image: str | None = None
    read_time_minutes: int = 5
    status: str = "draft"
    scheduled_at: datetime | None = None
    meta_title: str | None = None
    meta_description: str | None = None
    meta_keywords: str | None = None
    og_image: str | None = None


class PostCreate(PostBase):
    slug: str | None = None


class PostUpdate(BaseModel):
    title: str | None = None
    slug: str | None = None
    category: str | None = None
    excerpt: str | None = None
    body: str | None = None
    cover_image: str | None = None
    read_time_minutes: int | None = None
    status: str | None = None
    scheduled_at: datetime | None = None
    meta_title: str | None = None
    meta_description: str | None = None
    meta_keywords: str | None = None
    og_image: str | None = None


class PostOut(PostBase):
    id: int
    slug: str
    created_at: datetime
    updated_at: datetime
    published_at: datetime | None = None
    effective_meta_title: str
    effective_meta_description: str
    effective_og_image: str | None = None

    model_config = ConfigDict(from_attributes=True)


class InquiryCreate(BaseModel):
    name: str
    email: str
    company: str | None = None
    project_type: str = "Website Design & Dev"
    budget_range: str | None = "Custom Proposal"
    timeline: str | None = None
    message: str


class InquiryOut(BaseModel):
    id: int
    name: str
    email: str
    company: str | None = None
    project_type: str
    budget_range: str | None = "Custom Proposal"
    timeline: str | None = None
    message: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
