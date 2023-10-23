class User:
    def __init__(self,name):
        self.name=name
        self.account1=BankAccount(int_rate=.02, balance=0)     
        self.account2=BankAccount(int_rate=.04, balance=0)   
    def make_withdrawal (self,account):
        if account == self.account1:
            self.account1.deposit()
        else:
            self.account2.deposit()
	
    def display_user_balance(self):
        print("username:",self.name ,"account balance:",self.balance)
    def make_deposit(self,account):	
        if account == self.account1:
            self.account1.withdraw()
        else:
            self.account2.withdraw()
    	


class BankAccount:
	def __init__(self, int_rate, balance): 
		self.int_rate=int_rate
		self.balance=balance
	def deposit(self, amount):
		self.balance+=amount
		return self
	def  display_account_info(self):
		print("Balance:" , self.balance)
		return self
	def yield_interest(self):
		if self.balance>0:
			self.balance*=self.int_rate
			return self

	def withdraw(self, amount):
		if amount>self.balance:
			print( "Insufficient funds: Charging a $5 fee" )
			self.balance-=5
			return self
		else:
			self.balance-=amount
			return self
		

user1=User("yara")
acount1=BankAccount(.02,100)
user1.account1.deposit(100)
print(acount1.balance)
print(user1.account1)



