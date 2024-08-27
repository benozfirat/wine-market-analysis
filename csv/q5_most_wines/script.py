import pandas as pd
import sqlite3

conn = sqlite3.connect('utils/vivino.db')

query1 = """
    SELECT
        grapes.name,
        most_used_grapes_per_country.wines_count
    FROM
        grapes
    JOIN
        most_used_grapes_per_country ON grapes.id = most_used_grapes_per_country.grape_id
    GROUP BY
        grapes.id"""

query2 = """
    SELECT
        wines.name AS Wines,
        countries.name AS Country,
        wines.ratings_count AS Reviews,
        wines.ratings_average AS Rating
    FROM
        wines
    JOIN
        regions ON wines.region_id = regions.id,
        countries ON regions.country_code = countries.code"""

pd.read_sql_query(query1, conn).to_csv('csv/q5_most_wines/wines_count.csv', index=False)
pd.read_sql_query(query2, conn).to_csv('csv/q5_most_wines/wines_ratings.csv', index=False)