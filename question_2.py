class Employee:   
    def __init__(self) -> None:
        self._name = None
        self._age = None
        self._salary = None 

    def setName(self, name: str):
        self._name = name
    def getName(self) -> str:
        return self._name
    
    def setAge(self, age: int):
        self._age = age
    def getAge(self) -> int:
        return self._age
    
    def setSalary(self, salary: float):
        self._salary = salary
    def getSalary(self) -> float:
        return self._salary

if __name__ == "__main__" :
    employee1 = Employee()
    # Setting object attributes
    employee1.setName("Aaron")
    employee1.setAge(28)
    employee1.setSalary(15860.56)

    # Getting object attributes
    print(f"Name: {employee1.getName()}")
    print(f"Age: {employee1.getAge()}")
    print(f"Salary: GHc {employee1.getSalary()}")
