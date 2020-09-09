# This code rotates each word in the string half the word length
inp = input("Enter a string: ")
out = ''

for word in inp.split():
	length = len(word)
	for letter in range(int(length/2)+length%2):
		last = length - 1
		word = word[last] + word[:last]
	out += word

print(out)