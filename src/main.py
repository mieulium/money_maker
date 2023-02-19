import pandas as pd
import json
from data import query 


config = json.load(open("./config/config.json"))

# API allows only for last 100 rows
tres_data = query.query_treasury(date = '2001-01-01', config = config['query'])

tres_data.to_csv("./data/raw/us_interest_rates.csv")

