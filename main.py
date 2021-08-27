import requests
import time
from beautifultable import BeautifulTable

table = BeautifulTable()
localtime = time.asctime(time.localtime(time.time()))
print("\n--- "+localtime+" ---")
url = "https://api.coinlore.net/api/tickers/?start=0&limit=11"
res = requests.get(url).json()

table.rows.append([res['data'][0]['name'], res['data'][0]['price_usd']])
table.rows.append([res['data'][1]['name'], res['data'][1]['price_usd']])
table.rows.append([res['data'][2]['name'], res['data'][2]['price_usd']])
table.rows.append([res['data'][3]['name'], res['data'][3]['price_usd']])
table.rows.append([res['data'][4]['name'], res['data'][4]['price_usd']])
table.rows.append([res['data'][5]['name'], res['data'][5]['price_usd']])
table.rows.append([res['data'][6]['name'], res['data'][6]['price_usd']])
table.rows.append([res['data'][7]['name'], res['data'][7]['price_usd']])
table.rows.append([res['data'][8]['name'], res['data'][8]['price_usd']])
table.rows.append([res['data'][9]['name'], res['data'][9]['price_usd']])


table.columns.header = ["Name","Price"]
table.rows.header = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
print(table)
input()

# Made By Yasin Rezvani