class Animal():
	def __init__(self, name, age):
		self.age=age
		self.name=name

	def sleep(self):
		print self.name + " of " + str(self.age) + " is sleeping"

kitty = Animal("peuit", 5.5)
kitty.sleep() 

class bird(Animal):
	def __init__(self, name,age,wing_color):
		super(name, age)
		self.wing_color = wing color
		def fly(self):
			print "bird "+self.name+self.wing_color