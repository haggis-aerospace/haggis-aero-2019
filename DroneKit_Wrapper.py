# Eva Lott and Savio Andrade
# Dundee Haggis-Aero 2019
# Responsible for collecting all needed location and position data in a neat little class

from dronekit import connect
from numpy import pi

class Location:
    vehicle = None
    lat = None
    lon = None
    init_alt = None
    rel_alt = None
    pitch = None
    roll = None
    heading = None
    heartbeat=False

    def __init__(self):
        self.vehicle = connect('/dev/ttyACM0', wait_ready=True, baud=57600)
        self.init_alt = self.vehicle.location._alt

    def get_location(self):
        self.lat = self.vehicle.location._lat
        self.lon = self.vehicle.location._lon
        self.rel_alt = self.vehicle.location._alt - self.init_alt
        self.heading = self.vehicle._heading
        self.pitch = (self.vehicle._pitch/pi) + 0.5
        self.roll = (self.vehicle._roll/pi) + 0.5
# TODO write code to check for heartbeat
'''
    def get_heartbeat(self):
        self.vehicle.
'''
    # TODO remove (only used for testing)
    def print_attributes(self):
        self.get_location()
        print("lat", self.lat)
        print("lon", self.lon)
        print("rel_alt", self.rel_alt)
        print("pitch", self.pitch)
        print("roll", self.roll)
