from requests import Request, Session
import json, pprint
from api_key import api_key 


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


headers = {
   'Accepts':'application/json',
   'X-CMC_PRO_API_KEY':api_key,
 }

session = Session()
session.headers.update(headers)

res = session.get(url)
data = json.loads(res.text)
# pprint.pprint(data['data'])

i = 0
top_ten_list = []

while i < 50:
  coin_data = data['data'][i]
  top_ten_list.append(coin_data)
  i += 1