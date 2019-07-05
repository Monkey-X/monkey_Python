"""
循环结构 for-in循环  while循环
"""

"""
range(101) 可以产生0到100的整数序列
range(1,100) 产生1到99的整数序列
range(1,100,2)产生1到99的奇数数列，2是步长，数值的增量
"""
import random
from math import sqrt
sum = 0
for x in range(101):
    sum+=x
print(sum)

row = int(input('请输入行数：'))
for ii in range(row):
    for _ in range(ii+1):
        print('*',end='')
    print()

for ii in range(row):
    for jj in range(row):
        if jj < row -ii -1:
            print(' ',end="")
        else:
            print('*',end="")
    print()

#1~100之间的偶数和
sum1 = 0
for x in range(2,101,2):
    sum1+=x
print(sum1)

#输出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d' % (i,j,i*j),end='\t')
    print()

#正整数判断是否是一个素数
num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime = True
for x in range(2,end+1):
    if num % x ==0:
        is_prime = False
        break
if is_prime and num !=1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

#while循环

answer = random.randint(1,100)
counter = 0
while True:
    counter +=1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('答对了！！')
        break
print('你总共回答了%d次' % counter)
if counter >7:
    print("你的智商余额不足了")