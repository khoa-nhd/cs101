class Person():
    name = ""
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Khoa", 10)

print(person1.name)
print(person1.age)