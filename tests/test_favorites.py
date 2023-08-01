import time

import allure
import pytest


@allure.epic("Тесты на избранное")
class TestFavorite:

    @pytest.fixture(autouse=True)
    def setup(self, app):
        self.app = app

    @allure.description("Добавление товаров в избранное."
                        "Проверяется, что список избранного не пустой")
    def test_add_favorite(self, clear_favorites):
        count_items = 2

        item_id_list = self.app.search.get_random_item_id_list(count=count_items)

        rsp = self.app.favorites.favorites_add(items=item_id_list)
        result = rsp["result"]

        assert result != []
        assert len(result) == count_items

    @allure.description("Показать список избранного"
                        "Проверяется, что список не пустой, "
                        "количество добавленых товаров совпадает с количеством товаров в списке")
    def test_get_favorite(self, clear_favorites):
        count_items = 2

        item_id_list = self.app.search.get_random_item_id_list(count=count_items)

        self.app.favorites.favorites_add(items=item_id_list)
        rsp = self.app.favorites.favorites_get()
        result = rsp["result"]

        assert result != []
        assert len(result) == count_items

    @allure.description("Заменить товар в избранном"
                        "Проверяется, что последний товар заменил первый товар")
    def test_replace_favorite(self, clear_favorites):
        count_items = 2

        item_id_list = self.app.search.get_random_item_id_list(count=count_items)

        self.app.favorites.favorites_add(items=[item_id_list[0]])
        rsp = self.app.favorites.favorites_replace(items=[item_id_list[1]])
        result = rsp["result"]

        assert result == [item_id_list[1]]

    @allure.description("Удалить товар из избранного"
                        "Проверяется, что удаленного товара нет в избранном")
    def test_remove_favorite(self, clear_favorites):
        count_items = 2

        item_id_list = self.app.search.get_random_item_id_list(count=count_items)

        self.app.favorites.favorites_add(items=item_id_list)
        rsp = self.app.favorites.favorites_remove(items=[item_id_list[0]])
        result = rsp["result"]

        assert result == [item_id_list[1]]

    @allure.description("Очистить избранное"
                        "Проверяется, что список избранного пустой")
    def test_clear_all_favorite(self, clear_favorites):
        count_items = 2

        item_id_list = self.app.search.get_random_item_id_list(count=count_items)

        self.app.favorites.favorites_add(items=item_id_list)
        rsp = self.app.favorites.favorites_clear()
        result = rsp["result"]

        assert result == []
