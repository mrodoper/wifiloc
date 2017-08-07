import os

class BaseAlgorithm():
    """This class has the common operations needed for algorithms"""
    def __init__(self):
        """init function"""
        self._path = None
        self._file_name = None
        self._base = {}
        self._result = {}
        pass

    def load_mac_addresses(self, path=None, file_name=None):
        """Generic function to load the mac addresses from a file"""
        self._path = path
        if self._path is None:
            self._path = os.getcwd() 

        self._file_name = file_name
        if self._file_name is None:
            # TODO: get list of files here
            pass

        with open(file_name, "r") as csv_file:
            first_line = True
            for line in csv_file:
                if first_line:
                    first_line = False
                    continue
                line_split = line.split(",")
                self._base[line_split[0]] = [x for x in line_split[1:]]
