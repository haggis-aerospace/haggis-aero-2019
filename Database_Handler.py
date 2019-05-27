# Eva Lott & Savio Andrade & Ryan Anderson
# Dundee Haggis-Aero 2019
# Responsible for handling database for training data

import sys
import sqlite3
import Target


class Database():
    conn = None
    cursor = None
    target = None
    c = None
    def __init__(self, target_lat, target_lon, target_char):
        self.target = Target.Target(target_lon, target_lat, target_char)
        self.conn = sqlite3.connect("training_data.db")
        self.c = self.conn.cursor()

        self.c.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, DATETIME,
        uas_height DOUBLE, uas_long DOUBLE, uas_lat DOUBLE, uas_heading DOUBLE, uas_pitch DOUBLE, uas_roll DOUBLE, target_long DOUBLE, target_lat DOUBLE, target_letter CHAR, img_name TEXT)''')

        self.conn.commit()


    def collect(self, height, lat, lon, heading, pitch, roll, image_name):
        # Populate database
        self.c.execute('''INSERT INTO data (DATETIME, uas_height,uas_long, uas_lat,uas_heading, uas_pitch, uas_roll, target_long,target_lat,target_letter,img_name) VALUES(CURRENT_TIMESTAMP,?,?,?,?,?,?,?,?,?,?)''',
        (height, lon, lat, heading, pitch, roll, self.target.lon, self.target.lat, self.target.letter, image_name))

        self.c.execute('''SELECT * FROM data''')
        #print(self.c.fetchall())

        self.conn.commit()

    def clean(self):
        self.conn.close()
