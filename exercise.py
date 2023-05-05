row1='hello'
row2='world'
print(row1[:])
print(row1[1:])
print(row1[:1])
print(row1[2:3])
print(row1[0]+'ello')
print("hello,world!\n xiaozhang")
print(row1+row2)
if( "H" in row1) :
    print("H 在变量 row1 中")
else :
    print("H 不在变量 row1 中")

print (r'\n')
print (R'\n')
row1 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print( row1[0] )
print( row1[1] )
print( row1[2] )
print( row1[-1] )
print( row1[-2] )
print( row1[-3] )
for x in [1, 2, 3]: print(x, end=" ")
#增加#
list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)
#删除#
list = ['Google', 'Runoob', 1997, 2000]
del list[2]
print ("删除第三个元素 : ", list)
#拼接#
squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]
print(squares)
#嵌套#
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

tuple2 = ('5', '4', '8')
print(min(tuple2))
print(max(tuple2))
tuple3=tuple(list1)
print(tuple3)

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
print ("tinydict['Name']: ", tinydict['Name'])
print ("tinydict['Age']: ", tinydict['Age'])

dict1={'number':1,'name':'小张'}
print(dict1['name'])
dict1['age']=32
dict1['home']='南阳'
print(dict1['age'])
print(dict1['home'])
print(dict1)
del dict1['age']
print(dict1)

print(str(tinydict))
print(type(tinydict))
#集合（set）是一个无序的不重复元素序列#
jihe1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(jihe1)  
print ('orange'in jihe1)
print ('tomato'in jihe1)

a = set('abracadabra')
b = set('alacazam')
print(a-b)
print(a|b)  
print(a&b)
print(a^b) 
a = {x for x in 'abracadabra' if x not in 'rd'}
print(a)

n = 100
 
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,sum))


for i in range(5):
    print(i)

def hello():
    print("hello,world")
hello()