import deta
from core.config import settings

from .models import deta_instance


db = deta_instance.Base(settings.PROJECT_SHORTLINK_DOCUMENT_DB)


class ShortLinkSchema:
	short_url: str
	long_url: str
	count: int = 0


def create_new_link(data: ShortLinkSchema):
	return db.put(data)


def read_one_link(random_str: str):
	response = db.fetch({"short_url": random_str})
	if isinstance(response, deta.base.FetchResponse):
		data = response.items[0].get("long_url", "")
	else:
		data = next(response)[0].get("long_url", "")
	return data


def read_one_link_count(random_str: str):
	response = db.fetch({"short_url": random_str})
	if isinstance(response, deta.base.FetchResponse):
		count = response.items[0].get("count", 0)
	else:
		count = next(response)[0].get("count", 0)
	return count


def update_one_link_count(random_str: str):
	response = db.fetch({"short_url": random_str})
	if isinstance(response, deta.base.FetchResponse):
		item = response.items[0]
	else:
		item = next(response)[0]

	count = item.get("count") + 1
	item["count"] = count
	return db.put(item, item["key"])