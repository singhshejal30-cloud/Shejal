# # print("hello world")
# # print("shejal\nsingh")

# # firstname = "shejal"
# # lastname = "singh"
# # p# print(f"the division of {10} / {3} is: {10/3}")

# length = 10
# width = 20
# area = length * width
# print("the are of reactangle is:", area)

# x = 10
# result = x*2
# print("the result is:", result)
# firstname = 'shejal'
# lastname = "singh" 
# print("my name is:" +firstname+ " " +lastname+ "!")

# # #simpal way.
# # print("the sum of 5 & 10 is:", 5+10)
# print("the subraction of 5 & 10 is:", 5-10)
# print("the multiplication of 5 & 10 is:", 5*10)
# print("the division of 5 & 10 is:", 5/10)

# #formating(f) string:
# # print(f"the sum of {10} + {3} is: {10+3}")
# # print(f"the subtraction 0f {10} - {3} is: {10-3}")
# # print(f"the multiplicatin of {10} * {3} is: {10*3} ")


# #use of nested if.

college_ID = input("inter the ID:") 
if college_ID == "NSTI":
    trade = input("enter your trade:")
    if trade == "AIPA":
        print("eligible to enter in AI")
    elif trade == "COPA":
        print("eligible to inter in COPA")
    else:
        print("not a student of NSTI")        
else:
    print("not a student")
age = int(input("enter your age:"))
if age >= 18:
    citizenship = input("enter your citizenship:")
    if citizenship == "indian":
         print("eligible to voting")
    else:
         print("not indian citizen")
else:
    print("not eligible for voting")

age = int(input("enter your age:"))
citizenship = input("enter your citizenship:")
if age >= 18 and citizenship == "indian":
    print("eligible for voting")
else:
    print("not eligible for voting")

#

#STUDENT GRADE.
marks = int(input("enter your marks:"))
if marks >= 40:
    if marks >= 90:
        print("excllent")
    elif marks >= 75:
        print("very good")
    else:
        print("good")
else:
    print("fail")

#exam result checker
marks = int(input("enter the marks:"))
if marks >= 40:
    attendence = float(input("enter the attendence:"))
    if attendence >= 75:
        print("pass")
    else:
        print("good")
else:
     print("fail")

# login system
username = input("enter the username:")
password = input("enter the password:")
if username == "admin":
    if password == "1234":
        print("login successfully")
    else:
        print("incorrect password")
else:
    print("invalid username")

#temperature check.
temperature = int(input("enter the temperature:"))
if temperature > 0:
    if temperature < 20:
        print("it's cool")
    else:
        print("it's warm")
else:
    print("it's freezing")

#movie ticket discount.
age = int(input("enter your age:"))
day = input("enter the day (monday to sunday):")
if age <12:
    if day== "sunday":
        print("free ticket for kids!")
    else:
        print("half price ticket")
else:
    print("full price ticket")

#even and divisible by 5.
number = int(input("enter your number:"))
if number% 2 == 0:
    if number%5 == 0:
        print("even and divisible by 5")
    else:
        print("even but not divisible by 5")
else:
    print("odd number")            
    













    





        

