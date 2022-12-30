from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException

from core.config import settings
from routers.routes import router, templates


def mount_static(app):
	app.mount("/static", StaticFiles(directory="static"), name="static")


def start_app():
	app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
	app.include_router(router)
	mount_static(app)
	return app


app = start_app()

@app.exception_handler(StarletteHTTPException)
def invalid_routes(request: Request, exc: StarletteHTTPException):
	print(exc)
	return templates.TemplateResponse("shortURL/404.html", context={
		"request": request,
	})