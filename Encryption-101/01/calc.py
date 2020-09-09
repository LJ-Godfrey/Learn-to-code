# This program is a simple calculator

print("Hello user\nWelcome to this calculator")

# This is an infinite loop that is only broken when
# a successful equation is done.
while True:
    
    # Read the first number and the function
	num1 = eval(input("Enter the first number: "))
	func = input("Enter the function < + | - | * | / | ** | q (to quit) >: ")

	if func == "+":
		num2 = eval(input("Enter the second number: "))
		print("{} + {} = {}".format(num1, num2, num1 + num2))
		break
	elif func == "-":
		num2 = eval(input("Enter the second number: "))
		print("{} - {} = {}".format(num1, num2, num1 - num2))
		break
	elif func == "*":
		num2 = eval(input("Enter the second number: "))
		print("{} * {} = {}".format(num1, num2, num1 * num2))
		break
	elif func == "/":
		num2 = eval(input("Enter the second number: "))
		print("{} / {} = {}".format(num1, num2, num1 / num2))
		break
	elif func == "**":
		num2 = eval(input("Enter the second number: "))
		print("{} ** {} = {}".format(num1, num2, num1 ** num2))
		break
    # If the function was not valid, loop back
	else:
		print("The function {} is not valid".format(func))