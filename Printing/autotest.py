import auto

# Hello world test
auto.print_prog("helloworld")
auto.out_check("helloworld", "Hello World!")

# input test
num_tests = 4
for i in range(1, num_tests + 1):
    path = "tests/0" + str(i) + ".in"
    f = open(path, 'r')
    var = f.readline(); var = var[:len(var)-1]
    auto.inp_prog("inputOutput", path)
    print("\nTest 0{}:".format(i))
    auto.out_check("inputOutput", "Hello " + var + "!")