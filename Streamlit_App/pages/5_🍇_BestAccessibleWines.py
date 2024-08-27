import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder
from draft import display_aggrid_table, get_grape_count, get_wines_triage

st.set_page_config(page_title="Best Accessible Wines", page_icon="🍇")


st.header('Best Accessible Wines :earth_americas:')
df_grapes = pd.read_csv('utils/grapes_count.csv', encoding='UTF-8')
df_grapes= get_grape_count(df_grapes)
fig = df_grapes.iloc[0:5]
st.table(fig)


df_grapes.loc[df_grapes['Count'] < 200000, 'Grapes'] = 'Other Grapes' 
fig = px.pie(df_grapes, values='Count', names='Grapes', title='Grapes Count Percentage')
st.plotly_chart(fig)


##########################################

df_wines = pd.read_csv('utils/wines_ratings.csv', encoding='UTF-8')
df_wines = df_wines.drop(["Country"], axis=1)
Chardonnay, Cabernet_Sauvignon, Pinot_Noir = get_wines_triage(df_wines)

Chardonnay['Type'] = 'Chardonnay'
Cabernet_Sauvignon['Type'] = 'Cabernet Sauvignon'
Pinot_Noir['Type'] = 'Pinot Noir'

Chardonnay = Chardonnay.sort_values(by='Rating', ascending=False).reset_index()
Chardonnay = Chardonnay.iloc[0:5]
Chardonnay.drop('index',axis=1,inplace=True)

Cabernet_Sauvignon = Cabernet_Sauvignon.sort_values(by='Rating', ascending=False).reset_index()   
Cabernet_Sauvignon = Cabernet_Sauvignon.iloc[0:5]
Cabernet_Sauvignon.drop('index',axis=1,inplace=True)


Pinot_Noir = Pinot_Noir.sort_values(by='Rating', ascending=False).reset_index()
Pinot_Noir = Pinot_Noir.iloc[0:5]
Pinot_Noir.drop('index',axis=1,inplace=True)


Wines = pd.concat([Chardonnay, Cabernet_Sauvignon, Pinot_Noir]).reset_index()
Wines.drop('index',axis=1,inplace=True)
Wines.index = range(1, len(Wines) + 1)
st.table(Wines)

