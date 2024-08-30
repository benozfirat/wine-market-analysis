# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder  # For interactive data tables
from get_results import display_aggrid_table, get_most_popular_wines  # Custom functions from another module

# Set up the Streamlit page configuration, including the title and icon
st.set_page_config(page_title="Top 10 Most Popular", page_icon="📈")

# Display the header of the app
st.header('Top 10 Most Popular Wines :wine_glass:')

# Read the wine data from a CSV file into a DataFrame
df_top_ten_most_popular = pd.read_csv('utils/wines_data.csv', encoding='UTF-8')

# Display an interactive table of the top 10 most popular wines using a custom function
display_aggrid_table(
    get_most_popular_wines(df_top_ten_most_popular),  # Get the top 10 most popular wines from the data
    title="This following table shows the top 10 most popular wines based on the number of reviews with a rating of at least 4.2\n",  # Title for the table
    height=400  # Set the height of the table
)

# Create a bar chart using Plotly Express to visualize the top 10 most popular wines
fig = px.bar(
    get_most_popular_wines(df_top_ten_most_popular),  # Get the data for the top 10 most popular wines
    x='Wines',  # Set the x-axis to the wine names
    y="Rating",  # Set the y-axis to the ratings
    color='Reviews',  # Color the bars based on the number of reviews
    color_continuous_scale="Blues",  # Use a blue color scale
    height=700,  # Set the height of the chart
    width=900,  # Set the width of the chart
    title='Top 10 Most Popular Wines'  # Title for the chart
)

# Update the layout of the chart to set the y-axis range (rating range)
fig.update_layout(yaxis=dict(range=[4, 4.8]))

# Render the Plotly chart in the Streamlit app
st.plotly_chart(fig)
