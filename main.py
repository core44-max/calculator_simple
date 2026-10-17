from calculator import add, substrack, multiply, divide

a = 10
b = 0
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {substrack(a, b)}")
print(f"{a} * {b} = {multiply(a, b)}")
res = divide(a, b)
if res is not None:
    print(f"{a} / {b} = {divide(a, b)}")
