# -*- coding: utf-8 -*-
"""
第12章
"""


#%% 测试题
# 1： .append()方法添加一个元素, .extend()方法添加多个元素, .insert()方法插入一个元素
# 2： .remove()知道元素删除, del知道元素索引删除, .pop()知道索引删除或默认删除最后一个
# 3： 建立列表副本，使用.sort()方法   直接使用sorted()函数
# 4： in方法
# 5： .index()方法
# 6： 类似列表，但内部元素不可改变
# 7： 列表嵌套列表， 双重for循环
# 8： 双索引
# 9： 键值对的集合
# 10： 通过键
# 11： dict_name['键名']


#%% 动手试一试 1

names=[]
print('Enter 5 names')
for i in range(5):
    names.append(str(input()))

print('The names are',names)


#%% 2

names=[]
print('Enter 5 names')
for i in range(5):
    names.append(str(input()))
sort_names=sorted(names)
print('The names are',names)
print('The names are(sort)',sort_names)


#%% 3

names=[]
print('Enter 5 names')
for i in range(5):
    names.append(str(input()))

print('The third name you entered is:',names[2])


#%% 4

names=[]
print('Enter 5 names')
for i in range(5):
    names.append(str(input()))
print('The names are',names)

a=int(input('Replace one name. Which one?(1-5):'))
new=str(input('New name:'))
names[a-1]=new
print('The names are',names)


#%% 5

dictionary={}
key=[]
value=[]
option1=str(input('Add or look up a word (a/l)?'))
if option1=='a':
    key.append(str(input('Type the word:')))
    value.append(str(input('Type the definition:')))
    dictionary=dict(zip(key,value))
    print('Word added!')
    option2=str(input('Add or look up a word (a/l)?'))
    if option2=='l':
        new_key=str(input('Type the word:'))
        if new_key=='computer':
            print(dictionary.get(new_key))
        else:
            print('That word isn’t in the dictionary yet')
    else:
        print('Add or look up a word is wrong')
else:
        print('Add or look up a word is wrong') 






































