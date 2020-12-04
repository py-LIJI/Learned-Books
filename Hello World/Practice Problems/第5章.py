# -*- coding: utf-8 -*-
"""
第五章
"""

#%% 测试题 1
# 1：字符串
# 2：input('这是一条提示信息：')
# 3：使用int强制转换
# 4：使用float强制转换


#%% 动手试一试 1
a='li'
b='ji'
print(a+b)


#%% 2
a=input('姓：')
b=input('名：')
print(a+b)


#%% 3
a1=float(input('长（米）：'))
b1=float(input('宽（米）：'))
area=a1*b1
print(area,'平方米',end='')


#%% 4
a1=float(input('长（米）：'))
b1=float(input('宽（米）：'))
area=a1*b1
area1=area*9
money=area*20
print('总共需要多少地毯：'+str(area)+'平方米')
print('总共需要多少地毯：'+str(area1)+'平方英尺')
print('地毯总价格：'+str(money)+'元')


#%% 5
a2=float(input('有多少个五分币：'))
b2=float(input('有多少个二分币：'))
c2=float(input('有多少个一分币：'))
al=a2*5+b2*2+c2
print('总面值：'+str(al))












