'''
This script will plot the price data against time with the help of plotly library.

Author : Abhishek-2k19 (Abhishek S. Purohit)
Date : 13th May 2021
'''

import pandas as pd
import plotly.express as px
import glob
import plotly.graph_objects as go

prod = glob.glob("./*.csv",recursive=True)
filename = prod[0]

df = pd.read_csv(filename)

fig = go.Figure([go.Scatter(x=df['Timestamps'], y=df['price(INR)'],fill='tozeroy')],)
fig.update_xaxes(title = "Timeline",showticklabels = False)
fig.update_yaxes(title = "Price")
fig.update_layout(title = filename[2:-4])
fig.show()