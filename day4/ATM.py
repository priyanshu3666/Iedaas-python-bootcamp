class ATM():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
            self.balance +=amount
            print("congratulation you have deposit Rs. {}".format(amount))
        
    
    def withdrawl(self,amount):
        if amount < self.balance:
            self.balance -=amount
            print("congratulation you have withdrawl  Rs. {}".format(amount))
        else:
            print("the amount is excess than balance ")