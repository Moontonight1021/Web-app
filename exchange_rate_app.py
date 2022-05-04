#!python3

import streamlit as st
import pandas as pd
import numpy as np
import requests
import re

#app title
st.title('Currency Exchange Tool')

#currency exchange formula
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=ZCN351IDJC1IVE6E'

r = requests.get(url)
data = r.json()

st.write(data)