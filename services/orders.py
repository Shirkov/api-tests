import allure
from helpers.initial_data import DeliveryType, PaymentType, Contact

from helpers.request_services import rpc_request
from services.search import Search
from settings.env_config import settings


class Orders:
    def __init__(self, url, session):
        self.url = url
        self.session = session

    @allure.step
    def calculate(self, city_fias_id: str, channel_id: str, item_id: str, quantity: int = 1):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.orders.calculate",
                               "params": {
                                   "city_fias_id": city_fias_id,
                                   "channel_id": channel_id,
                                   "items": [
                                       {"id": item_id, "quantity": quantity}
                                   ]
                               }
                           })

    @allure.step
    def stores_list(self, city_id: str, item_id: str, quantity: int = 1):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.orders.stores.list",
                               "params": {
                                   "city_id": city_id,
                                   "total": None,
                                   "items": [
                                       {"id": item_id, "quantity": quantity}
                                   ]
                               }
                           })

    @allure.step
    def retry_stores_list(self, count_retry: int, city_id: str, count_items: int = 1, quantity: int = 1):
        search = Search(url=settings.search.search_url)

        while count_retry > 0:
            item_id_list = search.get_random_item_id_list(count=count_items)
            item_id = item_id_list[0]
            rsp = self.stores_list(city_id=city_id,
                                   item_id=item_id,
                                   quantity=quantity)

            if rsp.get("result", []):
                return rsp

            else:
                count_retry -= 1
                continue

    @allure.step
    def pickups_list(self, city_id: str, item_id: str, quantity: int = 1):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.orders.pickups.list",
                               "params": {
                                   "city_id": city_id,
                                   "total": 2012.0,
                                   "items": [
                                       {"id": item_id, "quantity": quantity}
                                   ]
                               }
                           })

    @allure.step
    def retry_pickups_list(self, count_retry: int, city_id: str, count_items: int = 1, quantity: int = 1):
        search = Search(url=settings.search.search_url)

        while count_retry > 0:
            item_id_list = search.get_random_item_id_list(count=count_items)
            item_id = item_id_list[0]
            rsp = self.pickups_list(city_id=city_id,
                                    item_id=item_id,
                                    quantity=quantity)

            if rsp.get("result", []):
                return rsp

            else:
                count_retry -= 1
                continue

    @allure.step("Получение списка адресов")
    def orders_list(self):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.orders.list",
                               "params": {"page": 1,
                                          "page_size": 100,
                                          "client_type": "site"}
                           })

    @allure.step
    def couriers_list(self, city_id: str, zip_code: str, street: str, building: str, fias_id: str, item_id: str,
                      quantity: int = 1):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.orders.couriers.list",
                               "params": {
                                   "city_id": city_id,
                                   "total": 2012.0,
                                   "items": [
                                       {"id": item_id, "quantity": quantity}
                                   ],
                                   "zip_code": zip_code,
                                   "street": street,
                                   "building": building,
                                   "fias_id": fias_id
                               }
                           })

    def retry_couriers_list(self, count_retry: int, city_id: str, zip_code: str, street: str, building: str,
                            fias_id: str, quantity: int = 1, count_items: int = 1):
        search = Search(url=settings.search.search_url)

        while count_retry > 0:
            item_id_list = search.get_random_item_id_list(count=count_items)
            item_id = item_id_list[0]
            rsp = self.couriers_list(city_id=city_id,
                                     zip_code=zip_code,
                                     street=street,
                                     building=building,
                                     fias_id=fias_id,
                                     item_id=item_id,
                                     quantity=quantity)

            if rsp.get("result", []):
                return item_id, rsp

            else:
                count_retry -= 1
                continue

    def get_orders_id_list(self):
        orders_list = []
        rsp = self.orders_list()
        for order in rsp["result"]["data"]:
            orders_list.append(order["order"]["id"])

        return orders_list

    @allure.step
    def get_orders_by_id(self, order_id: str):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.orders.get",
                               "params": {
                                   "order_id": order_id,
                                   "client_type": "site"
                               }
                           })

    @allure.step
    def create_order_courier_cod(self, delivery_id: str, city_fias_id: str, city_id: str, address_id: str, item_id: str,
                                 quantity: str = 1):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.orders.create",
                               "params": {
                                   "delivery_type": DeliveryType.delivery,
                                   "delivery_id": delivery_id,
                                   "city_fias_id": city_fias_id,
                                   "city_id": city_id,
                                   "payment_type": PaymentType.cod,
                                   "address_id": address_id,
                                   "items": [
                                       {"id": item_id, "quantity": quantity}
                                   ],
                                   "email": Contact.email,
                                   "phone": Contact.phone,
                                   "first_name": Contact.first_name,
                                   "last_name": Contact.last_name,
                                   "comments": "comment_order",
                                   "call_requested": False,
                                   "client_type": "site",
                                   "frontend_metadata": {}
                               }
                           })

    @allure.step
    def cancel(self, order_id: str, reason_id: str):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.orders.cancel",
                               "params": {
                                   "order_id": order_id,
                                   "reason_id": reason_id
                               }
                           })
