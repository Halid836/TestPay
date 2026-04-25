class Balance:
    def __init__(self, balance: int):
        self.balance = balance

class Transfer:
    def __init__(self, name: str, amount: int):
        self.name = name
        self.amount = amount
        
class Deposit:
    def __init__(self, deposit: int):
        self.deposit = deposit

b = Balance(9999)
print("balance:", b.balance)

tools = input("Number: ")

if tools == '1':
    user = input("Name: ")
    amount = int(input("amount: "))
    
    b.balance -= amount
    print("balance:", b.balance)

if tools == '2':
    dep = int(input("deposit summa :"))
    deps = Deposit(dep) 
    print("DEPOSIT :", deps.deposit)
    b.balance += deps.deposit
    print("balance:", b.balance)
   
if tools == '3':
    nam = input("Name:")
    sum_amount = int(input("amount :"))
    nams = Transfer(nam, sum_amount)
    b.balance -= nams.amount
    print(f"Transfer:\nName:{nams.name}\nAmount:{nams.amount}\n")
    print("balance:", b.balance)