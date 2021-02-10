from Manager import Manager
from Developer import developer



#Importing from the Employee class returns that there is no mg  module 
#Change names so they match across the board 
D1 = developer("Tom", 50000, "Python")
D2 = developer("Dick", 60000, "Python")
D3 = developer("Harry", 40000, "Java")
D4 = developer("Ann", 45000, "Python")
D5 = developer("Adam", 65000, "Java")
D6 = developer("Frank", 30000, "Java")
D7 = developer("Lucy", 35000, "Python")
D8 = developer("Fred", 55000, "Java")

devs = [D1, D2, D3, D4, D5, D6, D7, D8]

mgr = Manager("Susan", 80000, devs)

print("Java Developers:")
java_devs = mgr.all_java_devs()
for dev in java_devs:
    print(f"{dev.name}")

print("Python Developers:")
python_devs = mgr.all_python_devs()
for dev in python_devs:
    print(f"{dev.name}")