print("The best calculator ever")
x = int(input("X: "))
y = int(input("Y: "))

print(f"SUM: {x + y}")
print(f"SUB: {x - y}")
print(f"MUL: {x * y}")
print(f"POW: {x ** y}")
if y == 0:
	print("Can't do it!")
else:
	print(f"Div: {x / y}")
