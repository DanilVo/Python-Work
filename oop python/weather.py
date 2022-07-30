# import requests
# from pprint import PrettyPrinter

# printer = PrettyPrinter()

# API_KEY1 = "1353ad9c7af9a94f3f41d52e1c656a22abdba01ba8094ab0cfe3609c7385cc92"
# url = "https://api.ambeedata.com/weather/latest/by-lat-lng"


# querystring = {"lat":"12.9889055","lng":"77.574044"}
# headers = {
#     'x-api-key': f'{API_KEY1}',
#     'Content-type': "application/json"
#     }
# response = requests.request("GET", url, headers=headers, params=querystring).json()
# printer.pprint(round(((response['data']['apparentTemperature'])-32)*5/9))


import requests

API_KEY = "AIzaSyCeudtE8Z-ocATSKSm7YuRYQ6UiJlM6LFg"
