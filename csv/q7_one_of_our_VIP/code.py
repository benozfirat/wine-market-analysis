import sqlite3
import csv

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req =('''
        SELECT 
            vintages.name AS "vintages_name", 
            wines.name AS "wines_name", 
            vintages.ratings_average AS "vintages_ratings_average", 
            vintages.ratings_count AS "vintages_ratings_count", 
            vintages.price_euros AS "vintages_price_euros"
        From vintages
        JOIN wines ON vintages.wine_id = wines.id
        WHERE wines.name LIKE '%Cabernet Sauvignon%'
        ORDER BY vintages.ratings_average desc
        LIMIT 5;
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
