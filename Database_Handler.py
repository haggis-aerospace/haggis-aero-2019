# Eva Lott
# Dundee Haggis-Aero 2019
# Responsible for handling database for training data

import sqlite3
import DroneKit_Wrapper

conn = 0;
cursor = 0;

# Initialise location tracker class
location = Dronekit.Location()

def database_init()
    conn = sqlite3.connect("training_data.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, DATETIME
    uas_height DOUBLE, uas_long DOUBLE, uas_lat DOUBLE, uas_heading DOUBLE, uas_pitch DOUBLE, uas_roll DOUBLE, target_long DOUBLE, target_lat DOUBLE, target_letter CHAR, img_name TEXT)''')

    conn.commit()

def database_handler_collect(target_lon, target_lat, target_letter, img_filename):

    # Get current location
    location.get_location();

    # Populate database
    c.execute('''INSERT INTO data (uas_height,uas_long, uas_lat,uas_heading, uas_pitch, uas_roll target_long,target_lat,target_letter,img_name) VALUES(CURRENT_TIMESTAMP,?,?,?,?,?,?,?,?)''',
    (location.rel_alt, location.lon, location.lat, location.heading, location.pitch, location.roll, target_lon, target_lat, target_letter, img_filename))

    c.execute('''SELECT * FROM data''')
    print c.fetchall()

    conn.commit()

def database_handler_clean():
    conn.close()
