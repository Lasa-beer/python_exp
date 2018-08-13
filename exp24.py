# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/9 8:39
# File   : exp24.py
# IDE    : PyCharm

# python 最小公倍数算法

def lcm(x,y):   # 获取两个数的最小公倍数
    # 获取两个数的最大数
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0 and greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm
num1 = int(input('请输入第一个数字：'))
num2 = int(input('请输入第二个数字：'))

print('{0}和{1}的最小公倍数为：{2}'.format(num1,num2,lcm(num1,num2)))
