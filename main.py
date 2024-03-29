from datetime import datetime
from openai import OpenAI
import json
import requests

client = OpenAI(api_key="your_openai_api_key")

current_date = datetime.now().strftime("%d/%m/%Y")

role_prompt = f"""
    You are a data analysis chatbot.
    You need to carefully and clearly analyze the data sent in JSON format and provide the result, which is the quantity needed to restock for each product for the next month (Only one month) and provide an explanation (reason).
    The meanings of the data are as follows: 
    1.order_qty: the quantity needed to restock. 
    2.qty_expected_avrage_Q1: the expected quantity to be sold in quarter 1. 
    3.qty_sold_avrage_Q1: the average quantity sold in quarter 1. 
    4.days_in_stock_Q1: the number of days the product remained in stock in quarter 1. 
    5.qty_expected_avrage_Q2: the expected quantity to be sold in quarter 2. 
    6.qty_sold_avrage_Q2: the average quantity sold in quarter 2. 
    7.days_in_stock_Q2: the number of days the product remained in stock in quarter 2. 
    8.qty_expected_avrage_Q3: the expected quantity to be sold in quarter 3. 
    9.qty_sold_avrage_Q3: the average quantity sold in quarter 3. 
    10.days_in_stock_Q3: the number of days the product remained in stock in quarter 3. 
    11.qty_expected_avrage_Q4: the expected quantity to be sold in quarter 4. 
    12.qty_sold_avrage_Q4: the average quantity sold in quarter 4. 
    13.days_in_stock_Q4: the number of days the product remained in stock in quarter 4. 
    14.qty_last_halloween: the quantity sold during last year's Halloween. 
    15.qty_last_xmas: the quantity sold during last year's Christmas. 
    16.qtysold_30: the quantity sold in the last 30 days. 
    17.qtysold_60: the quantity sold in the last 60 days. 
    18.qtysold_90: the quantity sold in the last 90 days. 
    19.qtysold_180: the quantity sold in the last 180 days. 
    20.qtysold_720: the quantity sold in the last 2 years. 
    21.days_in_stock_12: the total number of days the product remained in stock in the last 12 months. 
    22.days_in_stock_24: the total number of days the product remained in stock in the last 24 months. 
    23.qty: the quantity of the product in stock. 
    24.created_at: the date the product was created. 
    25.b_fill_up_date: the date of the most recent restock. 
    26.qty_ordered: the total quantity sold. 
    27.qty_per_month: the average quantity sold per month. 
    28.b_ink_pris: Product cost price from the supplier.
    29.cost: Product cost from supplier inclusive of all fees.
    30.price: Retail price.
    31.special_price: Special retail price.
    32.last_time_sold: the most recent date the product was sold. 
    33.vendor_last_fillup_qty: the quantity restocked most recently. 
    34.qtysold_2024: the quantity sold in the year 2024. 
    35.qtysold_2023: the quantity sold in the year 2023. 
    36.qtysold_2022: the quantity sold in the year 2022. 
    37.qtysold_2021: the quantity sold in the year 2021. 
    38.qtysold_2020: the quantity sold in the year 2020. 
    These products are candies, pastries, and children's toys sold in Norway. 
    Currently, it's {current_date}. 
    Please take note of the holidays and major festivals in Norway, as well as analyze based on the quantity of items sold and the number of days in stock.
    The reason and the provided result need to include clear information about the product as well as the factors influencing that quantity.
    The output is in JSON format with the following structure('result': []) and containing the data: product_id, sku, order_qty, and reason.
"""

system = [{"role": "system", "content": role_prompt}]
chat_history = []  # past user and assistant turns for AI memory


def estimate_restock_quantity(data):
    data = str(data)
    user = [{"role": "user", "content": data}]
    chat_completion = client.chat.completions.create(
        messages = system + chat_history + user,
        model="gpt-3.5-turbo",
        top_p=0.9,
    )
    
    response = chat_completion.choices[0].message.content 
    
    return json.loads(response)


def truncate_collection():
    url = 'http://0.0.0.0:5000/api/estimate/truncate'
    response = requests.delete(url)
    
    if response.status_code < 200 or response.status_code >= 300 :
        print('Truncate collection failed')
    else:
        print('Truncate collection successful')


def save_estimate(data):
    url = 'http://0.0.0.0:5000/api/estimate/update'
    response = requests.post(url, json=data)

    if response.status_code < 200 or response.status_code >= 300 :
        print('API request failed')
    else:
        print('API request successful')
        
        
def main():
    # Get data (Temporarily use data from the sample_data.json file, later will use data from the STACO API response)
    f = open('/app/sample_data.json')
    data = json.load(f)
    # data = data['result']
    total_items = len(data)
    batch_size = 5 #The number of items will be analyzed in each iteration
    reset_collection = True
    
    for i in range(0, total_items, batch_size):
        if reset_collection:
            truncate_collection()
            reset_collection = False
            
        batch = data[i:i+batch_size]
        response = estimate_restock_quantity(batch)
        save_estimate(response)
        

if __name__ == '__main__':
    main()
