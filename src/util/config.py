"""This module is responsible for loading the config file and storing the settings locally"""
import os
import ruamel_yaml as yaml

from util.file_operations import read_file

BASE_FOLDER = "../"
CONFIG_FILE = "wifi_pos.config"

class Config(object):
    """Keeps the loaded configs in memory for others to consume"""

    def __init__(self):
        """The parameters to keep config settings"""
        self._config = None

    def load_config(self, config_file=os.path.join(BASE_FOLDER, CONFIG_FILE)):
        """Loads the config file to memory"""
        config_path = os.path.abspath(os.path.expanduser(config_file))
        try:
            self._config = yaml.load(read_file(config_path))
        except:
            pass
        return self._config

    @classmethod
    def load_config_to_memory(cls):
        """Loads the config to memoty"""
        conf = cls()
        return conf.load_config()
