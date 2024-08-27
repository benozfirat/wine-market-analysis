import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder
from draft import display_aggrid_table, get_most_popular_wines, get_gepetto, get_acidity, get_best_vintage_winery

st.set_page_config(page_title = "This is a Multipage WebApp") 
st.title("This is the Home Page Geeks.")
st.sidebar.success("Select Any Page from here") 
