import encrypt as en
import sys

method = input("Method: ")
string = input("String: ")

if method.lower() == "caesar":
    print(en.caesar(string))
elif method.lower() == "reverse":
    print(en.reverse(string))
elif method.lower() == "xor":
    key = int(input("Key: "))
    print(en.xor(string, key))
elif method.lower() == "rotate":
    print(en.rotate(string))
else:
    print("Error incorrect method. Please enter one of: Caesar, Reverse, Xor or Rotate")
    print("Usage: python3 {} <caesar|reverse|xor|rotate>".format(sys.argv[0]))