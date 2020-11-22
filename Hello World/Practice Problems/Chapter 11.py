# -*- coding: utf-8 -*-
"""
第11章
"""


#%% 测试题
#1 输入控制循环变量空间
#2 把一个循环放入另一个循环内部
#3 共打印15个星
#4 *** 
#  ***
#  ***
#  ***
#  ***
#5 共16种选择


#%% 动手试一试 1

import time

begin = int(input('countdown timer: how many seconds? '))
for i in range(begin, 0, -1):
    print(i)
    time.sleep(1)
print('BLAST OFF!')


#%% 2

import time

begin = int(input('countdown timer: how many seconds? '))
for i in range(begin, 0, -1):
    print(i, '\t', '* '*i)
    time.sleep(1)
print('BLAST OFF!')


#%% 2 内循环法

import time

begin = int(input('countdown timer: how many seconds? '))
for i in range(begin, 0, -1):
    print(i, ' ', end='')
    for j in range(i):
        print('* ', end='')
    print(' ')
    time.sleep(1)
print('BLAST OFF!')
   





















