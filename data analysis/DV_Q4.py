import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

df4 = pd.read_csv("wines_data.csv")

st.title('Wines with Specific Tastes')

# Explanation 
explanation1 = """
### Introduction

We identified a significant group of customers who prefer a specific combination of flavors: **coffee, toast, green apple, cream, and citrus**. We've dubbed this flavor profile **Flavor of Sunrise**. Among our wine offerings, **19** wines exhibit these characteristics. We'll delve deeper into these wines to understand their unique qualities.

"""
st.markdown(explanation1)

explanation2 = """ 
### Distribution of Wines 

The following bar chart reveals that *Champagne* in France is a dominant source of wines with the **Flavor of Sunrise** characteristics. Other regions contributing to this profile include *Sauternes* in France and *Trebbiano d'Abruzzo* in Italy.

"""
st.markdown(explanation2)

# Group the data by countries and regions, combining 'Champagne' regions
df4["regions_name"] = df4["regions_name"].apply(lambda x: "Champagne" if "Champagne" in x else x)

# Group by country and the modified region, then count occurrences
grouped_data = df4.groupby(["countries_name", "regions_name"]).size().unstack(fill_value=0)

# Create a horizontal stacked bar chart
plt.figure(figsize=(8, 4))
grouped_data.plot(kind='barh', stacked=True, figsize=(8, 4))

# Adding labels and title
plt.ylabel("Country")
plt.xlabel("Count of Wines")
plt.title("Distribution of Wines by Country and Region")
plt.gca().xaxis.set_major_locator(MultipleLocator(2))   
plt.legend(title="Region", bbox_to_anchor=(0.655, 0.95), loc='upper left')
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(plt)

explanation3 = """ 

Futhermore, Regional wines, named after their respective locales, showcase the unique character of their production areas.
**Champagne** produced in *Champagne*, is known for its effervescence, complex flavors, and elegant bubbles.
**Sauternes** is a sweet white wine produced in *Sauternes* region of Bordeaux, France, renowned for its golden color, luscious texture, and concentrated flavors of honey, apricot, and candied fruit, often resulting from the noble rot process. 
**Trebbiano d'Abruzzo** is a white wine produced in the *Trebbiano d'Abruzzo* region of Italy, known for its light, refreshing character with citrusy notes.
"""
st.markdown(explanation3)


# Group data by region and count occurrences
grouped_data = df4.groupby('regions_name').size().reset_index(name='count')

# Combine small regions into "Others" to make the pie chart cleaner (optional)
threshold = 5  # You can adjust this threshold
grouped_data.loc[grouped_data['count'] < threshold, 'regions_name'] = 'Others'
grouped_data = grouped_data.groupby('regions_name').sum().reset_index()

# Create two columns in Streamlit
col1, col2 = st.columns(2)

# First Pie Chart: Distribution of Wines by Region
with col1:
    plt.figure(figsize=(5, 5))
    plt.pie(grouped_data['count'], labels=grouped_data['regions_name'], autopct='%1.1f%%', colors=plt.cm.tab20.colors)
    plt.title('Distribution of Wines type')
    st.pyplot(plt)

# Second Bar Chart: Distribution of Average Ratings
with col2:
    # Get the 'ratings_average' column and count occurrences
    avg_ratings_counts = df4['ratings_average'].value_counts().sort_index()

    plt.figure(figsize=(5, 5))
    plt.bar(avg_ratings_counts.index, avg_ratings_counts, color='darkblue', width = 0.05)
    plt.xlabel('Average Rating')
    plt.ylabel('Count')
    plt.title('Distribution of Average Ratings')
    plt.xlim(4.3, 4.8) 
    st.pyplot(plt)

explanation4 = """ 

Most wines with the **Flavor of Sunrise** profile are Champagnes, accounting for 84.2% of the total. These Champagnes typically receive average ratings between 4.5 and 4.7. While the majority are from Champagne, two wines come from *Sauternes*. Despite similar acidity, intensity, and sweetness levels, the 'Sauternes (Premier Grand Cru Classé)'—the region's highest-ranked wine—received an average rating of 4.4, while the standard 'Sauternes' garnered a rating of 4.7. the Italian wine 'Trebbiano d'Abruzzo' earned an average rating of 4.4. For more details, please refer to the table below.
"""
st.markdown(explanation4)


explanation5 = """ 
###  Wines with Flavor of Sunrise 
"""
st.markdown(explanation5)
st.dataframe(df4[['wines_name', 'ratings_average', 'wines_acidity', 'wines_fizziness', 'wines_intensity', 'wines_sweetness', 'countries_name', 'regions_name']])