class User:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def transfer_money(self, other_user, amount):
        self.other_user=other_user
        self.balance-=amount
        self.other_user.make_deposit(amount)
    def make_withdrawal (self, amount):
        self.balance-=amount
    def display_user_balance(self):
        print("username:",self.name ,"account balance:",self.balance)
    def make_deposit(self, amount):	
    	self.balance += amount

user1=User(" Guido ", 150 )
user2=User(" Rossum", 100 )
user3=User(" Yara", 100 )

user1.make_deposit(100)
user1.make_deposit(200)
user1.make_deposit(300)
user1.make_withdrawal(100)
print(user1.balance)

user2.make_deposit(200)
user2.make_deposit(300)
user2.make_withdrawal(100)
user2.make_withdrawal(200)
print(user2.balance)

user3.make_deposit(100)
user3.make_withdrawal(100)
user3.make_withdrawal(200)
print(user3.balance)

user1.transfer_money( user2, 100)
print(user2.balance)
print(user1.balance)
