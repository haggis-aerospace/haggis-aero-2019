import sqlite3

conn = sqlite3.connect("training_data")

c = conn.cursor()


c.execute('''CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT, time datetime,
uas_height real, uas_long real, uas_lat real, uas_direction real,
target_long real, target_lat real, target_letter char, img_name text)''')

conn.commit()

conn.close()
