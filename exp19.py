# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/8 18:21
# File   : exp19.py
# IDE    : PyCharm

#斐波那契数列
# 获取用户输入的数据
nterms = int(input('你需要几项?'))

n1 = 0
n2 = 1
count = 2
if nterms <= 0:
    print('请输入一个正整数：')
elif nterms == 1:
    print('斐波那契数列：')
    print(n1)
else:
    print('斐波那契数列：')
    print(n1,',',n2,end = ', ')
    while count < nterms:
        nth = n1 + n2
        print(nth ,end = ', ')
        n1 = n2
        n2 = nth
        count += 1     # count 计算项数