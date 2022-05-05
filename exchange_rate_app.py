#!python3

import streamlit as st
import pandas as pd
import numpy as np
import requests
import re

#app title
st.title('Realtime Currency Exchange Tool')

currency_name_df = pd.read_csv('physical_currency_list.csv')
currency_codes = list(currency_name_df["currency code"])
currency_names = list(currency_name_df["currency name"])

d = {}

for code, name in zip(currency_codes,currency_names):
    d[name] = code

source_currency_name = st.selectbox("Source currency",currency_names)
source_currency = d[source_currency_name]

target_currency_name = st.selectbox("Target currency",currency_names)
target_currency = d[target_currency_name]

#currency exchange formula
url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={source_currency}&to_currency={target_currency}&apikey=ZCN351IDJC1IVE6E'

if(source_currency==target_currency):
    st.subheader("Please choose different currencies!")
else:
    r = requests.get(url)
    data = r.json()

    df = pd.json_normalize(data)
    
    st.table(df)
    
    rate = list(df['Realtime Currency Exchange Rate.5. Exchange Rate'])

    st.title("Converting between currencies")
    source_value1 = st.number_input(source_currency,min_value = 0)
    target_value1 = float(rate[0]) * float(source_value1)
    st.write(" =  " + target_currency)
    st.write(target_value1)
    
    source_value2 = st.number_input(target_currency,min_value = 0)
    target_value2 = float(source_value2)/float(rate[0])
    st.write(" =  " + source_currency)
    st.write(target_value2)