import sqlite3
import panda

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

 req = ('''
        SELECT
            Wines,
            Reviews,
            Rating,
            Tannin,
            Acidity,
            Intensity,
            avg(Vintage_Rating) as "Vintage Rating",
            COUNT(DISTINCT Keywords) as "Keywords_count"
            FROM (
            SELECT 
                wines.name AS "Wines",
                wines.ratings_count AS "Reviews",
                wines.ratings_average AS "Rating",
                wines.tannin AS "Tannin",
                wines.acidity AS "Acidity",
                wines.intensity AS "Intensity",
                keywords.name AS "Keywords",
                vintages.ratings_average AS "Vintage_Rating"
            FROM wines
            JOIN regions ON wines.region_id = regions.id
            JOIN keywords_wine ON wines.id = keywords_wine.wine_id
            JOIN keywords ON keywords.id = keywords_wine.keyword_id
            JOIN vintages ON wines.id = vintages.wine_id
            WHERE keywords.name IN ('dark fruit', 'blackcurrant', 'blackberry', 'cedar', 'tobacco', 'mint', 'earthy', 'leather', 'dried herbs', 'cigar Box')
           )
        GROUP BY Wines
''')

cursor.execute(req)

pd.read_sql_query(req, conn).to_csv('./csv/q7_one_of_our_VIP/wines_data.csv', index=False)

conn.close()
