# Eva Lott and Savio Andrade
# Dundee Haggis-Aero 2019
# Responsible for collecting all needed location and position data in a neat little class

from dronekit import connect
import dronekit
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
    mode = None

    def __init__(self):
        try:
            self.vehicle = connect('/dev/ttyACM0', wait_ready=True, baud=57600, heartbeat_timeout=180)
            self.vehicle.home_location = self.vehicle.location.global_frame
            self.init_alt = self.vehicle.location._alt
            self.mode = self.vehicle.mode.name

            print("\nConnected Successfully")
            print(" GPS: %s" % self.vehicle.gps_0)
            print(" Battery: %s" % self.vehicle.battery)
            print(" Last Heartbeat: %s" % self.vehicle.last_heartbeat)
            print(" Is Armable?: %s" % self.vehicle.is_armable)
            print(" System status: %s" % self.vehicle.system_status.state)
            print(" Mode: %s" % self.vehicle.mode.name)    # settable

        # Bad TTY connection
        except OSError as e:
            print('No serial exists!')
            print(e)
         # API Error
        except dronekit.APIException:
            print('Timeout!')


    def check_mode(self):
        self.mode = self.vehicle.mode.name
        return self.mode

    def get_altitude(self):
        self.rel_alt = self.vehicle.location._alt - self.init_alt
        return self.rel_alt
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
