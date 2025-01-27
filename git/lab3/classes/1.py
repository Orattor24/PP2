class help:

    def getString(self):
        self.string = input("Введите строку: ")

    def printString(self):
        print(self.string.upper())
help = help()
help.getString()
help.printString()