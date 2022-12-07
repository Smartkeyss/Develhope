list1 = ["lion", "monkey", "dog","fish"]
for i in list1:
    print(i)
tuple1 = ("lion", "monkey", "dog","fish")
for j in tuple1:
    print(j)
set1 = {"lion", "monkey", "dog","fish"}
for m in set1:
    print(m)
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}
y = dict1.items()
for i in y:
    x = i[0]
    y = i[1]
    print(f"{x} lives in {y}")
