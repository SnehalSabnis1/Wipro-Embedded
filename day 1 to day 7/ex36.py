class BelowMinimumbalance(Exception):
    def __init__(self):
        self.msg = "withdrawing below minimum balance"
    def __repr__(self):
        return self.msg

class BankAccount:
    def __init__(self,number,curbal,minbal):
        self.number = number
        self.curbal = curbal
        self.minbal = minbal

    def withdraw(self,amount):
        curbal = self.curbal
        self.curbal -= amount
        if self.curbal < self.minbal:
            self.curbal += amount
            raise BelowMinimumbalance
        return self.curbal
    
