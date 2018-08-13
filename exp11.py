# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/8 17:23
# File   : exp11.py
# IDE    : PyCharm

#判断是奇偶数

while True:
    try :
        num = int(input('请输入一个整数：'))
    except ValueError:
        print('输入的不是整数！')
        continue        #结束本次循环
    if (num % 2) == 0:
        print('{0}是偶数！'.format(num))
    else:
        print('{0}是奇数！'.format(num))



