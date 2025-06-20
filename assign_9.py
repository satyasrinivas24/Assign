#------------------------------------------------FOR LOOPS---------------------------------------
#1. Write a for loop that prints numbers from 1 to 5 using range().

# for i in range (1,6):
#     print(i)

#2) 2. Use a for loop with range() to print all even numbers between 10 and 20.

# for i in range (10,20):
#     if i%2==0:
#         print(i)

#3) 3. Ask the user for 3 names using input() in a loop. Store them in a list and print the list


# name = []
# for i in range(3):
#     user = input('enter the name:')
#     name.append(user)
# print(name)


#4)4. Given a list of numbers, use a for loop to print the square of each number

# list = [2,4,6,8,10]
# for i in list:
#     print(f"Square of {i} is {i**2}")


# #5)  5. Loop through a list of dictionaries with keys 'name' and 'age'. Print each name and age.

# list = [
#     {'name':'srinu','age':22},
#     {'name':'charpitha','age':22},
#     {'name':'triveni','age':21}
    

# ]
# for details in list:
#     print("name:",details['name'])
#     print("age:",details['age'])

# 6. Given a nested list of fruits like [['apple', 'banana'], ['grape', 'mango']], use a for loop to print all
 #fruits
 
# fruits = [['apple','banana'],['grape','mango']]
# for i in fruits:
#     for j in i:
        
    
#         print(j)
 
 
 #  7. Write a for loop that prints characters of a string entered by the user
 
# user = input("enter the string:")

# for char in user:
    

#     print(char) 

#88. Use range() to print numbers from 5 to 1 in reverse order

# for i in range (5,0,-1):
#     print(i)

#9Write a program that asks the user to input 3 subjects and 3 marks each, then print each subject
# with its mark.#

# subject = [
#     {'subjects': 'Maths','marks':78},
#     {'subfor i in range(3)jects': 'science','marks':80},
#     {'subjects': 'telugu', 'marks':97}
# ]









#10Write a program that asks the user to input 3 subjects and 3 marks each, then print each subject
 #with its mark.
 
list = [('car',2300000),('bike',250000),('bat',85000)]
for product,price in list:
    print(f"{product}: {price}")