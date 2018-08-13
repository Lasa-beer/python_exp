# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/8 9:43
# File   : exp4.py
# IDE    : PyCharm

# 二次方程 ax**2 + bx +c = 0
#a、b、c、用户提供，为实数 a！= 0

import cmath

a = float(input('请输入a:'))
b = float(input('请输入b：'))
c = float(input('请输入c:'))

# 计算
d = b**2 - 4*a*c
if d<0:
    print('该方程没有实数解')
elif d == 0:
    print('该方程有两个相等的实数解为：',(-b)/(2*a))
else:
    sol1 = (-b + cmath.sqrt(d))/(2*a)
    sol2 = (-b - cmath.sqrt(d))/(2*a)

    print('该方程有两个实数解分别为：{0}和{1}'.format(sol1,sol2))

