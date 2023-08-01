import allure

from helpers.request_services import rpc_request


class Addresses:
    def __init__(self, url, session):
        self.url = url
        self.session = session

    @allure.step
    def addresses_list(self):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.addresses.list",
                               "params": {
                                   "page": 1,
                                   "page_size": 10
                               }
                           })

    @allure.step
    def addresses_suggest(self,
                          city: str = None,
                          region: str = None,
                          area: str = None,
                          zip_code: str = None,
                          street: str = None,
                          building: str = None):

        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.addresses.suggest",
                               "params": {
                                   "city": city,
                                   "region": region,
                                   "area": area,
                                   "zip_code": zip_code,
                                   "street": street,
                                   "building": building
                               }
                           })

    @allure.step
    def addresses_create(self,
                         fias_id: str,
                         city: str = None,
                         region: str = None,
                         area: str = None,
                         zip_code: str = None,
                         street: str = None,
                         building: str = None,
                         suite: str = None,
                         entrance: str = None,
                         floor: str = None,
                         enter_code: str = None,
                         comments: str = None):

        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.addresses.create",
                               "params": {
                                   "fias_id": fias_id,
                                   "city": city,
                                   "region": region,
                                   "area": area,
                                   "zip_code": zip_code,
                                   "street": street,
                                   "building": building,
                                   "suite": suite,
                                   "entrance": entrance,
                                   "floor": floor,
                                   "enter_code": enter_code,
                                   "comments": comments,
                                   "frontend_metadata": {}
                               }
                           })

    @allure.step("Вернуть адрес по address_id")
    def addresses_get(self, address_id):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.addresses.get",
                               "params": {
                                   "address_id": address_id
                               }
                           })

    @allure.step("Изменить адрес")
    def addresses_update(self,
                         address_id: str,
                         suite: str,
                         entrance: str,
                         floor: str,
                         enter_code: str,
                         comments: str):

        """
        data must not contain
        {'area', 'building', 'region', 'street', 'city', 'zip_code'} properties
        """

        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.addresses.update",
                               "params": {
                                   "address_id": address_id,
                                   "suite": suite,
                                   "entrance": entrance,
                                   "floor": floor,
                                   "enter_code": enter_code,
                                   "comments": comments,
                                   "frontend_metadata": {}
                               }
                           })

    @allure.step("Удалить адрес")
    def addresses_delete(self, address_id):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "customer.addresses.delete",
                               "params": {
                                   "address_id": address_id
                               }
                           })

    @allure.step("Удалить все адреса клиента")
    def addresses_m_delete(self):
        address_list = []

        rsp = self.addresses_list()
        for data in rsp['result']['data']:
            address_id = data['id']
            address_list.append(address_id)

        if address_list:
            for address in address_list:
                self.addresses_delete(address_id=address)
