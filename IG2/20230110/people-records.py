class person:
    def __init__(self, name, age, info):
        self.name = name
        self.age = age
        self.info = info

    def __str__(self):
        personstr = "Name: " + self.name + " Age: " + str(self.age)
        personstr += " \nInfo: " + str(self.info)
        return personstr

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):

        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False


def enterRecord():
    # Default dictionary
    info = {"id": 0,
            "Gender": "",
            "Height": 0.00,
            "Left-handed": False,
            "Eye color": "",
            "Blood type": 'A',
            "Country": ""}
    name = input("Enter name: ")
    age = input("Enter age: ")
    print("Hello, " + name + "! Please input the following information:")
    for key in info:
        info[key] = input(key + ": ")
    return person(name, age, info)


def printRecord(p):
    print(p)


def main():
    nxt = ""
    p = []
    while nxt != "e":
        if nxt == "n":
            p.append(enterRecord())
        elif nxt == "v":
            for i in p:
                printRecord(i)
        nxt = input(
            "Would you like to enter a new record (n), view an existing record (v), or exit (e)?").lower()


if __name__ == '__main__':
    main()
