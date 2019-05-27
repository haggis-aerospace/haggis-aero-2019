#!/usr/bin/env python3

import threading, image_cap, Database_Handler, DroneKit_Wrapper
import time

global imgname
global lat
global lon
global heading
global pitch
global roll
global height

stopped = threading.Event()


#Continous DataStream
Drone = DroneKit_Wrapper.Location()
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
        print(lat, lon, heading, pitch, roll, height)


def image_stream(counter):
    imgname = image_cap.get_img(counter)
    #threading.Thread()

if __name__ == '__main__':
    try:
        global processLock
        processlock = threading.Lock()
        dsThread = threading.Thread(target=data_stream)
        dsThread.start()
        dsThread.join()
    except (KeyboardInterrupt, SystemExit):
        print("got Ctrl+C (SIGINT) or exit() is called")
        stopped.set() # signal threads to exit gracefully
