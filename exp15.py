# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/8 17:46
# File   : exp15.py
# IDE    : PyCharm

# 质数判断
while True:
    try:
        num = int(input('请输入一个数字：'))
    except ValueError:
        print('您输入的数字不是整数：')
        continue
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print('{0}不是质数。'.format(num))
                break
        else:
            print('{0}是质数。'.format(num))
    else:
        print('{0}不是质数。'.format(num))



