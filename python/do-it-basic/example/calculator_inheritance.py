# calculator_inheritance.py

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

# a = MoreFourCal(16, 2)
# a.pow()
# print(a.pow())