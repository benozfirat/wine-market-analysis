import sqlite3
import csv

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req = (
    '''
        select wines.name, is_natural, regions.name, wineries.name, ratings_average, ratings_count, url, acidity, fizziness, intensity, sweetness, tannin, user_structure_count
        from wines
        left join regions on wines.region_id = regions.id
        left join wineries on wines.winery_id = wineries.id
        where regions.country_code = 'BE'
        limit 10
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
