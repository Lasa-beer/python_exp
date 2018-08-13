# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/8 9:34
# File   : exp3.py
# IDE    : PyCharm

#python 平方根
#通过用户输入一个数字，并计算这个数字的平方根

# num = float(input('请输入一个数字：'))
# num_sqrt = num ** 0.5
# print('数字{0}的平方根为：{1}'.format(num,num_sqrt))
# print('%0.2f的平方根为%0.5f'%(num,num_sqrt))

import cmath
num = float(input('请输入一个数字：'))
num_sqrt = cmath.sqrt(num)

print('数字{0}的平方根为：{1}'.format(num,num_sqrt))