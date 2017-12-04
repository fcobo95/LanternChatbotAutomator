import pandas


class ReaderCSV:
    """
    DOCSTRING
    """

    def __init__(self, directory):
        with open(directory) as csv_data:
            self.final_csv_data = pandas.read_csv(csv_data, delimiter=',', skipinitialspace=True)
