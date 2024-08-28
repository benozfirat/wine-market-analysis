import sqlite3
import panda

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

 req = ('''
          SELECT 
              wines.name AS "Wines",
              wines.ratings_average AS "Rating",
              wines.ratings_count AS "Reviews",
              wines.is_natural AS "Natural",
              AVG(vintages.ratings_average) AS "Vintage Rating"
          FROM wines
          JOIN vintages ON wines.id = vintages.wine_id
          GROUP BY wines.name
''')

cursor.execute(req)

pd.read_sql_query(req, conn).to_csv('./csv/bq1_natural/wines_data.csv', index=False)

conn.close()
