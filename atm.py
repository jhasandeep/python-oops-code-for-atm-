class Atm : 
    
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input = input('''
        Hello, how would you like to proceed ? 
        1. Enter 1 to Create pin
        2. Enter 2 to depsoit 
        3. Enter 3 to withdraw
        4. Enter 4 to Check balance
        5. Enter 5 to exit \n''')
        
        if user_input == "1":
            self.crete_pin()
            
        elif user_input == "2":
            self.deposit()
            
        elif user_input == "3":
            self.withdraw()
            
        elif user_input== "4":
            self.check_balance()
            
        else:
            print("bye")
            
        
    def crete_pin(self):
        self.pin = input("Enter Your pin")
        print("Pin set Successfully")
        
    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = input("Enter your amount")
            self.balance += amount 
            print("Amount added Successfully")
        else:
            print("Wrong Pin !!!")
            
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = input("Enter your amount")
            self.balance -= amount 
            print("withdraw Successfully")
        else:
            print("Wrong Pin !!!")
            
    def check_balance(self):
        
        temp = input("Enter your pin")
        if temp == self.pin:
            
            
            print(f"Balance:{self.balance}")
        else:
            print("Wrong Pin !!!")
        
        
            
    
        
        
        
        
        
sbi = Atm()
sbi.check_balance()
