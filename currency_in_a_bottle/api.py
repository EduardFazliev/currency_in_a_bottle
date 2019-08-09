import bottle
import json
import datetime
import requests
from bottle import request, response, post
from bottle_rest import json_to_params

API_KEY='a28ec5e77b508be1ea54'
API='https://free.currconv.com/api/v7/convert?q={0}_{1}&compact=ultra&date={2}&apiKey={3}'


@post('/api/rate/transfer')
@json_to_params() 
def listing_handler(currency_code, date=None):
    requests.packages.urllib3.disable_warnings()
    
    if date is None:
        date = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        
    r = requests.get(API.format(currency_code, 'RUB', date, API_KEY), verify=False)
    result = r.json()
    print(result)
    rate = result[currency_code+'_RUB'][date]
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return {"code": currency_code, "rate": rate, "date": date}

app = application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(host = '127.0.0.1', port = 8000)