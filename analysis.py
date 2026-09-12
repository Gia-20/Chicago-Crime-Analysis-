import mysql.connector
import pandas as pd 

connection= mysql.connector.connect(
host='localhost',
user='root',
password='Password123',
database='chicago_crime'
)

query = 'select primary_type, count(*) as total from crimes group by primary_type order by total desc;'

df = pd.read_sql(query, connection)

import matplotlib.pyplot as plt 

plt.figure(figsize=(10,6))
plt.bar(df['primary_type'],df['total'])
plt.xlabel('crime type')
plt.ylabel('number of crimes')
plt.xticks(rotation=90)
plt.title('chicago crime counts by type')
plt.tight_layout()
plt.savefig('crime_by_type.png')
plt.show()

connection.close()
