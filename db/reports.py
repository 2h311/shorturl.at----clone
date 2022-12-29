import deta

from core.config import settings
from .models import deta_instance


db = deta_instance.Base(settings.PROJECT_REPORT_DOCUMENT_DB)


def create_new_report(data: dict[str, str]):
	return db.put(data)