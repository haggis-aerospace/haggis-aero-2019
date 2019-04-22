import sys
import sqlite3


if(len(sys.argv) == 9):

    conn = sqlite3.connect('''training_data''')
    c = conn.cursor()

    c.execute('''INSERT INTO data (time, uas_height,uas_long,uas_lat,uas_direction,
    target_long,target_lat,target_letter,img_name) VALUES(CURRENT_TIMESTAMP,?,?,?,?,?,?,?,?)''',(sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4])/360.0,
    sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8]))

    c.execute('''SELECT * FROM data''')
    print c.fetchall()

    conn.commit()
    conn.close()

else:
    print("error: inncorrect args; expected:8 found:" + str(int(len(sys.argv))-1))
    print("\nargs to be in following order:\nuas_height uas_long uas_lat uas_direction target_long target_lat target_leter img_name")
