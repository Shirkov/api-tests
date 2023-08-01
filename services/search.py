import allure
from helpers.initial_data import CityChannelId

from helpers.request_services import rpc_request
import requests
from settings.env_config import settings
import random


class Search:
    def __init__(self, url):
        self.url = url
        self.session = requests.session()

    @allure.step
    def query_grid(self, with_stocks: bool = True):
        return rpc_request(url=self.url,
                           session=self.session,
                           params={
                               "method": "Query.grid",
                               "params": {
                                   "engine": settings.search.engine,
                                   "fields": ["id", "link"],
                                   "with_stocks": with_stocks,
                                   "filters": {
                                       "category": ["hity-prodazh"]
                                   }
                               }
                           })

    @allure.step
    def get_random_item_id_list(self, count: int = 1):
        item_id_list = set()

        grid = self.query_grid()
        for items in grid["result"]["data"]:
            for item in items["items"]:
                item_id_list.add(item["id"])

        result = random.sample(list(item_id_list), k=count)

        return result

