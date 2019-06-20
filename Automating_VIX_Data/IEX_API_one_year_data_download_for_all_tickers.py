import requests
import json 


list_of_stocks = ['IVV', 'RSP', 'SCHX', 'SPY', 'VOO', 'VTI', 'XLE', 'XLI', 'XLK']

for stock in list_of_stocks:
    print(stock)
    response = requests.get('https://cloud.iexapis.com/stable/stock/' + stock + '/chart/1y?token=YOURTOKENHERE')


# Save JSON Response to '_current.json'
    data = response.json()
    with open(stock + '_current.json', 'w') as f:
        json.dump(data, f)

    print('Payload Saved for ' + stock)
    print()
    print('**********************************')
