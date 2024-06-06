# object oriented programing
""" class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def change_salary(self,amount):
        self.salary +=amount

         # string method
    def __str__(self):
        return(f"{self.name} has a salary of: {self.salary}")

        # creat employee instances


 
employees = [
    employee('zainab',5000),
    employee('tom',5000),
    employee('bob',7000),
    employee('aisha',6000)
    
]

# change salary by 10000
for employee in employees:
    if employee.name != 'aisha':
        employee.change_salary(10000)
for employee in employees:
    # print(f"{employee.name}'s new salary: {employee.salary}")
    print(employee)
 """


# p3 = employee('rice',5000)
# print(p3)


class Animal:# is the super class
    def __init__(self,name,specie):
        self.name = name #attribute
        self.specie = specie #attribute
    def speak(self):#method
        pass
class Dog(Animal): # sub class
    def __init__(self,name,breed):
        super().__init__(name,"Dog")#call the parent class constructor(i.e calling from super clas init)
        self.breed = breed   #adding attribute for dog class
    def speak(self):  #polymorph,overriding
        return f"{self.name} says woof!"
    
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name,"Cat")
        self.color = color
    def speak(self):
        return f"{self.name} says meow"
    
    # instance
dog = Dog("bingo","local dog")
cat = Cat("musu","tabbycat")
print(dog.speak())
print(cat.speak())
print(dog.name)
    



























        
        
    

    
# class Cat(Animal): # sub class
#     def __init__(self,name,color):
#         super().__init__(name,"Cat")#call the parent class constructor(i.e calling from super clas init)
#         self.color = color   #adding attribute for dog class
#     def speak(self):  #polymorph,overriding
#         return f"{self.name} says meow!"
#     #create instances for cat and dog
#     dog = Dog("bingo","local dog")
#     cat =   Cat()

    
        










   
    


