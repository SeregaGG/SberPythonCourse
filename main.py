import requests
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/Население_Земли'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
r = requests.get(url, headers=headers)
resp = requests.get(url, headers=headers)
print(resp.status_code)
bsbs = BeautifulSoup(resp.text, 'html.parser')

print(bsbs.find('table', attrs={'class': ['standart', 'sortable', 'jquery-tablesorter']}))
