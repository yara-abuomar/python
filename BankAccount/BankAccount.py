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
		   
			
acount1=BankAccount(.5,100)
acount2=BankAccount(.5,500)

acount1.deposit(100).deposit(100).deposit(300).withdraw(100).yield_interest().display_account_info()
acount2.deposit(100).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()


    
	