#!/usr/bin/env python3

# Savio Andrade
# Dundee Haggis-Aero 2019
# Responsible for building database and streaming images


import threading, image_cap, Database_Handler, DroneKit_Wrapper
import time
import gc
import argparse
import os
import platform
import sys

gc.enable()

#database modifier lock
global database_mod
database_mod = False

global imgname
global lat
global lon
global heading
global pitch
global roll
global height

stopped = threading.Event()

#Sys Args via Argparse
parser = argparse.ArgumentParser(description='Generates the dataset for the Haggis Target Detection Multiple Input-Output DCNN')
parser.add_argument('-tlat', type=float, help="Define target latitude coordinates in degrees")
parser.add_argument('-tlon', type=float, help="Define target longitude coordinates in degrees")
parser.add_argument('-tchar', type=char, help="Define target character")
parser.add_argument('-stalt', type=float, default=50.0, help="Define dataset creation start altitude")
parser.add_argument('-stmode', type=str, default='FBWA', help="Define dataset creation start mode")
args = parser.parse_args()

args.tchar = args.tchar.upper()
args.stmode = args.stmode.upper()

#image_name_counter
image_name_counter = 0

#init database handler
Database_Controller = Database_Handler.Database(args.tlat, args.tlon, args.tchar)
time.sleep(5)

#Continous DataStream
Drone = DroneKit_Wrapper.Location()
# TODO sleep until heartbeat is received
time.sleep(5)

def data_stream():
    while True:
        Drone.get_location()
        lat = Drone.lat
        lon = Drone.lon
        heading = Drone.heading
        pitch = Drone.pitch
        roll = Drone.roll
        height = Drone.rel_alt



def database_write(image_name):
    Database_Controller.collect(height, lat, lon, heading, pitch, roll, image_name)
    processLock.accuire()
    database_mod = False
    processLock.release()


def image_stream(counter):
    imgname = image_cap.get_img(counter)
    processLock.accuire()
    database_mod = True
    processLock.release()
    dbThread = threading.Thread(target=database_write, args=(imgname))
    dbThread.daemon=True
    db.start()

if __name__ == '__main__':
    while Drone.check_mode() != args.stmode and Drone.get_altitude() != args.stalt:
        print("Drone not at height or correct mode")
        print("Get to {}m to activate, Current Altitude :- {}m, Climb {}m to activate".format(args.stalt, Drone.get_altitude(), args.stalt-Drone.get_altitude()))
        print("Change Mode to {} to activate, Current Mode {}".format(args.stmode, Drone.check_mode()))
        time.sleep(0.5)
        if platform.system() == 'Linux':
            os.system('clear')
        else:
            os.system('cls')
    try:
        print('Started Database build process')
        global processLock
        processLock = threading.Lock()
        dsThread = threading.Thread(target=data_stream)
        dsThread.start()
        while True:
            image_stream(image_name_counter)
            image_name_counter+=1
        dsThread.join()
    except (KeyboardInterrupt, SystemExit):
        print("got Ctrl+C (SIGINT) or exit() is called")
        stopped.set() # signal threads to exit gracefully
        Database_Controller.clean() # close database cleanly
        print("All processes stopped. Closing python script")
        sys.exit(0)
