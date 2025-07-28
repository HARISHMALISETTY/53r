class BankAccount:
    def __init__(acnt,name,email,ph,balance):
        acnt.name=name
        acnt.email=email 
        acnt.ph=ph
        acnt.balance=balance
    def deposit(acnt,d_amnt):
        acnt.balance+=d_amnt
    def withdrawl(acnt,w_amnt):
        acnt.balance-=w_amnt
    def checkBalance(acnt):
        print(acnt.balance)
harish_acnt=BankAccount("Harish","harish@gmail.com",9848522114,10000)
harish_acnt.checkBalance()
harish_acnt.deposit(5000)
harish_acnt.checkBalance()
harish_acnt.withdrawl(2500)
harish_acnt.checkBalance()