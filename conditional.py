# age = int( input("how old are you?\n"))
# if age >= 18 and age <= 45:
#    print("You have access")
# else:
#    print("You are not allowed here.")
 
      
#  # Ask user to input an integer
# num = int(input("Please enter a number:\n"))
# # Check if the number is even or odd
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")




# #ask user to input their score 
# score =int (input("Please enter a number:\n "))
# # if score is between 90 to 100 print grade A
# if score >=90 and score <=100 :
#     print ("Grade A")
# # if score is between 80 to 89 print grade B
# if score >=80 and score <=89 :
#     print ("Grade B")
# # if score is between 70 to 79 print grade C
# if score >=70 and score <=79 :
#     print ("Grade C")
# # if score is between 60 to 69 print grade D
# if score >=60 and score <=69 :
#     print ("Grade D")
# # if score is between 0 to 59 print grade F
# if score >=0 and score <=59 :
#     print ("Grade F")




# #program to calculate the average of two numbers 
# #take two numbers as input 
# first_num = float (input ("Please enter a number:"))
# second_num = float (input ("Please enter another number:" ))
# #declare average = (num1+num2)/2
# average = (first_num + second_num)/2

# #display the average 
# print (f"The average of {first_num} and {second_num} is {average}")

# #accept an age input from the user and a full name 
# name = input ("What is your name?:")
# age = int(input("How old are you?:"))
# #if the age is less than 18 and the average is equal to 20 
# if age < 18 and int(average) == 20:
#     print(f"{name},you are not allowed to vote")



# #Ask user to input their purcchase amount as float 
# purchase_amount = float(input("What is your purchase amount"))

# #if the purchase is 100 cedis or more apply 20% discount and print amount to pay 
# if purchase_amount >= 100 :
#     discount = 0.2 * purchase_amount
#     amount_to_pay =purchase_amount - discount 
#     print(f"you have to pay : {amount_to_pay}")
# #if the purchase is 50 cedis or more apply 10% discount and print
# elif purchase_amount >= 50:
#     discount = 0.1 * purchase_amount
#     amount_to_pay =purchase_amount - discount 
#     print(f"you have to pay : {amount_to_pay}")
# #if the purchase isless than 50 cedis there is no  discount and print
# else:
#     print(f"You have to pay :{purchase_amount}")
    



#ask user to input the length of the 3 sides of a traingle
x = float (input("Enter the first side:"))
y = float (input("Enter the second side:"))
z = float (input("Enter the third side:"))
#if all sides are equal print Equilateral
if x == y and y == z :
    print("Equilateral triangle")
#if 2 sides are equal print Isosceles
if x == y or y == z or x==z:
    print("Isosceles triangle")    
#if no sides are equal print Scalene
else:
    print("Scalene triangle")



