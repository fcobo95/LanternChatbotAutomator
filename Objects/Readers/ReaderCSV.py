import pandas


class ReaderCSV:
    """
    DOCSTRING
    """

    def __init__(self):
        with open('../Data Files/MainCSV.csv') as csv_data:
            self.final_csv_data = pandas.read_csv(csv_data, delimiter=',', skipinitialspace=True)
