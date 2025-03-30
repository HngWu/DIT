class Linegraph:
    def __init__(self, data, label):
        self.__data__ = data
        self.__label__ = label
    def get_label(self):
        return self.__label__

    def get_data(self):
        return self.__data__


    def set_data(self, data):
        self.__data__ = data

    def set_label(self, label):
        self.__label__ = label


    def set_data_n_label(self):
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
        ]

        data = [0, 10, 15, 8, 22, 18, 25]

        self.__data__ = data
        self.__label__ = labels

class Piechart:
    def __init__(self, data, label):
        self.piechartdata = data
        self.piechartlabel = label

    def set_data(self, data):
        self.piechartdata = data

    def set_label(self, label):
        self.piechartlabel = label

    def get_data(self):
        return self.piechartdata

    def get_label(self):
        return self.piechartlabel

    def set_data_and_label(self):
        labels = ["Sembawang", "Ang Mo Kio", "Bishan", "Yishun"]
        values = [300, 50, 100, 40]
        self.piechartdata = values
        self.piechartlabel = labels