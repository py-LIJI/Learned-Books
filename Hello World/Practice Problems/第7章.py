# -*- coding: utf-8 -*-
"""
第7章
"""


#%% 测试题

# 1： Under 20
# 2： 20 or over
# 3： if x >= 30 and x <=40
# 4： if answer == 'Q' 
#        print('Q')
#     elif answer == 'q'
#        print('q')


#%%  课堂练习

a = int(input('请输入分数：'))
if 0 <= a <= 100:
    if a > 90:
        print('优秀')
    elif a > 80:
        print('良好')
    elif a > 70:
        print('中等')
    elif a >= 60:
        print('及格')
    else:
        print('不及格')
else:
    print('输入分数值不符合要求（0-100）！')



#%%  动手试一试  

money=float(input('购买金额：'))
if money >=0:
    if money<=10:
        cut_money=money*0.9
    else:
        cut_money=money*0.8
else:
    print('输入金额数值有误')
print('折扣后金额：'+str(cut_money))


#%%  2

sex=str(input('请问您的性别（女 或 男）：'))
if sex=='女':
    age=int(input('请问您的年龄：'))
    if 10<=age<=12:
        print('恭喜，有机会参加足球队')
    else:
        print('抱歉，您的年龄不符合要求')
else:
    print('抱歉，您的性别不符合要求')


#%%  3

size=int(input('size of tank (L):'))
full=int(input('percent full (%):'))
long=int(input('km per liter (km/L):'))
liter=size*full*long
print('you can go another'+str(liter)+'km')
if liter>200:
    print('you can wait next station')
else:
    print('the next gas station is 200km awary')
    
    
#%% 4

password = '123456'

n = str(input('请输入6位数字密码：')) 

if n == password:
    print('you are in')
else:
    print('your passward is wrong')
    
    
    





