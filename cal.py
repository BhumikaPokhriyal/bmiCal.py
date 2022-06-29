# importing modules
from pywebio.input import *
from pywebio.output import *

class BMIcalculator:

	# defining method
	def BMIclassifier(Height, Mass):
                
		for i1, i2 in [(16, 'severely underweight'),
					(18.5, 'underweight'),
					(25, 'normal'),
					(30, 'overweight'),
					(35, 'moderately obese'),
					(float('inf'), 'severely obese')]:
			if BMI <= i1:
				put_text('Your BMI is', BMI, 'and the person is :', i2)
				break

class BMIcalculator:

	def BMIclassifier(self, Height, Mass):

		BMI = (Mass)/(Height*Height)

		
		for i1, i2 in [(16, 'severely underweight'),
					(18.5, 'underweight'),
					(25, 'normal'), (30, 'overweight'),
					(35, 'moderately obese'),
					(float('inf'), 'severely obese')]:

			if BMI <= i1:
				put_text('Your BMI is', BMI, 'and the person is :', i2)
				break


# height input
Height = input("Please enter height in meters(m)", type=FLOAT)

# Mass input
Mass = input("Please enter Mass/Weight in Kilograms(Kg)", type=FLOAT)

obj = BMIcalculator()
obj.BMIclassifier(Height, Mass)
