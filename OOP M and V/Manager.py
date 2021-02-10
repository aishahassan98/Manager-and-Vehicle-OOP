from Employee import Employee

class Manager(Employee):
    def __init__(self, name, salary, staff):
       super().__init__(name,salary, staff)
       self.staff = staff

    def all_java_devs(self):
        java_devs = []
        for dev in self.staff:
            if dev.main_language == "Java":
                java_devs.append(dev)
        return java_devs

    def all_python_devs(self):
          python_devs = []
          for dev in self.staff:
            if dev.main_language == "Python":
                python_devs.append(dev)
            return python_devs





