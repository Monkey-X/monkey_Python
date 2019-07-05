"""
操作字符串
"""

def main():
    str1 = 'hello world!'

    print(len(str1))#计算字符串的长度
    print(str1.capitalize())# 首字母大写Hello,World!
    print(str1.upper())#字符串变大写后的拷贝

    print(str1.center(50,'*'))#字符串在指定的宽度居中，并在两侧填充指定符号
    print(str1.rjust(50,"_"))#在指定宽度中靠右，左侧填充指定的字符

    str2 = 'abc123456'
    print(str2.isalpha())#是否以字母构成
    print(str2.isdigit())#是否数字构成
    print(str2.isalnum())#是否以字母和数字构成
    print(str2.strip())#修剪字符串两侧的空格


def listmain():
    list1 =[1,2,3,4,5,6]
    list2 = ['hello','world']*5#复制列表中的数据
    list2.append(200)#在列表最后添加数据
    list1 +=[100,200]
    list1.insert(1,400)#在指定的位子插入数据
    print(list1)
    print(list2)

#列表的切片操作
def main2():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits +=['pitaya', 'pear', 'mango']
    for fruit in fruits:
        print(fruit.title(),end=' ')#元素首字母大写
    print()

    print('-------列表切片-------')
    fruit2 = fruits[1:4]#包左不包右
    fruit3 = fruits[:]#复制列表
    print(fruit3)
    print(fruit2)

    fruit4 = fruits[-3:-1]
    print(fruit4)

    fruit5 = fruits[::-1]
    print(fruit5)
    print("=======================================")
    print("=======================================")

def main3():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)#根据默认的字母表排序,都是字符串
    list3 = sorted(list1,reverse=True)#排序翻转
    list4 = sorted(list1,key=len)#通过key指定排序的规则参数
    print(list2)
    print(list3)
    print(list4)

#列表的生成式语法来创建列表
def main4():
    f= [x for x in range(1,10)]
    print(f)


if __name__ == "__main__":
    main()
    listmain()
    main2()
    main3()
    main4()