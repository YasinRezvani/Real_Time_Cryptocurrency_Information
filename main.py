import requests
import time
from beautifultable import BeautifulTable

table = BeautifulTable()
localtime = time.asctime(time.localtime(time.time()))
print("\n--- "+localtime+" ---")
url = "https://api.coinlore.net/api/tickers/?start=0&limit=11"
res = requests.get(url).json()

for i in range(0 , 10):
    table.rows.append([res['data'][i]['name'], res['data'][i]['price_usd']])



table.columns.header = ["Name","Price"]
table.rows.header = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
print(table)
input()

# Made By Yasin Rezvani