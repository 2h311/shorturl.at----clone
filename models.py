from deta import Deta

from config import settings


deta = Deta(settings.PROJECT_DETABASE_KEY)
db = deta.Base(settings.PROJECT_DETABASE_NAME)


class ShortLinkSchema:
	short_url: str
	long_url: str
	count: int = 0


def create_new_link(data: ShortLinkSchema):
	return db.put(data)


def read_one_link(random_str: str):
	return db.fetch({"short_url": random_str})


def read_one_link_count(random_str: str):
	items = db.fetch({"short_url": random_str}).items
	if items:
		count = items[0].get("count")
	else:
		count = 0
	return count


def update_one_link_count(random_str: str):
	response = db.fetch({"short_url": random_str})
	response.items[0]["count"] += 1
	return db.put(response.items[0], response.items[0]["key"])


def delete_one_link():
	...