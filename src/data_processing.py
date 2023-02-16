import pandas as pd 

market_data1 = pd.read_csv("data\raw\market_index_data_version1.csv")
market_data2 = pd.read_csv("data\raw\market_index_data_version2.csv")

market_data = pd.concat([market_data1, market_data2], axis = 0)

market_data.to_csv("data\intermediate\market_index_all.csv")