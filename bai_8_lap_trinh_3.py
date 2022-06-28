class Person():
    name = ""
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def increase_age(self):
        age1 = self.age + 1
        print("It's my birthday! I'm " + str(age1) +  " years old now.")
        
p1 = Person("Khoa", 10)
p1.increase_age()