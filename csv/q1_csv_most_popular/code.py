import sqlite3
import csv

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req = (
'''
    select wines.name as Wines, wines.ratings_average as "Avg Rating", count(vintages.id) as "Nbr of vintage", countries.name as country, wines.ratings_count as "Rating Count"
    from wines
    join vintages on wines.id = vintages.wine_id
    join regions on wines.region_id = regions.id
    join countries on regions.country_code = countries.code
    where wines.ratings_count > 10000
    group by vintages.wine_id;
'''
)

cursor.execute(req)

rows = cursor.fetchall()
csv_file_name = 'wines_data.csv'

with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    headers = [i[0] for i in cursor.description]
    csv_writer.writerow(headers)
    
    csv_writer.writerows(rows)

conn.close()
