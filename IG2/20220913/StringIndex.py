string = 'Computer Science'

print("Original string: ", string)


def tryit(text, i):
    try:
        a = text[i]
    except IndexError:
        return IndexError
    return a


print("\nstring[0]: \n", tryit(string, 0))
print("\nstring[1]: \n", tryit(string, 1))
print("\nstring[15]: \n", tryit(string, 15))
print("\nstring[16]: \n", tryit(string, 16))
print("\nstring[-1]: \n", tryit(string, -1))
print("\nstring[100]: \n", tryit(string, 100))
print("\nstring[-100]: \n", tryit(string, -100))
