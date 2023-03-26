addressBook = [["John Doe", "john.doe@example.com"],
               ["Jane Doe", "janedoe@outlook.org"],
               ["John Smith", "smithjohn@gmail.com"],
               ["Ye Tun", "yetun@hypermail.org"],
               ["GLatt", "nln@dumbmail.org"],
               ["Min Chan", "mcpro@rockstar.dev"]]

name = input("Please enter a name: ")
found = False
index = 0
length = len(addressBook)
while found == False and index < length:
    if name == addressBook[index][0]:
        found = True
    else:
        index = index + 1
if found == True:
    print(addressBook[index][1])
else:
    print("The name you entered does not exist.")
