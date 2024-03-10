class Employee:
    def __init__(self, name, id):
        self.__name = name  # Encapsulation of the name attribute
        self.__id = id  # Encapsulation of the id attribute

    # Getter method for name
    @property
    def name(self):
        return self.__name

    # Getter method for id
    @property
    def id(self):
        return self.__id

    def display_details(self):
        return f"Name: {self.__name}, ID: {self.__id}"

class RegularEmployee(Employee):
    def __init__(self, name, id):
        super().__init__(name, id)

class Manager(Employee):
    def __init__(self, name, id, bonus):
        super().__init__(name, id)
        self.__bonus = bonus  # Encapsulation of the bonus attribute

    # Getter method for bonus
    @property
    def bonus(self):
        return self.__bonus

    def display_details(self):
        return f"{super().display_details()}, Bonus: {self.__bonus}"

# Test cases
reg_emp = RegularEmployee("John Doe", 12345)
manager = Manager("Jane Doe", 54321, 5000)

print(reg_emp.display_details())
print(manager.display_details())
