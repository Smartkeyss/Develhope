name = ["John", "Tristram", "Baldwin", "Wally"]
surname = ["Doe", "Mcbride", "Preston", "Collins"]
def greet(name, surname):
    for j in surname:
        for i in name:
            print(f"hello {i} {j}!")
        break
    
greet(name, surname)
