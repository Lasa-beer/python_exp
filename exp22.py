# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/9 8:25
# File   : exp22.py
# IDE    : PyCharm

# python ASCII 码与字符相互转化

c = input('请数输入一个字符：')

# 用户输入 ASSCII 码为,,并将输入的数字转化为整型
a = int(input('请输入一个ASCII 码：'))

print(c + '的ASCII 码为：',ord(c))
print(a ,'对应的字符为：',chr(a))