#29/10/2021
#pavithra
#Bank account manager

def main():
   while True:
      
      print("Welcome to Bank")
      print("\n 1.Admin\n 2.User\n 3.Exit\n")
      select=input("Select your option: ")
      if select == '1':
            Admin()
      if select=='2':
            User()
      if select=='3':
            break
      


def Balance_check():
   print("Total Balance : ", baln_amount)
   
   
def Deposite_Amount():
    accs_no=input("Enter the Account number: ")
    accs_pin=input("Enter the Acount pin: ")
    a1=acc_no.index(accs_no)
    b1=acc_pin.index(accs_pin)

    if a1==b1:
       print("\nChoice your Account Type ")
       acc_type=input("\n 1.saving account\n 2.checking account\n 3.business account\n")

       deposite_amnt=input("Enter the Deposite Amount: ")
       balance[a1]=int(balance[a1])+int(deposite_amnt)
       print("Amount Successfully Depostited")
       print("Total Amount:",balance)
       main()
          

def Withdraw_Amount():
   
   accs_no=input("Enter the Account number: ")
   accs_pin=input("Enter the Acount pin: ")
   a1=acc_no.index(accs_no)
   b1=acc_pin.index(accs_pin)

   if a1==b1:
      print("\nChoice your Account Type ")
      acc_type=input("\n 1.saving account\n 2.checking account\n 3.business account\n")
      withdraw_amount=input("Enter the Withdraw Amount: ")
      withdraw=(balance[a1])-int(withdraw_amount)
      print("Amount Successfully Withdraw")
      print("Remaing Amount:",withdraw)
   

      User()
      

def User_baln_check():
   accs_no=input("Enter the Account number: ")
   accs_pin=input("Enter the Acount pin: ")
   a1=acc_no.index(accs_no)
   b1=acc_pin.index(accs_pin)

   if a1==b1:
      print("\nChoice your Account Type ")
      acc_type=input("\n 1.saving account\n 2.checking account\n 3.business account\n")
      balns_check=balance[a1]
      print("Your Account Balance",balns_check)


admin_name=['pavithra','geethanjali','soundharya']
admin_password=['123','456','789']
baln_amount=[20000]
acc_no=['200111','300222','400444']
acc_pin=['06660','07770','01230']
accs_type=['saving account','checking account','business account']
balance=[60000,10000,35000]


def Admin():
   name=input("Enter the admin name : ")
   password=input("Enter the admin password : ")
   a=admin_name.index(name)
   b=admin_password.index(password)
   if a==b:
      print("\n 1.Balance check\n 2.Exit\n")
      select1=input("Enter the choice : ")
      if select1=='1':
         Balance_check()
      if select1=='2':
         main()
      
   
def User():
   print("\n 1.Deposite\n 2.withdraw\n 3.Balance check\n 4.Exit")
   select2=input("Enter the choice : ")
   if select2=='1':
      Deposite_Amount()
   if select2=='2':
      print("h")
      Withdraw_Amount()
   if select2=='3':
      User_baln_check()


main()
