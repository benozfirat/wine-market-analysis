import sqlite3
import csv

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req = ('''
    select wines.name AS name, STRING_AGG(keywords_wine.sunrise, ', ') AS sunrise
    from wines
    join regions ON wines.region_id = regions.id
    join countries ON regions.country_code = countries.code
    join keywords_wine ON wines.id = keywords_wine.wine_id
    join keywords ON keywords.id = keywords_wine.keyword_id
    where keywords.name IN ('coffee', 'toast', 'green apple', 'cream', 'citrus') and keywords_wine.count >= 10
    group by wines.name
    order by wines.name DESC;
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
