# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/8 17:29
# File   : exp12.py
# IDE    : PyCharm

#判断用户输入的年份是否为闰年：

year = int(input('请输入一个年份：'))
if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print('{0}是闰年！'.format(year))
else:
    print('{0}不是闰年！'.format(year))
