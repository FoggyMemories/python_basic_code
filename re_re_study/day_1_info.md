# day 1

---

## 指示代码块

Python使用缩进来指示代码块。
空格数取决于习惯，但是至少需要一个，且在同意代码块中必须使用相同数量的空格，否则Python会出错。
---

## Python中的注释

注释以（#）开头
或者以（"""）包围注释的代码或文字
---

## 创建变量

变量是存放数据值的容器
与其他编程语言不同的是,Python是弱类型,没有声明变量的命令.
首次为其赋值时,才会创建变量.

* 变量不需要使用任何特定类型声明,甚至可以在设置后更改其类型.  
  字符串变量可以使用单引号或者双引号进行声明

> - Python 变量命名规则：  
    * 变量名必须以字母或下划线字符开头  
    * 变量名称不能以数字开头  
    * 变量名只能包含字母数字字符和下划线（A-z、0-9 和 _）  
    * 变量名称区分大小写（age、Age 和 AGE 是三个不同的变量）

Python允许在同一行为多个变量进行赋值:
> - x, y, z = "Orange", "Banana", "Cherry"

Python可以在一行中为多个变量分配相同的值：
> - x = y = z = "Orange"
---

## 全局变量

使用global关键字,则该变量属于全局范围:

```
  def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

---

## Python数据类型

Python默认拥有一下内置数据类型:

|   类型    |              文本              |
|:-------:|:----------------------------:|
|  文本类型:  |             str              |
| 数值类型：	  |     int, float, complex      |
| 序列类型：	  |      list, tuple, range      |
| 映射类型：	  |             dict             |
| 集合类型：	  |        set, frozenset        |
| 布尔类型：	  |             bool             |
| 二进制类型：	 | bytes, bytearray, memoryview |

使用type()函数获取对任何对象的数据类型

```python
    x = 1
print(type(x))
```

---

## Python数字

Python 中有三种数字类型：

* int
* float
* complex

为变量赋值时,将创建数值类型的变量:
> > - 实例:
>```python
>    x = 10   # int
>    y = 6.3  # float
>    z = 2j   # complex
>```

* Int或整数是完整的数字，正数或负数，没有小数，长度不限。
* Float浮动或“浮点数”是包含小数的正数或负数。  
  浮点数也可以是带有“e”的科学数字，表示 10 的幂。
* Complex复数用 "j" 作为虚部编写：

```python
    x = 10  # int
y = 6.3  # float
z = 1j  # complex

# 把整数转换为浮点数

a = float(x)

# 把浮点数转换为整数

b = int(y)

# 把整数转换为复数：

c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```

> - 运行结果:  
    10.0  
    6  
    (10+0j)

### 随机数

Python中没有random()函数来创建随机数,但是Python有一个名为random的内置模块,可用于生成随机数:

> > - 实例:  
      > > 导入random模块,并显示1到9之间的随机数:
>```python
>    import random
>    print(random.randrange(1,10))
>```
> - 运行结果:  
    > 5

---

## Python Casting

指定变量类型  
Python是一门面向对象的语言,因此它使用类来定义数据类型,包括其原始类型.  
因此,使用构造函数在python中的转换:

* int() - 用整数字面量、浮点字面量构造整数（通过对数进行下舍入），或者用表示完整数字的字符串字面量
* float() - 用整数字面量、浮点字面量，或字符串字面量构造浮点数（提供表示浮点数或整数的字符串）
* str() - 用各种数据类型构造字符串，包括字符串，整数字面量和浮点字面量

> > - 例如:
> - 整数
> ```python
>    x = int(1)   # x 将是 1
>    y = int(2.5) # y 将是 2
>    z = int("3") # z 将是 3
> ```
> - 浮点数
> ```python
>   x = float(1)     # x 将是 1.0
>   y = float(2.5)   # y 将是 2.5
>   z = float("3")   # z 将是 3.0
>   w = float("4.6")# w 将是 4.6
> ```
> - 字符串
> ```python
>   x = str("S2") # x 将是 'S2'
>   y = str(3)    # y 将是 '3'
>   z = str(4.0)  # z 将是 '4.0'
> ```
---

## Python字符串

### 字符串字面量

python 中的字符串字面量由单引号或双引号括起。  
通过使用变量名称后跟等号和字符串，可以把字符串赋值给变量：
> - 实例:
> ```python
>     a = "Hello"
>     print(a)
> ```

### 多行字符串

您可以使用三个引号(或三个单引号)将多行字符串赋值给变量：
> - 实例:
> ```python
>   """test"""  
>   '''test'''
> ```

### 字符串是数组

Python 中的字符串是表示 unicode 字符的字节数组。  
Python 没有字符数据类型，单个字符就是长度为 1 的字符串。  
方括号可用于访问字符串的元素。
> - 实例:
> ```python
>   a = "Hello, World!"
>   print(a[1])
> ```
> - 运行结果:  
    > e

### 裁切

使用裁切语法返回一定范围的字符。  
指定开始索引和结束索引，以冒号分隔，以返回字符串的一部分。
> - 实例:获取从位置 2 到位置 5（不包括）的字符：
> ```python
>   b = "Hello, World!"
>   print(b[2:5])
> ```
> - 运行结果:  
    > llo

> - 实例 :获取从位置 5 到位置 1 的字符，从字符串末尾开始计数：
> ```python
>     b = "Hello, World!"
>     print(b[-5:-2])
> ```
> - 运行结果:  
    > orl

### 字符串长度

如需获取字符串的长度，使用len()函数。  
len()函数返回字符串的长度

### 字符串方法

* strip()方法删除开头和结尾的空白字符：

```python
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"
```

* lower() 返回小写的字符串：

```python
a = "Hello, World!"
print(a.lower())  # hello, world!
```

* upper() 方法返回大写的字符串：

```python
a = "Hello, World!"
print(a.upper())  # HELLO, WORLD!
```

* replace() 用另一段字符串来替换字符串：

```python
a = "Hello, World!"
print(a.replace("World", "Kitty"))  # Hello, Kitty!
```

* split() 方法在找到分隔符的实例时将字符串拆分为子字符串：

```python
a = "Hello, World!"
print(a.split(","))  # ['Hello', ' World!']
```

### 检查字符串

如需检查字符串中是否存在特定短语或字符，我们可以使用 in 或 not in 关键字。

* 检查以下文本中是否存在短语 "ina"：

```python
txt = "China is a great country"
x = "ina" in txt
print(x)  # True
```

* 检查以下文本中是否没有短语 "ain"：

```python
txt = "China is a great country"
x = "ain" not in txt
print(x)  # True
```

### 字符串级联（串联）

如需串联或组合两个字符串，可以使用 + 运算符。

* 将变量 a 与变量 b 合并到变量 c 中：

```python
a = "Hello"
b = "World"
c = a + b
print(c)  # HelloWorld
```

* 在它们之间添加一个空格：

```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # Hello World
```

> * 在python中,不能直接将字符串与数字进行组合
> ```python
> age = 63
> txt = "My name is Bill, I am " + age
> print(txt) # 运行报错(TypeError)
> ```

format() 方法接受传递的参数，格式化它们，并将它们放在占位符 {} 所在的字符串中：

* 使用 format() 方法将数字插入字符串：

```python
age = 63
txt = "My name is Bill, and I am {}"
print(txt.format(age))  # My name is Bill, and I am 63
```

* format() 方法接受不限数量的参数，并放在各自的占位符中：

```python
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))  # I want 3 pieces of item 567 for 49.95 dollars.
```

* 可以使用索引号 {0} 来确保参数被放在正确的占位符中：

```python
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))  # I want to pay 49.95 dollars for 3 pieces of item 567.
```

### 字符串方法

* 注释：所有字符串方法都返回新值。它们不会更改原始字符串。

| 方法              | 描述                           |
|:----------------|:-----------------------------|
| capitalize()	   | 把首字符转换为大写。                   |
| casefold()      | 	把字符串转换为小写。                  |
| center()        | 	返回居中的字符串。                   |
| count()	        | 返回指定值在字符串中出现的次数。             |
| encode()        | 	返回字符串的编码版本。                 |
| endswith()      | 	如果字符串以指定值结尾，则返回 true。       |
| expandtabs()    | 	设置字符串的 tab 尺寸。              |
| find()	         | 在字符串中搜索指定的值并返回它被找到的位置。       |
| format()        | 	格式化字符串中的指定值。                |
| format_map()    | 	格式化字符串中的指定值。                |
| index()	        | 在字符串中搜索指定的值并返回它被找到的位置。       |
| isalnum()       | 	如果字符串中的所有字符都是字母数字，则返回 True。 |
| isalpha()	      | 如果字符串中的所有字符都在字母表中，则返回 True。  |
| isdecimal()	    | 如果字符串中的所有字符都是小数，则返回 True。    |
| isdigit()	      | 如果字符串中的所有字符都是数字，则返回 True。    |
| isidentifier()	 | 如果字符串是标识符，则返回 True。          |
| islower()	      | 如果字符串中的所有字符都是小写，则返回 True。    |
| isnumeric()     | 	如果字符串中的所有字符都是数，则返回 True。    |
| isprintable()	  | 如果字符串中的所有字符都是可打印的，则返回 True。  |
| isspace()	      | 如果字符串中的所有字符都是空白字符，则返回 True。  |
| istitle()       | 	如果字符串遵循标题规则，则返回 True。       |
| isupper()	      | 如果字符串中的所有字符都是大写，则返回 True。    |
| join()          | 	把可迭代对象的元素连接到字符串的末尾。         |
| ljust()	        | 返回字符串的左对齐版本。                 |
| lower()	        | 把字符串转换为小写。                   |
| lstrip()        | 	返回字符串的左修剪版本。                |
| maketrans()     | 	返回在转换中使用的转换表。               |
| partition()	    | 返回元组，其中的字符串被分为三部分。           |
| replace()	      | 返回字符串，其中指定的值被替换为指定的值。        |
| rfind()	        | 在字符串中搜索指定的值，并返回它被找到的最后位置。    |
| rindex()        | 	在字符串中搜索指定的值，并返回它被找到的最后位置。   |
| rjust()         | 	返回字符串的右对齐版本。                |
| rpartition()    | 	返回元组，其中字符串分为三部分。            |
| rsplit()        | 	在指定的分隔符处拆分字符串，并返回列表。        |
| rstrip()	       | 返回字符串的右边修剪版本。                |
| split()	        | 在指定的分隔符处拆分字符串，并返回列表。         |
| splitlines()    | 	在换行符处拆分字符串并返回列表。            |
| startswith()    | 	如果以指定值开头的字符串，则返回 true。      |
| strip()	        | 返回字符串的剪裁版本。                  |
| swapcase()      | 	切换大小写，小写成为大写，反之亦然。          |
| title()         | 	把每个单词的首字符转换为大写。             |
| translate()     | 	返回被转换的字符串。                  |
| upper()	        | 把字符串转换为大写。                   |
| zfill()	        | 在字符串的开头填充指定数量的 0 值。          |