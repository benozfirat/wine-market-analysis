import pandas as pd
import sqlite3

conn = sqlite3.connect('utils/vivino.db')

query = """
    SELECT
    country,
    avg_price,
    avg_rating,
    countries.wines_count,
    countries.wineries_count,
    (avg_price * 0.3) + (avg_rating * 0.3) + (countries.wines_count * 0.1) + (countries.wineries_count * 0.1) + (countries.users_count * 0.2) AS overall_score
FROM (
    SELECT
        countries.name AS country,
        AVG(vintages.price_euros) AS avg_price,
        AVG(wines.ratings_average) AS avg_rating
    FROM
        countries
    JOIN
        regions ON countries.code = regions.country_code,
        wines ON regions.id = wines.region_id,
        vintages ON wines.id = vintages.wine_id
    LEFT JOIN
        wineries ON wines.winery_id = wineries.id
    GROUP BY
        countries.name)
JOIN
    countries ON countries.name = country"""

pd.read_sql_query(query, conn).to_csv('csv/q2_countries/vintage_count_per_wine.csv', index=False)