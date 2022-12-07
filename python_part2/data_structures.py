list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}
print(len(list1))
print(len(tuple1))
print(len(set1))
print(len(dict1))
print(list1[0])
print(tuple1[0])
print(dict1["lion"])
list1[1] = "rabbit"
print(list1)
tuple1[1] = "rabbit"
print(tuple1)
##it is not successful as tuple object do not support item assignment 
##ie tuple cannot be updated
list1.append("monkey")
print(list1)
list1.remove("rabbit")
print(list1)

