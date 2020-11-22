# -*- coding: utf-8 -*-
"""
第8章
"""


#%% 测试题
# 1： 循环5次
# 2： 循环3次，循环值1，3，5
# 3： 为1，2，3，4，5，6，7
# 4： 为0，1，2，3，4，5，6，7
# 5： 为2，4，6，8
# 6： 为10，8，6，4，2
# 7： continue
# 8： 当条件为False时


#%% 动手试一试 1

n = int(input('which multiplication table would you like?:\n'))

print('here is your table:')
for i in range(1, 11):
    print(n, '×', i, '=', n*i)
    
    
#%% 2

n = int(input('which multiplication table would you like?:\n'))

print('here is your table:')

i = 1
while i <11:
    print(n, '×', i, '=', n*i)
    i = i + 1


#%% 3

n = int(input('which multiplication table would you like?:\n'))
high = int(input('how high do you want to go?:\n'))

print('here is your table:')
for i in range(1, high + 1):
    print(n, '×', i, '=', n*i)






























