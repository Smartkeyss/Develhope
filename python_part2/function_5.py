import random
def random_list_summer():
    randomlist = []
    for i in range(15):
        n = random.randint(-100,100)
        randomlist.append(n)
    print(randomlist)
random_list_summer()
