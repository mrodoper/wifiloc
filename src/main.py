"""This module is more like a script to start the parsing process"""
from source.sourcer import Sourcer
from locations.average import AverageAlgorithm
from util.file_operations import create_tmp_folder, create_results_folder
from util.config import Config

#load config file
config = Config.load_config_to_memory()

create_tmp_folder()
create_results_folder()
# FORM MAIN DATABASE
# List gpx files
basic_sourcer = Sourcer(config)
basic_sourcer.init_sourcing()
basic_sourcer.print_source_files()
# Process the gpx files
source_file_names = basic_sourcer.get_complete_file_list()
basic_sourcer.process_source_files(source_file_names, extensions="gpx")
basic_sourcer.process_scan_results()
# Create mac addresses->estimation coordinates database with various algorithms
average_algorithm = AverageAlgorithm()
average_algorithm.load_mac_addresses(file_name=config["mac_coordinates"])
average_algorithm.average()
if not average_algorithm.print_to_file():
    print("Could not print to file")
# FORM SPARSE DATABASE
# Create sparse databases

# NOTES
# Update all above databases with new scan result entry
