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

query2 = 'select year, count(*) as total from crimes group by year order by year asc;'

df2 = pd.read_sql(query2, connection)

plt.figure (figsize=(8,5))
plt.plot(df2['year'], df2 ['total'], marker='o')
plt.xlabel('year')
plt.ylabel('number of crimes')
plt.title('chicago crime trends by year')
plt.tight_layout()
plt.savefig('crime_by_year.png')
plt.show()

query3 = "select primary_type, count(*) as total_crime, sum(case when arrest = 'true' then 1 else 0 end) as arrest, round(sum(case when arrest = 'true' then 1 else 0 end)/count(*) * 100, 1) as arrest_rate_pct from crimes group by primary_type order by arrest_rate_pct desc;"

df3 = pd.read_sql(query3, connection)

plt.figure (figsize=(8,10))
plt.barh(df3['primary_type'], df3 ['arrest_rate_pct'])
plt.xlabel('arrest rate(%)')
plt.ylabel('crime type')
plt.title('arrest rate by crime type')
plt.tight_layout()
plt.savefig('arrest_rate_by_type.png')
plt.show()

connection.close()


