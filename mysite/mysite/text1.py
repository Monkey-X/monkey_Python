"""
使用变量保存数据并进行算术计算
 
 Version：0.1
 Author：xlc
"""
import math
a =321
b = 123

print(a+b)
print(a-b)
print(a*b)
print(a/b)
#相除取整数
print(a//b)
#相除取余数
print(a%b)
#取几次方
print(a**b)

print("----------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
c = int(input('c = '))#将输入的数字字符串转为整数
d = int(input('d = '))
print('%d+%d=%d' % (c,d,c+d))
print(type(c))

print("-----------------------------------------------------------------------------------------------------------")
"""
将华氏温度转变为摄氏温度
F= 1.8C +32
"""

f= float(input('请输入华氏温度：'))
c= (f-32) / 1.8
print('%f华氏度 = %f摄氏度' % (f,c))


print("----------------------------------------------------")

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius

area = math.pi * radius * radius

print('周长:%f' % perimeter)
print('面积:%f' % area)
