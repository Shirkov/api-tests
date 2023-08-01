import pytest as pytest
import requests
from helpers.initial_data import Address, CancelReasons
from services.addresses import Addresses
from services.app import AppSys, App
from services.auth import SysAuth, CustomerAuth
from services.cart import Cart
from services.favorites import Favorites
from services.orders import Orders
from settings.env_config import settings


@pytest.fixture(scope="session", autouse=True)
def sys_auth():
    """Авторизация системного пользователя"""
    session = requests.Session()
    auth = SysAuth(url=settings.cms.cms_url, session=session)
    auth.login(login=settings.cms.cms_sys_login,
               password=settings.cms.cms_sys_password)

    yield auth.get_session()
    auth.logout()


@pytest.fixture(scope="session", autouse=True)
def app_sys(sys_auth):
    """Инициализация системных сервисов """
    return AppSys(sys_auth)


@pytest.fixture(scope="session", autouse=True)
def auth():
    """Авторизация обычного пользователя"""
    session = requests.Session()
    auth = CustomerAuth(url=settings.cms.cms_url, session=session)
    auth.customer_login(login=settings.cms.cms_login)
    verify_rsp = auth.customer_verify(password=settings.cms.cms_password)

    assert verify_rsp["result"]["verified"] is True

    yield auth.get_session()
    auth.customer_logout()


@pytest.fixture(scope="session", autouse=True)
def app(auth):
    """Инициализация пользовательских сервисов """
    return App(auth)


@pytest.fixture()
def clear_favorites(auth):
    Favorites(url=settings.cms.cms_url, session=auth).favorites_clear()


@pytest.fixture()
def clear_cart(auth):
    Cart(url=settings.cms.cms_url, session=auth).cart_clear()


@pytest.fixture()
def addresses_delete(auth):
    """Удаление ранее созданных адресов"""
    address = Addresses(url=settings.cms.cms_url, session=auth)
    address.addresses_m_delete()


@pytest.fixture()
def addresses_suggest(auth):
    address = Addresses(url=settings.cms.cms_url, session=auth)
    suggest_rsp = address.addresses_suggest(city=Address.city,
                                            region=Address.region,
                                            area=Address.area,
                                            zip_code=Address.zip_code,
                                            street=Address.street,
                                            building=Address.building)

    return suggest_rsp


@pytest.fixture()
def address_create(auth, addresses_suggest):
    address = Addresses(url=settings.cms.cms_url, session=auth)
    suggest_rsp = addresses_suggest

    fias_id = suggest_rsp["result"][0]["fias_id"]
    address_rsp = address.addresses_create(fias_id=fias_id,
                                           city=Address.city,
                                           region=Address.region,
                                           area=Address.area,
                                           zip_code=Address.zip_code,
                                           street=Address.street,
                                           building=Address.building,
                                           suite=Address.suite,
                                           entrance=Address.entrance,
                                           floor=Address.floor,
                                           enter_code=Address.enter_code,
                                           comments=Address.comments)

    return address_rsp


@pytest.fixture(scope="class")
def delete_orders(auth, sys_auth):
    """Отмена всех заказов и последующее их удаление из аккаунта"""
    yield
    orders = Orders(url=settings.cms.cms_url, session=auth)
    orders_id_list = orders.get_orders_id_list()
    if orders_id_list:
        for order_id in orders_id_list:
            orders.cancel(order_id=order_id, reason_id=CancelReasons.other)
        sys_cms = SysAuth(url=settings.cms.cms_url, session=sys_auth)
        sys_cms.order_m_delete(order_id=orders_id_list)
