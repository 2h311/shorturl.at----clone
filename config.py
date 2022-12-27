import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
	PROJECT_DOMAIN_DEV: str = "http://127.0.0.1:8000/"
	PROJECT_DOMAIN_PROD: str = "https://shorturl_at.deta.dev/"
	
	PROJECT_TITLE: str = "shortURL-at"
	PROJECT_VERSION: str = "No Version - Just A Clone"

	PROJECT_DETABASE_KEY = os.getenv("DETABASE_KEY")