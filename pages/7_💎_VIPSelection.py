# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder
from get_results import get_cabernet  # Importing custom function to process Cabernet data

# Streamlit configuration: Set up the page title and icon
st.set_page_config(page_title="VIP Selection", page_icon="💎")

# Display the header for the VIP selection
st.header('VIP Selection of the month :top:')

# Explanation of the selection process and categories for Cabernet Sauvignon wines
explanation = """
### Cabernet Sauvignon :wine_glass:

This month, we have selected the best Cabernet Sauvignon wines for our VIP members.
Here are the top 3 wines in each category: Best Rated, Most Popular, Best Composition, Best Vintage Rated, and Best Taste Match.
"""
# Display the explanation using markdown formatting
st.markdown(explanation)

# Load Cabernet Sauvignon data from a CSV file
df_cabernet = pd.read_csv('utils/Cabernet_Sauvignon.csv', encoding='UTF-8')

# Process the data using the custom function 'get_cabernet'
df_cabernet = get_cabernet(df_cabernet)

# Round off specific columns for better presentation
df_cabernet['Tannin'] = df_cabernet['Tannin'].round(2)
df_cabernet['Acidity'] = df_cabernet['Acidity'].round(2)
df_cabernet['Vintage Rating'] = df_cabernet['Vintage Rating'].round(2)

# --- Best Rated Cabernet Sauvignon ---
# Display the subheader for Best Rated wines
st.subheader('Best Rated Cabernet Sauvignon :star2: \n')

# Sort the wines by their Rating in descending order and reset the index
best_rated = df_cabernet.sort_values(by='Rating', ascending=False).reset_index()
best_rated.drop('index', axis=1, inplace=True)  # Drop the old index column
best_rated.index = range(1, len(best_rated) + 1)  # Reset the index for display

# Drop columns not needed for this table
best_rated = best_rated.drop(["Tannin", "Acidity", "Keywords", 'Intensity'], axis=1)

# Display the top 3 wines as a table
fig = best_rated.iloc[0:3]
st.table(fig)

# --- Most Popular Cabernet Sauvignon ---
# Display the subheader for Most Popular wines
st.subheader('Most Popular Cabernet Sauvignon :sunglasses: \n')

# Sort the wines by the number of Reviews in descending order and reset the index
most_popular = df_cabernet.sort_values(by='Reviews', ascending=False).reset_index()
most_popular.drop('index', axis=1, inplace=True)  # Drop the old index column
most_popular.index = range(1, len(most_popular) + 1)  # Reset the index for display

# Drop columns not needed for this table
most_popular = most_popular.drop(["Tannin", "Acidity", "Keywords", 'Intensity'], axis=1)

# Display the top 3 wines as a table
fig = most_popular.iloc[0:3]
st.table(fig)

# --- Best Composition Cabernet Sauvignon ---
# Display the subheader for Best Composition wines
st.subheader('Best Composition of Cabernet Sauvignon :thumbsup: \n')

# Sort the wines by Tannin and Acidity levels in descending order and reset the index
best_composition = df_cabernet.sort_values(by=['Tannin', 'Acidity'], ascending=False).reset_index()

# Filter to select wines with Tannin and Acidity both greater than 3.4
best_composition = best_composition[best_composition['Tannin'] > 3.4]
best_composition = best_composition[best_composition['Acidity'] > 3.4]
best_composition.drop('index', axis=1, inplace=True)  # Drop the old index column
best_composition.index = range(1, len(best_composition) + 1)  # Reset the index for display

# Drop columns not needed for this table
best_composition = best_composition.drop(['Reviews', 'Vintage Rating', 'Keywords', 'Intensity'], axis=1)

# Display the top 3 wines as a table
fig = best_composition.iloc[0:3]
st.table(fig)

# --- Best Vintage Rated Cabernet Sauvignon ---
# Display the subheader for Best Vintage Rated wines
st.subheader('Best Vintage Rated Cabernet Sauvignon :older_adult: \n')

# Sort the wines by Vintage Rating in descending order and reset the index
best_vintage = df_cabernet.sort_values(by='Vintage Rating', ascending=False).reset_index()
best_vintage.drop('index', axis=1, inplace=True)  # Drop the old index column
best_vintage.index = range(1, len(best_vintage) + 1)  # Reset the index for display

# Drop columns not needed for this table
best_vintage = best_vintage.drop(['Tannin', 'Acidity', 'Keywords', 'Intensity'], axis=1)

# Display the top 3 wines as a table
fig = best_vintage.iloc[0:3]
st.table(fig)

# --- Best Taste Match Cabernet Sauvignon ---
# Display the subheader for Best Taste Match wines
st.subheader('Best Taste Match of Cabernet Sauvignon :test_tube: \n')

# Sort the wines by Keywords and Intensity in descending order and reset the index
best_taste = df_cabernet.sort_values(by=["Keywords", 'Intensity'], ascending=False).reset_index()
best_taste.drop('index', axis=1, inplace=True)  # Drop the old index column
best_taste.index = range(1, len(best_taste) + 1)  # Reset the index for display

# Drop columns not needed for this table
best_taste = best_taste.drop(['Reviews', 'Tannin', 'Acidity', 'Vintage Rating'], axis=1)

# Display the top 3 wines as a table
fig = best_taste.iloc[0:3]
st.table(fig)
