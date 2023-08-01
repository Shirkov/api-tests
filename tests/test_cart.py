import allure
import pytest
from models_response.cart.cart_rsp import CartRsp


@allure.epic("Тесты на корзину")
class TestCart:

    @pytest.fixture(autouse=True)
    def setup(self, app):
        self.app = app

    @allure.description("Добавление товаров в корзину."
                        "Проверяется, что возвращается словарь корзины с товарами")
    def test_add_cart(self, clear_cart):
        count_items = 1
        quantity = 2

        item_id_list = self.app.search.get_random_item_id_list(count=count_items)

        rsp = self.app.cart.cart_add(item=item_id_list[0], quantity=quantity)
        result = rsp["result"]

        assert CartRsp(**result[0])

    @allure.description("Показать корзину с товарами."
                        "Проверяется, что возвращается словарь корзины с товарами")
    def test_get_cart(self, clear_cart):
        count_items = 1
        quantity = 2

        item_id_list = self.app.search.get_random_item_id_list(count=count_items)

        rsp = self.app.cart.cart_add(item=item_id_list[0], quantity=quantity)
        rsp = self.app.cart.cart_get()
        result = rsp["result"]

        assert CartRsp(**result[0])

    @allure.description("Удалить товар из корзины."
                        "Проверяется, что возвращается пустой список корзины")
    def test_remove_cart(self, clear_cart):
        count_items = 1
        quantity = 2

        item_id_list = self.app.search.get_random_item_id_list(count=count_items)

        self.app.cart.cart_add(item=item_id_list[0], quantity=quantity)
        rsp = self.app.cart.cart_remove(item=item_id_list[0], quantity=quantity)
        result = rsp["result"]

        assert result == []

    @allure.description("Заменить товар в корзине."
                        "Проверяется, что возвращается список с замененным товаром")
    def test_replace_cart(self, clear_cart):
        count_items = 2
        quantity = 2

        item_id_list = self.app.search.get_random_item_id_list(count=count_items)

        self.app.cart.cart_add(item=item_id_list[0], quantity=quantity)
        rsp = self.app.cart.cart_replace(item=item_id_list[1], quantity=quantity)
        result = rsp["result"]
        cart_rsp = CartRsp(**result[0])

        assert [cart_rsp.id] == [item_id_list[1]]

    @allure.description("Очистка корзины."
                        "Проверяется, что возвращается пустой список корзины")
    def test_clear_cart(self, clear_cart):
        count_items = 1

        item_id_list = self.app.search.get_random_item_id_list(count=count_items)

        self.app.cart.cart_add(item=item_id_list[0], quantity=2)
        rsp = self.app.cart.cart_clear()
        result = rsp["result"]

        assert result == []
