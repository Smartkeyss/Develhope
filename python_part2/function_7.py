list = [0, 1, 2, 3, 4]
mylist = []
def myfunct():
    for i in list:
        if i % 2 == 0:
            print(i)
a = myfunct()
x = lambda a: a**2
y = x(a)
print(y)

