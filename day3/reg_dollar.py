import re
a = "ISE Students"
x = re.findall("Students$",a)
if x:
    print("Yes, the string matches with 'Students'")
else:
    print("NO match")