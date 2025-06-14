#first create the hotel bill 
# start neeed to known about the menu
# and next want to select the items what do we want
# then the quatity of items what there want
# then product 1 of the items price into quatity how mny they were taken
total_bill = 0
menu = {
        'idly' : 40,
        'bonda': 45,
        'dosa' : 60,
        'sp.dosa' : 70,
        'puri'  : 50,
        'vaada' : 35,
        'upma'  : 30
}
item_1_choice = input("what do you want sir!:")
item_1_quantity =int(input("how many do you want sir!:"))

item_2_choice = input("next,what do you want sir!:")
item_2_quantity = int(input("how many do you want sir!:"))

item_1_bill = item_1_quantity*menu.get(item_1_choice)
item_2_bill = item_2_quantity*menu.get(item_2_choice)

total_bill = item_1_bill + item_2_bill
print(total_bill)

detail_bill = f""" 
##########WELCOME TO GODAVARIS HOTEL #######
BILL_ID = 34578
{item_1_choice}X{menu.get(item_1_choice)} = {item_1_bill}
{item_2_choice}X{menu.get(item_2_choice)} = {item_2_bill}
--------------------------------------------------------------------------------------------------------
GST - 0%
tax - 0%
---------------------------------------------------------------------------------------------------------
Total_bill:rs.{total_bill}
---------------------------------------------------------------------------------------------------------
                        THANK YOU FOR COMING VISIT AGAIN!
"""
print(detail_bill)