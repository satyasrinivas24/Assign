#1.) fav food
# food = {
#        "fruits":76,
#        "fastfood":100,
#        "choco"  : 29 
# }
# print(food)

#2.) 3 subject
# sub_1 = input("enter the sub-1 and marks:")
# sub_2 = input("enter the sub-2 and marks:")
# sub_3 = input("enter the sub-3 and marks:")
# print(dict(sub_1,sub_2,sub_3))
#3)
# student = {'name': 'srinu','age': 22,'grade':12}
# student ['city']='kakinada'
# print(student)

#4)update anthor dict()
# a = {'a':1,'b':2}
# b = {'b':2,'c':3}
# c= a.update(b)
# print(a)

#5)
# person_A ={'Java':'good','python':'verygood'}
# person_B ={'problem_solving':'ok','communication':'bad'}
# merge = {** person_A,**person_B}
# print(merge)

#6)
# b = {'apple':5,'banana':3,'orange':8}
# a = b.keys()
# print(a)
#7)
# a= {'red': '#FF0000','green':'#00FF00','blue':'#0000FF'}
# b= a.values()
# print("values:",b)
#8)
# a = {'pen': 2, 'pencil': 5, 'eraser': 1}
# b = a.pop('pencil')
# print("removed:",b)
# print("updated dictionary:",a)
#9)
# a = {'pen': 2, 'pencil': 5}
# print(a.get('marker'))
#10)
# car = {"Mahindra_Thar":1988,"Audi":1970,"skoda":1980}
# a = car.popitem()
# print("removed:",a)
#11)
# book = {'Book1': 'Author1', 'Book2': 'Author2'}
# book.clear()
# print("cleared:",book)

#13)
# d1 = ['name', 'age', 'city']
# d2 = ['John', 25 ,'NYC']
# d3 = dict(zip(d1,d2))
# print(d3)

#14)
# from collections import Counter
# a = input("Enter the 5 separted word by space:").split()

# b = Counter(a)
# print(dict(b))


#15)
# data = {'x': 10, 'y': 20, 'z': 30}
# filtered = {k: v for k, v in data.items() if v > 15}
# print("15. Filtered items:", filtered)


#16)
# movies = {'Inception': 2010, 'Interstellar': 2014, 'The Matrix': 1999}
# print("16. Number of movies:", len(movies))

#17)
# langs = {'java': 1995, 'python': 1991, 'c++': 1985}
# print("17. Is 'python' present?", 'python' in langs)

#18)
# student = {
#     'personal_info': {'name': 'Alice', 'age': 15},
#     'grades': {'math': 95, 'science': 88}
# }
# print("18. Math grade:", student['grades']['math'])

#19)

# text = 'hello'
# ascii_dict = {ch: ord(ch) for ch in text}
# print("19. ASCII dictionary:", ascii_dict)

#20)
# original = {'a': 1, 'b': 2}
# copy_dict = original.copy()
# copy_dict['b'] = 5
# print("20. Original dictionary:", original)
# print("    Modified copy:", copy_dict)


