import sqlite3

db_name: str = "hw_solution"
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS shopping (id INTEGER PRIMARY KEY, name TEXT, amount INTEGER);
''')

print("Table created or already exists.")

cursor.execute('''
INSERT INTO shopping VALUES (1, 'Avokado', 5);
INSERT INTO shopping VALUES (2, 'Milk', 2);
INSERT INTO shopping VALUES (3, 'Bread', 3);
INSERT INTO shopping VALUES (4, 'Chocolate', 8);
INSERT INTO shopping VALUES (5, 'Bamba', 5);
INSERT INTO shopping VALUES (6, 'Orange', 10);
''')
print("Data inserted.")
conn.commit()

cursor.execute('SELECT * FROM shopping')
rows = cursor.fetchall()
print("All Data:")
for row in rows:
    print(dict(row))


cursor.execute('SELECT * FROM shopping WHERE amount > 5')
rows = cursor.fetchall()
print("\nItems with amount > 5:")
for row in rows:
    print(dict(row))


cursor.execute("DELETE from shopping WHERE name LIKE 'Orange';")
conn.commit()
print("\n'Orange' has been deleted.")


cursor.execute('SELECT * FROM shopping')
rows = cursor.fetchall()
print("\nData after deletion:")
for row in rows:
    print(dict(row))


cursor.execute("UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'")
conn.commit()
print("\n'Bamba' has been renamed to 'Bisli'.")


cursor.execute('SELECT * FROM shopping')
rows = cursor.fetchall()
print("\nData after renaming 'Bamba' to 'Bisli':")
conn.commit()
for row in rows:
    print(dict(row))


cursor.execute("UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'")
conn.commit()
print("\n'Amount for Milk' has been updated to 1.")


cursor.execute('SELECT * FROM shopping')
rows = cursor.fetchall()
print("\nData after updating 'Milk' amount:")
for row in rows:
    print(dict(row))


cursor.execute("SELECT COUNT(*) FROM shopping")
count = cursor.fetchone()
print("\nTotal number of items in shopping list:", count[0])


cursor.execute("SELECT * FROM shopping WHERE id > 0")
rows = cursor.fetchall()
print("\nAll items with id > 0:")
for row in rows:
    print(dict(row))

conn.close()
