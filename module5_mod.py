class NumberIndexSearch:
    def __init__(self):
        self.numbers = []

    def append_number(self, number):
        self.numbers.append(number)

    def search_for_index(self, x):
        if x in self.numbers: 
            return self.numbers.index(x)+1
        else:
            return -1