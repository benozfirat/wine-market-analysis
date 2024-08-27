import pandas as pd
import sqlite3

conn = sqlite3.connect('utils/vivino.db')

query = """
    SELECT
        countries.name AS country,
        SUM((wines.ratings_average)*(wines.ratings_count)) / SUM(wines.ratings_count) AS wines_rating,
        SUM((vintages.ratings_average)*(vintages.ratings_count)) / SUM(vintages.ratings_count) AS vintages_rating
    FROM
        countries
    JOIN
        regions ON country_code = countries.code,
        wines ON region_id = regions.id,
        vintages ON wine_id = wines.id
    GROUP BY
        countries.name"""

pd.read_sql_query(query, conn).to_csv('csv/q6_average_rating/rating_per_countries.csv', index=False)