from settings.env_config import settings


class Address:
    city = "Москва"
    region = ""
    area = ""
    zip_code = "115446"
    street = "Каширское Шоссе"
    building = "23"
    suite = "120"
    entrance = "3"
    floor = "5"
    enter_code = "domofone"
    comments = "autotest"
    frontend_metadata = {}


class AddressUpdate:
    suite = "122"
    entrance = "5"
    floor = "7"
    enter_code = "tuk-tuk"
    comments = "autotest_update"
    frontend_metadata = {}


class CityChannelId:
    moscow = "20"
    yekaterinburg = "0"
    st_petersburg = "15"


class Contact:
    first_name = "test_first_name"
    last_name = "test_last_name"
    phone = settings.cms.cms_login
    email = "test@mail.com"


class DeliveryType:
    delivery = "delivery"
    pickup = "pickup"
    store = "store"


class PaymentType:
    cod = "cod"


class CancelReasons:
    other = "other"
