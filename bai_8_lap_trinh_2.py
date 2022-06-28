class Person():
    name = ""
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print( "Hi, I'm " + self.name + ". I'm " + str(self.age) + " years old.")
        
p1 = Person("Khoa", 10)
p1.introduce()