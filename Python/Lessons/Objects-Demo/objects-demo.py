class Name():
    # constructor
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # return statement for print() 
    def __str__(self):
        s = self.fname + ' ' + self.lname
        return s


names = []
names.append(Name('Mr', 'Smith'))
names.append(Name('Ms', 'Jones'))

for name in names:
    print(name)