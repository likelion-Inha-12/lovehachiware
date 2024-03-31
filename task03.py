from task02 import Account

class PlusFunction(Account):
    def __init__(self,name,money,interest):
         super().__init__(name,money)
        
         self.interest = interest
    def display(self):
       print("%s님의 계좌 잔액은 %d원입니다." % (self.name,  self.money))
       print("이자율: 0.5%")
   
    def add_interest(self):
        interest = self.money*self.interest
        self.money += interest
        print("%s님의 계좌에 %d원의 이자가 추가되었습니다."%(self.name, interest))

#저축 계좌 생성
new_account = PlusFunction("sungmin",1000,0.05)

#초기 잔액 표시
new_account.display()

#입금하기
new_account.add(500)

#이자 추가하기
new_account.add_interest()

#출금하기
new_account.delete(100)

#최종 잔액 표시
new_account.display()
