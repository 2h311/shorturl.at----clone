from deta import Deta

from config import settings


deta = Deta(settings.PROJECT_DATABASE_KEY)

shortlink_document_db = deta.Base(settings.PROJECT_SHORTLINK_DOCUMENT_DB)
report_document_db = deta.Base(settings.PROJECT_REPORT_DOCUMENT_DB)


class ShortLinkSchema(Enum):
	short_url: str
	long_url: str
	count: int = 0


class ReportedURLs:
	reported_url: str
	comment: str


def create_new_link(data: ShortLinkSchema):
	return db.put(data)


def read_one_link(random_str: str):
	response = db.fetch({"short_url": random_str})
	if response:
		response = next(response)
	return response


def read_one_link_count(random_str: str):
	response = db.fetch({"short_url": random_str})
	if response:
		count = next(response)[0].get("count")
	else:
		count = 0
	return count


def update_one_link_count(random_str: str):
	response = db.fetch({"short_url": random_str})
	if response:
		item = next(response)
		print("update_one_link_count: ", item)
		item[0]["count"] += 1
	return db.put(item[0], item[0]["key"])


def delete_one_link():
	...