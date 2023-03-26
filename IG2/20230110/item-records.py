item = {
    "Item-code": "ITM-001",
    "Item-name": "Item-1",
    "Quantity": 50,
    "Price": 999.99,
    "Reorder": 10,
    "Category": "Electronics"
}


class Item:
    def __init__(self, item_code, item_name, quantity, price, reorder, category):
        self.item_code = item_code
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        self.reorder = reorder
        self.category = category

    def __str__(self):
        itemstr = "Item-code: " + self.item_code + " Item-name: " + self.item_name
        itemstr += " Quantity: " + \
            str(self.quantity) + " Price: " + str(self.price)
        itemstr += " Reorder: " + \
            str(self.reorder) + " Category: " + self.category
        return itemstr

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.item_code == other.item_code and self.item_name == other.item_name:
            return True
        else:
            return False


def enterRecord():
    item_code = input("Enter item code: ")
    item_name = input("Enter item name: ")
    quantity = input("Enter quantity: ")
    price = input("Enter price: ")
    reorder = input("Enter reorder: ")
    category = input("Enter category: ")
    return Item(item_code, item_name, quantity, price, reorder, category)


def printRecord(i):
    print(i)


def main():
    nxt = ""
    i = []
    while nxt != "e":
        if nxt == "n":
            i.append(enterRecord())
        elif nxt == "v":
            for i in i:
                printRecord(i)
        nxt = input(
            "Would you like to enter a new record (n), view an existing record (v), or exit (e)?").lower()


if __name__ == '__main__':
    main()
