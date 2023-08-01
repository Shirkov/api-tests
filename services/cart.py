import allure

from helpers.request_services import rpc_request


class Cart:
    def __init__(self, url, session):
        self.url = url
        self.session = session

    @allure.step
    def cart_get(self):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.cart.get"
                           })

    @allure.step
    def cart_clear(self):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.cart.clear"
                           })

    @allure.step
    def cart_add(self, item: str, quantity: int):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.cart.add",
                               "params": {
                                   "items": [
                                       {"id": item, "quantity": quantity}
                                   ]
                               }
                           })

    @allure.step
    def cart_remove(self, item: str, quantity: int):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.cart.remove",
                               "params": {
                                   "items": [
                                       {"id": item, "quantity": quantity}
                                   ]
                               }
                           })

    @allure.step
    def cart_replace(self, item: str, quantity: int):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.cart.replace",
                               "params": {
                                   "items": [
                                       {"id": item, "quantity": quantity}
                                   ]
                               }
                           })
