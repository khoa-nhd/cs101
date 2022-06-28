class Person():
    name = ""
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
def compare_age(person1, person2):
    age1 = person1.age
    age2 = person2.age
    name1 = person1.name
    name2 = person2.name
    if age1 > age2:
        print(name1 + " is older than " + name2)
    elif age2 > age1:
        print(name2 + " is older than " + name1)
    else:
        print(name1 + " and " + name2 + " are of the same age")

person1 = Person("Khoa", 10)
person2 = Person("Khoi", 6)
compare_age(person1, person2)