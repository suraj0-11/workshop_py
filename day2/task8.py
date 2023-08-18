student = {
    "suraj" : 45,
    "sagar" : 31,
    "rajiv" : 32,
    "satvik" : 47
}

names = student.keys()
for n in names:
    print(n)

avg = int(sum(student.values())/len(student))

print(f"Average marks is {avg}")

top = max(student, key=student.get)
print(f"Topper is {top}")