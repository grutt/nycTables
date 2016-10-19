from bs4 import BeautifulSoup
import requests
import sqlite3

c = sqlite3.connect('nyc.db')
# Create table
c.execute('''Drop TABLE communityBoards''')
c.execute('''CREATE TABLE communityBoards
             (board text, area text, pop text, normedPop text, neighborhoods text)''')

r = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City')
soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find("table")
data = []
for row in table.findAll("tr"):
    dataRow = []
    for i, col in enumerate(row.findAll("td")):
        dataRow.append(col.find(text=True).encode('utf-8'))
    print(len(dataRow))
    if(len(dataRow)>=5):
        c.execute("INSERT INTO communityBoards VALUES (?,?,?,?,?)", dataRow)



# print(data)


# Save (commit) the changes
c.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
c.close()
