import sqlite3
import panda

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req =('''
        SELECT 
            wines.name AS "Wines",
            countries.name AS "Country",
            wines.ratings_count AS "Reviews",
            wines.ratings_average AS "Rating",
            wines.tannin AS "Tannin",
            wines.acidity AS "Acidity",
            AVG(vintages.ratings_average) AS "Vintage Rating"
        FROM wines
        JOIN regions ON wines.region_id = regions.id
        JOIN countries ON regions.country_code = countries.code
        JOIN keywords_wine ON wines.id = keywords_wine.wine_id
        JOIN vintages ON wines.id = vintages.wine_id
        GROUP BY wines.name
        ORDER BY wines.ratings_average DESC
      ''')

cursor.execute(req)

pd.read_sql_query(req, conn).to_csv('./csv/q7_one_of_our_VIP/wines_data.csv', index=False)

conn.close()
