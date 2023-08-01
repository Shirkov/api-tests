from services.addresses import Addresses
from services.auth import SysAuth, CustomerAuth
from services.cart import Cart
from services.favorites import Favorites
from services.orders import Orders
from services.search import Search
from settings.env_config import settings


class AppSys:
    """ Сервисы CMS c админской авторизацией"""

    def __init__(self, session):
        self.sys_auth = SysAuth(url=settings.cms.cms_url, session=session)


class App:
    """ Сервисы CMS с пользовательской  авторизацией"""

    def __init__(self, session):
        self.customer_auth = CustomerAuth(url=settings.cms.cms_url, session=session)
        self.favorites = Favorites(url=settings.cms.cms_url, session=session)
        self.search = Search(url=settings.search.search_url)
        self.cart = Cart(url=settings.cms.cms_url, session=session)
        self.addresses = Addresses(url=settings.cms.cms_url, session=session)
        self.orders = Orders(url=settings.cms.cms_url, session=session)
