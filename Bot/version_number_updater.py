import json
import Bot.constants as constants
class version_number_updater:
    def __init__(self):
        self.assets = None
        self.version_number = None
        self.__establish_current_version_number()

    def get_version_number(self):
        return self.version_number

    def update_version_number(self, request_string:str):
        if request_string is None:
            return

        indexValue = -10
        try:
            new_version_number = request_string[indexValue:]
            self.assets["version_number"] = new_version_number
            self.version_number = new_version_number
            self.__write_to_version_number()
        except:
            return

    def __establish_current_version_number(self):
        with open(constants.ASSETS_URI, "r") as f:
            self.assets = json.load(f)
        self.version_number = self.assets["version_number"]

    def __write_to_version_number(self):
        with open(constants.ASSETS_URI, "w") as f:
            json.dump(self.assets, f, indent=4)
