import sqlite3
import csv

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req = ('''
        SELECT 
            wines_name AS "wines_name",
            GROUP_CONCAT(keyword_name, ',') AS sunrise,
            countries_name,
            ratings_average,
            wines_acidity,
            wines_fizziness,
            wines_intensity,
            wines_sweetness,
            wines_tannin,
            regions_name
        FROM (
            SELECT DISTINCT 
                wines.name AS "wines_name", 
                keywords.name AS keyword_name, 
                countries.name AS "countries_name", 
                wines.ratings_average AS "ratings_average",
                wines.acidity AS "wines_acidity",
                wines.fizziness AS "wines_fizziness",
                wines.intensity AS "wines_intensity",
                wines.sweetness AS "wines_sweetness",
                wines.tannin AS "wines_tannin",
                regions.name AS "regions_name"
            FROM wines
            JOIN regions ON wines.region_id = regions.id
            JOIN countries ON regions.country_code = countries.code
            JOIN keywords_wine ON wines.id = keywords_wine.wine_id
            JOIN keywords ON keywords.id = keywords_wine.keyword_id
            WHERE keywords.name IN ('coffee', 'toast', 'green apple', 'cream', 'citrus')
            AND keywords_wine.count >= 10
            ORDER BY keywords.name
        ) AS unique_keywords
        GROUP BY wines_name
        HAVING COUNT(DISTINCT keyword_name) = 5
        ORDER BY wines_name DESC;
''')

cursor.execute(req)

rows = cursor.fetchall()
csv_file_name = './csv/q4_keyword/wines_data.csv'

with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    headers = [i[0] for i in cursor.description]
    csv_writer.writerow(headers)
    
    csv_writer.writerows(rows)

conn.close()
