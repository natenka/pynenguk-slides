## Корисні вбудовані функції

---
## Функція print

---
### Функція print

Функція print виводить усі елементи, розділяючи їх значенням sep, та
завершує виведення значенням end.
```
print(*items, sep=' ', end='\n', file=sys.stdout, flush=False)
```

---
### Функція print

Всі елементи, що передаються як аргументи, конвертуються в рядки:

```python
def f(a):
    return a


In [5]: print(1, 2, f, range(10))
1 2 <function f at 0xb4de926c> range(0, 10)
```


---
### sep

Параметр sep контролює те, який роздільник використовуватиметься між елементами.

За замовчуванням використовується пробіл:

```python
In [8]: print(1, 2, 3)
1 2 3
```

---
### sep

Можна змінити значення sep на будь-який інший рядок:

```python
In [9]: print(1, 2, 3, sep='|')
1|2|3

In [10]: print(1, 2, 3, sep='\n')
1
2
3

In [11]: print(1, 2, 3, sep='\n' + '-' * 10 + '\n')
1
----------
2
----------
3

```


---
### end

Параметр end контролює те, яке значення буде виведено після виведення
всіх елементів. За замовчуванням використовується символ нового рядка:

```python
In [19]: print(1, 2, 3)
1 2 3

```

Можна змінити значення end на будь-який інший рядок:
```python
In [20]: print(1, 2, 3, end='\n' + '-' * 10)
1 2 3
----------
```


---
### flush

За замовчуванням під час запису у файл або виведення на стандартний
потік виводу буферизується вивід. Параметр flush дозволяє вимкнути
буферизацію.


---
## Функція range

---
### Функція range

Функція range повертає незмінну послідовність чисел як об'єкт range.

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Параметри функції:

* start - з якого числа починається послідовність. За замовчуванням - 0
* stop - до якого числа продовжується послідовність чисел. Зазначене число не входить до діапазону
* step - з яким кроком ростуть числа. За замовчуванням 1

---
### Функція range

Функція range хранит только информацию о значениях start, stop и step и вычисляет значения по мере необходимости.
Это значит, что, независимо от размера диапазона, который описывает функция range, она всегда будет занимать фиксированный объем памяти.

---
### Функція range

Самый простой вариант range - передать только значение stop:
```python
In [1]: range(5)
Out[1]: range(0, 5)

In [2]: list(range(5))
Out[2]: [0, 1, 2, 3, 4]
```

---
### Функція range

Если передаются два аргумента, то первый используется как start, а второй - как stop:
```python
In [3]: list(range(1, 5))
Out[3]: [1, 2, 3, 4]
```

И, чтобы указать шаг последовательности, надо передать три аргумента:
```python
In [4]: list(range(0, 10, 2))
Out[4]: [0, 2, 4, 6, 8]

In [5]: list(range(0, 10, 3))
Out[5]: [0, 3, 6, 9]
```

---
### Функція range

С помощью range можно генерировать и убывающие последовательности чисел:
```python
In [6]: list(range(10, 0, -1))
Out[6]: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

In [7]: list(range(5, -1, -1))
Out[7]: [5, 4, 3, 2, 1, 0]
```

Для получения убывающей последовательности надо использовать отрицательный шаг и соответственно указать start - большим числом, а stop - меньшим.

В убывающей последовательности шаг тоже может быть разным:
```python
In [8]: list(range(10, 0, -2))
Out[8]: [10, 8, 6, 4, 2]
```

---
### Функція range

Функція поддерживает отрицательные значения start и stop:
```python
In [9]: list(range(-10, 0, 1))
Out[9]: [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

In [10]: list(range(0, -10, -1))
Out[10]: [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
```

---
### Функція range

Объект range поддерживает все [операции](https://docs.python.org/3.6/library/stdtypes.html#sequence-types-list-tuple-range), которые поддерживают последовательности в Python, кроме сложения и умножения.

Проверка, входит ли число в диапазон, который описывает range:
```python
In [11]: nums = range(5)

In [12]: nums
Out[12]: range(0, 5)

In [13]: 3 in nums
Out[13]: True

In [14]: 7 in nums
Out[14]: False
```

> Начиная с версии Python 3.2, эта проверка выполняется за постоянное время (O(1)).

---
### Функція range

Можно получить конкретный элемент диапазона:
```python
In [15]: nums = range(5)

In [16]: nums[0]
Out[16]: 0

In [17]: nums[-1]
Out[17]: 4
```

---
### Функція range

Range поддерживает срезы:
```python
In [18]: nums = range(5)

In [19]: nums[1:]
Out[19]: range(1, 5)

In [20]: nums[:3]
Out[20]: range(0, 3)
```

---
### Функція range

Можно получить длину диапазона:
```python
In [21]: nums = range(5)

In [22]: len(nums)
Out[22]: 5
```

---
### Функція range

А также минимальный и максимальный элемент:
```python
In [23]: nums = range(5)

In [24]: min(nums)
Out[24]: 0

In [25]: max(nums)
Out[25]: 4
```

---
### Функція range

Кроме того, объект range поддерживает метод index:
```python
In [26]: nums = range(1, 7)

In [27]: nums.index(3)
Out[27]: 2
```

---
## Функція sorted

---
### Функція sorted

Функція ```sorted()``` возвращает новый отсортированный список, который получен из итерируемого объекта, который был передан как аргумент.
Функція также поддерживает дополнительные параметры, которые позволяют управлять сортировкой.

---
### sorted всегда возвращает список

```python
In [1]: list_of_words = ['one', 'two', 'list', '', 'dict']

In [2]: sorted(list_of_words)
Out[2]: ['', 'dict', 'list', 'one', 'two']

In [3]: tuple_of_words = ('one', 'two', 'list', '', 'dict')

In [4]: sorted(tuple_of_words)
Out[4]: ['', 'dict', 'list', 'one', 'two']

In [5]: set_of_words = {'one', 'two', 'list', '', 'dict'}

In [6]: sorted(set_of_words)
Out[6]: ['', 'dict', 'list', 'one', 'two']
```


---
## enumerate

---
### enumerate

Функція enumerate очікує як аргумент ітерований об'єкт і повертає ітератор, у
якому кожен елемент є кортежем із двох елементів: числа та елементу ітерованого об'єкту.


Синтаксис:

```python
enumerate(iterable, start=0)
```

Приклад:

```python
In [5]: list1 = ['str1', 'str2', 'str3']

In [6]: for position, string in enumerate(list1):
   ...:     print(position, string)
   ...:
0 str1
1 str2
2 str3
```

---
### enumerate

Enumerate вміє генерувати числа не тільки з нуля, але і з будь-якого значення,
яке йому вказали в параметрі start:

```python
In [7]: list1 = ['str1', 'str2', 'str3']

In [8]: for position, string in enumerate(list1, 100):
   ...:     print(position, string)
   ...:
100 str1
101 str2
102 str3
```


---
## Функція zip

---
### Функція zip

* як аргументи функції передаються послідовності
* zip повертає ітератор з кортежами, в якому n-ий кортеж складається з n-их елементів послідовностей, які були передані як аргументи
* якщо на вхід були передані послідовності різної довжини, то всі вони будуть скорочені до довжини найкоротшої послідовності

Синтаксис

```python
zip(*iterables, strict=False)
```

```python
In [1]: a = [1, 2, 3]

In [2]: b = [100, 200, 300]

In [3]: list(zip(a, b))
Out[3]: [(1, 100), (2, 200), (3, 300)]
```

---
### Функція zip

Використання zip зі списками різної довжини:

```python
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
list3 = [100, 200, 300]

In [5]: list(zip(list1, list2, list3))
Out[5]: [(1, 10, 100), (2, 20, 200), (3, 30, 300)]
```

Виклик zip зі  списками різної довжини та `strict=True`:

```python
In [6]: list(zip(list1, list2, list3, strict=True))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[6], line 1
----> 1 list(zip(list1, list2, list3, strict=True))

ValueError: zip() argument 3 is shorter than arguments 1-2
```

---
### Використання zip для створення словника

```python
d_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
d_values = ['london_r1', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.1']

In [2]: r1 = dict(zip(d_keys, d_values))

In [3]: r1
Out[3]:
{'hostname': 'london_r1',
 'location': '21 New Globe Walk',
 'vendor': 'Cisco',
 'model': '4451',
 'ios': '15.4',
 'ip': '10.255.0.1'}
```

---
## Функція all

---
### Функція all

Функція all повертає True, якщо всі елементи істинні (або об'єкт порожній).

```python
In [1]: all([False, True, True])
Out[1]: False

In [2]: all([True, True, True])
Out[2]: True

In [3]: all([])
Out[3]: True
```

---
### Функція all

```python
In [4]: IP = '10.0.1.1'

In [5]: all(i.isdigit() for i in IP.split('.'))
Out[5]: True

In [6]: all(i.isdigit() for i in '10.1.1.a'.split('.'))
Out[6]: False
```

---
## Функція any

---
### Функція any

Функція any() возвращает True, если хотя бы один элемент истина.
```python
In [7]: any([False, True, True])
Out[7]: True

In [8]: any([False, False, False])
Out[8]: False

In [9]: any([])
Out[9]: False

In [10]: any( i.isdigit() for i in '10.1.1.a'.split('.'))
Out[10]: True
```

---
### Функція any

Функція any повертає True, якщо хоча б один елемент істинний.

```python
In [7]: any([False, True, True])
Out[7]: True

In [8]: any([False, False, False])
Out[8]: False

In [9]: any([])
Out[9]: False

In [10]: any(i.isdigit() for i in '10.1.1.a'.split('.'))
Out[10]: True
```


---
### Анонимная функция (лямбда-выражение)

В Python лямбда-выражение позволяет создавать анонимные функции - функции, которые не привязаны к имени.

В анонимной функции:

* может содержаться только одно выражение
* могут передаваться сколько угодно аргументов

Стандартная функция:

```python
def sum_arg(a, b):
    return a + b
```

Аналогичная анонимная функция, или лямбда-функция:

```python
sum_arg = lambda a, b: a + b
```

---
### Функція map

Функція map применяет функцию к каждому элементу последовательности и
возвращает итератор с результатами.

Например, с помощью map можно выполнять преобразования элементов.
Перевести все строки в верхний регистр:

```python
In [1]: list_of_words = ['one', 'two', 'list', '', 'dict']

In [2]: map(str.upper, list_of_words)
Out[2]: <map at 0xb45eb7ec>

In [3]: list(map(str.upper, list_of_words))
Out[3]: ['ONE', 'TWO', 'LIST', '', 'DICT']
```

---
### Функція map

Конвертация в числа:

```python
In [3]: list_of_str = ['1', '2', '5', '10']

In [4]: list(map(int, list_of_str))
Out[4]: [1, 2, 5, 10]
```

Вместе с map удобно использовать лямбда-выражения:

```python
In [5]: vlans = [100, 110, 150, 200, 201, 202]

In [6]: list(map(lambda x: 'vlan {}'.format(x), vlans))
Out[6]: ['vlan 100', 'vlan 110', 'vlan 150', 'vlan 200', 'vlan 201', 'vlan 202']
```

---
## Функція filter

Функція ``filter`` применяет функцию ко всем элементам последовательности
и возвращает итератор с теми объектами, для которых функция вернула
True.

Например, вернуть только те строки, в которых находятся числа:

```python
In [1]: list_of_strings = ['one', 'two', 'list', '', 'dict', '100', '1', '50']

In [2]: filter(str.isdigit, list_of_strings)
Out[2]: <filter at 0xb45eb1cc>

In [3]: list(filter(str.isdigit, list_of_strings))
Out[3]: ['100', '1', '50']
```

---
## Функція filter

Из списка чисел оставить только нечетные:

```python
In [3]: list(filter(lambda x: x % 2 == 1, [10, 111, 102, 213, 314, 515]))
Out[3]: [111, 213, 515]
```

Аналогично, только четные:

```python
In [4]: list(filter(lambda x: x % 2 == 0, [10, 111, 102, 213, 314, 515]))
Out[4]: [10, 102, 314]
```
