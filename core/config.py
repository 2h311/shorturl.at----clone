import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
	PROJECT_DOMAIN_DEV: str = "127.0.0.1:8000/"
	PROJECT_DOMAIN_PROD: str = "ywlc70.deta.dev/"
	
	PROJECT_TITLE: str = "shortURL-at"
	PROJECT_VERSION: str = "No Version - Just A Clone"

	PROJECT_DATABASE_KEY = os.getenv("DATABASE_KEY")	
	PROJECT_SHORTLINK_DOCUMENT_DB = os.getenv("SHORTLINKS_DOCUMENT_DB")
	PROJECT_REPORT_DOCUMENT_DB = os.getenv("REPORTS_DOCUMENT_DB")


settings = Settings()