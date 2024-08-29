import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder


def display_aggrid_table(df, title="Table infos", height=400):
    st.write(title)
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination()
    gb.configure_side_bar()
    gb.configure_selection('single')
    gridOptions = gb.build()
    AgGrid(df, gridOptions=gridOptions, height=height, fit_columns_on_grid_load=True)

def get_most_popular_wines(df):
    df = df[df['wines_rating_avg'] >= 4.2] 
    df= df.sort_values('wines_rating_count', ascending=False).reset_index()
    df=df.iloc[0:10]
    df.drop('index',axis=1,inplace=True)
    df = df.rename(columns={
    "wines_name": "Wines",
    "countries_name": "Country",
    "nbr_of_vintage:": "Nbr of Vintages",
    "wines_rating_count": "Reviews",
    "wines_rating_avg": "Rating"})
    return df

def get_geppetto(df):
    df = df.sort_values(["wines_ratings_count"], ascending=False)
    df=df.iloc[0:10]
    df = df.sort_values(["wines_ratings_avg", "vintages_ratings_avg"], ascending=[False,False]).reset_index()
    df= df.iloc[0:3]
    df.drop('index',axis=1,inplace=True)
    df.index = range(1, len(df) + 1)
    df = df.rename(columns={
    "wines_name": "Wines",
    "countries_name": "Country",
    "wines_ratings_count": "Reviews",
    "vintages_ratings_avg": "Vintage Rating",
    "wines_ratings_avg": "Rating"})
    return df

def get_acidity(df):
    df = df.sort_values(["ratings_count"], ascending=False)
    df=df.iloc[0:50]
    df = df.sort_values(by='acidity', ascending=False).reset_index()
    df= df.iloc[0:3]
    df.drop('index',axis=1,inplace=True)
    df.index = range(1, len(df) + 1)
    df = df.rename(columns={
    "country": "Country",
    "vintage count":"Vintage Reviews",
    "ratings_count": "Reviews",
    "ratings_average": "Rating",
    "acidity": "Acidity"
    })
    return df

def get_best_vintage_winery(df):
    df= df.drop(['list_of_years','wines_ratings_count'], axis=1)
    df= df[df['vintages_count'] > 3]
    df = df.sort_values(["total_ratings_count"], ascending=False)
    df=df.iloc[0:50]
    df = df.sort_values(["vintages_ratings_avg"], ascending=False).reset_index()
    df= df.iloc[0:3]
    df.drop('index',axis=1,inplace=True)
    df.index = range(1, len(df) + 1)
    df = df.rename(columns={
    "wines_name": "Wines",
    "region_name": "Region",
    "countries_name": "Country",
    "vintages_price_avg": "Price",
    "total_ratings_count":"Vintage Reviews",
    "vintages_ratings_avg": "Vintage Rating",
    "vintages_count": "Nbr of Vintages",
    })
    return df

def get_grape_count(df):
    df = df.sort_values(["wines_count"], ascending=False).reset_index()
    df.drop('index',axis=1,inplace=True)
    df.index = range(1, len(df) + 1)
    df = df.rename(columns={
    "name": "Grapes",
    "wines_count": "Count"
})
    return df

def get_wines_triage(df):
    df = df.rename(columns={
    "wines_name": "Wines",
    "countries_name": "Country",
    "nbr_of_vintage:": "Nbr of Vintages",
    "wines_rating_count": "Reviews",
    "wines_rating_avg": "Rating"})

    Chardonnay = df[df['Wines'].str.contains('Chardonnay')]
    Cabernet_Sauvignon = df[df['Wines'].str.contains('Cabernet Sauvignon')]
    Pinot_Noir = df[df['Wines'].str.contains('Pinot Noir')]

    return Chardonnay, Cabernet_Sauvignon, Pinot_Noir

def get_cabernet(df):
    df = df[df['Wines'].str.contains('Cabernet Sauvignon')]
    df = df.rename(columns={
    "Keywords_count": "Keywords"})
    return df

def get_potion(df):
    df=df.sort_values(by=['Keywords_count','Rating'], ascending=False).reset_index()
    df=df.iloc[0:3]
    df.drop('index',axis=1,inplace=True)
    df.index = range(1, len(df) + 1)
    df = df.rename(columns={
    "Keywords_count": "Keywords",})
    return df


#Datasets
df_top_ten_most_popular = pd.read_csv('utils/wines_data.csv', encoding='latin-1')
df_gepetto = pd.read_csv('utils/Geppetto_Award.csv', encoding='latin-1')
df_acidity = pd.read_csv('utils/Acidity.csv', encoding='latin-1')
df_best_vintage_winery = pd.read_csv('utils/Best_vintage_winery.csv', encoding='latin-1')
df_grape_count = pd.read_csv('utils/grapes_count.csv', encoding='UTF-8')

df_wines = pd.read_csv('utils/wines_data.csv', encoding='UTF-8')
Chardonnay, Cabernet_Sauvignon, Pinot_Noir = get_wines_triage(df_wines)

Chardonnay['Type'] = 'Chardonnay'
Cabernet_Sauvignon['Type'] = 'Sauvignon Blanc'
Pinot_Noir['Type'] = 'Pinot Noir'

Chardonnay = Chardonnay.sort_values(by='Rating', ascending=False).reset_index()
Chardonnay = Chardonnay.iloc[0:5]
Chardonnay.drop('index',axis=1,inplace=True)
Chardonnay.index = range(1, len(Chardonnay) + 1)

Cabernet_Sauvignon = Cabernet_Sauvignon.sort_values(by='Rating', ascending=False).reset_index()   
Cabernet_Sauvignon = Cabernet_Sauvignon.iloc[0:5]
Cabernet_Sauvignon.drop('index',axis=1,inplace=True)
Cabernet_Sauvignon.index = range(1, len(Cabernet_Sauvignon) + 1)

Pinot_Noir = Pinot_Noir.sort_values(by='Rating', ascending=False).reset_index()
Pinot_Noir = Pinot_Noir.iloc[0:5]
Pinot_Noir.drop('index',axis=1,inplace=True)
Pinot_Noir.index = range(1, len(Pinot_Noir) + 1)


