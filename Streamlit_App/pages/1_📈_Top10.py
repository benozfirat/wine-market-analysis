import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder
from draft import display_aggrid_table, get_most_popular_wines

st.set_page_config(page_title="Top 10 Most Popular", page_icon="📈")
st.header('Top 10 Most Popular Wines')

df_top_ten_most_popular = pd.read_csv('utils/wines_data.csv', encoding='UTF-8')
display_aggrid_table(get_most_popular_wines(df_top_ten_most_popular),title= "Most popular wines with a rating of at least 4.2  \n"  , height=400)
fig = px.bar(get_most_popular_wines(df_top_ten_most_popular), x='Wines', y="Rating", color='Reviews',color_continuous_scale="Blues",height=700, width=900, title='Top 10 Most Popular Wines')
fig.update_layout(yaxis=dict(range=[4, 4.8]))
st.plotly_chart(fig)