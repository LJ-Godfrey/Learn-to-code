import encrypt as en

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
    print("Error incorrect method")