import re

str1 = "I stay in 1st main road"

spl = ''.join(re.split(r'oa', str1))
print("---------------------------------------")
print("BEFORE")
print(str1)
print("---------------------------------------")
print("AFTER")
print(spl)
print("---------------------------------------")
