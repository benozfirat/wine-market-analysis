import pandas as pd
import sqlite3

conn = sqlite3.connect('utils/vivino.db')

query = """
    SELECT
        countries.name AS country,
        AVG(wines.ratings_average) AS wine_rating,
        AVG(vintages.ratings_average) AS vintage_rating
    FROM
        countries
    JOIN
        regions ON country_code = countries.code,
        wines ON region_id = regions.id,
        vintages ON wine_id = wines.id
    GROUP BY
        countries.name"""

pd.read_sql_query(query, conn).to_csv('csv/q6_average_rating/rating_per_countries.csv', index=False)