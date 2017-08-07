"""This file is for sourcing various coordinate and mac address couples"""
from __future__ import print_function
from source.ap_location import APObservationPoints
from source.scan import SingleScanResult

import re
import os

# TODO: If new source files are added do not reprocess the same files
class Sourcer(object):
    """Class for gathering various sources and processing them to get the lat
    long with ap dictionaries
    """

    def __init__(self, config):
        """Init the variables

        :param config: config dictionary
        """
        self.file_list = {}
        self.parsed_scans = []
        self.ap_location_list = None
        self._config = config
        self._supported_extensions = self._config["extensions"]["database"]

    def init_sourcing(self):
        """Init sourcing all files"""
        for extension in self._supported_extensions:
            self.file_list[extension] = self._get_source_files(extension)

    def _get_source_files(self, extension):
        """This function is for getting the files with the given extension"""
        database_folder = os.path.join(self._config["database_root_dir"],\
                self._config["raw_file_folder"], extension)
        files = [os.path.join(path, name) for path, _, files in\
                os.walk(os.path.join(os.getcwd(), database_folder)) for name\
                in files if extension in name and "swp" not in name]
        return files

    def print_source_files(self):
        """This function is for printing the acquired files in the list"""
        for extension in self._supported_extensions:
            print(", ".join(self.file_list[extension]))

    def get_complete_file_list(self):
        """This function returns the complete file list"""
        return self.file_list

    def process_source_files(self, source_file_names, extensions):
        """This function
        1) parses the files
        2) creates coordinates to mac addresses SingleScanResult objects
        """

        for source_file_name in source_file_names["gpx"]:
            file_name = open(source_file_name, "r")
            new_scan_found = None
            for line in file_name:

                name = re.search(r'<name>(.+?)</name>', line)
                if name is not None:
                    print("found %s" % (name).group(1))

                if "<trkpt " in line:
                    #print("new scan started")
                    new_scan_found = SingleScanResult()

                # TODO: String comparison with in might be faster than in
                if "</trkpt>" in line:
                    #print("new scan ended")
                    new_scan_found.set_name(name)
                    self.parsed_scans.append(new_scan_found)
                    name = None
                    new_scan_found = None

                # Create coordinates->mac addresses map
                if new_scan_found:
                    try:
                        lon = re.search(r'lon=(.*?)><ele>', line)
                        if lon is not None:
                            #print("found %s" % (lon).group(1))
                            pass
                        lat = re.search(r'lat=(.*?) ', line)
                        if lat is not None:
                            #print("found %s" % (lat).group(1))
                            pass
                        if lat is not None and lon is not None:
                            #print("set the coordinates")
                            new_scan_found.set_coordinates(lat.group(1),\
                                    lon.group(1))
                            lon = lat = None
                        time = re.search(r'<time>(.*?)</time>', line)
                        if time is not None:
                            #print("found %s" % (time).group(1))
                            #TODO: Do the time formating
                            new_scan_found.set_time(time)
                            time = None
                        mac = re.search(\
                                r'((([a-f]{0,2}[A-F]{0,2}[0-9]{0,2}){2}):){5}([a-f]{0,2}[A-F]{0,2}[0-9]{0,2}){2}'\
                                , line)
                        if mac is not None:
                            #print("added a new mac %s" % (mac.group(0)))
                            new_scan_found.add_mac(mac.group(0))
                            mac = None
                    except AttributeError as exception:
                        print("exception happened " + str(exception))
                        pass

    # Create Mac addresses->all coordinates database
    def process_scan_results(self):
        """Function to create a dictionary, for example:

        { mac1 : [(lat1,long1), (lat2,lon2)],
          mac2 : [(lat1,long1), (lat2,lon2)] }
        """
        self.ap_location_list = \
                APObservationPoints(self._config["mac_coordinates"])
        for scan in self.parsed_scans:
            for mac in scan.get_mac_list():
                self.ap_location_list.add_new_point(mac, scan.get_coordinates())
        self.write_mac_coordinates_to_file()

    def write_mac_coordinates_to_file(self):
        """Function to write the mac coordinates to csv file"""
        if self.ap_location_list:
            self.ap_location_list.write_ap_observations_to_csv()
