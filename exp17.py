# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/8 18:07
# File   : exp17.py
# IDE    : PyCharm

# 阶乘实例

while True:
    try:
        num = int(input('请输入一个整数：'))
    except ValueError:
        print('你输入的不是整数')
    f = 1
    if num < 0:
        print('抱歉，负数没有阶乘！')
    elif num == 0:
        print('0 的阶乘为 1')
    else:
        for i in range(1,num+1):
            f = f * i
        print('{0}的阶乘为：{1}'.format(num,f))

