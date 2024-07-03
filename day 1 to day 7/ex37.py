class BelowMinimumbalance(Exception):
    def __init__(self):
        self.msg = "withdrawing below minimum balance"
    def __str__(self):
        return self.msg

class BankAccount:
    def __init__(self,number,curbal,minbal):
        self.number = number
        self.curbal = curbal
        self.minbal = minbal

    def withdraw(self,amount):
        curbal = self.curbal
        self.curbal -= amount
        print(self.curbal)
        if self.curbal < self.minbal:
            self.curbal += amount
            raise BelowMinimumbalance
        return self.curbal
    
#create an instance of BankAccount and then call withdraw method to ensure the script
#raises the custom exception

try:
    b = BankAccount(123,1500,500)
    b.withdraw(1200)

except BelowMinimumbalance as e:
    print(e)