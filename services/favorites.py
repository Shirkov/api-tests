import allure

from helpers.request_services import rpc_request


class Favorites:
    def __init__(self, url, session):
        self.url = url
        self.session = session

    @allure.step
    def favorites_get(self):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.favorites.get"
                           })

    @allure.step
    def favorites_clear(self):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.favorites.clear"
                           })

    @allure.step
    def favorites_add(self, items: list):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.favorites.add",
                               "params": {
                                   "items": items
                               }
                           })

    @allure.step
    def favorites_remove(self, items: list):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.favorites.remove",
                               "params": {
                                   "items": items
                               }
                           })

    @allure.step
    def favorites_replace(self, items: list):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.favorites.replace",
                               "params": {
                                   "items": items
                               }
                           })
