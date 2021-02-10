from Employee import Employee

class developer(Employee):
    def __init__(self, name, salary, main_language):
       super().__init__(name,salary, main_language)
       self.main_language = main_language


D1 = developer("Tom", 50000, "Python")
D2 = developer("Dick", 60000, "Python")
D3 = developer("Harry", 40000, "Java")
D4 = developer("Ann", 45000, "Python")
D5 = developer("Adam", 65000, "Java")
D6 = developer("Frank", 30000, "Java")
D7 = developer("Lucy", 35000, "Python")
D8 = developer("Fred", 55000, "Java")

