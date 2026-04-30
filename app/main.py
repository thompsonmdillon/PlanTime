from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Creates a fastapi instance
app = FastAPI()
# Mounts the static folder to the /static URL path, referred by FastAPI as static. If a there is a request to a file with /static, FastAPI serves it from the static/ folder directly via mount.
app.mount("/static", StaticFiles(directory="static"), name="static")
# Create an instance, templates, to later render and return a TemplateResponse. All html files are in templates directory.
templates = Jinja2Templates(directory="templates")

def render_page():
    return
# root() runs whenever FastAPI requests the "/" path. Route returns HTML. root() passes an instance of the Request object named request. Returns template instance.
@app.get("/")
async def root():
    return {"message": "Hello World"}