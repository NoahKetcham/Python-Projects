
import sqlite3

#list of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
             'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('test2.db')#Connecting to the DB
cur = conn.cursor() #Use cursor to input into DB

#Creating table in DB
with conn:
    cur.execute("CREATE TABLE IF NOT EXISTS table_db ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            filename TEXT)") #The \ allows for the use of a multiline string, ''' is also acceptable
    conn.commit()#Commit changes


#Reading from the supplied list of filenames and filtering the files with a .txt format.

with conn:
    for fileName in fileList:
        if fileName.endswith('.txt'):
            cur.execute('INSERT INTO table_db (filename) VALUES (?)', (fileName,))
    conn.commit()

#QUERE THE DATABASE FOR TEXT FILES

    cur.execute('SELECT filename FROM table_db WHERE filename LIKE "%.txt"')
    txtFiles = cur.fetchall()
conn.close()#Close connection

#PRINT THE TEXT FILES
for txtFile in txtFiles:
    print(txtFile[0])
