"""
Python 的分支结构
使用缩进的方式来设置代码的层次结构
"""
from random import randint

username = input('请输入用户名：')
password = input('请输入口令：')

if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')

print('-------------------------------------')

x = float(input('x = '))
if x > 1:
    y = 3 * x -5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x +3
print("y = %f" % y)


print('-----------------------------------------')

value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f 厘米' % (value,value*2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value,value/2.54))
else:
    print('请输入有效的单位')

print('-----------------------------------------')

"""
获取随机数
"""
face = randint(1,6)
if face ==1:
    result='aaaa'
elif face ==2:
    result='bbbb'
elif face ==3:
    result = 'ccc'
else:
    result ='dddd'
print(face)

