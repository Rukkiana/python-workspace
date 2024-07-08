""" # itration
Employees = [
    {
    "name": "rukayya",
    "details":{
        "age":"",
        "position":'ceo',
        "task":["banker",'hr']}
    },

    {
    "name": "fatima",
    "details":{
        "age":"",
        "position":'finance',
        "task":["coding",'manager']}
    },
    {
    "name": "firdaus",
    "details":{
        "age":"",
        "position":'chairman',
        "task":["survey",'clerk']}
    },

    {
    "name": "ABdulganee",
    "details":{
        "age":"",
        "position":'MD',
        "task":["manager",'controller']}
    },
    {
    "name": "rukayya",
    "details":{
        "age":"",
        "position":'ceo',
        "task":["fatima",'zainab']}
    }
]
task=Employees[0]["details"]["task"][0]
print(task)
# for employee in Employees:
#     print(employee["name"].upper())
def name(employees):
    for employee in employees:
        yield employee['name']
    print(employee) """
    
    # name = (employee['name'])
    # print(name.upper())

    # iteration,for generators we use yield in place of return

    # instantiate a list object
"""  list_instance =[1,2,3,4]
    iterator =iter (list_instance)
    # convert the list to an iterator
    print(next(iterator))

# generator
def factors(n):
    for val in range(1, n+1):
        if n % val ==0:
            yield val
print(factors(20))
factors_of_20 = factors(20)
print(next(factors_of_20))
print((val  for val in range(1,20+1) if n % val == 0)) """




#     def factors(n):
#     for val in range(1, n+1):
#         if n % val ==0:
#             yield val
# print(factors(20))
# factors_of_20 = factors(20)
# print(next(factors_of_20))

# num = [1,2,3,4]
# def square(num_list:list):
#      return[i**2 for i in num_list]
# print(square(num))





# list comprehension
num = [0,1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]
# list comprehension to get the square of the odd numbers
squares = [x**2 for x in num if x %2 ==1]

print(squares)
squares = [x**2 for x in num if x %2 ==0]
print(squares)
prime = [n**2 for n in num if all (n % i != 0 for i in range(2,n)) and n >1 ]
print(prime)
primes = [n for n in num if all (n % i != 0 for i in range(2,n)) and n >1 ]
print(primes)


words = ['bag','desk','teacher']
words =[word.capitalize() for word in words ]
print(words)
words = [word for word in words if len(word)> 4 ]
print(words)

num = [(cube,cube **3 ) for  cube in num] 
print(num)

number2 = range (0,31)
n8um = [ n for n in number2]

multiple_of_3 = ['fizz'  for n in number2 if n % 3 ==0 and n %5 != 0]

multiple_of_5 = [ 'buss'for n in number2 if n % 5 ==0 and n %3 !=0]
multiple3and4 = ['fizzbuss'for n in number2  if n%15 ==0  ]
print(n8um)
# for n in number2  
# print(multiple_of_3)
# print(multiple_of_5)
# print(multiple3and4)



# fixxy = [
#     'fizzbuss' if n % 15 == 0 else 'buss' if n % 5 == 0 else 'fizz' if n % 3 == 0 else str(n) for n in range(1,40)
# ]
# print(fixxy)

""" numbers = []
def puzzle():
    for i in range(1,30):
        if i %3 ==0 and i %5 == 0 and i != 0:
            numbers.append('fissbuss')
        elif i %5 == 0 and i != 0:
            numbers.append('buss')
        elif i % 3 ==0 and i !=  0:
            numbers.append('fizz')
        else:
         numbers.append(i)
    print(f' {numbers}')
puzzle() """

fizzbuss = ['fissbuss' if i%3 ==0 and i%5 ==0 and i!=0 else 'buss' if i %5==0 else 'fiss' if i%3 ==0  else str(i) for i in range(1,31)]
print(fizzbuss)




















# number2 =[
#     'fizzbuss'  if n % 15 == 0 else 'buss' if n % 5 ==0 else 'fizz'if n % 3 ==0 else str(n) for n in range(1,31)

# ]
# print(number2)
    
 








