print(set())
print(len(set()))

A = {1,2,3,3,5,8,9}
B = {2,3,6,8,9}

print(A)
print(len(A))
print(B)
print(len(B))
print(7 in A)
print(2 in B)

#for loop
for item in A:
    print(item)

    # note: no index in set and u can use .add to add an item instead of insert
    # set ignore duplicate and just print only one
A.add(100)
A.update([12,13,14,15])
print(A)   
fruits = {'banana','orange','mango','apple'}
vegetable = ('carrot','tomato','okro','onion')
fruits.update(vegetable)
print(fruits)


print(B)
B.remove(6)
print(B)
print(A.clear())
print(A)
st1 = {'one','two','three','four','five'}
st2 = {'two','three'}

print(st2.issubset(st1))
print(st2.issuperset(st1))

# del A
# print(A)
fruits =['banana','orange','mango','banana','apple', 'mango']
print(set(fruits))

A = {1,2,3,3,5,8,9}
B = {2,3,6,8,9}

#A n B ={2,3,8,9} *intersetion of A AND B
#A U B ={1,2,3,5,6,8,9} * A UNION OR COMBINE B
#A \ B ={1,5} * A WITHOUT B
#B \ A ={6} *B WITHOUT A
#(A\B) U (B\A)={1,5,6}*SYMETHRIC  DIFFERENCE
#set and list is use to remove duplicate
# things to note in set
#set do not allow duplicate
#set does not allow ordering
#set does not allow accesing by item by index
print(A.union(B))
print(B.union(A))
print(A.intersection(B))
print(B.intersection(A))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))
print(A.symmetric_difference_update(B))
# if they do not intersect,which dey do and the answer is false
print(A.isdisjoint(B))


