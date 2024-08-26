import sqlite3
import csv

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req = ('''
        SELECT 
            wines.name AS wine_name, 
            regions.name AS region_name, 
            AVG(vintages.price_euros) AS AVG_price,
            GROUP_CONCAT(vintages.year ORDER BY vintages.year ASC) AS list_of_years,
            AVG(vintages.ratings_average) AS avg_ratings,
            SUM(vintages.ratings_count) AS total_ratings_count
        FROM vintages
        JOIN wines ON vintages.wine_id = wines.id
        JOIN regions ON wines.region_id = regions.id
        JOIN countries ON regions.country_code = countries.code
        AND vintages.ratings_count > 500
        GROUP BY wines.name
        ORDER BY wines.name
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
