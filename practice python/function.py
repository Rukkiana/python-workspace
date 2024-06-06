def Animal():
    return 'I love Animals'
print(Animal())
def square(n,m):
    return (n * m)

print(square(2,3))
def square(n):
    square = n ** 2
    return square

# def square(n):
#     print(n * n)
print(square(2))
print(square(5)) 
print(square(10))

def add_two_numbers(a,b):
    return a + b
print(add_two_numbers(1,5))

def add_two_numbers(a,b):
    return a - b
print(add_two_numbers(10,5))

def fullname(firstname,lastname):
    fullname = firstname + " " + lastname 
    return (fullname)
    
print(fullname('RUKAYYA','ABDULKADIR'))

def fullname(firstname,lastname):
    fullname =  ' I AM ' + firstname + " " + lastname + ' I AM 20 YEARS OLD '
    return (fullname.strip())
    
print(fullname('RUKAYYA','ABDULKADIR'))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total =total + i
    return total
print(sum_of_numbers(100))

def calculate_weight(mass=100,gravity=9.81):
    return round(mass * gravity,1)
    
print(calculate_weight(75))
print(calculate_weight(75,1.62))
print(calculate_weight())
def interest(principal:int,time:int,rate:int):
    if rate < 100:
        interest = (principal * rate * time) / 100
        return interest 
    else:
        raise ValueError("Rate must be an integer and not more than 100")
     
print(interest(1000,2,5 ))

# def interest(principal:int,rate,time:int):
#     if  rate <100 and int:

#         interest=(principal * rate * time)/100
#         return interest
#     else:

#         raise ValueError('rate must be integer and less than 100')
# print(interest(1000,120,5))


        
        
    




















































