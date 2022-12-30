
import deta

from core.config import settings
from .models import deta_instance


db = deta_instance.Base(settings.PROJECT_CONTACT_DOCUMENT_DB)


class Contact:
	fullname: str
	email: str
	message: str


def create_new_contact(data: Contact):
	return db.put(data)


