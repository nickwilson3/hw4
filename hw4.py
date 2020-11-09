import requests
from bs4 import BeautifulSoup
import json

keyword = 'shoes'
headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
results = []
for i in range(11):
    r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword+'&_pgn='+str(i+1), headers=headers)
    print('status_code=',r.status_code)
    print('page number = ', str(i+1))

    soup = BeautifulSoup(r.text, 'html.parser')
    #print('r.text=',r.text)

    boxes = soup.select('.clearfix.s-item__wrapper')
    for box in boxes:

        result = {}
        names = box.select('.s-item__title')
        for name in names:
            result['name'] = name.text
        prices = box.select('.s-item__price')
        for price in prices:
            result['price'] = price.text
        secondary_info = box.select('.SECONDARY_INFO')
        for status in secondary_info:
            result['status'] = status.text
        results.append(result)
    print('len(results)=',len(results))


j = json.dumps(results)
with open('items.json','w') as f:
    f.write(j)



