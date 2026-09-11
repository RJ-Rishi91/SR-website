import os
import shutil
import uuid
from dotenv import load_dotenv
from slugify import slugify

load_dotenv()

from fastapi import BackgroundTasks, Depends, FastAPI, File, HTTPException, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session

from . import auth, crud, models, schemas
from .database import Base, engine, get_db
from .scheduler import start_scheduler
from .webhook import trigger_github_rebuild

Base.metadata.create_all(bind=engine)

UPLOAD_DIR = os.getenv("UPLOAD_DIR")
if not UPLOAD_DIR:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    UPLOAD_DIR = os.path.join(base_dir, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI(title="Studio Ravya API", version="1.0.0")

# Mount uploads directory for serving uploaded images
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

# CORS middleware allowing localhost, preview ports, and production domains
raw_origins = os.getenv("CORS_ORIGINS", "http://localhost:4321,http://127.0.0.1:4321").split(",")
origins = [o.strip() for o in raw_origins if o.strip() and o.strip() != "*"]
if not origins:
    origins = ["http://localhost:4321", "http://127.0.0.1:4321"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=r"^https?://(localhost|127\.0\.0\.1)(:[0-9]+)?$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_anti_crawler_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Robots-Tag"] = "noindex, nofollow, noarchive"
    return response


@app.get("/robots.txt", response_class=PlainTextResponse)
def backend_robots():
    return "User-agent: *\nDisallow: /\n"


_scheduler = None


@app.on_event("startup")
def startup_init():
    global _scheduler
    try:
        import sys
        backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if backend_dir not in sys.path:
            sys.path.insert(0, backend_dir)
        from seed_posts import seed_posts
        seed_posts()
    except Exception as err:
        print(f"[Startup] Auto-seed note: {err}")

    try:
        _scheduler = start_scheduler()
    except Exception as err:
        print(f"[Startup] Scheduler startup note: {err}")


from fastapi.responses import HTMLResponse, PlainTextResponse

# ---------- Root Gateway Dashboard ----------

@app.get("/", response_class=HTMLResponse)
def root_gateway():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Studio Ravya API Engine</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #120E0A;
      --card: #1C1713;
      --elevated: #28211C;
      --primary: #F5A623;
      --amber: #E08B10;
      --text: #FBF8F5;
      --muted: #A09488;
      --border: rgba(245, 166, 35, 0.2);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2rem 1rem;
    }
    .container {
      max-width: 680px;
      width: 100%;
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 2.5rem;
      box-shadow: 0 10px 40px rgba(0,0,0,0.6), 0 0 30px rgba(245,166,35,0.08);
      position: relative;
      overflow: hidden;
    }
    .container::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; height: 2px;
      background: linear-gradient(90deg, transparent, var(--primary), transparent);
    }
    .header {
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 1.5rem;
    }
    .emblem {
      width: 48px;
      height: 48px;
      border-radius: 12px;
      background: rgba(245, 166, 35, 0.15);
      border: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: center;
    }
    h1 {
      font-family: 'Newsreader', Georgia, serif;
      font-size: 1.75rem;
      font-weight: 600;
      letter-spacing: 0.04em;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.25rem 0.75rem;
      background: var(--elevated);
      border: 1px solid var(--border);
      border-radius: 9999px;
      font-size: 0.75rem;
      font-family: monospace;
      color: var(--primary);
      margin-bottom: 1.5rem;
    }
    .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10B981;
      box-shadow: 0 0 8px #10B981;
    }
    p.desc {
      color: var(--muted);
      font-size: 0.925rem;
      line-height: 1.6;
      margin-bottom: 2rem;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1rem;
      margin-bottom: 2rem;
    }
    .endpoint-card {
      background: var(--elevated);
      border: 1px solid rgba(245, 166, 35, 0.15);
      border-radius: 12px;
      padding: 1.25rem;
      text-decoration: none;
      color: inherit;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }
    .endpoint-card:hover {
      border-color: var(--primary);
      transform: translateY(-2px);
      box-shadow: 0 4px 16px rgba(245, 166, 35, 0.15);
    }
    .endpoint-title {
      font-weight: 600;
      font-size: 0.95rem;
      color: var(--text);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .endpoint-path {
      font-family: monospace;
      font-size: 0.75rem;
      color: var(--primary);
    }
    .endpoint-desc {
      font-size: 0.8rem;
      color: var(--muted);
    }
    .footer-bar {
      padding-top: 1.5rem;
      border-top: 1px solid rgba(245, 166, 35, 0.1);
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.8rem;
      color: var(--muted);
    }
    .footer-bar a {
      color: var(--primary);
      text-decoration: none;
    }
    .footer-bar a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="emblem">
        <svg width="24" height="24" viewBox="0 0 32 32" fill="none">
          <circle cx="16" cy="16" r="6" fill="#F5A623"/>
          <path d="M16 4V8M16 24V28M4 16H8M24 16H28M7.5 7.5L10.3 10.3M21.7 21.7L24.5 24.5M7.5 24.5L10.3 21.7M21.7 10.3L24.5 7.5" stroke="#F5A623" stroke-width="2" stroke-linecap="round"/>
        </svg>
      </div>
      <div>
        <h1>STUDIO RAVYA</h1>
        <p style="font-size:0.75rem; color: var(--primary); font-family: monospace; text-transform: uppercase;">FastAPI Core Engine · Localhost:8000</p>
      </div>
    </div>

    <div class="badge">
      <span class="dot"></span>
      <span>SYSTEM STATUS: OPERATIONAL</span>
    </div>

    <p class="desc">
      Welcome to the headless backend pipeline powering Studio Ravya. This server provides automated lead intake, SQLite editorial persistence, webhook dispatchers, and tokenized CMS endpoints.
    </p>

    <div class="grid">
      <a href="/docs" class="endpoint-card">
        <div class="endpoint-title">
          <span>Interactive Swagger UI</span>
          <span>↗</span>
        </div>
        <div class="endpoint-path">GET /docs</div>
        <div class="endpoint-desc">Explore and test all REST endpoints interactively.</div>
      </a>

      <a href="/api/health" class="endpoint-card">
        <div class="endpoint-title">
          <span>Health Telemetry</span>
          <span>↗</span>
        </div>
        <div class="endpoint-path">GET /api/health</div>
        <div class="endpoint-desc">Live daemon ping and studio operational state.</div>
      </a>

      <a href="/api/posts" class="endpoint-card">
        <div class="endpoint-title">
          <span>Editorial Feed (9 Posts)</span>
          <span>↗</span>
        </div>
        <div class="endpoint-path">GET /api/posts</div>
        <div class="endpoint-desc">JSON array of all active published articles.</div>
      </a>

      <a href="http://localhost:4321/admin" class="endpoint-card">
        <div class="endpoint-title">
          <span>Admin CMS Portal</span>
          <span>↗</span>
        </div>
        <div class="endpoint-path">http://localhost:4321/admin</div>
        <div class="endpoint-desc">Editorial composer, lead inbox & settings suite.</div>
      </a>
    </div>

    <div class="footer-bar">
      <span>Studio Director: <a href="https://onerishi.in" target="_blank">Rushal S. (OneRishi)</a></span>
      <a href="http://localhost:4321">← Return to Studio Website</a>
    </div>
  </div>
</body>
</html>
"""

# ---------- Health Check ----------

@app.get("/api/health")
def health():
    return {"status": "ok", "studio": "Studio Ravya"}



# ---------- Public Content Endpoints ----------

@app.get("/api/posts", response_model=list[schemas.PostOut])
def list_published_posts(category: str | None = None, db: Session = Depends(get_db)):
    return crud.get_published_posts(db, category)


@app.get("/api/posts/{slug}", response_model=schemas.PostOut)
def get_published_post(slug: str, db: Session = Depends(get_db)):
    post = crud.get_post_by_slug(db, slug)
    if not post or post.status != "published":
        raise HTTPException(status_code=404, detail="Post not found")
    return post


# ---------- Public Inquiry / Lead Capture ----------

@app.post("/api/inquiries", response_model=schemas.InquiryOut)
def submit_inquiry(inquiry: schemas.InquiryCreate, db: Session = Depends(get_db)):
    created = crud.create_inquiry(db, inquiry)
    print(f"[Inquiry] Received new client lead from {created.name} ({created.email}) for {created.project_type}")
    return created


# ---------- Admin Authentication ----------

@app.post("/api/admin/login", response_model=schemas.TokenResponse)
def login(payload: schemas.LoginRequest):
    if not auth.verify_admin_password(payload.password):
        raise HTTPException(status_code=401, detail="Incorrect master password")
    return schemas.TokenResponse(access_token=auth.create_access_token())


# ---------- Admin Content Management ----------

@app.get("/api/admin/posts", response_model=list[schemas.PostOut])
def list_all_posts(db: Session = Depends(get_db), _: bool = Depends(auth.get_current_admin)):
    return crud.get_all_posts(db)


@app.get("/api/admin/posts/{post_id}", response_model=schemas.PostOut)
def get_admin_post(post_id: int, db: Session = Depends(get_db), _: bool = Depends(auth.get_current_admin)):
    post = crud.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@app.post("/api/admin/posts", response_model=schemas.PostOut)
def create_post(
    post: schemas.PostCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    _: bool = Depends(auth.get_current_admin),
):
    created = crud.create_post(db, post)
    if created.status == "published":
        background_tasks.add_task(trigger_github_rebuild, "cms_post_published", {"post_id": created.id, "action": "created"})
    return created


@app.put("/api/admin/posts/{post_id}", response_model=schemas.PostOut)
def update_post(
    post_id: int,
    updates: schemas.PostUpdate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    _: bool = Depends(auth.get_current_admin),
):
    db_post = crud.get_post_by_id(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    was_published = db_post.status == "published"
    updated = crud.update_post(db, db_post, updates)
    if was_published or updated.status == "published":
        background_tasks.add_task(trigger_github_rebuild, "cms_post_published", {"post_id": updated.id, "action": "updated"})
    return updated


@app.delete("/api/admin/posts/{post_id}")
def delete_post(
    post_id: int,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    _: bool = Depends(auth.get_current_admin),
):
    db_post = crud.get_post_by_id(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    was_published = db_post.status == "published"
    crud.delete_post(db, db_post)
    if was_published:
        background_tasks.add_task(trigger_github_rebuild, "cms_post_published", {"post_id": post_id, "action": "deleted"})
    return {"deleted": True}


# ---------- Admin Inquiries Management ----------

@app.get("/api/admin/inquiries", response_model=list[schemas.InquiryOut])
def list_inquiries(db: Session = Depends(get_db), _: bool = Depends(auth.get_current_admin)):
    return crud.get_all_inquiries(db)


# ---------- Admin File Uploads ----------

ALLOWED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"}


@app.post("/api/admin/upload")
async def upload_image(
    request: Request,
    file: UploadFile = File(...),
    _: bool = Depends(auth.get_current_admin),
):
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in ALLOWED_IMAGE_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type '{ext}'. Allowed: {', '.join(sorted(ALLOWED_IMAGE_EXTENSIONS))}",
        )

    clean_stem = slugify(os.path.splitext(file.filename or "image")[0]) or "image"
    unique_name = f"{uuid.uuid4().hex[:10]}_{clean_stem}{ext}"
    dest_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(dest_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    base = os.getenv("API_BASE_URL") or str(request.base_url).rstrip("/")
    full_url = f"{base}/uploads/{unique_name}"

    return {
        "url": full_url,
        "filename": unique_name,
    }
