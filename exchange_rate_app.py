#!python3

import streamlit as st
import pandas as pd
import numpy as np
import requests
import re

#app title
st.title('Currency Exchange Tool')

source_currency = st.selectbox("Source currency",('USD','CAD','JPY'))

target_currency = st.selectbox("Target currency",('USD','CAD','JPY'))

#currency exchange formula
url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={source_currency}&to_currency={target_currency}&apikey=ZCN351IDJC1IVE6E'


r = requests.get(url)
data = r.json()

df = pd.json_normalize(data)


st.table(df)