fruit = {
    "Apple": "A round fruit with a firm texture and sweet or tart flavor.",
    "Banana": "A long, curved fruit with a soft, sweet flesh inside a yellow peel.",
    "Cherry": "A small, round, red or black fruit with a single hard seed inside.",
    "Date": "A sweet brownish fruit from the date palm tree, often eaten dried.",
    "Grape": "A small, round fruit that grows in clusters on vines. It can be green, red, or purple."
}
lookup = input("Enter fruit: ")
if lookup in fruit:
    print("--------------------------------------------")
    print("Before")
    print(fruit[lookup])
    print("--------------------------------------------")
    fruit[lookup] = "it's a fruit"
    print("After")
    print(fruit[lookup])
    print("--------------------------------------------")
else :
    print("Fruit not exist")
