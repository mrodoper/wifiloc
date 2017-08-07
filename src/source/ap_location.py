"""This module is for keeping track of observation points for each WiFi AP
Also different algorithms can be called with these points to find approximate
coordinates
"""

class APObservationPoints(object):
    """Class for keeping track of each AP's observation points (lat. long)"""
    def __init__(self, output_file):
        """The init function for the class"""
        self.ap_observations = {}
        self._output_file = output_file

    def add_new_point(self, mac, coordinates):
        """The function to add new mac and coordinates"""
        #TODO: This function does more thant the above comment
        #print("mac is %s" %(mac))
        #print("coordinates is %s" %(coordinates))
        try:
            #print("Added a new coordinate to existing mac")
            self.ap_observations[mac].append(coordinates)
        except Exception:
            #print("Created a new coordinate for new mac")
            self.ap_observations[mac] = [coordinates]

    def write_ap_observations_to_csv(self):
        """"Function to write the ap_observations to a csv file"""
        #TODO: Make the file name dynamic
        with open(self._output_file, "w") as csv_file:
            csv_file.write("MAC,coordinates\n")
            csv_file.flush()
            for mac, coordinates in self.ap_observations.items():
                csv_file.write("%s,%s\n" %(mac,\
                        ",".join([",".join([pair for pair in pairs]) for pairs\
                        in coordinates])))
                csv_file.flush()
