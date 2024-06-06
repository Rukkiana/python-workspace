""" a=4
b=3
print('%d + %d =%d'%(a,b,a+ b))
print('%d / %d =%.2f'%(a,b,a/ b))
print('%s%s' %('water','melon'))
print('{} % {} = {}'.format(a, b, a % b))%r """




""" i = 1
while i < 6:
  print(i)
  i += 1 """

""" i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 """

""" i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)  """

""" 
i = 2
while i < 6:
  print(i)
  i += 2
else:
  print("i is no longer less than 6") """

# Print i as long as i is less than 6
""" i = 1
while i < 6:
    print(i)
    i +=1 """

# if statement 


""" a = 7.5
if a > 7.5:
  print(f'{a} is possitive')
elif a < 7:
  print(f'{a}is negative')
elif a == 7.5:
  print(f'{a} is a float number')
else:
  print('do something else')  """






  # if conditios with float
""" a = 7.5
if type(a) == 'int':
    if a > 7:
      print(f'{a} is possitive')
    elif a < 7:
      print(f'{a}is negative')
    elif a == 7:
      print(f'{a} is equal to 7')
    else:
      print('do something else')
else:
  print('its a float number') """


""" number = range(100)
print(list(number)) """

""" name = 'rukayyah'
value = 'too long' if len(name) >5  else 'too short'
print(value) """

# explanation on isinstance function:

""" x = 10
print(isinstance(x, int))  # True, because x is an integer

y = "Hello"
print(isinstance(y, int))  # False, because y is not an integer, it's a string """

# The not operator negates the result of isinstance(rate, int).
# If isinstance(rate, int) is True (meaning rate is an integer), not True becomes False.
# If isinstance(rate, int) is False (meaning rate is not an integer), not False becomes True
# Valid Rate (Integer and <= 100):

# interest(1000, 2, 5)
# isinstance(5, int) returns True
# not True returns False, so no exception is raised.
# Invalid Rate (Greater than 100):

# interest(1000, 2, 105)
# isinstance(105, int) returns True
# not True returns False, but rate > 100 is True
# Since the combined condition is True (due to the or operator), a ValueError is raised.
# Invalid Rate (Not an Integer):

# interest(1000, 2, "five")
# isinstance("five", int) returns False
# not False returns True, so a ValueError is raised.
# This way, the function ensures that rate is both an integer and within the acceptable range. 


""" def calculate_interest(principal, rate, time):
    # Ensure principal is an integer
    if not isinstance(principal, int):
        raise ValueError("Principal must be an integer")

    # Ensure rate is an integer and not more than 100
    if not isinstance(rate, int) or rate > 100:
        raise ValueError("Rate must be an integer and not more than 100")

    # Ensure time is an integer
    if not isinstance(time, int):
        raise ValueError("Time must be an integer")

    # Calculate the interest
    interest = (principal * rate * time) / 100
    return interest

# Example usage:
principal = 1000  # Example principal
rate = 5          # Example rate
time = 2          # Example time
interest = calculate_interest(principal, rate, time)
print(f"The interest is: {interest}") """


rate = 50
# isinstance(rate, int) is True, so not isinstance(rate, int) is False
# rate > 100 is False
# The combined condition is False, so no error is raised


rate = "fifty"
# isinstance(rate, int) is False, so not isinstance(rate, int) is True
# rate > 100 is not checked because the first condition is already True
# The combined condition is True, so ValueError is raised


rate = 150
# isinstance(rate, int) is True, so not isinstance(rate, int) is False
# rate > 100 is True
# The combined condition is True, so ValueError is raised

score = 40
if score >90:
    print('u av A')
elif score < 90 and score >=80:
    print('u av B')
elif score < 80 and score >=70:
    print('u av C')
elif score < 70 and score >=60:
    print('u av D')
elif score < 60 and score >=50:
    print('u av E')
else:
    print('u failed')


# loops
# for loops
""" for i in range(10):
    print(i)

countries=['NIGERIA','ENGLAND','kENYA','UNITED STATE']
for country in countries:
    print(country)

countries_with_land = []

for b in countries:
  if 'LAND' in b:
    countries_with_land.append(b)
    print(countries_with_land)

countries_without_land = []
for i in countries:
    if 'LAND' not in i:
      countries_without_land.append(i)
print(countries_without_land)

countries_with_state = []
for i in countries:
    if 'STATE' in i:
        
      countries_with_state.append(i)
      print(countries_with_state)

      nums = [0,1,2,3,4,5]
      total = 0
      for num in nums:
          total += num
      print(total)
      even = []
      for num in nums:
         if num % 2 == 0:
            even.append(num)
      print(even)

      odd = []
      for num in nums:
        if num % 2 != 0:
           odd.append(num)
      print(odd)

      num = [1,2,3,4,-5,6,-7]
      for i in num:
         if i < 0:
            continue
         print(i)

         num = [1,2,3,4,-5,6,-7]
      for i in num:
         if i < 0:
            break
         print(i)
 """

""" countries=['NIGERIA','ENGLAND','kENYA','UNITED STATE']
for c in countries:
  if "LAND" in c:
      continue
  print(c)

countries=['NIGERIA','ENGLAND','kENYA','UNITED STATE']
for c in countries:
  print([c, c.lower(), c.upper()[:3],len(c)])   
# OR\n
print([[c, c.lower(), c.upper()[:3],len(c)]for c in countries])


for c in countries:
    if "LAND" in c:
        break
    print(c)
 """

""" data = [['NIGERIA', 'nigeria', 'NIG', 7], ['ENGLAND', 'england', 'ENG', 7], ['kENYA', 'kenya', 'KEN', 5], ['UNITED STATE', 'united state', 'UNI', 12]]

number = []
for list in data:
    number.append(list[3])
print(number) """

""" for i in range(4,-1,-1):
  print(i)
number = [1,2,3,4,5,6,7]
for i in number [::-1]:
    print(i) """
# for i in ['python','java','css']:
#     print(i)
# 

# USE FOR LOOP TO ILETERATE FOM 0 TO 100 AND PRINT THE SUM OF ALL NUMBERS:
sum =0
for i in range(101):
    sum = sum + i
print(sum)
sum = 0
for i in range(101):
    if i % 2 == 0:
        sum = sum + i
print(sum)



sum = 0
for i in range(101):
    if i % 2 != 0:
        sum = sum + i
print(sum)

        





# for list in  data:
#     print(list[3])


          
# for i in range(13):
#   for a in range(1,3):
#    print(f'{i} * {a} = {i * a}')

# for i in range(1, 13):
  #  print(f'{i} * {i} = {i * i}') for multiplication
  #  print(f'{i}^2 = {i ** 2}  {i} ^ 3 = {i ** 3}') for power of 2 , 3
  # print(f'{i}/2 = {i/ 2}  {i} //3 = {i// 3}')

            
          
            


            


      








   






    














    


  
        
  
  

