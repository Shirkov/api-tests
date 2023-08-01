import allure
from helpers.request_services import rpc_request


class SysAuth:
    def __init__(self, url, session):
        self.url = url
        self.session = session

    @allure.step
    def login(self, login, password):
        """Авторизация клиента"""
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "auth.login",
                               "params": {
                                   "username": login,
                                   "password": password
                               }
                           })

    @allure.step
    def logout(self):
        """Выход клиента"""
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "auth.logout"})

    @allure.step
    def order_m_delete(self, order_id):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "orders.m_delete",
                               "params": {
                                   "id": order_id,
                               }
                           })

    def get_session(self):
        """Получить сессию"""
        return self.session


class CustomerAuth:
    def __init__(self, url, session):
        self.url = url
        self.session = session

    @allure.step
    def customer_login(self, login):
        """Авторизация клиента"""
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.login",
                               "params": {
                                   "login": login,
                                   "profile": {
                                       "some_value": True
                                   }}
                           })

    @allure.step
    def customer_verify(self, password):
        """Авторизация клиента"""
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.verify",
                               "params": {
                                   "code": password
                               }
                           })

    @allure.step
    def customer_logout(self):
        """Выход клиента"""
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.logout"})

    def get_session(self):
        """Получить сессию"""
        return self.session
