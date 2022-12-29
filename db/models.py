from deta import Deta

from core.config import settings

deta_instance = Deta(settings.PROJECT_DATABASE_KEY)