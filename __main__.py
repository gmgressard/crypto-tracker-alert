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
# pprint.pprint(data)

# i = 0 #refers to position in list of dictionaries of cryptocurrencies 

name = data['data'][0]['name']
symbol = data['data'][0]['symbol']
rank = data['data'][0]['cmc_rank']
price = data['data'][0]['quote']['USD']['price']



