import sqlite3
import panda

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req = ('''
    SELECT
        Wines,
        Reviews,
        Rating,
        COUNT(DISTINCT Keywords) as "Keywords_count"
        FROM (
        SELECT 
            wines.name AS "Wines",
            wines.ratings_count AS "Reviews",
            wines.ratings_average AS "Rating",
            countries.name AS "Country",
            keywords.name AS "Keywords"
        FROM wines
        JOIN regions ON wines.region_id = regions.id
        JOIN countries ON regions.country_code = countries.code
        JOIN keywords_wine ON wines.id = keywords_wine.wine_id
        JOIN keywords ON keywords.id = keywords_wine.keyword_id
        JOIN vintages ON wines.id = vintages.wine_id
        WHERE keywords.name IN ('coffee', 'bacon fat', "baby\'breath", 'chalk', 'Clay Dust', 'kerosene', 'pencil lead', 'potpourri', 'rubber ciment', 'wet gravel', "cat\'s pee")
        AND keywords_wine.count >= 10
   )
    GROUP BY Wines
''')

cursor.execute(req)

pd.read_sql_query(req, conn).to_csv('./csv/bq1_natural/wines_data.csv', index=False)

conn.close()
