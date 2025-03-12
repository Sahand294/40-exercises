import math
try:
    input = float(input("put a number in:"))
except:
    raise ValueError("put in a number next time!")
if input < 0:
    raise ValueError("put in a positive number")
print(math.sqrt(input))