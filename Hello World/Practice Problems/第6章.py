# -*- coding: utf-8 -*-
"""
第6章
"""

#%% 测试题
# 1： 使用easygui.msgbox()
# 2： 使用easygui.enterbox()
# 3： 使用easygui.integerbox()
# 4： 整数框输入后，再用float()转换
# 5： 你不操作，也会输出的值软件的默认地址


#%% 动手试一试 1

import easygui

easygui.msgbox('this program converts fahrenheit to celsius')

fahrenheit = float(easygui.integerbox('type in a temperature in fahrenheit:'))
celsius = (fahrenheit - 32)*5/9

easygui.msgbox('that is '+str(celsius)+' degrees celsius')


#%% 2

import easygui

easygui.msgbox('这个程序可以形成一个及新地址')
en1 = easygui.enterbox('请输入您的姓名：')
en2 = easygui.enterbox('请输入您的街道：')
en3 = easygui.enterbox('请输入您的城市和省：')
en4 = easygui.enterbox('请输入您的邮政编码：')

easygui.msgbox('您的寄信地址是：\n'+ str(en1)+'\n'+str(en2)+'\n'+str(en3)+'\n'+str(en4))


#%% PS:章节重要程序 使用easygui的猜数字游戏

import random
import easygui

secret = random.randint(1, 99)
guess = 0
tries = 0

easygui.msgbox('从1-99个数字中，使用6次机会猜中给出的数字')

while guess != secret and tries < 6:
    guess = easygui.integerbox('请输入您猜的整数')
    if not guess:
        break
    if guess < secret:
        easygui.msgbox(str(guess)+'太小了，再猜')
    elif guess > secret:
        easygui.msgbox(str(guess)+'太大了，再猜')
    tries += 1

if guess == secret:
    easygui.msgbox('恭喜，你猜中了')
else:
    easygui.msgbox('抱歉，你的次数用完了')
























