import streamlit as st
import pandas as pd

# Load and prepare the data
df2 = pd.read_csv("countries.csv")
df2 = df2.drop('user_structure_count', axis=1)
df_numeric = df2.select_dtypes(include=['number'])

# Normalize the numeric columns
df_normalized = (df_numeric - df_numeric.min()) / (df_numeric.max() - df_numeric.min())
df2[df_numeric.columns] = df_normalized

# Calculate the overall_score
df2['overall_score'] = ((1 - df2['avg_price']) * 0.4 + 
                        df2['avg_rating'] * 0.3 + 
                        df2['wines_count'] * 0.2 + 
                        df2['wineries_count'] * 0.1)

# Round the values
df2 = df2.round(3)

# Sort by overall_score
df2 = df2.sort_values(by='overall_score', ascending=False)

# Rename the columns
df2.rename(columns={
    'country': 'Country',
    'avg_price': 'Price Score',
    'avg_rating': 'Rating Score',
    'wines_count': 'Wines Count',
    'wineries_count': 'Wineries Count',
    'overall_score': 'Overall Score'
}, inplace=True)

# Display top 5 results
top_5 = df2.head(5)

# Streamlit app layout
st.title("Top 5 Countries by Overall Score")

# Explanation of the overall score calculation
explanation = """
### Explanation of Overall Score Calculation

The **Overall Score** is calculated using the following formula:

Overall Score = (1 - Average Price) * 0.4 + (Average Rating * 0.3) + (Wines Count * 0.2) + (Wineries Count * 0.1)

- **Average Price** is inverted (1 - Average Price) to reflect that a lower price is better.
- **Average Rating** reflects the quality of the wines.
- **Wines Count** and **Wineries Count** provide an indication of the quantity and diversity.
- The weights assigned to each factor represent their relative importance in the overall score.
"""

# Display the explanation
st.markdown(explanation)

# Display the top 5 results as a dataframe
st.dataframe(top_5.reset_index(drop=True), use_container_width=True)