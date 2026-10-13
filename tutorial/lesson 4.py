import math
from os import read

age = 0

if age >= 13:
    print('teen!!!!!!!')
else:
    print('kid!')

age2 = 7
age2 = math.ceil(age2)
if age2 >= 13:
    print("Teen")
elif age2 >= 8:
    print("Kid")
else:
    print("Little")
print('age:', age2)

temp = 1000
if temp > 100:
    print("tooo warm day!")
elif temp > 25:
    print("Hot day!")
elif temp > 15:
    print("Nice day!")
else:
    print("Cold day!")



password = 'python123'
if password == "python123":
    print("Access granted!")
else:
    print("Wrong password!")