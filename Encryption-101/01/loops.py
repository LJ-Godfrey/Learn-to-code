# This code is a basic loop that runs something x number of times

inp = input("Enter something...: ")

#This is an infinite loop that breaks when the letter 'q' is entered
while inp != 'q':
	print("You entered: {}".format(inp))
	inp = input("Enter something else: ")

'''
i = 0
while i < 10:
	print(i)
	i = i + 1

for i in range(0, 10):
	print(i)

'''

# This is a list of different strings.
list_a = ['a', 'b', 'c', 'joel', 'hi', '4', '5', '9']
#(len(list_a))
#for value in list_a[:list_a[5]]:
#	print(value)

# This joins each element (string) in the list with a -.
print('-'.join(list_a))

# This is a dictionary
dict_a = {'a':'Hello, govna', 'b':'Wassup dude'}

asciii = {'a': ['A', 'a', '4']}
# This prints the string corresponding with 'b' key (Wassup dude)
print(dict_a['b'])