import pandas as pd
import sqlite3

conn = sqlite3.connect('utils/vivino.db')

query = """
    SELECT
        wines.name AS wine_name,
        wines.sweetness,
        countries.name AS country_name,
        COUNT (vintages.id) AS vintage_count
    FROM
        wines
    JOIN
        regions ON wines.region_id = regions.id,
        countries ON regions.country_code = countries.code,
        vintages ON wines.id = vintages.wine_id
    GROUP BY
        vintages.wine_id"""

pd.read_sql_query(query, conn).to_csv('csv/q3_sweetness/vintage_count_per_wine.csv', index=False)