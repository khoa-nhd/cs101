class Person():
    name = ""
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self, person):
        name1 = self.name
        name2 = person.name
        print("Hi, "+ name2 + "! I'm " + name1 +". Nice to meet you!")
        
        
person1 = Person("Khoa", 10)
person2 = Person("Khoi", 6)
person1.greet(person2)
person2.greet(person1)