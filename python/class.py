""" import random

n = random.randrange(1, 10)
attempt = 5
while attempt > 0:
    guess = int(input('make your guessing'))
    if guess > n:
        print('too high')
    elif guess < n:
        print('too  low')
    else:
        print('you guessed it right')
        break
    attempt -=1
    if attempt > 0:
        print(f"you have {attempt} {'attempt' if attempt <= 1 else 'attempts'} left ")
    else :
        print('you av exhaust your attempts')     """


#week2
""" count = 0
while count < 5:
    if count == 3:
        print('count is 3')
    count +=1 """

 
""" # for loops
for number in range(2,10,2):
    print(number)

fruits = ["apple", "banana", "mango"]
for friut in fruits:
    print('fruit')


# break and continue
for i in range(10):
    if i > 5:
        break
    print(i)


     # continue
for i in range(10):
    if i % 2 ==0:
        continue
    print(i) 
 """

""" function
def test():
    global food
    food = ["eba", "amala", "egg","indomie"]
    for i in range(len(food)):
        print(i, food[i])

test()        
# print(food)

#  area
def area(length,breath):
    return length*breath
print(area(4,5)) """


""" def interest( principal:int,time,rate, a=100):
    
    interest =(principal * time * rate)/a
    return interest

print(interest( 10, 3, 2)) """






# ASSIGNMENT: principal:takes integer,rate:integer but not more than 100,time only int



# def interest(principal:int,time:int,rate:int):
#     if rate < 100:
#         interest = (principal * rate * time) / 100
#         return interest 
#     else:
#         raise ValueError("Rate must be an integer and not more than 100")
     
# print(interest(1000,2,5 ))





# assignment  two:
# Write a function count_movies_by_genre(movies) that takes the list of movies as input.
# The function should iterate through the movie list and count the occurrences of each genre.
# Use a dictionary to store genre names (as keys) and their corresponding movie counts (as values)







movies = [
    ["Casablanca", "Michael Curtiz", 1942, "Drama"],
    ["The Godfather", "Francis Ford Coppola", 1972, "Crime"],
    ["The Shawshank Redemption", "Frank Darabont", 1994, "Drama"],
    ["The Dark Knight", "Christopher Nolan", 2008, "Action, Thriller"],
    ["Living in Bondage", "Ola Balogun", 1992, "Drama"],
    ["Nneka the Pretty Serpent", "Christian Chukwu", 1994, "Drama, Thriller"],
    ["Rattlesnake", "Amaka Igwe", 1995, "Crime, Thriller"],
    ["Aki na Ukwa", "Chico Ejiro", 2002, "Comedy"],
    ["Saworo IDE", "unknown ", 1997, "Drama"]
]
""" def count_by_genre(movies):
    genres = {}
    for movie in movies:
        genres= movie[3]
        print(genres)
    return genres
# print(count_by_genre(movies))



def count_by_genre(movies):
    genres_count = {}
    for movie in movies:
        genres = movie[3].split(',')
        print(genres)
    for genre in genres:
        if genre in genres_count:
            genres_count[genre] +=1
        else:
            genres_count = 1
        return genres_count
def find_movies_after_year(movies:list, year):
        return [movie for movie in movies if movie[2] > year]
print(count_by_genre(movies))
print(find_movies_after_year(movies,1994))
 """
def count_by_genre(movies):
    genre_count = {}
    for movie in movies:
        genre= movie[3].split(',')
        if genre in genre_count:
           genre_count[genre] += 1
        else:
           genre_count[genre] = 1
           












 





   
        






       











    
   















 







    

