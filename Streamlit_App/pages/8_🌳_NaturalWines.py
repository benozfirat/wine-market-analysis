# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Streamlit configuration: Set up the page title and icon
st.set_page_config(page_title="Natural Wines", page_icon="🌳")

# Display the header for the Natural Wines section
st.header('Natural Wines :deciduous_tree:')

# Explanation of the section on Natural Wines
explanation = """
### Should we invest more into Natural Wines? 🌿 \n 

**Natural wines are made from grapes that are grown without the use of artificial or synthetic chemicals, such as herbicides and pesticides.**

"""
# Display the explanation using markdown formatting
st.markdown(explanation)

# Load the dataset for Natural Wines from a CSV file
df_natural = pd.read_csv('utils/Natural_Wines.csv', encoding='UTF-8')

# Convert the 'Natural' column from numerical (0/1) to categorical (No/Yes)
df_natural['Natural'] = df_natural['Natural'].apply(lambda x: 'Yes' if x == 1 else 'No')

# --- Natural Wines Percentage ---
# Count the number of natural vs. normal wines
natural_counts = df_natural['Natural'].value_counts().reset_index()
natural_counts.columns = ['Natural', 'count']  # Rename columns for clarity

# Create a pie chart to visualize the proportion of natural vs. normal wines
fig = px.pie(natural_counts, values='count', names='Natural', title=' ', color_discrete_sequence=["#A30000","#F6D173"])
st.subheader('Is it a natural wine? (Wines from our website) :bar_chart: \n')
st.plotly_chart(fig)

# --- Normal vs Natural Wines Comparison in terms of Ratings ---
# Separate the dataset into natural and normal wines
natural_wines = df_natural[df_natural['Natural'] == 'Yes']
normal_wines = df_natural[df_natural['Natural'] == 'No']

# Calculate the average rating for both natural and normal wines
avg_rating_natural = natural_wines['Rating'].mean()
avg_rating_normal = normal_wines['Rating'].mean()

# Calculate the average vintage rating for both natural and normal wines
vintage_rating_natural = natural_wines['Vintage Rating'].mean()
vintage_rating_normal = normal_wines['Vintage Rating'].mean()

# Create a new DataFrame to hold the comparison data
new_df = pd.DataFrame({'Type': ['Natural', 'Normal'],
                       'Average Rating': [avg_rating_natural, avg_rating_normal],
                       'Average Vintage Rating': [vintage_rating_natural, vintage_rating_normal]})

# Display the subheader and description for the comparison chart
st.subheader('Normal vs Natural Wines Comparison :bar_chart: \n')
st.write('Comparison between Natural and Normal Wines based on their average ratings and average vintage ratings.')

# Create a bar chart comparing average ratings and vintage ratings between natural and normal wines
fig1 = go.Figure(data=[
    go.Bar(name='Wine Average', x=new_df['Type'], y=new_df['Average Rating'], text=new_df['Average Rating'].round(2), textposition='auto', marker=dict(color='#F55B5B')),
    go.Bar(name='Vintage Average', x=new_df['Type'], y=new_df['Average Vintage Rating'], text=new_df['Average Vintage Rating'].round(2), textposition='auto', marker=dict(color='#5752D1'))
])
fig1.update_layout(yaxis=dict(range=[0, 5]))  # Set the y-axis range from 0 to 5
st.plotly_chart(fig1)

# --- Normal vs Natural Wines Comparison in terms of Reviews count ---
# Calculate the average number of reviews for both natural and normal wines
reviews_natural = natural_wines['Reviews'].mean()
reviews_normal = normal_wines['Reviews'].mean()

# Create a new DataFrame to hold the comparison data for reviews
new_df2 = pd.DataFrame({'Type': ['Natural', 'Normal'],
                        'Average Reviews': [reviews_natural, reviews_normal]})

# Create a bar chart comparing the average number of reviews between natural and normal wines
fig2 = px.bar(new_df2, x='Type', y='Average Reviews', color='Type', title=' ', color_discrete_sequence=["#F55B5B","#5752D1"])

# Display the subheader and description for the reviews comparison chart
st.subheader('Average Reviews per Type :bar_chart: \n')
st.write('Comparison between Natural and Normal Wines based on their average reviews.')
st.plotly_chart(fig2)
