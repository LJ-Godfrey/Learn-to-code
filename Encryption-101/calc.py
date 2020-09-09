print("Hello user\nWelcome to this calculator")

while True:
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
	else:
		print("The function {} is not valid".format(func))