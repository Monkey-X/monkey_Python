"""
def 用来定义函数
"""
#求阶乘
def factorial(num):
    result =1
    for n in range(1,num+1):
        result *= n
    return result

#m = int(input('m='))
#n = int(input('n='))

#print(factorial(m))
print('-------')
#print(factorial(n))

"""
1.函数的参数可以有默认值
2.支持使用可变参数
"""
from random import randint

def roll_dice(n=2):
    total =0
    for _ in range(n):
        total += randint(1,6)
    return total
def add(a=0,b=0,c=0):
    return a+b+c


print(roll_dice())
print(roll_dice(3))
print(add())
print(add(1))
print(add(1,2))
print(add(a=100,c=50))

#可变函数
def add1(*args):
    total =0
    for val in args:
        total +=val
    return total 
print(add1())
print(add1(1,2,3))


##__name__是Python中一个隐含的变量它代表了模块的名字
#只有被Python解析器直接执行的模块的名字才是__main__
#模块中编写了执行了代码，可以将执行代码放在if条件中
if __name__ == '__main__':
    add1()