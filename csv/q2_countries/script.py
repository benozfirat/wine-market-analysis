import pandas as pd
import sqlite3

conn = sqlite3.connect('utils/vivino.db')

query = """
    SELECT
    countries.name AS country,
    AVG(vintages.price_euros) AS avg_price,
    AVG(wines.ratings_average) AS avg_rating,
    countries.wines_count,
    countries.wineries_count,
    wines.user_structure_count
FROM
    countries
JOIN
    regions ON countries.code = regions.country_code,
    wines ON regions.id = wines.region_id,
    vintages ON wines.id = vintages.wine_id
LEFT JOIN
    wineries ON wines.winery_id = wineries.id
GROUP BY
    countries.name"""

pd.read_sql_query(query, conn).to_csv('csv/q2_countries/countries.csv', index=False)