import pytest as pytest
from models_response.auth.auth_login import AuthSysLoginRsp

from settings.env_config import settings
import allure


@allure.epic("Тесты на авторизацию пользователя")
class TestAuth:

    @pytest.fixture(autouse=True)
    def setup(self, app_sys, app):
        self.app_sys = app_sys
        self.app = app

    @allure.description("Авторизация системного пользователя")
    def test_sys_auth(self):
        rsp = self.app_sys.sys_auth.login(login=settings.cms.cms_sys_login,
                                          password=settings.cms.cms_sys_password)

        assert AuthSysLoginRsp(**rsp["result"])

    @allure.description("Выход системного пользователя")
    def test_sys_logout(self):
        rsp = self.app_sys.sys_auth.logout()
        self.app_sys.sys_auth.login(login=settings.cms.cms_sys_login, password=settings.cms.cms_sys_password)

        assert rsp["result"] is None

    @allure.description("Авторизация обычного пользователя")
    def test_customer_auth(self):
        rsp = self.app.customer_auth.customer_verify(password=settings.cms.cms_password)

        assert rsp["result"]["verified"] is True

    @allure.description("Выход обычного пользователя")
    def test_customer_logout(self):
        rsp = self.app.customer_auth.customer_logout()
        self.app.customer_auth.customer_login(login=settings.cms.cms_login)
        self.app.customer_auth.customer_verify(password=settings.cms.cms_password)

        assert rsp["result"] is True
