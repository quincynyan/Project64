fruit = [['kale', 'spinach', 'Sprouts'], ['olives', 'tomatoes', 'Avocado'], ['apple', 'banana', 'mango']]
label = [None] * len(fruit)
for i in range(0, len(fruit)):
	x = ""
	for j in range(0, len(fruit[0])):
		x = x + fruit[i][j][0]
	label[i] = x

theFruitBasket = open("theFruitBasket.txt", "w")
for i in range(0, len(label)):
	theFruitBasket.write(label[i] + "\n")
print("Labels = ", label)