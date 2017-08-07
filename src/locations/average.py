import os

from locations import BaseAlgorithm
from util.file_operations import(TMP_FOLDER, RESULTS_FOLDER)

class AverageAlgorithm(BaseAlgorithm):
    """Simple class that only averages all lat, long"""
    def __init__(self):
         """The constructor"""
         super().__init__()
         self._result = {}

    def average(self):
        """Function to average all points"""
        print("Averaging")
        for key, value in self._base.items():
            if len(value[::2]) != len(value[1::2]):
                print("Different lat lon sizes %s, %s", len(value[::2]), len(value[1::2]))

            lat_avg = sum(map(float,value[::2]))/float(len(value[::2]))
            lon_avg = sum(map(float,value[1::2]))/float(len(value[1::2]))

            self._result[key] = [lat_avg, lon_avg]

    def print_to_file(self, file_name="average_result.csv"):
        """Function to write the dictionary (self._result) to a file"""
        if not self._result:
            print("Could not print to file. The results structure is empty")
            return False
        with open(os.path.join(RESULTS_FOLDER, file_name), "w") as out_file:
            out_file.write("mac,lat,long\n") 
            out_file.flush()
            for key, value in self._result.items():
                out_file.write("%s,%s,%s\n" %(key, value[0], value[1]))
            out_file.flush()
        return True
