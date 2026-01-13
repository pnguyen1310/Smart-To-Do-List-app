from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from .auth import router as auth_router
from .notes import router as notes_router
from .nextact import router as nextact_router

app = FastAPI()

# Phục vụ file tĩnh
static_path = Path(__file__).parent.parent / "static"
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Đường dẫn templates
templates_path = Path(__file__).parent.parent / "templates"

@app.get("/")
def read_root():
    return FileResponse(templates_path / "login.html", media_type="text/html")

@app.get("/login")
def login_page():
    return FileResponse(templates_path / "login.html", media_type="text/html")

@app.get("/register")
def register_page():
    return FileResponse(templates_path / "register.html", media_type="text/html")

@app.get("/dashboard")
def dashboard_page():
    return FileResponse(templates_path / "dashboard.html", media_type="text/html")

app.include_router(auth_router)
app.include_router(notes_router)
app.include_router(nextact_router)