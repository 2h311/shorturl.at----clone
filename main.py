import string
import random

from fastapi import FastAPI, Request, APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException

from deta import Deta
from config import settings

from models import create_new_link, read_one_link, update_one_link_count, read_one_link_count


templates = Jinja2Templates(directory="templates")
router = APIRouter()
app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)


@router.get("/")
async def index(request: Request):
	return templates.TemplateResponse("shortURL/index.html", context={
		"request": request,
	})


@router.post("/shortener")
async def shorten_url(request: Request, link: str = Form(...)):
	random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
	create_new_link({
		"short_url": random_str,
		"long_url": link,
		"count": 0,
	})
	return templates.TemplateResponse("shortURL/shortener.html", context={
		"request": request,
		"shortened_url": random_str,
		"long_url": link,
	})


@router.get("/contact")
async def contact(request: Request):
	return templates.TemplateResponse("shortURL/contact.html", context={
		"request": request,
	})


@router.post("/contact")
async def contact(request: Request, fullname: str = Form(...), email: str = Form(...), message: str = Form(...)):
	data = {
		"fullname": fullname,
		"email": email,
		"message": message
	}
	return templates.TemplateResponse("shortURL/contact.html", context={
		"request": request, 
		"show_message": True
	})


@router.get("/privacy-policy")
async def privacy(request: Request):
	return templates.TemplateResponse("shortURL/privacy.html", context={
		"request": request,
	})


@router.get("/report-malicious-url")
async def report(request: Request):
	return templates.TemplateResponse("shortURL/report_url.html", context={
		"request": request, 
		"value1": random.randint(1, 9),
		"value2": random.randint(1, 9),
	})


@router.post("/report-malicious-url")
async def report(request: Request, value1: str = Form(...), value2: str = Form(...), math_answer: str = Form(...)):
	answer = int(value1) + int(value2)
	if answer == int(math_answer):
		return templates.TemplateResponse("shortURL/report_url.html", context={
			"request": request,
			"report_response": "true", 
		})
	else:
		return templates.TemplateResponse("shortURL/report_url.html", context={
			"request": request,
			"report_response": "false",
		})


@router.get("/url-click-counter")
async def counter(request: Request):
	return templates.TemplateResponse("shortURL/click_counter.html", context={
		"request": request,
	})


@router.post("/url-total-clicks")
async def total_clicks(request: Request, shortened_url: str = Form(...)):
	string = shortened_url.split("/")[-1]
	counts = read_one_link_count(string)
	print(counts)
	return templates.TemplateResponse("shortURL/total_clicks.html", context={
		"request": request,
		"counts": counts,
	})


@router.get("/terms-of-service")
async def terms_of_service(request: Request):
	return templates.TemplateResponse("shortURL/terms_of_service.html", context={
		"request": request,
	})


@router.get("/{short_url}")
async def read_url(short_url: str):
	response = read_one_link(short_url)
	if response:
		# fetch original link from detabase
		original_link = response.items[-1].get("long_url")
		# update the count of the link from detabase
		update_one_link_count(short_url)
		# redirect to original link
		return RedirectResponse(original_link)
	else:
		return templates.TemplateResponse("shortURL/404.html", context={
			"request": request,
		})


@app.exception_handler(StarletteHTTPException)
async def invalid_routes(request: Request, ecx: StarletteHTTPException):
	return templates.TemplateResponse("shortURL/404.html", context={
		"request": request,
	})


app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)