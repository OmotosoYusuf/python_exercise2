
Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> range(1,4)
range(1, 4)
>>> print(range(1,4))
range(1, 4)
>>> for number in range(1,4)
SyntaxError: invalid syntax
>>> for number in range(1,4):
	print(number)

	
1
2
3
>>> number = [1,2,3,4]
>>> print(number[1:4])
[2, 3, 4]
>>> number.append(5,6)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    number.append(5,6)
TypeError: append() takes exactly one argument (2 given)
>>> number.append(5)
>>> number
[1, 2, 3, 4, 5]
>>> print(number[1:4])
[2, 3, 4]
>>> print(number[0:4])
[1, 2, 3, 4]
>>> for i in number[0:4]:
	print(i)

	
1
2
3
4
>>> for i in range(0,4):
	print(i)

	
0
1
2
3
>>> for i in range(-1,4):
	print(i)

	
-1
0
1
2
3
>>> number = ['one', 'two', 'three']
>>> number2 = number.append('four')
>>> number2
>>> 
>>> number.append('four')
>>> number
['one', 'two', 'three', 'four', 'four']
>>> number.pop('four')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    number.pop('four')
TypeError: 'str' object cannot be interpreted as an integer
>>> number.remove('four')
>>> number
['one', 'two', 'three', 'four']
>>> number.del('three')
SyntaxError: invalid syntax
>>> studAge = {'Bayo':25, 'Sayo':23, 'Tayo':26}
>>> studAge.items()
dict_items([('Sayo', 23), ('Tayo', 26), ('Bayo', 25)])
>>> studAge.setdefault('Dayo', 'Layo')
'Layo'
>>> studAge.items()
dict_items([('Sayo', 23), ('Dayo', 'Layo'), ('Tayo', 26), ('Bayo', 25)])
>>> studAge.values()
dict_values([23, 'Layo', 26, 25])
>>> 'surprise'






