import os
import pandas as pd

data = pd.read_csv('nasdaq_listed_symbols.csv')

symbols = data['Symbol'] 
company_name = data['Company_Name']
