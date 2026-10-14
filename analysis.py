import getpass
import mysql.connector
import pandas as pd 

connection= mysql.connector.connect(
host='localhost',
user='root',
password=getpass.getpass('MySQL password:Geetanjali2006 '),
database='chicago_crime'
)

query = 'select primary_type, count(*) as total from crimes group by primary_type order by total desc;'

df = pd.read_sql(query, connection)

import matplotlib.pyplot as plt 

plt.figure(figsize=(10,6))
plt.bar(df['primary_type'],df['total'])
plt.xlabel('Crime Type')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=90)
plt.title('Chicago Crime Counts by Type')
plt.tight_layout()
plt.savefig('crime_by_type.png')
plt.show()

query2 = 'select year, count(*) as total from crimes group by year order by year asc;'

df2 = pd.read_sql(query2, connection)

plt.figure (figsize=(8,5))
plt.plot(df2['year'], df2 ['total'], marker='o')
plt.xticks(df2['year'])
plt.xlabel('Year (2026 is a partial year)')
plt.ylabel('Number of Crimes')
plt.title('Chicago Crime Trends by Year')
plt.tight_layout()
plt.savefig('crime_by_year.png')
plt.show()

query3 = "select primary_type, count(*) as total_crime, sum(case when arrest = 'true' then 1 else 0 end) as arrest, round(sum(case when arrest = 'true' then 1 else 0 end)/count(*) * 100, 1) as arrest_rate_pct from crimes group by primary_type order by arrest_rate_pct desc;"

df3 = pd.read_sql(query3, connection)

plt.figure (figsize=(8,10))
plt.barh(df3['primary_type'], df3 ['arrest_rate_pct'])
plt.xlabel('Arrest Rate(%)')
plt.ylabel('Crime Type')
plt.title('Arrest Rate by Crime Type')
plt.tight_layout()
plt.savefig('arrest_rate_by_type.png')
plt.show()

query4 = "select hour(str_to_date(date_occurred, '%m/%d/%Y %h:%i:%s %p')) as hour_of_day, count(*) as total from crimes group by hour_of_day order by hour_of_day;"

df4 = pd.read_sql(query4, connection)

plt.figure(figsize=(10,5))
plt.bar(df4['hour_of_day'], df4['total'])
plt.xticks(range(0, 24))
plt.xlabel('Hour of Day (0 = midnight)')
plt.ylabel('Number of Crimes')
plt.title('Chicago Crimes by Hour of Day')
plt.tight_layout()
plt.savefig('crime_by_hour.png')
plt.show()

query5 = "select district, count(*) as total from crimes where district is not null group by district order by total desc limit 10;"

df5 = pd.read_sql(query5, connection)

plt.figure(figsize=(8,5))
plt.bar(df5['district'].astype(str), df5['total'])
plt.xlabel('Police District')
plt.ylabel('Number of Crimes')
plt.title('Top 10 Chicago Police Districts by Crime Count')
plt.tight_layout()
plt.savefig('crime_by_district.png')
plt.show()


connection.close()


