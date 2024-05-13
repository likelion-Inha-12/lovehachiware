# ~님의 계좌 잔액은 ~원입니다.
#원이 입금되었습니다
#~원이 출금되었습니다

class Account:
    def __init__ (self,name,money):
        self.name = name
        self.money = money
        print(name,money)
    
    def add(self,plusmoney):
       self.money = self.money+plusmoney
       print("%d원이 입금되었습니다."%plusmoney)

    def delete(self,minusmoney):
        
        if minusmoney > self.money:
            # 우리 돈보다 출금할 돈이 많으면 경고문이 떠야함
            print("출금 금액이 잔액을 초과하거나 잘못 입력되었습니다")
        else :
            self.money = self.money - minusmoney
            print("%d원이 출금되었습니다"%minusmoney)

    def check(self):
        print("%s님의 계좌 잔액은 %d원입니다."%(self.name,self.money)) 

sungmin_account = Account("ssm", 10000)


sungmin_account.check()
sungmin_account.add(10)
sungmin_account.check()
sungmin_account.delete(50)
sungmin_account.check()
