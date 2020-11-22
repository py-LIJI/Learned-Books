# -*- coding: utf-8 -*-
"""
第13章
"""


#%% 测试题

#1 def
#2 函数名+括号
#3 调用函数时，把参数放进函数名后的括号内
#4 最多5-6个
#5 使用关键字return
#6 局部变量会消失


#%% 动手试一试 1

def mynamebig():
    print('''
          CCCC         A          RRRRR         TTTTTTTT           EEEEEEEE           RRRRRRR
         C           A   A        R    R           T               E                  R      R
        C           A     A       RRRRRR           T               EEEEEEEE           RRRRRRR
        C          AAAAAAAA       R    R           T               E                  R    R       
         CCCCC    A        A      R     R          T               EEEEEEEE           R     R
         ''')

print(mynamebig())


#%% 2

def information(xx_name, xx_address, xx_street, xx_city, xx_provence, xx_pcode, xx_country):
    print('name:',xx_name,'\n')
    print('dress:',xx_address,'\n')
    print('street:',xx_street,'\n')
    print('city:',xx_city,'\n')
    print('prov:',xx_provence,'\n')
    print('pcode:',str(xx_pcode),'\n')
    print('country:',xx_country,'\n')

print(information('小明','61号', '唐明顿街', '伦敦市', '大伦敦省','023566', '英国'))


#%% 3 

def calculateTax(price, tax_rate):
    total=price+(price*tax_rate)
    my_price=1000
    print('my_price(inside function)=',my_price)
    return total

my_price=float(input('enter a price:'))

totalprice=calculateTax(my_price, 0.06)

print('my_price=',my_price,'total price=',totalprice,)
print('my_price(out fuction)=',my_price)


#%% 4 

def totalmoney(m025,m01,m005,m001):
    momey=m025*0.25+m01*0.1+m005*0.05+m001*0.01
    return momey

qu=int(input('quarters:'))
di=int(input('dimes:'))
ni=int(input('nickels:'))
pe=int(input('pennies:'))


print('total is $'+str(totalmoney(qu, di, ni, pe)))









