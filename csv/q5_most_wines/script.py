import pandas as pd
import sqlite3

conn = sqlite3.connect('utils/vivino.db')

query = """
    SELECT
        grapes.name,
        most_used_grapes_per_country.wines_count
    FROM
        grapes
    JOIN
        most_used_grapes_per_country ON grapes.id = most_used_grapes_per_country.grape_id
    GROUP BY
        grapes.id"""

pd.read_sql_query(query, conn).to_csv('csv/q5_most_wines/wines_count.csv', index=False)