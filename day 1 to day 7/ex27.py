class Bankaccount:
    def __init__(self,name,number,doj,curbalance):
        self.name=name
        self.number=number
        self.doj=doj
        self.curbalance=curbalance


def incre_decre(self,amount.op):
    if op=='withdraw':
        self.curbalance -= amount
    elif op=='deposite':
        self.curbalance += amount