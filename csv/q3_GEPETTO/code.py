import sqlite3
import csv

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req = ('''
        SELECT 
            wines.name AS "wines_name", 
            countries.name AS "countries_name",
            SUM(wines.ratings_count) AS "wines_ratings_count",
            AVG(vintages.ratings_average) AS "vintages_ratings_avg",
            AVG(wines.ratings_average) AS "wines_ratings_avg"
            
        FROM 
            wines 
        JOIN regions ON wines.region_id = regions.id
        JOIN countries ON regions.country_code = countries.code
        JOIN vintages ON wines.id = vintages.wine_id
        WHERE 
            countries.name = 'Italie'
        GROUP BY 
            wines.name
        ORDER BY 
            wines.ratings_average DESC
        ''')

cursor.execute(req)

rows = cursor.fetchall()
csv_file_name = './csv/q3_GEPETTOwines_data.csv'

with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    headers = [i[0] for i in cursor.description]
    csv_writer.writerow(headers)
    
    csv_writer.writerows(rows)

conn.close()
