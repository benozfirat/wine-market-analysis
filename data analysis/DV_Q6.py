import streamlit as st
import pandas as pd

# Load the data
df6 = pd.read_csv("rating_per_countries.csv")

# Map countries to flags
flags = {
    'Afrique du Sud': '🇿🇦',
    'Allemagne': '🇩🇪',
    'Argentine': '🇦🇷',
    'Australie': '🇦🇺',
    'Chili': '🇨🇱',
    'Croatie': '🇭🇷',
    'Espagne': '🇪🇸',
    'France': '🇫🇷',
    'Grèce': '🇬🇷',
    'Hongrie': '🇭🇺',
    'Israël': '🇮🇱',
    'Italie': '🇮🇹',
    'Moldavie': '🇲🇩',
    'Portugal': '🇵🇹',
    'Roumanie': '🇷🇴',
    'Suisse': '🇨🇭',
    'États-Unis': '🇺🇸'
}

# Add the flag column
df6['Flag'] = df6['country'].map(flags)

# Round the ratings to two decimal places
df6['wines_rating'] = df6['wines_rating'].round(2)
df6['vintages_rating'] = df6['vintages_rating'].round(2)

# Sort by Wine scores and assign medals
df_wine = df6.sort_values(by='wines_rating', ascending=False).reset_index(drop=True)
df_wine['Rank'] = range(1, len(df_wine) + 1)
df_wine.loc[0:2, 'Rank'] = ['🥇', '🥈', '🥉']

# Sort by Vintage scores and assign medals
df_vintage = df6.sort_values(by='vintages_rating', ascending=False).reset_index(drop=True)
df_vintage['Rank'] = range(1, len(df_vintage) + 1)
df_vintage.loc[0:2, 'Rank'] = ['🥇', '🥈', '🥉']

# Streamlit app layout
st.title("Wine and Vintage Leaderboards")

# Function to generate HTML table without index
def generate_table_html(df, rating_column):
    table_html = f"<table><tr><th>Rank</th><th>Flag</th><th>Country</th><th>{rating_column}</th></tr>"
    for i, row in df.iterrows():
        table_html += f"<tr><td>{row['Rank']}</td><td>{row['Flag']}</td><td>{row['country']}</td><td>{row[rating_column]}</td></tr>"
    table_html += "</table>"
    return table_html

# Create two columns in Streamlit
col1, col2 = st.columns(2)

# Display Wine leaderboard in the first column
with col1:
    st.markdown("### Wine Leaderboard")
    st.markdown(generate_table_html(df_wine, 'wines_rating'), unsafe_allow_html=True)

# Display Vintage leaderboard in the second column
with col2:
    st.markdown("### Vintage Leaderboard")
    st.markdown(generate_table_html(df_vintage, 'vintages_rating'), unsafe_allow_html=True)

