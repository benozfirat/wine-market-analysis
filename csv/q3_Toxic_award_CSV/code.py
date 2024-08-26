import sqlite3
import csv

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req = ('''
        SELECT 
            wines.name as "wines name",
            wines.acidity,
            wines.ratings_count,
            wines.ratings_average,
            countries.name as country,
            count(vintages.id) as "vintage count"
        FROM
            wines
        JOIN regions ON wines.region_id = regions.id
        JOIN countries ON regions.country_code = countries.code
        JOIN vintages ON wines.id = vintages.wine_id
        GROUP BY wines.name
        ORDER BY wines.ratings_average DESC;
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