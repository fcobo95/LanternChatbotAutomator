import json


class ReaderJSON:
    """
    DOCSTRING
    """

    def __init__(self, directory=None):
        with open(directory) as json_data:
            self.final_json_data = json.load(json_data)
