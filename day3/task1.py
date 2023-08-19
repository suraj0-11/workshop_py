import re
str1 = "I stay in 1st main road"
out = re.sub(r'oa', '', str1)
print("---------------------------------------")
print("BEFORE")
print(str1)
print("---------------------------------------")
print("AFTER")
print(out)
print("---------------------------------------")

