import sqlite3
import csv

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req = ('''
    SELECT name as "wines_name",
        GROUP_CONCAT(keyword_name, ',') AS sunrise
    FROM (
        SELECT DISTINCT wines.name AS name, keywords.name AS keyword_name
        FROM wines
        JOIN regions ON wines.region_id = regions.id
        JOIN countries ON regions.country_code = countries.code
        JOIN keywords_wine ON wines.id = keywords_wine.wine_id
        JOIN keywords ON keywords.id = keywords_wine.keyword_id
        WHERE keywords.name IN ('coffee', 'toast', 'green apple', 'cream', 'citrus')
        AND keywords_wine.count >= 10
        ORDER BY keywords.name
    ) AS unique_keywords
    GROUP BY name
    HAVING COUNT(DISTINCT keyword_name) = 5
    ORDER BY name DESC;
''')

cursor.execute(req)

rows = cursor.fetchall()
csv_file_name = 'wines_data.csv'

with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    headers = [i[0] for i in cursor.description]
    csv_writer.writerow(headers)
    
    csv_writer.writerows(rows)

conn.close()
