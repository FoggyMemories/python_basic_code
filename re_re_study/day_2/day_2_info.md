# day 2

---

## Python布尔

* 布尔标识两值之一:True或者False

### 布尔值

* 计算 Python 中的任何表达式时,会获得两个返回值: True 或 False。

> - 实例:
> ```python 
> print(8 > 7) # True
> print(8 == 7) # False
> print(8 < 7) # False
> ```

* 当在 if 语句中运行条件时，Python 返回 True 或 False：

> - 实例:
> ```python
> a = 200
> b = 33
> 
> if b > a:
>   print("b is greater than a")
> else:
>   print("b is not greater than a")
> ```

### 评估值和变量

* bool() 函数可让您评估任何值，并为您返回 True 或 False。
* 字符串：在 Python 中，任何非空字符串都会被评估为 True。只有空字符串 "" 才会被评估为 False。
* 数字：在 Python 中，任何非零数字都会被评估为 True。只有数字 0（包括 0.0 等）会被评估为 False。
* 除空列表外，任何列表、元组、集合和字典均为 True。

实际上，除空值（例如 ()、[]、{}、""、数字 0 和值 None）外，没有多少值会被评估为 False。当然，值 False 的计算结果为 False。

> - 实例:评估字符串和数字
> ```python
> print(bool("Hello")) # True
> print(bool(10)) # True
> print(bool(["apple", "cherry", "banana"])) # True
> ```

-
	* 在这种情况下，一个值或对象的计算结果为 False，即如果对象由带有 __len__ 函数的类生成的，且该函数返回 0 或 False：

> - 实例:
> ```python
> class myclass():
>   def __len__(self):
>     return 0
> 
> myobj = myclass()
> print(bool(myobj)) # False
> ```

### 函数可返回布尔

* Python 还有很多返回布尔值的内置函数，例如 isinstance() 函数，该函数可用于确定对象是否具有某种数据类型：

> - 实例:检查对象是否是整数:
> ```python
> x = 200
> print(isinstance(x, int)) # True
> ```
 
---

## Python运算符

Python 在以下组中划分运算符：

* 算术运算符
* 赋值运算符
* 比较运算符
* 逻辑运算符
* 身份运算符
* 成员运算符
* 位运算符

### Python 算术运算符

* 算术运算符与数值一起使用来执行常见的数学运算：

| 运算符 |     名称     | 实例      |
|:---:|:----------:|:--------|
|  +  |     加      | x+y     |
|  -  |     减	     | x - y	  |
|  *  |     乘	     | x * y	  |
|  /  |     除	     | x / y	  |
|  %  |     取模     | 	x % y	 |
| **  |     幂	     | x ** y	 |
| //  | 	地板除（取整除）	 | x // y  |

### Python赋值运算符

* 赋值运算符用于变量赋值:

| 运算符   | 实例       | 等同于          |
|-------|----------|--------------|
| +=	   | x += 3	  | x = x + 3	   |
| -=	   | x -= 3	  | x = x - 3	   |
| *=	   | x *= 3	  | x = x * 3	   |
| /=	   | x /= 3	  | x = x / 3	   |
| %=	   | x %= 3	  | x = x % 3	   |
| //=	  | x //= 3	 | x = x // 3	  |
| **=	  | x **= 3	 | x = x ** 3	  |
| &=	   | x &= 3	  | x = x & 3	   |
| \| =	 | x \|= 3  | 	x = x \| 3	 |
| ^=	   | x ^= 3	  | x = x ^ 3	   |
| \>>=	 | x >>= 3	 | x = x >> 3	  |
| <<=	  | x <<= 3	 | x = x << 3   |

### Python比较运算符

* 比较运算符用于比较两个值：

| 运算符 | 名称    | 实例     |
|-----|-------|--------|
| ==  | 等于    | x == y |
| !=  | 不等于   | x != y |
| \>  | 大于    | x > y  |
| <   | 小于    | x < y  |
| \>= | 大于或等于 | x >    |
| <=  | 小于或等于 | x <= y |

### Python 逻辑运算符

* 逻辑运算符用于组合条件语句：

| 运算符	 | 描述                        | 	实例	                   |
|------|---------------------------|------------------------|
| and	 | 如果两个语句都为真，则返回 True。	      | x > 3 and x < 10	      |
| or   | 	如果其中一个语句为真，则返回 True。     | 	x > 3 or x < 4	       |
| not	 | 反转结果，如果结果为 true，则返回 False | 	not(x > 3 and x < 10) |

### Python 身份运算符

* 身份运算符用于比较对象，不是比较它们是否相等，但如果它们实际上是同一个对象，则具有相同的内存位置：

| 运算符	    | 描述	                      | 实例         |
|---------|--------------------------|------------|
| is	     | 如果两个变量是同一个对象，则返回 true。	  | x is y	    |
| is not	 | 如果两个变量不是同一个对象，则返回 true。	 | x is not y |

### Python 成员运算符

* 成员资格运算符用于测试序列是否在对象中出现：

| 运算符	    | 描述	                         | 实例	        |
|---------|-----------------------------|------------|
| in	     | 如果对象中存在具有指定值的序列，则返回 True。   | 	x in y    |
| not in	 | 如果对象中不存在具有指定值的序列，则返回 True。	 | x not in y |

### Python 位运算符

* 位运算符用于比较（二进制）数字：

| 运算符	 | 描述                    | 	实例                          |
|------|-----------------------|------------------------------|
| &	   | AND	                  | 如果两个位均为 1，则将每个位设为 1。         |
| \| 	 | OR	                   | 如果两位中的一位为 1，则将每个位设为 1。       |
| ^	   | XOR	                  | 如果两个位中只有一位为 1，则将每个位设为 1。     |
| ~	   | NOT	                  | 反转所有位。                       |
| <<	  | Zero fill left shift	 | 通过从右侧推入零来向左移动，推掉最左边的位。       |
| \>>	 | Signed right shift	   | 通过从左侧推入最左边的位的副本向右移动，推掉最右边的位。 |

---

## Python列表

Python 集合（数组）  
Python 编程语言中有四种集合数据类型：

* 列表（List）是一种有序和可更改的集合。允许重复的成员。
* 元组（Tuple）是一种有序且不可更改的集合。允许重复的成员。
* 集合（Set）是一个无序和无索引的集合。没有重复的成员。
* 词典（Dictionary）是一个无序，可变和有索引的集合。没有重复的成员。

### 列表

* 列表是一个有序且可更改的集合。在 Python 中，列表用方括号编写。

> - 实例:创建列表:
> ```python
> thislist = ["apple", "banana", "cherry"]
> print(thislist) # ['apple', 'banana', 'cherry']
> ```

#### 项目访问

* 可以通过引用索引号来访问列表项：

> - 实例:通过引用索引号来访问列表项
> ```python
> thislist = ["apple", "banana", "cherry"]
> print(thislist[1]) # banana
> ```

#### 负的索引

* 负索引表示从末尾开始，-1 表示最后一个项目，-2 表示倒数第二个项目，依此类推。

> - 实例:打印列表的最后一项
> ```python
> thislist = ["apple", "banana", "cherry"]
> print(thislist[-1]) # cherry
> ```

#### 索引范围

* 通过指定范围的起点和终点来指定索引范围。
* 指定范围后，返回值将是包含指定项目的新列表。

> - 实例:返回第三、第四、第五项
> ```python
> thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
> print(thislist[2:5]) # ['cherry', 'orange', 'kiwi']
> ```

*
	* 负的索引范围同理

#### 更改项目值

* 更改特定项目的值，引用索引号

> - 实例:更改第二项:
> ```python
> thislist = ["apple", "banana", "cherry"]
> thislist[1] = "mango"
> print(thislist) # ['apple', 'mango', 'cherry']
> ```

#### 遍历列表

* 使用 for 循环遍历列表项：

> - 实例:逐个打印列表中的所有项目
> ```python
> thislist = ["apple", "banana", "cherry"]
> for x in thislist:
>   print(x)
> # apple
> # banana
> # cherry
> ```

#### 检查项目是否存在

* 如需确定列表中是否存在指定的项，使用 in 关键字：

> - 实例:检查列表中是否存在 “apple”：
> ```python
> thislist = ["apple", "banana", "cherry"]
> if "apple" in thislist:
>   print("Yes, 'apple' is in the fruits list")
> 
> # Yes, 'apple' is in the fruits list
> ```

#### 列表长度

* 如需确定列表中有多少项，使用 len()方法：

> - 实例:打印列表中的项目数:
> ```python
> thislist = ["apple", "banana", "cherry"]
> print(len(thislist)) # 3
> ```

#### 添加项目

* 如需将项目添加到列表的末尾，使用 append() 方法：

> - 实例:使用 append() 方法追加项目:
> ```python
> thislist = ["apple", "banana", "cherry"]
> thislist.append("orange")
> print(thislist) # ['apple', 'banana', 'cherry', 'orange']
> ```

* 如需在指定的索引处添加项目，使用 insert() 方法：

> - 实例:插入项目作为第二个位置：
> ```python
> thislist = ["apple", "banana", "cherry"]
> thislist.insert(1, "orange")
> print(thislist) # ['apple', 'orange', 'banana', 'cherry']
> ```

#### 删除项目

* 删除指定项目

> - 实例:用remove() 方法删除指定的项目：
> ```python
> thislist = ["apple", "banana", "cherry"]
> thislist.remove("banana")
> print(thislist)
> ```

* 删除指定的索引

> - 实例:用 pop() 方法删除指定的索引（如果未指定索引，则删除最后一项）：
> ```python
> thislist = ["apple", "banana", "cherry"]
> thislist.pop()
> print(thislist) # ['apple', 'banana']
> ```

* 删除指定的索引

> - 实例:用 del 关键字删除指定的索引：
> ```python
> thislist = ["apple", "banana", "cherry"]
> del thislist[0]
> print(thislist) # ['banana', 'cherry']
> ```
> - 用 del 关键字删除完整的列表
> ```python
> thislist = ["apple", "banana", "cherry"]
> del thislist
> ```
> - 同样的,用clear()方法清空列表:
> ```python
> thislist = ["apple", "banana", "cherry"]
> thislist.clear()
> print(thislist)
> ```

#### 复制列表

* 只能通过键入 list2 = list1 来复制列表，因为：list2 将只是对 list1 的引用，list1 中所做的更改也将自动在 list2 中进行。
* 有一些方法可以进行复制，一种方法是使用内置的 List 方法 copy()。

> - 实例:使用 copy() 方法来复制列表:
> ```python
> thislist = ["apple", "banana", "cherry"]
> mylist = thislist.copy()
> print(mylist)
> ```

* 制作副本的另一种方法是使用内建的方法 list()。

> - 实例:使用 list() 方法复制列表:
> ```python
> thislist = ["apple", "banana", "cherry"]
> mylist = list(thislist)
> print(mylist)
> ```

#### 合并两个列表

* 在 Python 中，有几种方法可以连接或串联两个或多个列表。
* 最简单的方法之一是使用 + 运算符。

> - 实例:合并两个列表:
> ```python
> list1 = ["a", "b" , "c"]
> list2 = [1, 2, 3]
> 
> list3 = list1 + list2
> print(list3) # ['a', 'b', 'c', 1, 2, 3]
> ```

* 使用 extend() 方法，将一个列表中的元素添加到另一列表中：

> - 实例:使用 extend() 方法将 list2 添加到 list1 的末尾：
> ```python
> list1 = ["a", "b" , "c"]
> list2 = [1, 2, 3]
> 
> list1.extend(list2)
> print(list1)
> ```

## 列表方法

| 方法        | 描述                         |
|-----------|----------------------------|
| append()	 | 在列表的末尾添加一个元素               |
| clear()	  | 删除列表中的所有元素                 |
| copy()	   | 返回列表的副本                    |
| count()	  | 返回具有指定值的元素数量。              |
| extend()	 | 将列表元素（或任何可迭代的元素）添加到当前列表的末尾 |
| index()	  | 返回具有指定值的第一个元素的索引           |
| insert()	 | 在指定位置添加元素                  |
| pop()	    | 删除指定位置的元素                  |
| remove()	 | 删除具有指定值的项目                 |
| reverse() | 	颠倒列表的顺序                   |
| sort()	   | 对列表进行排序                    |
