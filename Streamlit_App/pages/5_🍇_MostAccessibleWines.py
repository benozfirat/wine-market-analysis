# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder
from get_results import display_aggrid_table, get_grape_count, get_wines_triage  # Custom functions for data processing

# Streamlit configuration: Set up the page title and icon
st.set_page_config(page_title="Most Accessible Wines", page_icon="🍇")

# Display the header of the app
st.header('Most Accessible Varieties :earth_americas:')

# Explanation of the criteria for identifying the most common grape varieties
explanation = """
### Most Common Grapes 🍇

To determine the 15 most accessible wines, we first needed to determine the most common grape varieties.
We have analyzed the data and found that the most common grape varieties are Chardonnay, Cabernet Sauvignon, and Pinot Noir.
"""
# Display the explanation using markdown for formatting
st.markdown(explanation)

# Load the grape count data from a CSV file
df_grapes = pd.read_csv('utils/grapes_count.csv', encoding='UTF-8')

# Process the grape count data using a custom function
df_grapes = get_grape_count(df_grapes)

# Display the top 5 most common grape varieties as a table
fig = df_grapes.iloc[0:5]
st.table(fig)

# Group less common grape varieties under the label 'Other Grapes' for a cleaner pie chart
df_grapes.loc[df_grapes['Count'] < 200000, 'Grapes'] = 'Other Grapes'

# Create a pie chart showing the distribution of grape varieties
fig = px.pie(df_grapes, values='Count', names='Grapes', title='Grapes Count Percentage')
st.plotly_chart(fig)

##########################################

# Explanation of the criteria for identifying the most common wines based on the grape varieties
explanation = """
### Most Common Wines 🍷

With the most common grape varieties identified, we can now determine the top 5 best accessible wines for each variety based on their ratings.
"""
# Display the explanation using markdown for formatting
st.markdown(explanation)

# Load the wine ratings data from a CSV file
df_wines = pd.read_csv('utils/wines_ratings.csv', encoding='UTF-8')

# Drop the 'Country' column as it's not needed for this analysis
df_wines = df_wines.drop(["Country"], axis=1)

# Use custom function to separate the data into different grape varieties
Chardonnay, Cabernet_Sauvignon, Pinot_Noir = get_wines_triage(df_wines)

# Assign a 'Type' label to each DataFrame for easier identification later
Chardonnay['Type'] = 'Chardonnay'
Cabernet_Sauvignon['Type'] = 'Cabernet Sauvignon'
Pinot_Noir['Type'] = 'Pinot Noir'

# Sort the Chardonnay wines by Rating and Reviews, then select the top 5
Chardonnay = Chardonnay.sort_values(by=['Rating', 'Reviews'], ascending=False).reset_index()
Chardonnay = Chardonnay.iloc[0:5]
Chardonnay.drop('index', axis=1, inplace=True)

# Sort the Cabernet Sauvignon wines by Rating and Reviews, then select the top 5
Cabernet_Sauvignon = Cabernet_Sauvignon.sort_values(by=['Rating', 'Reviews'], ascending=False).reset_index()   
Cabernet_Sauvignon = Cabernet_Sauvignon.iloc[0:5]
Cabernet_Sauvignon.drop('index', axis=1, inplace=True)

# Sort the Pinot Noir wines by Rating and Reviews, then select the top 5
Pinot_Noir = Pinot_Noir.sort_values(by=['Rating', 'Reviews'], ascending=False).reset_index()
Pinot_Noir = Pinot_Noir.iloc[0:5]
Pinot_Noir.drop('index', axis=1, inplace=True)

# Combine the top 5 wines from each variety into a single DataFrame
Wines = pd.concat([Chardonnay, Cabernet_Sauvignon, Pinot_Noir]).reset_index()

# Drop the unnecessary index column and reindex the DataFrame
Wines.drop('index', axis=1, inplace=True)
Wines.index = range(1, len(Wines) + 1)

# Display the combined DataFrame of top wines as a table
st.table(Wines)
