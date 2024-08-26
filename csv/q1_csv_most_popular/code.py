import sqlite3
import csv

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req = ('''
        SELECT 
            wines.name AS "wines_name", 
            countries.name AS country, 
            COUNT(vintages.id) AS "nbr_of_vintage", 
            wines.ratings_count AS "wines_rating_count",
            wines.ratings_average AS "wines_rating_avg"       
            
        FROM 
            wines
        JOIN vintages ON wines.id = vintages.wine_id
        JOIN regions ON wines.region_id = regions.id
        JOIN countries ON regions.country_code = countries.code
        WHERE 
            wines.ratings_count > 10000
        GROUP BY 
            wines.id, wines.name, wines.ratings_average, countries.name, wines.ratings_count
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
