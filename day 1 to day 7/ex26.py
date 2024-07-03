list_of_accounts=[]
account1={'name':'bob','number':12345,'doj':'12-03-2024','curbalance':1000}
list_of_accounts.append(account1)
account2={'name':'john','number':12346,'doj':'18-03-2024','curbalance':500}
list_of_accounts.append(account2)


def incre_decre_curbalance(number,amount.op):
    for d in list_of_accounts:
        if d['number']==number:
            if op=='withdraw':
                d['curbalance'] -= amount
            elif op=='deposite':
                d['curbalance'] += amount