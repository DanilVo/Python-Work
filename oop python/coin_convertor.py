from requests import *
from pprint import PrettyPrinter

API_KEY = "c9eb178fc5fe011578b4"
BASE_URL = "https://api.currconv.com"
ALL_JSON = f"/api/v7/convert?q=USD_PHP,PHP_USD&compact=ultra&apiKey={[API_KEY]}"

printer = PrettyPrinter()

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    printer.pprint(data)
get_links()