cars = ["Ford", "Volvo", "BMW", "Fiat", "Audi", "Mercedes", "VW"]
print(cars)
print(len(cars))

cars.append("Opel")
print(cars)
print(len(cars))

cars.pop(1)
print(cars)
print(len(cars))

cars.remove("BMW")
print(cars)
print(len(cars))

cars.insert(1, "Volvo")
print(cars)
print(len(cars))

cars.sort()
print(cars)
print(len(cars))

cars.reverse()
print(cars)
print(len(cars))

cars.clear()
print(cars)
print(len(cars))
