import requests

def call_api():
    url = 'http://0.0.0.0:5000/api/estimate/update'
    data = {
        "result": [
            {
                "product_id": 126543,
                "sku": 141589,
                "order_qty": 3,
                "reason": "The product 'Tyrker Shot - Bland Din Egen Shot' has been selling steadily with an average of 0.4 units per month. Despite low sales in Q1 and Q2, recent trends show an increase in sales. Considering the upcoming festive season and recent sales patterns, restocking 3 units for the next month is recommended."
            },
            {
                "product_id": 217688,
                "sku": 191498,
                "order_qty": 7,
                "reason": "The product 'Super Sur - Real Candy Shot i Patentflaske' has shown a consistent increase in sales with an average of 1.3 units per month. With higher sales in Q3 and Q4 and considering the upcoming holidays, restocking 7 units for the next month is recommended."
            },
            {
                "product_id": 221220,
                "sku": 122199,
                "order_qty": 4,
                "reason": "The product 'Liverpool FC Nøkkelring' has shown stable sales with an average of 0.7 units per month. Recent sales in Q4 indicate an increase in demand. Restocking 4 units for the next month is recommended based on the current sales trend."
            },
            {
                "product_id": 217643,
                "sku": 42511,
                "order_qty": 4,
                "reason": "The product 'Morsom T-Rex Kulepenn - Assorterte Farger' has been consistently selling with an average of 0.8 units per month. Recent sales in Q4 show an increase in demand. Restocking 4 units for the next month is recommended based on the current sales trend."
            },
            {
                "product_id": 220858,
                "sku": 346260,
                "order_qty": 3,
                "reason": "The product '5 stk Viskelær Formet som Iskrem' has shown steady sales with an average of 0.5 units per month. Recent sales in Q3 and Q4 indicate a slight increase in demand. Restocking 3 units for the next month is recommended based on the current sales trend."
            },
            {
                "product_id": 217949,
                "sku": 173746,
                "order_qty": 7,
                "reason": "The product '8 stk Pappkrus med Gullfolierte Fotavtrykk 270 ml' has been selling well with an average of 1.6 units per month. Recent sales trends show a consistent demand. Restocking 7 units for the next month is recommended based on the current sales pattern."
            },
            {
                "product_id": 218564,
                "sku": 42613,
                "order_qty": 4,
                "reason": "The product '6 stk. 30 cm - Glossy Mirror Sølvfargede Ballonger' has shown a stable sales pattern with an average of 0.9 units per month. Recent sales in Q4 indicate a slight decrease in demand. Restocking 4 units for the next month is recommended based on the current sales trend."
            },
            {
                "product_id": 211858,
                "sku": 131563,
                "order_qty": 13,
                "reason": "The product '60 år - 6 stk Svarte, Sølv- og Gullfarget Ballonger 30 cm' has been consistently popular with an average of 2.9 units sold per month. Recent sales trends indicate a steady demand. Restocking 13 units for the next month is recommended based on the current sales pattern and upcoming festive seasons."
            },
            {
                "product_id": 226240,
                "sku": 603428,
                "order_qty": 2,
                "reason": "The product 'Inflatimals Panda - Stor Uppblåsbar Panda på Pinne 1,4 Meter' has shown an increasing trend with an average of 1.3 units sold per month. Recent sales indicate a growing demand. Restocking 2 units for the next month is recommended based on the current sales pattern."
            },
            {
                "product_id": 217958,
                "sku": 42607,
                "order_qty": 10,
                "reason": "The product 'Craze Inkee Enhjørning Badebombe - Søt Popkorn Aroma - Med Overraskelse!' has been very popular with an average of 6.7 units sold per month. Recent sales trends show a consistent high demand. Restocking 10 units for the next month is recommended based on the current sales pattern and upcoming holidays."
            }
        ],
        "reset_collection": '1'
    }
    response = requests.post(url, json=data)
    print(response)

    if response.status_code < 200 or response.status_code >= 300 :
        print('API request failed')
    else:
        print('API request successful')

if __name__ == '__main__':
    call_api()
