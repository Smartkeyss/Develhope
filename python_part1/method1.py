selectanumber =int(input("Please type a number\t: "))
if selectanumber == 1:
    print(type("Hello World"))
elif selectanumber == 2:
    print(type(True))
elif selectanumber == 3:
    print(type(False))
elif selectanumber == 4:
    print(type(33))
elif selectanumber == 5:
    print(type(24.5))
elif selectanumber == 6:
    print(type(4+1j))
elif selectanumber == 7:
    print(type(4j))
elif selectanumber == 8:
    print(type(["lion", "monkey", "dog","fish"]))
elif selectanumber == 9:
    print(type(("lion", "monkey", "dog","fish")))
elif selectanumber == 10:
    print(type({"name" : "John", "surname" : "Doe", "age":22}))
elif selectanumber == 11:
    print(type({"lion", "monkey", "dog","fish"}))
else:
    print("Wrong number, try again")

