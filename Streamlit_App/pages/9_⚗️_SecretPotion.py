# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from get_results import get_potion  # Custom function for processing data related to the "Secret Potion"

# Streamlit configuration: Set up the page title and icon
st.set_page_config(page_title="Secret Potion", page_icon="⚗️")

# Display the header for the Secret Potion section
st.header('Secret Potion :male_mage:')

# Explanation of the section on Mr. Geppetto's Secret Potion
explanation = """
### Mr. Gepetto\'s Secret Potion  🧪

Before he was a businessman, Mr. Geppetto was a sorcerer. 
He created a secret potion that would give him the answer to all of his questions.
While the potion seemed weird, Mr. Geppetto liked the taste.
So here are the top 3 wines that taste the most like the ingredients Mr. Geppetto used for his potion.

**List of ingredients:** Coffee, Bacon fat, Baby breath, Chalk, Clay Dust, Kerosene, Pencil lead, Potpourri, Rubber cement, Wet gravel, Cat's pee
"""
# Display the explanation using markdown formatting
st.markdown(explanation)

# Load the dataset for the Secret Potion wines from a CSV file
df_secret_potion = pd.read_csv('utils/Secret_Potion.csv', encoding='UTF-8')

# Process the data using the custom function get_potion to identify relevant wines
fig1 = get_potion(df_secret_potion)

# Round the Rating values to 2 decimal places for better readability
fig1['Rating'] = fig1['Rating'].round(2)

# Display the processed data in a table format
st.table(fig1)

# --- Displaying the Top 3 wines that resemble the secret potion ingredients ---
# Select the top 3 wines based on the processed data
df_top3 = fig1.head(3)

# Assign ranks for the podium display (1st, 2nd, and 3rd places)
df_top3['Rank'] = [1.5, 1, 0.5]  # Adjust ranks for display
df_top3_podium = [df_top3.iloc[1], df_top3.iloc[0], df_top3.iloc[2]]  # Rearrange for podium display

# Create a bar chart to visualize the top 3 wines
fig1 = px.bar(df_top3_podium, x='Wines', y="Rank", text="Rating", 
              color=['#C0C0C0', "#FFD700", '#CD7F32'],  # Colors for Silver, Gold, and Bronze positions
              title='Top 3 Geppetto\'s Potion', height=600, width=800)

# Set the y-axis range to keep the ranks between 0 and 3 and hide the legend
fig1.update_layout(yaxis=dict(range=[0, 3]), showlegend=False)

# Display the bar chart in the Streamlit app
st.plotly_chart(fig1)
