#Write a function called greet_user that takes a named argument 'name' and returns 'Hello,
 #{name}!
# def greet(name):
#     return f"hello, {name}!"
# print (greet("srinu"))

     
     
     
#2.) Create a function 'check_temperature' that takes a named argument 'temp' and returns 'Fever' if
 #temp > 99 else 'Normal'.
 
# def check_temperature(temp):
#     if temp > 99:
#         return 'fever'
#     else:
#         return 'normsl'
# a=check_temperature(99)
# print(a)
    
        

#3)  Define a function 'get_last_fruit' that takes a list of fruits as input and returns the last fruit
# user = input("enter the fruits with separted by commas:")
# fruit_list = user.split(',')
# def get_last_fruit(fruits):
#     return fruits[-1]
# a= get_last_fruit(fruit_list)
# print(a)

#$) Create a function 'get_price_tag' that takes a 'price' and returns 'Expensive' if price > 1000 else
 #'Affordable'
# def get_last_price(price):
#     if price > 1000:
#         return 'expensive'
#     else:
#         return 'affordable'
# a= get_last_price(2300)
# print(a)


# 6. Define a function 'uppercase_if_string' that takes one argument and returns it in uppercase if it's a
#+--12 string, else return 'Invalid input'

# def uppercase_if_string(name):
#     if type(name) == str:
#         return name.upper()
#     else:
#         return 'invalid input'
    
# q=uppercase_if_string("Hitman")
# print(q)
# a = uppercase_if_string(67899)
# print(a)
    
   
#7. Write a function 'safe_divide' that takes two numbers as keyword arguments 'num' and 'den'.
# Return the result if den is not 0, else return 'Cannot divide'
    
# def safe_divide(num,den):
#     a = num/den
#     if den != 0:
#         return 'can divide'
#     else:
#         return 'cannot divide'
    
# b = safe_divide(10,)
# print(b)
            
            
            # 8. Write a function 'check_login' that takes a dictionary with 'username' and 'password'. Return
# 'Login successful' if password is not empty

# def check_login(detais):
#     if details.get('password')
    
    
    
    
    
    
    
    
    
  #9. Create a function 'get_full_name' that takes 'first' and 'last' as named arguments and returns full
 #name in title case  
# def get_full_name(first,last):
#     return f"{first}{last}".title()
    
# full_name = get_full_name('satya','srinivas')
# print(full_name)

#10 Write a function 'get_discounted_price' that takes 'price' and 'is_member'. If is_member is True,
# return price * 0.9 else return price


def get_discounted_price(price,is_member):
    if   is_member:
        
        return price * 0.9 if is_member
    else:
        return price
a= get_discounted_price(1000,'true')
print(a)
        

    
    