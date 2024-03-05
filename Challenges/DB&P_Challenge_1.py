import sqlite3

# Create a database in RAM and establish a connection
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# 1. Create the database table named Roster
cursor.execute('''CREATE TABLE Roster
               (Name TEXT, Species TEXT, IQ INT)''')

# 2. Populate the table with the provided values
entries = [
    ('Jean-Baptiste Zorg', 'Human', 122),
    ('Korben Dallas', 'Meat Popsicle', 100),
    ('Ak\'not', 'Mangalore', -5)
]
cursor.executemany('INSERT INTO Roster VALUES (?,?,?)', entries)

# 3. Update the Species of Korben Dallas to Human
cursor.execute('UPDATE Roster SET Species = ? WHERE Name = ?', ('Human', 'Korben Dallas'))

# 4. Display the names and IQs of everyone in the table who is classified as Human
cursor.execute('SELECT Name, IQ FROM Roster WHERE Species = "Human"')
humans = cursor.fetchall()

# Close the connection to the database
conn.close()

# Print the results
for human in humans:
    print(f"Name: {human[0]}, IQ: {human[1]}")
