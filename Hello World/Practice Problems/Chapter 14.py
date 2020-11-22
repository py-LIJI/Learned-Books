# -*- coding: utf-8 -*-
"""
第14章

"""
                 

#%% 测试题
# 1： 使用cass关键字
# 2： 对象特征，对象中的变量
# 3： 对象动作，对象中的函数
# 4： 类是对象的定义或者蓝图，从这个类中建立的对象就是实例
# 5： 使用self
# 6： 不同的对象，使用相同的方法名称，实现的是不同的动作
# 7： 子类从父类那里得到的属性和方法


#%% 动手试一试 1

class BankAccount:
    def __init__(self, acct_number, acct_name):
        self.acct_number = acct_number
        self.acct_name = acct_name
        self.balance=0.0
    
    def __str__(self):
        msg = 'this bankaccount is '+self.acct_name
        return msg
    
    def displaybalance(self):
        print('this account balance is', self.balance)
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print('you deposit is ', amount)
        print('you new balance is ', self.balance)
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print('your balance dont have so much money!')
        print('you withdraw is ', amount)
        print('your new balance is ', self.balance)
        
mybankaccount = BankAccount(123456, 'xiangming')
print(mybankaccount)
mybankaccount.displaybalance()
mybankaccount.deposit(12000)
mybankaccount.withdraw(6500)


#%% 2

class InterectAccont(BankAccount):
    def __init__(self, acct_number, acct_name, percent):
        # 声明调用父类的__init__方法
        # BankAccount.__init__(self, acct_number, acct_name)
        super().__init__(acct_number, acct_name)
        self.percent = percent
        
    def addInterect(self):
        earn = self.balance*self.percent
        self.balance = self.balance + earn
        print('本年利息', earn)
        print('账户余额', self.balance)
        
myearn = InterectAccont(123456, 'xiangming', 0.05)
myearn.addInterect()

        
        
        
        












            
        















