>>> import sqlite3
>>> db = sqlite3.connect('database.db')
>>> db.execute('create table rescu(Name text, Phone number int, email add text, message text')

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    db.execute('create table rescu(Name text, Phone number int, email add text, message text')
OperationalError: near "add": syntax error
>>> db.execute('create table rescu(Name text, Phone number int, email address text, message text')

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    db.execute('create table rescu(Name text, Phone number int, email address text, message text')
OperationalError: near "text": syntax error
>>> db.execute('create table rescu(Name text, Phone number int, email address text, message text)')
<sqlite3.Cursor object at 0x02C0EF60>
>>> 
