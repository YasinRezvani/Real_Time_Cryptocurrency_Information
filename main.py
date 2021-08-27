import requests
import time
from beautifultable import BeautifulTable

table = BeautifulTable()
localtime = time.asctime(time.localtime(time.time()))
print("\n--- "+localtime+" ---")
url = "https://api.coinlore.net/api/tickers/?start=0&limit=11"
res = requests.get(url).json()