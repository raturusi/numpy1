from pathlib import Path
import requests

url = "https://5ka.ru/api/v2/special_offers/"
#url = "https://5ka.ru/special_offers/"
param = {
    "page": 1,
    "categories": None,
    "orderring": None,
    "records_per_page": 50
}
headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}
#html_temp = Path(__file__).parent.joinpath("temp.html")
response = requests.get(url, params=param, headers=headers)

json_temp = Path(__file__).parent.joinpath("temp.json")
json_temp.write_text(response.text, encoding="UTF-8")
#html_temp.write_bytes(response.content)