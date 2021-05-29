class Date:
    def __init__(self, day, month, year):
        print("Building object")
        self.day = day
        self.month = month
        self.year = year

    def foramatdate(self):
        print(f'{self.day:02d}/{self.month:02d}/{self.year}')