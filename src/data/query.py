import pandas as pd
import requests 
import json 

def query_treasury(date, config):
    if date != None: 
        requesting_url = config["base_url"]+config["int_rate_url"]+config["filter"]+config["date"] + str(date)
    else: 
        requesting_url = config["base_url"]+config["int_rate_url"]
    res = requests.get(requesting_url)
    try: 
        root = res.json()
        results = pd.DataFrame(root['data'])
    except: 
        results = "Error"
    return results