from deta import Deta

from config import Settings


deta = Deta(Settings.PROJECT_DETABASE_KEY)
# db = deta.Base()