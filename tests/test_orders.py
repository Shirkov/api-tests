import allure
import pytest
from helpers.initial_data import Address, CityChannelId
from models_response.orders.calculate_rsp import CalculateRsp
from models_response.orders.courier_list_rsp import CourierRsp
from models_response.orders.orders_list_rsp import OrdersListRsp
from models_response.orders.orders_rsp import OrdersRsp
from models_response.orders.pickups_list_rsp import PickupsRsp
from models_response.orders.stores_list_rsp import StoresRsp


@allure.epic("Тесты на обработку заказа")
@pytest.mark.usefixtures("delete_orders")
class TestOrders:

    @pytest.fixture(autouse=True)
    def setup(self, app):
        self.app = app

    @allure.description("Расчет корзины"
                        "Проверяется, что возвращается ответ калькуляции")
    def test_calculate_cart_total_value(self, addresses_delete, addresses_suggest):
        count_items = 1

        item_id_list = self.app.search.get_random_item_id_list(count=count_items)

        suggest_rsp = addresses_suggest
        city_fias_id = suggest_rsp["result"][0]["city_fias_id"]
        item_id = item_id_list[0]
        rsp = self.app.orders.calculate(city_fias_id=city_fias_id,
                                        channel_id=CityChannelId.moscow,
                                        item_id=item_id,
                                        quantity=1)

        assert CalculateRsp(**rsp["result"])

    @pytest.mark.skip("Ждем настройку магазинов")
    @allure.description("Список доступных магазинов"
                        "Проверяется, что возвращается список магазинов")
    def test_list_available_stores(self, addresses_delete, address_create):
        count_items = 1
        count_retry = 10

        address_create_rsp = address_create
        city_id = address_create_rsp["result"]["city_id"]

        rsp = self.app.orders.retry_stores_list(count_retry=count_retry,
                                                city_id=city_id,
                                                count_items=count_items)

        assert StoresRsp(**rsp["result"][0])
        assert rsp["result"] != []

    @pytest.mark.skip("Ждем настройку пунктов")
    @allure.description("Список доступных пунктов выдачи"
                        "Проверяется, что возвращается список пунктов")
    def test_list_available_pickup_points(self, addresses_delete, address_create):
        count_items = 1
        count_retry = 10

        address_create_rsp = address_create

        city_id = address_create_rsp["result"]["city_id"]
        rsp = self.app.orders.retry_pickups_list(count_items=count_items,
                                                 count_retry=count_retry,
                                                 city_id=city_id)

        assert PickupsRsp(**rsp["result"][0])
        assert rsp["result"] != []

    @pytest.mark.skip("Ждем настройку курьерских слотов доставки")
    @allure.description("Список доступных слотов курьерской доставки"
                        "Проверяется, что возвращается список доступных слотов на доставку курьером")
    def test_list_available_courier_slots(self, addresses_delete, addresses_suggest, address_create):
        count_items = 1
        count_retry = 10

        suggest_rsp = addresses_suggest
        fias_id = suggest_rsp["result"][0]["fias_id"]
        address_create_rsp = address_create

        city_id = address_create_rsp["result"]["city_id"]
        _, rsp = self.app.orders.retry_couriers_list(count_retry=count_retry,
                                                     count_items=count_items,
                                                     city_id=city_id,
                                                     zip_code=Address.zip_code,
                                                     street=Address.street,
                                                     building=Address.building,
                                                     fias_id=fias_id)

        assert CourierRsp(**rsp["result"][0])
        assert rsp["result"] != []

    @allure.description("Создание заказа с доставкой курьером, оплата наличными. "
                        "Проверяется, что есть id заказа")
    @pytest.mark.skip("Пока на паузе")
    def test_create_order_courier_cod(self, addresses_delete, addresses_suggest, address_create):
        count_items = 1
        count_retry = 10

        suggest_rsp = addresses_suggest
        fias_id = suggest_rsp["result"][0]["fias_id"]

        address_create_rsp = address_create
        city_id = address_create_rsp["result"]["city_id"]
        city_fias_id = address_create_rsp["result"]["ext_data"]["city"]["fiasId"]
        address_id = address_create_rsp["result"]["id"]

        item_id, couriers_list = self.app.orders.retry_couriers_list(count_retry=count_retry,
                                                                     count_items=count_items,
                                                                     city_id=city_id,
                                                                     zip_code=Address.zip_code,
                                                                     street=Address.street,
                                                                     building=Address.building,
                                                                     fias_id=fias_id)

        delivery_id = couriers_list["result"][0]["id"]
        rsp = self.app.orders.create_order_courier_cod(delivery_id=delivery_id,
                                                       address_id=address_id,
                                                       city_fias_id=city_fias_id,
                                                       city_id=city_id,
                                                       item_id=item_id)

        assert rsp["result"]["order"]["id"]

    @allure.description("Показать список заказов пользователя"
                        "Проверяется, что есть список с заказами")
    @pytest.mark.skip("Пока на паузе")
    def test_get_orders_list(self):
        rsp = self.app.orders.orders_list()

        assert OrdersListRsp(**rsp["result"])

    @allure.description("Показать заказ по его id. "
                        "Проверяется, что отдается структура заказа,"
                        "что id запрашиваемого заказа соответствует id полученого заказа. ")
    @pytest.mark.skip("На проде заказы не создаем")
    def test_get_order_by_order_id(self):
        order_list = self.app.orders.orders_list()
        order_id = order_list["result"]["data"][0]["order"]["id"]

        rsp = self.app.orders.get_orders_by_id(order_id=order_id)
        order = rsp["result"]["order"]

        assert OrdersRsp(**order)
        assert order_id == order["id"]
