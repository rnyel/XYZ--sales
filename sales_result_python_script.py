import sqlite3
import pandas as pd

# Connect to the SQLite database “SALES”
conn = sqlite3.connect('SALES.db')
curs=conn.cursor()

# SQL query to fetch data
sql_query = """
    SELECT c.customer_id, c.age, i.item_name, SUM(o.quantity) AS total_quantity
    FROM Customer c
    JOIN Sales s ON c.customer_id = s.customer_id
    JOIN Orders o ON s.sales_id = o.sales_id
    JOIN Items i ON o.item_id = i.item_id
    WHERE c.age BETWEEN 18 AND 35 AND o.quantity IS NOT NULL
    GROUP BY c.customer_id, c.age, i.item_name
    HAVING total_quantity > 0
    ORDER BY c.customer_id, i.item_name;
"""
curs.execute(sql_query)
result=curs.fetchall()

# Close the database connection
conn.close()

# Read SQL query into a DataFrame
df = pd.DataFrame(result, columns=['customer_id', 'age', 'item_name', 'total_quantity'])


# Write the DataFrame to a CSV file
df.to_csv('output.csv', sep=';', index=False)
