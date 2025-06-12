#Assignment-3
# sets
#sets
# a = {'Mas','Science','Social'}
# print(a)

 #3 2) hobbies
# a = {input("enter 1 hobbies:"),(input("enter 2 hobbies:"),(input("enter 3 hobbies:")))}
# print("hobbies set:",hobbies)


# 3) colour set
# colour = {'red','blue','green'}
# colour.add("yellow")
# print(colour)

#4) update the first set
# set1 = {'apple','banana'}
# set2 = {'banana','cherry'}
# set1.update(set2)
# print("update set1:",set1)

#5) create two cities union
# personA = {'hyd','chennai','delhi'}
# personB ={'mumbai','chennai','hyd'}
# personC = personA|personB
# print(personC)

#6) intersection
# a = {'alex','john','mike'}
# b= {'john','mike','lisa'}
# c= a & b
# print(c)

# 7) create a set items:

# a = {'pen','pencil','eraser'} 
# a.discard("pencil")
# print(a){'
# 8) remove function

# item ={"marker",}
# item.remove("marker")
# print(item)

# 9)  weekday
# weekday = {'mon','tue','wed','thu','fri'}
# removed = weekday.pop()
# print(removed)
# print("update  weekday sets:",weekday)

#10) clear set

# s = {'audio','suzik','thar','bmw','ford'}
# s.clear()
# print(s)

#11) delete tools
# tools = {"fan","ac","bag","tv"}
# del tools

#12) string
# string = {'hello',}
# print(string)

#13) five words
user = input("enter five separated word by space:").split()
res = set(user)
print(res)
words = set(input("13. Enter five words separated by space: ").split())
print("Unique words:", words)



#14 unique elemnts
A = {'a','b','c'}
B = {'c','d','e'}
print("element that unique of A:",A.difference(B))

#15 count of item
items = {'AC','fans','chair','table','mobile'}
print(len(items))

