"""This class is for each scan run and each scan result"""
import logging

class SingleScanResult(object):
    """Class for getting one scan result and storing it in an object"""
    #TODO: Check the coordinate system and support other ones as well
    #TODO: Convert the coordinate system
    def __init__(self):
        """Constructor that also initializes the variables"""
        self.name = "noname"
        #TODO: Need to set a time representation
        self.time = "notime"
        self.coordinates = ["0.0", "0.0"]
        self.ap_list = []

    def set_name(self, name="noname"):
        """Sets a unique name for the scan"""
        self.name = name

    def get_name(self):
        """Gets a unique name for the scan"""
        return self.name

    def set_time(self, time="notime"):
        """Sets time for the scan"""
        self.name = time

    def get_time(self):
        """Gets the time for the scan"""
        return self.time

    def set_coordinates(self, latitude="0.0", longitude="0.0", coordinates=None):
        """Set the coordinates of a scan"""
        #TODO: Do a lat long check
        if isinstance(coordinates, list) and coordinates:
            self.coordinates = [coordinates[0].replace("\"", ""),\
                    coordinates[1].replace("\"", "")]
        else:
            #TODO: Check is strip gets rid of "\n"
            latitude = latitude.replace("\"", "")
            longitude = longitude.replace("\"", "")
            self.coordinates = [latitude, longitude]

    def get_coordinates(self):
        """Get the coordinates of a scan"""
        return self.coordinates

    def add_mac(self, mac_address=""):
        """Add an AP recorded at this location to the list"""
        if not mac_address:
            logging.warning("Incorrect MAC address")
            return
        #TODO:What if I want to replace other chars as well. Explore regex
        self.ap_list.append(str(mac_address).lower().replace(":", ""))

    def get_mac_list(self):
        """Return the pa_list of a scan"""
        return self.ap_list

    def print_scan_results(self):
        """Method to print a single scan result"""
        print("Name: %s\nTime: %s\nCoortinates: %d, %d\nMAC addresses %s",\
                self.name,\
                self.time,\
                self.coordinates[0],\
                self.coordinates[1],\
                ", ".join(self.ap_list))

    def __str__(self):
        """Overwrite the str function"""
        return "Name: {}\nTime: {}\nCoortinates: {}, {}\nMAC addresses {}".\
                format(self.name,\
                self.time,\
                self.coordinates[0],\
                self.coordinates[1],\
                ", ".join(self.ap_list))

