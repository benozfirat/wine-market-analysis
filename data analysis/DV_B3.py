import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    # Load the original data (non-normalized)
    df = pd.read_csv("countries.csv", usecols=['country', 'avg_price', 'avg_rating', 'wines_count', 'wineries_count'])
    
    # Convert string columns to categorical to save memory
    df['country'] = df['country'].astype('category')
    
    # Normalize the numeric columns
    df_numeric = df[['avg_price', 'avg_rating', 'wines_count', 'wineries_count']]
    df_normalized = (df_numeric - df_numeric.min()) / (df_numeric.max() - df_numeric.min())
    
    # Calculate the Price Score as 1 - normalized price
    df_normalized['price_score'] = 1 - df_normalized['avg_price']
    
    return df, df_normalized

# Load data
df_original, df_normalized = load_data()

# Factor mapping: Display name -> DataFrame column name
factor_map = {
    'Price': 'price_score',
    'Rating': 'avg_rating',
    'Wines Count': 'wines_count',
    'Wineries Count': 'wineries_count'
}

# Single multiselect for ranking factors
st.title("Rank the Importance of Each Factor")

factor_choices = ['Price', 'Rating', 'Wines Count', 'Wineries Count']
ranked_factors = st.multiselect(
    '**Rank the factors from most to least important (drag to reorder):**',
    factor_choices,
    default=factor_choices
)

# Ensure the list has all factors
if len(ranked_factors) != 4:
    st.error("Please rank all four factors.")
else:
    weights = {
        ranked_factors[0]: 0.4,
        ranked_factors[1]: 0.3,
        ranked_factors[2]: 0.2,
        ranked_factors[3]: 0.1
    }

    # Calculate the overall_score based on user selections
    df_normalized['overall_score'] = (
        df_normalized[factor_map[ranked_factors[0]]] * weights[ranked_factors[0]] +
        df_normalized[factor_map[ranked_factors[1]]] * weights[ranked_factors[1]] +
        df_normalized[factor_map[ranked_factors[2]]] * weights[ranked_factors[2]] +
        df_normalized[factor_map[ranked_factors[3]]] * weights[ranked_factors[3]]
    )

    # Add the overall_score to the original data
    df_original['overall_score'] = df_normalized['overall_score']

    # Round the values in the original data
    df_original = df_original.round(3)

    # Sort by overall_score
    df_original = df_original.sort_values(by='overall_score', ascending=False)

    # Rename the columns to more user-friendly names
    df_original.rename(columns={
        'country': 'Country',
        'avg_price': 'Average Price',
        'avg_rating': 'Average Rating',
        'wines_count': 'Wines Count',
        'wineries_count': 'Wineries Count',
        'overall_score': 'Overall Score'
    }, inplace=True)

    # Display top 3 results
    top_3 = df_original.head(5)

    st.subheader("Top 5 Countries by Customized Overall Score")

    # Display the top 3 results as a dataframe with original data
    st.dataframe(top_3.reset_index(drop=True), use_container_width=True)


