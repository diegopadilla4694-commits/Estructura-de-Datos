class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        self.varia = 3

    def __hidden(self):
        self.orale = 5


obj = Classy()
obj.method()
obj._Classy__hidden()


print(obj.__dict__)
print(Classy.__dict__)
    


