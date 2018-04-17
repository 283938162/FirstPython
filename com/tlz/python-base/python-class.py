# coding:utf-8


class People:
	age = 13

	# def __init__(self, name):
	# 	self.name = name

	def __init__(self):
		pass

	@property
	def get_name(self):
		return self.name

# print(People('zhangsan').name)
# print(People().age)


class Vehicle:
	print('汽车！')

	# 公共实例变量  相当于java中的静态变量 这个变量早于对象
	first_var = 'common'

	# 构造函数
	def __init__(self, wheels, brand):
		self.wheels = wheels
		self.brand = brand

	# Python中，我们可以使用@property (修饰符)来定义getters和setters
	@property
	def get_number_of_wheels(self):
		return self.wheels

	def set_number_of_wheels(self, number):
		self.wheels = number


# 实现继承  子类继承父类 在 Python 中，我们将父类类名 作为子的参数来进行继承
class ElectricVehicle(Vehicle):
	def __init__(self,wheels,brand):
		Vehicle.__init__(self,wheels,brand)


# 父类实例化
# car = Vehicle(4, 'Tesla Model S')
# print(car.get_number_of_wheels)
#
# car.set_number_of_wheels(6)
# print(car.get_number_of_wheels)


eCar = ElectricVehicle(7,'Telsa Z')
print(eCar.get_number_of_wheels)

