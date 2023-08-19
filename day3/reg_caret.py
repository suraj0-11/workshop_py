import re
a = "ISE Students"
x = re.findall("^ISE",a)
if x:
    print("Yes, the string matches with 'ISE'")
else:
    print("NO match")