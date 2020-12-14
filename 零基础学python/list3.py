# -*- coding: utf-8 -*-
"""
第三章实战
"""


#%% 1

print("""
查询能量请输入能量来源！退出程序请输入0
能量来源如下：
生活缴费，行走捐，共享单车，线下支付，网络购票""")
cross=str(input( ))
if cross=="生活缴费":
    print(str(50)+"g")
elif cross=="行走捐":
    print(str(200)+"g")
elif cross=="共享单车":
    print(str(250)+"g")
elif cross=="线下支付":
    print(str(300)+"g")
elif cross=="网络购票":
    print(str(350)+"g")
else:
    print("已退出！")
    

#%% 2

import random                #加载random随机函数模组
R=random.randint(1,10)       #生成1-10之间的随机数
print(R)
N=int(input("请输入1~10之间的任意一个数："))
if N>=1 and N<=10:
    if N==R:
        print("恭喜你，你赢了，猜中的数字是："+str(N))
    elif N>=1 and N<R:
        print("太小，请重新输入：")
    elif N<=10 and N>R:
        print("太大，请重新输入！")
elif N==-1:
     print("已退出程序！")
else:
     print("抱歉，您输入的数字不合规范！")


#%% 3

print("""
欢迎回来，请开始游戏······
请输入（中心，音乐块，微信支付块）；""")
string=str(input("请输入："))
if string=="中心":
    print("您的分数为："+str(32))
elif string=="音乐块":
    print("您的分数为："+str(30))
elif string=="微信支付块":
    print("您的分数为："+str(42))
else:
    pass


#%% 4

print("""
输入1：查询当前余额
输入2：查询当前剩余流量
输入3：查询当前剩余通话
输入0：退出自助查询系统""")
N=int(input( ))
if N==1:
    print("当前余额为："+str(999)+"元")
elif N==2:
    print("当前剩余流量为："+str(5)+"G")
elif N==3:
    print("当前剩余通话为："+str(189)+"分钟")
elif N==0:
    print("退出自助查询系统！")
else:
    print("抱歉，您输入的数字有误！")





