import pandas as pd
import numpy as np
from datetime import datetime
import itertools

# JSON API
import requests
import json

# data visualization
import matplotlib
import seaborn as sns
import statsmodels.api as sm

# ignore warnings
import warnings

def items_acquisition():
    base_url = 'https://python.zach.lol'

    response = requests.get('https://python.zach.lol/api/v1/items')
    data = response.json()

    items = pd.DataFrame(data['payload']['items'])

    while (data['payload']['page']) < data['payload']['max_page']:
        
        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
        items = pd.concat([items, pd.DataFrame(data['payload']['items'])]).reset_index()
        items.drop(columns=['index'], inplace=True)
        
        if (data['payload']['next_page']) == data['payload']['max_page']:
            break
        
        print((data['payload']['page']))
        
    return items


def stores_acquisitions():
    base_url = 'https://python.zach.lol'
    
    response = requests.get('https://python.zach.lol/api/v1/stores')
    data = response.json()

    stores = pd.DataFrame(data['payload']['stores'])

    return stores

def sales_acquisitions():
    base_url = 'https://python.zach.lol'

    response = requests.get('https://python.zach.lol/api/v1/sales')
    data_sa = response.json()
    
    sales = pd.DataFrame(data_sa['payload']['sales'])
    
    while (data_sa['payload']['page']) < data_sa['payload']['max_page']:
        
        response = requests.get(base_url + data_sa['payload']['next_page'])
        data_sa = response.json()
        sales = pd.concat([sales, pd.DataFrame(data_sa['payload']['sales'])]).reset_index()
        sales.drop(columns=['index'], inplace=True)
        
        if (data_sa['payload']['next_page']) == data_sa['payload']['max_page']:
            break
        
        print((data_sa['payload']['page']))
        
    return sales