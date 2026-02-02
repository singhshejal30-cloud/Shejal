# class Bankaccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance

#     def add_amount(self,amount):
#         self.__balance+=amount

#     def withdraw(self,amount):
#         if amount <= self.__balance:
#             self.__balance -= amount       

#     def show_balance(self):
#         return self.__balance
    
# x=Bankaccount("shejal",1000) 

# x.add_amount(300)

# print(x.show_balance())

# class ATM:
#     def __init__(self,pin,balance):
#         self.__pin = pin
#         self.__balance=balance

#     def check_balance(self,pin):
#         if pin == self.__pin:
#             return self.__balance
#         else:
#             return "incorrect pin"

# x=ATM(1806,150000)
# print(x.check_balance(1806))

# class Bankaccount:
#     def __init__(self,account_number,balance):
#         self.amount_number=account_number
#         self.__balance = balance            #private variable
    
#     def deposite(self,amount):
#         self.__balance+=amount
#         print(f'Deposited {amount}.newbalance{self.__balance}')

#     def get_balance(self):
#         return self.__balance

# account = Bankaccount("1234",5000)
# account.deposite(2000)
# print(account.get_balance())

# class Employee:
#     def __init__(self):
#         self.name =""
#         self.__salary = 0

#     def set_details(self,name,salary):
#         self.name = name
#         if salary > 0:
#             self.__salary = salary

#     def showname(self):
#         print("name:",self.name)

#     def updatesalary(self,amount):
#         if amount > 0:
#             self.__salary = self.__salary +amount
#         else:
#             print("possitive ammount")

#     def showsalary(self):
#         print("salary:",self.__salary)

# emp = Employee()
# emp.set_details("shejal",800000)
# emp.showname()
# emp.updatesalary(3000)
# emp.showsalary()       


               

                    

    

