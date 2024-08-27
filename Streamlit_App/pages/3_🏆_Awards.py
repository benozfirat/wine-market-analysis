import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder
from draft import get_gepetto, get_acidity, get_best_vintage_winery 

st.set_page_config(page_title="Awards", page_icon="🏆")

df_gepetto = pd.read_csv('utils/Gepetto_Award.csv', encoding='UTF-8')
df_acidity = pd.read_csv('utils/Acidity.csv', encoding='UTF-8')
df_best_vintage_winery = pd.read_csv('utils/Best_vintage_winery.csv', encoding='UTF-8')

#Geppetto Award
st.header('Gepetto Award :pinched_fingers:')
st.write('Best wine from Italy based on:\n - Italy\'s Top10 most popular wineries in number of Reviews\n - Rating\n - Vintage Rating\n')

fig1 = get_gepetto(df_gepetto)
fig1['Vintage Rating'] = fig1['Vintage Rating'].round(2)
fig1['Rating'] = fig1['Rating'].round(2)
st.table(fig1)

df_top3 = fig1.head(3)
df_top3['Rank']= [1.5,1,0.5]
df_top3_podium= [df_top3.iloc[1],df_top3.iloc[0],df_top3.iloc[2]]

fig1=px.bar(df_top3_podium, x='Wines', y="Rank", text="Rating", color=['#C0C0C0',"#FFD700",'#CD7F32'],
            title='Top 3 Gepetto Award',
            height=600, width=800)
fig1.update_layout(yaxis=dict(range=[0, 3]),showlegend=False)
st.plotly_chart(fig1)

#LoL Player Award
st.header('Toxic as LoL Player Award :japanese_ogre:')
st.write('Best Acidity rate from the top 50 in terms of number of Reviews\n ')
fig2 = get_acidity(df_acidity)
fig2['Acidity'] = fig2['Acidity'].round(2)
fig2['Rating'] = fig2['Rating'].round(2)
st.table(fig2)

df_top3 = fig2.head(3)
df_top3['Rank']= [1.5,1,0.5]
df_top3_podium= [df_top3.iloc[1],df_top3.iloc[0],df_top3.iloc[2]]

fig2=px.bar(df_top3_podium, x='Wines', y="Rank", text="Acidity", color=['#C0C0C0',"#FFD700",'#CD7F32'],
            title='Top 3 Acidity Award',
            height=600, width=800)
fig2.update_layout(yaxis=dict(range=[0, 3]), showlegend=False)
st.plotly_chart(fig2)

#Best vintage winery Award
st.header('Best vintage winery Award :wine_glass:')
st.write('Best Vintage winery based on:\n - Top50 most popular wineries in nbr. of Reviews\n - Who made at least 3 vintages\n - The rating for wines with more than 3 vintages\n')
fig3= get_best_vintage_winery(df_best_vintage_winery)
fig3['Vintage Rating'] = fig3['Vintage Rating'].round(2)
fig3['Price'] = fig3['Price'].round(2)
st.table(fig3)

df_top3 = fig3.head(3)
df_top3['Rank']= [1.5,1,0.5]
df_top3_podium= [df_top3.iloc[1],df_top3.iloc[0],df_top3.iloc[2]]

fig3=px.bar(df_top3_podium, x='Wines', y="Rank", text="Vintage Rating", color=['#C0C0C0',"#FFD700",'#CD7F32'],
            title='Top 3 Best Vintage Winery Award',
            height=600, width=800)
fig3.update_layout(yaxis=dict(range=[0, 3]),showlegend=False)
st.plotly_chart(fig3)

