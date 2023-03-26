class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def myFunc(self):
		print("Hello my name is ", self.name)
		print("I am ", str(self.age), " years old")

p1 = Person("John", 36)
p1.myFunc()