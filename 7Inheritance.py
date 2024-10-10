# Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f'My name is {self.name} and age is {self.age}')    

person = Person('Anas', 20) 

person.intro()
 
class Student(Person):
    def __init__(self, n, a, r, m):
        super().__init__(name, age)
        self.rollno = r
        self.marks = m

s = Student('Ahmad', 19, 45, 95.5)   

s.intro()

print(s.name, s.age, s.marks, s.rollno)


