class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, chislo):
        self.balance += chislo

    def withdraw(self, chislo):
        if chislo > self.balance:
            print("Недостаточно средств")
        else:
            self.balance -= chislo
            print(f"Баланс: {self.balance}")

name = str(input())
chislo = int(input())
account = Account(name, chislo)

dep = int(input("Введите сумму для депозита: "))
account.deposit(dep)

withd = int(input())
account.withdraw(withd)