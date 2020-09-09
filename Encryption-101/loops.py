inp = input("Enter something...: ")

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
list_a = ['a', 'b', 'c', 'joel', 'hi', '4', '5', '9']
#(len(list_a))
#for value in list_a[:list_a[5]]:
#	print(value)

print('-'.join(list_a))

dict_a = {'a':'Hello, govna', 'b':'Wassup dude'}

asciii = {'a': ['A', 'a', '4']}
print(dict_a['b'])