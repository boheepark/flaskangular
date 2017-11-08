import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''
          DROP TABLE user;
          ''')
c.execute('''
        DROP TABLE trade;
        ''')
conn.commit()
conn.close()
