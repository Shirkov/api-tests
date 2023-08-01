import pytest as pytest
from helpers.initial_data import Address, AddressUpdate
from models_response.addresses.addresses_create_rsp import AddressesCreateRsp
from models_response.addresses.addresses_suggest_rsp import AddressesSuggestRsp

import allure


@allure.epic("Тесты на адреса пользователя")
class TestAddresses:

    @pytest.fixture(autouse=True)
    def setup(self, app):
        self.app = app

    @allure.description("Заведение адреса.")
    def test_suggest_address(self):
        rsp = self.app.addresses.addresses_suggest(city=Address.city,
                                                   region=Address.region,
                                                   area=Address.area,
                                                   zip_code=Address.zip_code,
                                                   street=Address.street,
                                                   building=Address.building
                                                   )

        assert AddressesSuggestRsp(**rsp["result"][0])

    @allure.description("Создание адреса."
                        "Проверяется что возвращается адрес со всеми атрибутами")
    def test_create_address(self, addresses_delete, address_create):
        rsp = address_create

        assert AddressesCreateRsp(**rsp["result"])

    @allure.description("Вернуть список созданных адресов."
                        "Проверяется что возвращается список адресов со всеми атрибутами адреса")
    def test_get_address_list(self, addresses_delete, address_create):
        rsp = self.app.addresses.addresses_list()

        assert AddressesCreateRsp(**rsp["result"]["data"][0])

    @allure.description("Вернуть адрес по address_id."
                        "Проверяется что возвращается адрес со всеми атрибутами адреса,"
                        "id вернувшегося адреса = address_id ")
    def test_get_address(self, addresses_delete, address_create):
        address_create_rsp = address_create

        address_id = address_create_rsp["result"]["id"]
        address_get_rsp = self.app.addresses.addresses_get(address_id=address_id)

        assert AddressesCreateRsp(**address_get_rsp["result"])
        assert address_id == address_get_rsp["result"]["id"]

    @allure.description("Обновить адрес. "
                        "Проверяются обновленные поля адреса")
    def test_update_address(self, addresses_delete, address_create):
        address_create_rsp = address_create

        address_id = address_create_rsp["result"]["id"]
        rsp = self.app.addresses.addresses_update(address_id=address_id,
                                                  suite=AddressUpdate.suite,
                                                  entrance=AddressUpdate.entrance,
                                                  floor=AddressUpdate.floor,
                                                  enter_code=AddressUpdate.enter_code,
                                                  comments=AddressUpdate.comments)

        address = AddressesCreateRsp(**rsp["result"])

        assert address.id == address_id
        assert address.suite == AddressUpdate.suite
        assert address.entrance == AddressUpdate.entrance
        assert address.floor == AddressUpdate.floor
        assert address.enter_code == AddressUpdate.enter_code
        assert address.comments == AddressUpdate.comments

    @allure.description("Удаление адреса."
                        "Проверяется что список адресов пуст")
    def test_delete_address(self, addresses_delete, address_create):
        address_create_rsp = address_create

        address_id = address_create_rsp["result"]["id"]
        self.app.addresses.addresses_delete(address_id=address_id)

        address_list_rsp = self.app.addresses.addresses_list()

        assert address_list_rsp["result"]["data"] == []
