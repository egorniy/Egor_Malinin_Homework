import sqlite3
import xml.etree.ElementTree as et
tree=et.ElementTree(file='d:\\Project\Homework\\22.10.21\\menu.xml')
root = tree.getroot()
connection=sqlite3.connect(root.tag + '.sqlite')
cursor= connection.cursor()
for child in root:
    table = '''CREATE TABLE %s (
                                price TEXT,
                                name TEXT);''' % child.tag
    cursor.execute(table)
    print('Child: ', child.tag,child.attrib)
    for gc in child:
        print('Gc: ', gc.tag, gc.attrib, gc.text)
        com = """INSERT INTO %s VALUES (\"%s\", \"%s\");""" % (child.tag, gc.attrib['price'], gc.text)
        cursor.execute(com)
    
    cursor.execute('SELECT * FROM %s' % child.tag)
    print(cursor.fetchall())
            
connection.commit()
cursor.close()
connection.close()






s = ['one','two','three ','four' ,'five']
x = [2, 3, 4, 5]
z = np.random.random(100)
z1 = [10, 17, 24, 16, 22]
z2 = [12, 14, 21, 13, 17]

# bar()
fig = plt.figure()
plt.bar(x, z1)
plt.title('Simple bar chart')
plt.grid(True)   # линии вспомогательной сетки



plt.show()