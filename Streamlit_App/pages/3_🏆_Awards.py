# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder
from get_results import get_geppetto, get_acidity, get_best_vintage_winery  # Custom functions to process data

# Streamlit configuration: Set up the page title and icon
st.set_page_config(page_title="Awards", page_icon="🏆")

# Display the header of the app
st.header('Awards :trophy:')

# Explanation text for the awards and criteria
explanation = """
Our dear leader/dictator, Mr. Geppetto, driven by a deep passion for exceptional wine, is thrilled to announce three prestigious awards for the top wineries in recognition of their outstanding craftsmanship. 

**These awards are based on the following criteria:**

- **Geppetto Award**: The best wine from Italy based on Italy's Top 10 most popular wineries in terms of Reviews, Rating, and Vintage Rating.
- **Toxic as LoL Player Award**: The best Acidity rate from the top 50 in terms of the number of Reviews.
- **Best Vintage Winery Award**: The best Vintage winery that produced at least 3 vintages, based on the Top 50 most popular wineries by number of Reviews and the average rating of their vintages.
"""

# Display the explanation using markdown for formatting
st.markdown(explanation)

# Load the datasets for each award category from CSV files
df_geppetto = pd.read_csv('utils/Geppetto_Award.csv', encoding='UTF-8')
df_acidity = pd.read_csv('utils/Acidity.csv', encoding='UTF-8')
df_best_vintage_winery = pd.read_csv('utils/Best_vintage_winery.csv', encoding='UTF-8')

# Geppetto Award Section
st.subheader('Geppetto Award :pinched_fingers:')

# Process and display the Geppetto Award data
fig1 = get_geppetto(df_geppetto)  # Custom function to get Geppetto Award data
fig1['Vintage Rating'] = fig1['Vintage Rating'].round(2)  # Round Vintage Rating to 2 decimal places
fig1['Rating'] = fig1['Rating'].round(2)  # Round Rating to 2 decimal places
st.table(fig1)  # Display the data as a table

# Prepare the top 3 results for the podium visualization
df_top3 = fig1.head(3)
df_top3['Rank'] = [1.5, 1, 0.5]  # Assign ranks for podium positions
df_top3_podium = [df_top3.iloc[1], df_top3.iloc[0], df_top3.iloc[2]]  # Arrange for podium (2nd, 1st, 3rd)

# Create a bar chart for the top 3 Geppetto Award winners
fig1 = px.bar(df_top3_podium, x='Wines', y="Rank", text="Rating", 
              color=['#C0C0C0', "#FFD700", '#CD7F32'],  # Silver, Gold, Bronze colors
              title='Top 3 Geppetto Award',
              height=600, width=800)
fig1.update_layout(yaxis=dict(range=[0, 3]), showlegend=False)  # Adjust y-axis range and remove legend
st.plotly_chart(fig1)  # Display the chart

# Toxic as LoL Player Award Section
st.subheader('Toxic as LoL Player Award :japanese_ogre:')

# Process and display the Acidity Award data
fig2 = get_acidity(df_acidity)  # Custom function to get Acidity Award data
fig2['Acidity'] = fig2['Acidity'].round(2)  # Round Acidity to 2 decimal places
fig2['Rating'] = fig2['Rating'].round(2)  # Round Rating to 2 decimal places
st.table(fig2)  # Display the data as a table

# Prepare the top 3 results for the podium visualization
df_top3 = fig2.head(3)
df_top3['Rank'] = [1.5, 1, 0.5]  # Assign ranks for podium positions
df_top3_podium = [df_top3.iloc[1], df_top3.iloc[0], df_top3.iloc[2]]  # Arrange for podium (2nd, 1st, 3rd)

# Create a bar chart for the top 3 Acidity Award winners
fig2 = px.bar(df_top3_podium, x='Wines', y="Rank", text="Acidity", 
              color=['#C0C0C0', "#FFD700", '#CD7F32'],  # Silver, Gold, Bronze colors
              title='Top 3 Acidity Award',
              height=600, width=800)
fig2.update_layout(yaxis=dict(range=[0, 3]), showlegend=False)  # Adjust y-axis range and remove legend
st.plotly_chart(fig2)  # Display the chart

# Best Vintage Winery Award Section
st.subheader('Best Vintage Winery Award :wine_glass:')

# Process and display the Best Vintage Winery data
fig3 = get_best_vintage_winery(df_best_vintage_winery)  # Custom function to get Best Vintage Winery data
fig3['Vintage Rating'] = fig3['Vintage Rating'].round(2)  # Round Vintage Rating to 2 decimal places
fig3['Price'] = fig3['Price'].round(2)  # Round Price to 2 decimal places
st.table(fig3)  # Display the data as a table

# Prepare the top 3 results for the podium visualization
df_top3 = fig3.head(3)
df_top3['Rank'] = [1.5, 1, 0.5]  # Assign ranks for podium positions
df_top3_podium = [df_top3.iloc[1], df_top3.iloc[0], df_top3.iloc[2]]  # Arrange for podium (2nd, 1st, 3rd)

# Create a bar chart for the top 3 Best Vintage Winery Award winners
fig3 = px.bar(df_top3_podium, x='Wines', y="Rank", text="Vintage Rating", 
              color=['#C0C0C0', "#FFD700", '#CD7F32'],  # Silver, Gold, Bronze colors
              title='Top 3 Best Vintage Winery Award',
              height=600, width=800)
fig3.update_layout(yaxis=dict(range=[0, 3]), showlegend=False)  # Adjust y-axis range and remove legend
st.plotly_chart(fig3)  # Display the chart
