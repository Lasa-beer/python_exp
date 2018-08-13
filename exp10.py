# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/8 10:26
# File   : exp10.py
# IDE    : PyCharm

#自定义一个函数来判断字符串是否为数字

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass
    return False


print(is_number('boo'))
