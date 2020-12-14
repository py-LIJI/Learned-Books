# -*- coding: utf-8 -*-
"""
第二章实战
"""

#%% 1

print("欢迎使用XXX充值业务，请输入充值金额：")    #输出提示信息
money=int(input( ))    #输入充值金额，加不加空格都行
print("充值成功，您本次充值"+str(money)+"元")     #输出金额


#%% 2

print("""
       * * * * *
      *          *
     *  @       @  *
     *             *
      *     @     *
        *        *
         * * * *
         """)


#%% 3

father=float(input("请输入父亲的身高：\n"))
mather=float(input("请输入母亲的身高：\n"))
son=(father+mather)*0.54
print("预测儿子的身高为："+str(son))


#%% 4

N=int(input("请输入当天行走的步数！：\n"))
K=N*28
Kk=float(K/1000)
print("今天共消耗卡路里："+str(K)+"(即"+str(Kk)+"千卡）")

