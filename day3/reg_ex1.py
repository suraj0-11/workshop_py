import re
a = "Dept of ISE, 4th sem students"
x = re.findall("\w",a)
print(len(x))
print(x)