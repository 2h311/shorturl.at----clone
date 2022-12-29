from core.config import settings

from .models import deta


db = deta.Base(settings.PROJECT_REPORT_DOCUMENT_DB)


class ReportedURLs:
	reported_url: str
	comment: str


def create_new_report(data: ReportedURLs):
	print(data)