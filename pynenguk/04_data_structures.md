## Типи даних у Python

---
## Типи даних у Python

У Python є кілька базових типів даних:

* Numbers (числа)
* Strings (рядки)
* Lists (списки)
* Dictionaries (словники)
* Tuples (кортежі)
* Sets (множини)
* Boolean (логічний тип даних)


---
## Типи даних у Python

* змінювані (списки, словники та множини)
* незмінні (числа, рядки та кортежі)
* упорядковані (списки, кортежі, рядки та словники)
* невпорядковані (множини)


---
## Типи даних у Python


``` mermaid
flowchart TD
  A[змінювані] --> B[список];
  A --> C[словник];
  A --> D[множина];
  F[незмінні] --> R[число];
  F --> S[рядок];
  F --> T[кортеж];
```


``` mermaid
flowchart TD
  A[упорядковані] --> B[список];
  A --> T[кортеж];
  A --> S[рядок];
  A --> C[словник];
  F[невпорядковані] --> D[множина];
```

---
## Типи даних у Python


---
## Типи даних у Python

| Название    | Название        | Пример |
|-------------|-----------------|--------------|
| Number      | число           | ``1, 100`` |
|             |                 |
| String      | строка          | ``"interface Gi0/0"`` |
|             |                 |
| List        | список          | ``[1, 2, 3]`` |
|             |                 |
| Dictionary  | словарь         | ``{"username": "user1", "permissions": 100}`` |
|             |                 |
| Tuple       | кортеж          | ``("line console 0", "login local")`` |
|             |                 |
| Set         | множество       | ``{3, 10, 100, 4, 5}`` |
|             |                 |
| Boolean     | булево значение | ``True, False`` |

---
## Типи даних у Python

|             |               |
|-------------|--------------|
| String      | Для хранения текста и произвольных данных, для которых в Python нет типа |
| List        | Набор данных, очень часто однотипных данных: список вланов, команд, строк файла |
| Dictionary  | Используется для данных типа поле: значение |
| Tuple       | Неизменяемый набор данных, который часто возвращается из внешних источников - БД, CSV. |
|             | Также используется когда данные это набор значений: (x, y) |
| Set         | Для хранения уникальных данных. Плюс часто используется промежуточно для |
|             | операций с множествами |
| Boolean     | Указывает, что какое-то значение истинное или ложное. Например {"routing": True} |
| None        | Используется, когда надо указать, что в этом месте нет никакого значения |


|             |              |
|-------------|--------------|
| String      | "interface Gi0/0" |
| List        | [1, 2, 3] |
| Dictionary  | {"username": "user1", "permissions": 100} |
| Tuple       | ("line console 0", "login local") |
| Set         | {3, 10, 100, 4, 5} |
| Boolean     | True, False |


---
## Строки (Strings)

---
### Строки

Строка в Python:
* последовательность символов, заключенная в кавычки
* неизменяемый упорядоченный тип данных

```python
In [9]: 'Hello'
Out[9]: 'Hello'

In [10]: "Hello"
Out[10]: 'Hello'
```

---
### Строки

```python
tunnel = """
interface Tunnel0
 ip address 10.10.10.1 255.255.255.0
 ip mtu 1416
 ip ospf hello-interval 5
 tunnel source FastEthernet1/0
 tunnel protection ipsec profile DMVPN
"""

In [12]: tunnel
Out[12]: '\ninterface Tunnel0\n ip address 10.10.10.1 255.255.255.0\n ip mtu 1416\n ip ospf hello-interval 5\n tunnel source FastEthernet1/0\n tunnel protection ipsec profile DMVPN\n'

In [13]: print(tunnel)

interface Tunnel0
 ip address 10.10.10.1 255.255.255.0
 ip mtu 1416
 ip ospf hello-interval 5
 tunnel source FastEthernet1/0
 tunnel protection ipsec profile DMVPN
```


---
### Строки. Индекс

Обращение по индексу к символам:
```python
In [20]: string1 = 'interface FastEthernet1/0'

In [21]: string1[0]
Out[21]: 'i'
```

Если нужно обратиться к какому-то по счету символу, начиная с конца, то можно указывать отрицательные значения (на этот раз с единицы).

```python
In [22]: string1[1]
Out[22]: 'n'

In [23]: string1[-1]
Out[23]: '0'
```

---
### Строки. Срез

Срез строки (срез выполняется по второе число, не включая его):
```python
In [24]: string1[0:9]
Out[24]: 'interface'

In [25]: string1[10:22]
Out[25]: 'FastEthernet'
```

Если не указывается второе число, то срез будет до конца строки:
```python
In [26]:  string1[10:]
Out[26]: 'FastEthernet1/0'
```

Срезать три последних символа строки:
```python
In [27]: string1[-3:]
Out[27]: '1/0'
```

---
### Строки

Строка в обратном порядке:
```python
In [28]: a = '0123456789'

In [29]: a[::]
Out[29]: '0123456789'

In [30]: a[::-1]
Out[30]: '9876543210'
```

---
### Строки

Записи ```a[::]``` и ```a[:]``` дают одинаковый результат, но двойное двоеточие позволяет указывать, что надо брать не каждый элемент, а, например, каждый второй.

Например, таким образом можно получить все четные числа строки a:
```python
In [31]: a[::2]
Out[31]: '02468'
```

Так можно получить нечетные:
```python
In [32]: a[1::2]
Out[32]: '13579'
```

---
### Строки

Строки можно суммировать. Тогда они объединяются в одну строку:
```python
In [14]: intf = 'interface'

In [15]: tun = 'Tunnel0'

In [16]: intf + tun
Out[16]: 'interfaceTunnel0'

In [17]: intf + ' ' + tun
Out[17]: 'interface Tunnel0'
```


Строку можно умножать на число. В этом случае, строка повторяется указанное количество раз:
```python
In [18]: intf * 5
Out[18]: 'interfaceinterfaceinterfaceinterfaceinterface'

In [19]: '#' * 40
Out[19]: '########################################'
```

---
### Полезные методы для работы со строками

При автоматизации очень часто надо будет работать со строками, так как конфигурационный файл, вывод команд и отправляемые команды - это строки.
Знание различных методов (то есть, действий), которые можно применять к строкам, помогает более эффективно работать с ними.
Строки неизменяемый тип данных, поэтому все методы, которые преобразуют строку возвращают новую строку, а исходная строка остается неизменной.

---
### Полезные методы для работы со строками

|             |  Разделение строки на части |
|:------------|:-----------------------------------------------------------------------------|
| join        | Concatenate any number of strings.                                           |
| split       | Return a list of the words in the string, using sep as the delimiter string. |
| splitlines  | Return a list of the lines in the string, breaking at line boundaries.       |
| partition   | Partition the string into three parts using the given separator.             |
| rpartition  | Partition the string into three parts using the given separator.             |
| rsplit      | Return a list of the words in the string, using sep as the delimiter string. |
|             |  |


| | Удаление whitespace символов |
|:-------|:--------------------------------------------------------------------------|
| strip  | Return a copy of the string with leading and trailing whitespace removed. |
| rstrip | Return a copy of the string with trailing whitespace removed.             |
| lstrip | Return a copy of the string with leading whitespace removed.              |
|        |  |

| |  Проверка начала/конца строки |
|----------------|:-------------------------------------------------------------------------|
| startswith     | Return True if S starts with the specified prefix, False otherwise.      |
| endswith       | Return True if S ends with the specified prefix, False otherwise.      |
|        |  |

---
### Полезные методы для работы со строками

|  | Проверка того, что находится в строке |
|:------------------|:-------------------------------------------------------------------------|
| isalnum()      | Return True if the string is an alpha-numeric string, False otherwise.   |
| isalpha()      | Return True if the string is an alphabetic string, False otherwise.      |
| isascii()      | Return True if all characters in the string are ASCII, False otherwise.  |
| isdecimal()    | Return True if the string is a decimal string, False otherwise.          |
| isdigit()      | Return True if the string is a digit string, False otherwise.            |
| isidentifier() | Return True if the string is a valid Python identifier, False otherwise. |
| islower()      | Return True if the string is a lowercase string, False otherwise.        |
| isnumeric()    | Return True if the string is a numeric string, False otherwise.          |
| isprintable()  | Return True if the string is printable, False otherwise.                 |
| isspace()      | Return True if the string is a whitespace string, False otherwise.       |
| istitle()      | Return True if the string is a title-cased string, False otherwise.      |
| isupper()      | Return True if the string is an uppercase string, False otherwise.       |
|        |  |


|            | Преобразования регистра |
|:-----------|:---------------------------------------------------------------------------------|
| lower      | Return a copy of the string converted to lowercase.                              |
| capitalize | Return a capitalized version of the string.                                      |
| swapcase   | Convert uppercase characters to lowercase and lowercase characters to uppercase. |
| title      | Return a version of the string where each word is titlecased.                    |
| upper      | Return a copy of the string converted to uppercase.                              |
| casefold   | Return a version of the string suitable for caseless comparisons.                |
|        |  |



---
### Полезные методы для работы со строками


|  | Выравнивание текста |
|:-------------------------------------|:---------------------------------------------------------------------------------|
| center | Return a centered string of length width.                                        |
| ljust  | Return a left-justified string of length width.                                  |
| rjust  | Return a right-justified string of length width.                                 |
| zfill                | Pad a numeric string with zeros on the left, to fill a field of the given width. |
|        |  |


| | Поиск, подсчет элементов |
|:--------|:-------------------------------------|
| count   | S.count(sub[, start[, end]]) -> int  |
| find    | S.find(sub[, start[, end]]) -> int   |
| index   | S.index(sub[, start[, end]]) -> int  |
| replace | S.replace(old, new)                  |
| rfind   | S.rfind(sub[, start[, end]]) -> int  |
| rindex  | S.rindex(sub[, start[, end]]) -> int |
|        |  |

| | Другие методы |
|:----------------------------------------|:------------------------------------|
| expandtabs | Return a copy where all tab characters are expanded using spaces.       |
| format     | S.format(*args, **kwargs) -> str  |
| format_map | S.format_map(mapping) -> str  |
| maketrans  | Return a translation table usable for str.translate(). |
| translate  | Replace each character in the string using the given translation table. |
| encode   | Encode the string using the codec registered for encoding.              |


---
### ```upper(), lower(), swapcase(), capitalize()```

Методы ```upper()```, ```lower()```, ```swapcase()```, ```capitalize()``` выполняют преобразование регистра строки:
```python
In [25]: string1 = 'FastEthernet'

In [26]: string1.upper()
Out[26]: 'FASTETHERNET'

In [27]: string1.lower()
Out[27]: 'fastethernet'

In [28]: string1.swapcase()
Out[28]: 'fASTeTHERNET'

In [29]: string2 = 'tunnel 0'

In [30]: string2.capitalize()
Out[30]: 'Tunnel 0'
```

---
### Строки - неизменяемый тип данных

Очень важно обращать внимание на то, что часто методы возвращают преобразованную строку. И, значит, надо не забыть присвоить ее какой-то переменной (можно той же).
```python
In [31]: string1 = string1.upper()

In [32]: print(string1)
FASTETHERNET
```

---
### ```startswith(), endswith()```

Проверка на то, начинается или заканчивается ли строка на определенные символы (методы ```startswith()```, ```endswith()```):
```python
In [40]: string1 = 'FastEthernet0/1'

In [41]: string1.startswith('Fast')
Out[41]: True

In [42]: string1.startswith('fast')
Out[42]: False

In [43]: string1.endswith('0/1')
Out[43]: True

In [44]: string1.endswith('0/2')
Out[44]: False
```

---
### ```replace()```

Замена последовательности символов в строке на другую последовательность (метод ```replace()```):
```python
In [45]: string1 = 'FastEthernet0/1'

In [46]: string1.replace('Fast', 'Gigabit')
Out[46]: 'GigabitEthernet0/1'
```

---
### ```strip()```

Часто при обработке файла файл открывается построчно.
Но в конце каждой строки, как правило, есть какие-то спецсимволы (а могут быть и в начале). Например, перевод строки.

Для того, чтобы избавиться от них, очень удобно использовать метод ```strip()```:
```python
In [47]: string1 = '\n\tinterface FastEthernet0/1\n'

In [48]: print(string1)

    interface FastEthernet0/1


In [49]: string1
Out[49]: '\n\tinterface FastEthernet0/1\n'

In [50]: string1.strip()
Out[50]: 'interface FastEthernet0/1'
```

---
### ```strip()```

По умолчанию, метод strip() убирает whitespace символы.
В этот набор символов входят: ` \t\n\r\f\v`

Методу strip можно передать как аргумент любые символы.
Тогда в начале и в конце строки будут удалены все символы, которые были указаны в строке:
```python
In [51]: ad_metric = '[110/1045]'

In [52]: ad_metric.strip('[]')
Out[52]: '110/1045'
```

Метод strip() убирает спецсимволы и в начале, и в конце строки.
Если необходимо убрать символы только слева или только справа, можно использовать, соответственно, методы ```lstrip()``` и ```rstrip()```.

---
### ```split()```

Метод ```split()``` разбивает строку на части, используя как разделитель какой-то символ (или символы).
По умолчанию, в качестве разделителя используются пробелы.
Но в скобках можно указать любой разделитель.

В результате, строка будет разбита на части по указанному разделителю и представлена в виде частей, которые содержатся в списке.

---
### ```split()```

```python
In [53]: string1 = ' switchport trunk allowed vlan 10,20,30,100-200\n'

In [54]: commands = string1.split()

In [55]: print(commands)
['switchport', 'trunk', 'allowed', 'vlan', '10,20,30,100-200']

In [56]: vlans = commands[-1].split(',')

In [57]: print(vlans)
['10', '20', '30', '100-200']
```

---
### ```split()```

У метода ```split()``` есть ещё одна хорошая особенность: по умолчанию метод разбивает строку не по одному пробелу, а по любому количеству пробелов.

Это будет очень полезным при обработке команд show. Например:
```python
In [58]: sh_ip_int_br = "FastEthernet0/0       15.0.15.1    YES manual up         up"

In [59]: sh_ip_int_br.split()
Out[59]: ['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up']
```

---
## Форматирование строк

---
### Форматирование строк

* с оператором ```%``` (более старый вариант)
* методом ```format()``` (новый вариант)
* f-строки - новый вариант, который появился в Python 3.6. 


---
### Форматирование строк с методом format

Пример использования метода format:
```python
In [1]: "interface FastEthernet0/{}".format('1')
Out[1]: 'interface FastEthernet0/1'
```

Специальный символ ```{}``` указывает, что сюда подставится значение, которое передается методу format.
При этом, каждая пара фигурных скобок обозначает одно место для подстановки.

---
### Форматирование строк

Значения, которые подставляются в фигурные скобки, могут быть разного типа.
Например, это может быть строка, число или список:
```python
In [3]: print('{}'.format('10.1.1.1'))
10.1.1.1

In [4]: print('{}'.format(100))
100

In [5]: print('{}'.format([10, 1, 1, 1]))
[10, 1, 1, 1]
```

---
### Форматирование строк

С помощью форматирования строк можно выводить результат столбцами.
В форматировании строк можно указывать, какое количество символов выделено на данные.
Если количество символов в данных меньше, чем выделенное количество символов, недостающие символы заполняются пробелами.

---
### Форматирование строк

Например, таким образом можно вывести данные столбцами одинаковой ширины по 15 символов с выравниванием по правой стороне:
```python
In [3]: vlan, mac, intf = ['100', 'aabb.cc80.7000', 'Gi0/1']

In [4]: print("{:>15} {:>15} {:>15}".format(vlan, mac, intf))
            100  aabb.cc80.7000           Gi0/1
```

Выравнивание по левой стороне:
```python
In [5]: print("{:15} {:15} {:15}".format(vlan, mac, intf))
100             aabb.cc80.7000  Gi0/1
```

---
### Форматирование строк

Шаблон для вывода может быть и многострочным:
```python
In [6]: ip_template = '''
   ...: IP address:
   ...: {}
   ...: '''

In [7]: print(ip_template.format('10.1.1.1'))

IP address:
10.1.1.1
```

---
### Форматирование строк

С помощью форматирования строк можно также влиять на отображение чисел.

Например, можно указать, сколько цифр после запятой выводить:
```python
In [9]: print("{:.3f}".format(10.0/3))
3.333
```

---
### Форматирование строк

С помощью форматирования строк можно конвертировать числа в двоичный формат:
```python
In [11]: '{:b} {:b} {:b} {:b}'.format(192, 100, 1, 1)
Out[11]: '11000000 1100100 1 1'
```

При этом по-прежнему можно указывать дополнительные параметры, например, ширину столбца:
```python
In [12]: '{:8b} {:8b} {:8b} {:8b}'.format(192, 100, 1, 1)
Out[12]: '11000000  1100100        1        1'
```

---
### Форматирование строк

А также можно указать, что надо дополнить числа нулями, вместо пробелов:
```python
In [13]: '{:08b} {:08b} {:08b} {:08b}'.format(192, 100, 1, 1)
Out[13]: '11000000 01100100 00000001 00000001'
```

---
### Форматирование строк

В фигурных скобках можно указывать имена.
Это позволяет передавать аргументы в любом порядке, а также делает шаблон более понятным:
```python
In [15]: '{ip}/{mask}'.format(mask=24, ip='10.1.1.1')
Out[15]: '10.1.1.1/24'
```

---
### Форматирование строк

Еще одна полезная возможность форматирования строк - указание номера аргумента:
```python
In [16]: '{1}/{0}'.format(24, '10.1.1.1')
Out[16]: '10.1.1.1/24'
```

---
### Форматирование строк

За счет этого, например, можно избавиться от повторной передачи одних и тех же значений:
```python
In [19]: ip_template = '''
    ...: IP address:
    ...: {:<8} {:<8} {:<8} {:<8}
    ...: {:08b} {:08b} {:08b} {:08b}
    ...: '''

In [20]: print(ip_template.format(192, 100, 1, 1, 192, 100, 1, 1))

IP address:
192      100      1        1
11000000 01100100 00000001 00000001
```

---
### Форматирование строк

Указав индексы значений, которые передаются методу format, можно избавиться от дублирования:
```python
In [21]: ip_template = '''
    ...: IP address:
    ...: {0:<8} {1:<8} {2:<8} {3:<8}
    ...: {0:08b} {1:08b} {2:08b} {3:08b}
    ...: '''

In [22]: print(ip_template.format(192, 100, 1, 1))

IP address:
192      100      1        1
11000000 01100100 00000001 00000001
```

---
## f-строки

В Python 3.6 добавился новый вариант форматирования строк: f-строки или
интерполяция строк. F-строки позволяют не только подставлять какие-то
значения в шаблон, но и позволяют выполнять вызовы функций, методов и
тп.

Во многих ситуациях f-строки удобней и проще использовать, чем format,
кроме того, f-строки работают быстрее, чем format и другие методы
форматирования строк.

---
## Синтаксис f-строк

F-строки - это литерал строки с буквой ``f`` перед ним. Внутри f-строки
в паре фигурных скобок указываются имена переменных, которые надо
подставить:

```python
In [1]: ip = '10.1.1.1'

In [2]: mask = 24

In [3]: f"IP: {ip}, mask: {mask}"
Out[3]: 'IP: 10.1.1.1, mask: 24'
```

---
## Синтаксис f-строк

Очень важное отличие f-строк от format: f-строки это выражение, которое
выполняется, а не просто строка. 

Поэтому, например, нельзя сначала написать шаблон, а затем определить
переменные, которые используются в шаблоне:

```python
In [1]: f"IP: {ip}, mask: {mask}"
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-e6f8e01ac9c4> in <module>()
----> 1 f"IP: {ip}, mask: {mask}"

NameError: name 'ip' == not defined
```

---
## Синтаксис f-строк

Кроме подстановки значений переменных, в фигурных скобках можно писать
выражения:

```python
In [5]: first_name = 'William'

In [6]: second_name = 'Shakespeare'

In [7]: f"{first_name.upper()} {second_name.upper()}"
Out[7]: 'WILLIAM SHAKESPEARE'
```

---
## Синтаксис f-строк

После двоеточия в f-строках можно указывать те же значения, что и при
использовании format:

```python
In [9]: oct1, oct2, oct3, oct4 = [10, 1, 1, 1]

In [10]: print(f'''
    ...: IP address:
    ...: {oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
    ...: {oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}''')

IP address:
10       1        1        1
00001010 00000001 00000001 00000001
```

---
## Объединение литералов строк

---
## Объединение литералов строк

В Python есть очень удобная функциональность - объединение литералов строк.

```python
In [1]: s = ('Test' 'String')

In [2]: s
Out[2]: 'TestString'

In [3]: s = 'Test' 'String'

In [4]: s
Out[4]: 'TestString'
```

---
## Объединение литералов строк

Можно даже переносить составляющие строки на разные строки, но только если они в скобках
```python
In [5]: s = ('Test'
   ...: 'String')

In [6]: s
Out[6]: 'TestString'
```

---
## Объединение литералов строк

Этим очень удобно пользоваться в регулярных выражениях:
```python
regex = ('(\S+) +(\S+) +'
         '\w+ +\w+ +'
         '(up|down|administratively down) +'
         '(\w+)')
```

---
## Объединение литералов строк

Так регулярное выражение можно разбивать на части и его будет проще понять.
Плюс можно добавлять поясняющие комментарии в строках.
```python
regex = ('(\S+) +(\S+) +' # interface and IP
         '\w+ +\w+ +'
         '(up|down|administratively down) +' # Status
         '(\w+)') # Protocol
```

---
## Объединение литералов строк

Также этим приемом удобно пользоваться, когда надо написать длинное сообщение:
```python
In [7]: message = ('При выполнении команды "{}" '
   ...: 'возникла такая ошибка "{}".\n'
   ...: 'Исключить эту команду из списка? [y/n]')

In [8]: message
Out[8]: 'При выполнении команды "{}" возникла такая ошибка "{}".\nИсключить эту команду из списка? [y/n]'
```

---
## Список (List)

---
### Список

Список:
* изменяемый упорядоченный тип данных.
* последовательность элементов, разделенных между собой запятой и заключенных в квадратные скобки.

```python
In [1]: list1 = [10, 20, 30, 77]
In [2]: list2 = ['one', 'dog', 'seven']
In [3]: list3 = [1, 20, 4.0, 'word']
```

---
### Список

Так как список - это упорядоченный тип данных, то, как и в строках, в списках можно обращаться к элементу по номеру, делать срезы:
```python
In [4]: list3 = [1, 20, 4.0, 'word']

In [5]: list3[1]
Out[5]: 20

In [6]: list3[1::]
Out[6]: [20, 4.0, 'word']

In [7]: list3[-1]
Out[7]: 'word'

In [8]: list3[::-1]
Out[8]: ['word', 4.0, 20, 1]
```

---
### Список

Перевернуть список наоборот можно и с помощью метода reverse():
```python
In [10]: vlans = ['10', '15', '20', '30', '100-200']

In [11]: vlans.reverse()

In [12]: vlans
Out[12]: ['100-200', '30', '20', '15', '10']
```

---
### Список

Так как списки изменяемые, элементы списка можно менять:
```python
In [13]: list3
Out[13]: [1, 20, 4.0, 'word']

In [14]: list3[0] = 'test'

In [15]: list3
Out[15]: ['test', 20, 4.0, 'word']
```

---
### Список

Можно создавать и список списков. И, как и в обычном списке, можно обращаться к элементам во вложенных списках:
```python
In [16]: interfaces = [['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up'],
   ....: ['FastEthernet0/1', '10.0.1.1', 'YES', 'manual', 'up', 'up'],
   ....: ['FastEthernet0/2', '10.0.2.1', 'YES', 'manual', 'up', 'down']]

In [17]: interfaces[0][0]
Out[17]: 'FastEthernet0/0'

In [18]: interfaces[2][0]
Out[18]: 'FastEthernet0/2'

In [19]: interfaces[2][1]
Out[19]: '10.0.2.1'
```

---
### Список

Функция len возвращает количество элементов в списке:

```python
In [1]: items = [1, 2, 3]

In [2]: len(items)
Out[2]: 3
```

А функция sorted сортирует элементы списка по возрастанию и возвращает новый список с отсортированными элементами:

```python
In [1]: names = ['John', 'Michael', 'Antony']

In [2]: sorted(names)
Out[2]: ['Antony', 'John', 'Michael']
```


---
### Полезные методы для работы со списками

---
### Полезные методы для работы со списками

Список - это изменяемый тип данных, поэтому очень важно обращать внимание на то, что большинство методов для работы со списками меняют список на месте, при этом ничего не возвращая.

|                  | |
|:------------------------------------------|:-----------------------------------------------------|
| append(object, /)                         | Append object to the end of the list.                |
| extend(iterable, /)                       | Extend list by appending elements from the iterable. |
| remove(value, /)                          | Remove first occurrence of value.                    |
| insert(index, object, /)                  | Insert object before index.                          |
| pop(index=-1, /)                          | Remove and return item at index (default last).      |
| count(value, /)                           | Return number of occurrences of value.               |
| index(value, start=0, stop=2147483647, /) | Return first index of value.                         |
| sort(key=None, reverse=False)    | Sort the list in ascending order and return None. |
| clear()                                   | Remove all items from list.                          |
| copy()                                    | Return a shallow copy of the list.                   |
| reverse()                                 | Reverse IN PLACE.                                  |


---
### ```join()```

Метод __join()__ собирает список строк в одну строку с разделителем, который указан перед join:
```python
In [16]: vlans = ['10', '20', '30']

In [17]: ','.join(vlans)
Out[17]: '10,20,30'
```

---
### ```append()```

Метод __append()__ добавляет в конец списка указанный элемент:
```python
In [18]: vlans = ['10', '20', '30', '100-200']

In [19]: vlans.append('300')

In [20]: vlans
Out[20]: ['10', '20', '30', '100-200', '300']
```

Метод append меняет список на месте и ничего не возвращает.

---
### Объединение списков

Если нужно объединить два списка, то можно использовать два способа: метод __extend()__ и операцию сложения.

У этих способов есть важное отличие - extend меняет список, к которому примерен метод, а суммирование возвращает новый список, который состоит из двух.

---
### ```extend()```

Метод extend:
```python
In [21]: vlans = ['10', '20', '30', '100-200']

In [22]: vlans2 = ['300', '400', '500']

In [23]: vlans.extend(vlans2)

In [24]: vlans
Out[24]: ['10', '20', '30', '100-200', '300', '400', '500']
```

---
### Суммирование списков

```python
In [27]: vlans = ['10', '20', '30', '100-200']

In [28]: vlans2 = ['300', '400', '500']

In [29]: vlans + vlans2
Out[29]: ['10', '20', '30', '100-200', '300', '400', '500']
```

---
### Суммирование списков

Обратите внимание на то, что при суммировании списков в ipython появилась строка Out.
Это означает, что результат суммирования можно присвоить в переменную:
```python
In [30]: result = vlans + vlans2

In [31]: result
Out[31]: ['10', '20', '30', '100-200', '300', '400', '500']
```

---
### ```pop()```

Метод __pop()__ удаляет элемент, который соответствует указанному номеру. Но, что важно, при этом метод возвращает этот элемент:
```python
In [28]: vlans = ['10', '20', '30', '100-200']

In [29]: vlans.pop(-1)
Out[29]: '100-200'

In [30]: vlans
Out[30]: ['10', '20', '30']
```

Без указания номера удаляется последний элемент списка.

---
### ```remove()```

Метод __remove()__ удаляет указанный элемент.

remove() не возвращает удаленный элемент: 
```python
In [31]: vlans = ['10', '20', '30', '100-200']

In [32]: vlans.remove('20')

In [33]: vlans
Out[33]: ['10', '30', '100-200']
```

---
### ```remove()```

В методе remove надо указывать сам элемент, который надо удалить, а не его номер в списке.
Если указать номер элемента, возникнет ошибка:
```python
In [34]: vlans.remove(-1)
-------------------------------------------------
ValueError      Traceback (most recent call last)
<ipython-input-32-f4ee38810cb7> in <module>()
----> 1 vlans.remove(-1)

ValueError: list.remove(x): x not in list
```

---
### ```index()```

Метод __index()__ используется для того, чтобы проверить, под каким номером в списке хранится элемент:
```python
In [35]: vlans = ['10', '20', '30', '100-200']

In [36]: vlans.index('30')
Out[36]: 2
```

---
### ```insert()```

Метод __insert()__ позволяет вставить элемент на определенное место в списке:
```python
In [37]: vlans = ['10', '20', '30', '100-200']

In [38]: vlans.insert(1,'15')

In [39]: vlans
Out[39]: ['10', '15', '20', '30', '100-200']
```

---
### Варианты создания списка

---
### Варианты создания списка

Создание списка с помощью литерала:
```python
In [1]: vlans = [10, 20, 30, 50]
```

> Литерал - это выражение, которое создает объект.


---
### Варианты создания списка

Создание списка с помощью функции __list()__:
```python
In [2]: list1 = list('router')

In [3]: print(list1)
['r', 'o', 'u', 't', 'e', 'r']
```
---
### Типы данных в Python

| Название    | Название        | Пример |
|-------------|-----------------|--------------|
| Number      | число           | ``1, 100`` |
|             |                 |
| String      | строка          | ``"interface Gi0/0"`` |
|             |                 |
| List        | список          | ``[1, 2, 3]`` |
|             |                 |
| Dictionary  | словарь         | ``{"username": "user1", "permissions": 100}`` |
|             |                 |
| Tuple       | кортеж          | ``("line console 0", "login local")`` |
|             |                 |
| Set         | множество       | ``{3, 10, 100, 4, 5}`` |
|             |                 |
| Boolean     | булево значение | ``True, False`` |
---
## Словарь (Dictionary)

---
### Словарь (ассоциативный массив, хеш-таблица)

* изменяемый упорядоченный тип данных 
* данные в словаре - это пары ```ключ: значение```
* доступ к значениям осуществляется по ключу, а не по номеру, как в списках
* словари упорядочены в порядке добавления данных
* так как словари изменяемы, то элементы словаря можно менять, добавлять, удалять
* ключ должен быть объектом неизменяемого типа:
 * число
 * строка
 * кортеж
* значение может быть данными любого типа

---
### Словарь

Пример словаря:
```python
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

london = {
        'id': 1,
        'name':'London',
        'it_vlan':320,
        'user_vlan':1010,
        'mngmt_vlan':99,
        'to_name': None,
        'to_id': None,
        'port':'G1/0/11'
}
```

---
### Словарь

Для того, чтобы получить значение из словаря, надо обратиться по ключу, таким же образом, как это было в списках, только вместо номера будет использоваться ключ:
```python
In [1]: london = {'name': 'London1', 'location': 'London Str'}

In [2]: london['name']
Out[2]: 'London1'

In [3]: london['location']
Out[3]: 'London Str'
```

---
### Словарь

Аналогичным образом можно добавить новую пару ключ:значение:
```python
In [4]: london['vendor'] = 'Cisco'

In [5]: print(london)
{'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
```

---
### Словарь

В словаре в качестве значения можно использовать словарь:
```python
london_co = {
    'r1' : {
    'hostname': 'london_r1',
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'hostname': 'london_r2',
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'hostname': 'london_sw1',
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101'
    }
}
```

---
### Словарь

Получить значения из вложенного словаря можно так:
```python
In [7]: london_co['r1']['ios']
Out[7]: '15.4'

In [8]: london_co['r1']['model']
Out[8]: '4451'

In [9]: london_co['sw1']['ip']
Out[9]: '10.255.0.101'
```

---
### Словарь

Функция sorted сортирует ключи словаря по возрастанию и возвращает
новый список с отсортированными ключами:

```python
In [1]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

In [2]: sorted(london)
Out[2]: ['location', 'name', 'vendor']
```


---
### Полезные методы для работы со словарями

|   | Методы словарей |
|----------|-------------------------------------------|
| get      | Return the value for key if key is in the dictionary, else default.
| update   | Update D from dict/iterable E and F.
| pop      | remove specified key and return the corresponding value.
|          | If key is not found, d is returned if given, otherwise KeyError is raised
| popitem  | Remove and return a (key, value) pair as a 2-tuple.
| setdefault | Insert key with a value of default if key is not in the dictionary.
| keys     | Return  a set-like object providing a view on D's keys
| values   | Return an object providing a view on D's values
| items    | Return a set-like object providing a view on D's items
| clear    | Remove all items from D.
| copy     |  a shallow copy of D
| fromkeys | Create a new dictionary with keys from iterable and values set to value.

---
### ```clear()```

Метод __clear()__ позволяет очистить словарь:
```python
In [1]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco', 'model': '4451', 'ios': '15.4'}

In [2]: london.clear()

In [3]: london
Out[3]: {}
```

---
### ```copy()```

Метод __copy()__ позволяет создать полную копию словаря. 

Если указать, что один словарь равен другому:
```python
In [4]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

In [5]: london2 = london

In [6]: id(london)
Out[6]: 25489072

In [7]: id(london2)
Out[7]: 25489072

In [8]: london['vendor'] = 'Juniper'

In [9]: london2['vendor']
Out[9]: 'Juniper'
```

---
### ```copy()```

Если нужно сделать копию словаря, надо использовать метод copy():
```python
In [10]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

In [11]: london2 = london.copy()

In [12]: id(london)
Out[12]: 25524512

In [13]: id(london2)
Out[13]: 25563296

In [14]: london['vendor'] = 'Juniper'

In [15]: london2['vendor']
Out[15]: 'Cisco'
```

---
### ```get()```

Если при обращении к словарю указывается ключ, которого нет в словаре, возникает ошибка:
```python
In [16]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

In [17]: london['ios']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-17-b4fae8480b21> in <module>()
----> 1 london['ios']

KeyError: 'ios'
```

---
### ```get()```

Метод __get()__ запрашивает ключ и, если его нет, вместо ошибки возвращает ```None```.
```python
In [18]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

In [19]: print(london.get('ios'))
None
```

Метод get() позволяет также указывать другое значение вместо ```None```:
```python
In [20]: print(london.get('ios', 'Ooops'))
Ooops
```

---
### ```setdefault()```

Метод __setdefault()__ ищет ключ и, если его нет, вместо ошибки создает ключ со значением ```None```.
```python
In [21]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

In [22]: ios = london.setdefault('ios')

In [23]: print(ios)
None

In [24]: london
Out[24]: {'ios': None, 'location': 'London Str', 'name': 'London1', 'vendor': 'Cisco'}
```

Но, если ключ есть, setdefault возвращает значение, которое ему соответствует:
```python
In [25]: london.setdefault('name')
Out[25]: 'London1'
```

---
### ```setdefault()```

Второй аргумент позволяет указать, какое значение должно соответствовать ключу:
```python
In [26]: model = london.setdefault('model', 'Cisco3580')

In [27]: print(model)
Cisco3580

In [28]: london
Out[28]:
{'ios': None,
 'model': 'Cisco3580',
 'location': 'London Str',
 'name': 'London1',
 'vendor': 'Cisco'}
```

---
### ```setdefault()```

Метод setdefault заменяет такую конструкцию:
```python
In [30]: if key in london:
    ...:     value = london[key]
    ...: else:
    ...:     london[key] = 'somevalue'
    ...:     value = london[key]
    ...:
```


---
### ```keys(), values(), items()```

Методы __keys()__, __values()__, __items()__:
```python
In [24]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

In [25]: london.keys()
Out[25]: dict_keys(['name', 'location', 'vendor'])

In [26]: london.values()
Out[26]: dict_values(['London1', 'London Str', 'Cisco'])

In [27]: london.items()
Out[27]: dict_items([('name', 'London1'), ('location', 'London Str'), ('vendor', 'Cisco')])

```

---
### ```keys(), values(), items()```

Все три метода возвращают специальные объекты view, которые отображают ключи, значения и пары ключ-значение словаря соответственно.

Очень важная особенность view заключается в том, что они меняются вместе с изменением словаря. И фактически они лишь дают способ посмотреть на соответствующие объекты, но не создают их копию.

---
### ```keys(), values(), items()```

На примере метода keys():
```python
In [28]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

In [29]: keys = london.keys()

In [30]: print(keys)
dict_keys(['name', 'location', 'vendor'])
```

---
### ```keys(), values(), items()```

Сейчас переменной keys соответствует view dict_keys, в котором три ключа: name, locationa и vendor.

Но, если мы добавим в словарь еще одну пару ключ-значение, объект keys тоже поменяется:

```python
In [31]: london['ip'] = '10.1.1.1'

In [32]: keys
Out[32]: dict_keys(['name', 'location', 'vendor', 'ip'])
```

---
### ```keys(), values(), items()```

Если нужно получить обычный список ключей, который не будет меняться с изменениями словаря, достаточно конвертировать view в список:
```python
In [33]: list_keys = list(london.keys())

In [34]: list_keys
Out[34]: ['name', 'location', 'vendor', 'ip']

```

---
### ```del```
Удалить ключ и значение:
```python
In [35]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

In [36]: del(london['name'])

In [37]: london
Out[37]: {'location': 'London Str', 'vendor': 'Cisco'}
```

---
### ```update```

Метод update позволяет добавлять в словарь содержимое другого словаря:

```python
In [38]: r1 = {'name': 'London1', 'location': 'London Str'}

In [39]: r1.update({'vendor': 'Cisco', 'ios':'15.2'})

In [40]: r1
Out[40]: {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco', 'ios': '15.2'}
```

---
### ```update```

Аналогичным образом можно обновить значения:

```python
In [41]: r1.update({'name': 'london-r1', 'ios':'15.4'})

In [42]: r1
Out[42]:
{'name': 'london-r1',
 'location': 'London Str',
 'vendor': 'Cisco',
 'ios': '15.4'}
```


---
## Варианты создания словаря

---
### Литерал

Словарь можно создать с помощью литерала:
```python
In [1]: r1 = {'model': '4451', 'ios': '15.4'}
```

---
### dict

Конструктор __dict__ позволяет создавать словарь несколькими способами.

Если в роли ключей используются строки, можно использовать такой вариант создания словаря:
```python
In [2]: r1 = dict(model='4451', ios='15.4')

In [3]: r1
Out[3]: {'ios': '15.4', 'model': '4451'}
```

---
### dict

Второй вариант создания словаря с помощью dict:
```python
In [4]: r1 = dict([('model','4451'), ('ios','15.4')])

In [5]: r1
Out[5]: {'ios': '15.4', 'model': '4451'}
```

---
### dict.fromkeys

В ситуации, когда надо создать словарь с известными ключами, но, пока что, пустыми значениями (или одинаковыми значениями), очень удобен метод __fromkeys()__:
```python
In [5]: d_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']

In [6]: r1 = dict.fromkeys(d_keys)

In [7]: r1
Out[7]: 
{'ios': None,
 'ip': None,
 'hostname': None,
 'location': None,
 'model': None,
 'vendor': None}
```

---
### dict.fromkeys

По умолчанию, метод fromkeys подставляет значение None.
Но можно указывать и свой вариант значения:
```python
In [8]: router_models = ['ISR2811', 'ISR2911', 'ISR2921', 'ASR9002']

In [9]: models_count = dict.fromkeys(router_models, 0)

In [10]: models_count
Out[10]: {'ASR9002': 0, 'ISR2811': 0, 'ISR2911': 0, 'ISR2921': 0}

```

---
### dict.fromkeys

Этот вариант создания словаря подходит не для всех случаев.
Например, при использовании изменяемого типа данных в значении, будет создана ссылка на один и тот же объект:
```python
In [11]: router_models = ['ISR2811', 'ISR2911', 'ISR2921', 'ASR9002']

In [12]: routers = dict.fromkeys(router_models, [])

In [13]: routers
Out[13]: {'ASR9002': [], 'ISR2811': [], 'ISR2911': [], 'ISR2921': []}

In [14]: routers['ASR9002'].append('london_r1')

In [15]: routers
Out[15]:
{'ASR9002': ['london_r1'],
 'ISR2811': ['london_r1'],
 'ISR2911': ['london_r1'],
 'ISR2921': ['london_r1']}
```


---
## Кортеж (Tuple)

---
### Кортеж

Кортеж - это неизменяемый упорядоченный тип данных.

Кортеж в Python - это последовательность элементов, которые разделены между собой запятой и заключены в скобки.

Грубо говоря, кортеж - это список, который нельзя изменить. То есть, в кортеже есть только права на чтение. Это может быть защитой от случайных изменений.

---
### Кортеж

Создать пустой кортеж:
```python
In [1]: tuple1 = tuple()

In [2]: print(tuple1)
()
```

Кортеж из одного элемента (обратите внимание на запятую):
```python
In [3]: tuple2 = ('password',)
```

---
### Кортеж

Кортеж из списка:
```python
In [4]: list_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']

In [5]: tuple_keys = tuple(list_keys)

In [6]: tuple_keys
Out[6]: ('hostname', 'location', 'vendor', 'model', 'IOS', 'IP')
```

К объектам в кортеже можно обращаться, как и к объектам списка, по порядковому номеру:
```python
In [7]: tuple_keys[0]
Out[7]: 'hostname'
```

---
### Кортеж

Но так как кортеж неизменяем, присвоить новое значение нельзя:
```python
In [8]: tuple_keys[1] = 'test'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-1c7162cdefa3> in <module>()
----> 1 tuple_keys[1] = 'test'

TypeError: 'tuple' object does not support item assignment
```

---
### Методы кортежа

|   | Методы кортежа |
|---------|--------------------------------------|
| count   | S.count(sub[, start[, end]]) -> int  |
| index   | S.index(sub[, start[, end]]) -> int  |

---
## Множество (Set)

---
### Множество

Множество - это изменяемый неупорядоченный тип данных. В множестве всегда содержатся только уникальные элементы.

Множество в Python - это последовательность элементов, которые разделены между собой запятой и заключены в фигурные скобки.

---
### Множество

С помощью множества можно легко убрать повторяющиеся элементы:
```python
In [1]: vlans = [10, 20, 30, 40, 100, 10]

In [2]: set(vlans)
Out[2]: {10, 20, 30, 40, 100}

In [3]: set1 = set(vlans)

In [4]: print(set1)
{40, 100, 10, 20, 30}
```

---
### Полезные методы для работы с множествами

---
### Методы множеств

| Название                      | Описание |
|-------------------------------|--------------|
| add                           | Add an element to a set. |
| update                        | Update a set with the union of itself and others. |
| remove                        | Remove an element from a set; it must be a member. |
| discard                       | Remove an element from a set if it is a member. |
| pop                           | Remove and return an arbitrary set element. Raises KeyError if the set is empty. |
| clear                         | Remove all elements from this set. |
| copy                          | Return a shallow copy of a set. |
| | |
| difference                    | Return the difference of two or more sets as a new set. |
| intersection                  | Return the intersection of two sets as a new set. |
| union                         | Return the union of sets as a new set. |
| symmetric_difference          | Return the symmetric difference of two sets as a new set. |
| difference_update             | Remove all elements of another set from this set. |
| intersection_update           | Update a set with the intersection of itself and another. |
| symmetric_difference_update   | Update a set with the symmetric difference of itself and another. |
| isdisjoint                    | Return True if two sets have a null intersection. |
| issubset                      | Report whether another set contains this set. |
| issuperset                    | Report whether this set contains another set. |


---
### ```add()```

Метод ```add()``` добавляет элемент во множество:
```python
In [1]: set1 = {10, 20, 30, 40}

In [2]: set1.add(50)

In [3]: set1
Out[3]: {10, 20, 30, 40, 50}
```

---
### ```discard()```

Метод ```discard()``` позволяет удалять элементы, не выдавая ошибку, если элемента в множестве нет:
```python
In [3]: set1
Out[3]: {10, 20, 30, 40, 50}

In [4]: set1.discard(55)

In [5]: set1
Out[5]: {10, 20, 30, 40, 50}

In [6]: set1.discard(50)

In [7]: set1
Out[7]: {10, 20, 30, 40}
```

---
### ```clear()```

Метод ```clear()``` очищает множество:
```python
In [8]: set1 = {10, 20, 30, 40}

In [9]: set1.clear()

In [10]: set1
Out[10]: set()
```

---
### Операции с множествами

Множества полезны тем, что с ними можно делать различные операции и находить объединение множеств, пересечение и так далее.

Объединение множеств можно получить с помощью метода ```union()``` или оператора ```|```:
```python
In [1]: vlans1 = {10, 20, 30, 50, 100}
In [2]: vlans2 = {100, 101, 102, 102, 200}

In [3]: vlans1.union(vlans2)
Out[3]: {10, 20, 30, 50, 100, 101, 102, 200}

In [4]: vlans1 | vlans2
Out[4]: {10, 20, 30, 50, 100, 101, 102, 200}
```

---
### Операции с множествами

Пересечение множеств можно получить с помощью метода ```intersection()``` или оператора ```&```:
```python
In [5]: vlans1 = {10, 20, 30, 50, 100}
In [6]: vlans2 = {100, 101, 102, 200}

In [7]: vlans1.intersection(vlans2)
Out[7]: {100}

In [8]: vlans1 & vlans2
Out[8]: {100}
```

---
### Варианты создания множества

---
### Варианты создания множества

Нельзя создать пустое множество с помощью литерала (так как в таком случае это будет не множество, а словарь):
```python
In [1]: set1 = {}

In [2]: type(set1)
Out[2]: dict
```

---
### Варианты создания множества

Пустое множество можно создать таким образом:
```python
In [3]: set2 = set()

In [4]: type(set2)
Out[4]: set
```

---
### Варианты создания множества

Множество из строки:
```python
In [5]: set('long long long long string')
Out[5]: {' ', 'g', 'i', 'l', 'n', 'o', 'r', 's', 't'}
```

---
### Варианты создания множества

Множество из списка:
```python
In [6]: set([10, 20, 30, 10, 10, 30])
Out[6]: {10, 20, 30}
```


---
## Преобразование типов

---
## Преобразование типов

В Python есть несколько полезных встроенных функций, которые позволяют преобразовать данные из одного типа в другой.

---
### ```int()```

```int()``` - преобразует строку в int:
```python
In [1]: int("10")
Out[1]: 10
```

С помощью функции int можно преобразовать и число в двоичной записи в десятичную (двоичная запись должна быть в виде строки) 
```python
In [2]: int("11111111", 2)
Out[2]: 255
```

---
### ```bin()```

Преобразовать десятичное число в двоичный формат можно с помощью ```bin()```:
```python
In [3]: bin(10)
Out[3]: '0b1010'

In [4]: bin(255)
Out[4]: '0b11111111'
```

---
### ```hex()```

Аналогичная функция есть и для преобразования в шестнадцатеричный формат:
```python
In [5]: hex(10)
Out[5]: '0xa'

In [6]: hex(255)
Out[6]: '0xff'
```

---
### ```list()```

Функция ```list()``` преобразует аргумент в список: 
```python
In [7]: list("string")
Out[7]: ['s', 't', 'r', 'i', 'n', 'g']

In [8]: list({1,2,3})
Out[8]: [1, 2, 3]

In [9]: list((1,2,3,4))
Out[9]: [1, 2, 3, 4]
```

---
### ```set()```

Функция ```set()``` преобразует аргумент в множество: 
```python
In [10]: set([1,2,3,3,4,4,4,4])
Out[10]: {1, 2, 3, 4}

In [11]: set((1,2,3,3,4,4,4,4))
Out[11]: {1, 2, 3, 4}

In [12]: set("string string")
Out[12]: {' ', 'g', 'i', 'n', 'r', 's', 't'}
```

Эта функция очень полезна, когда нужно получить уникальные элементы в последовательности.

---
### ```tuple()```

Функция ```tuple()``` преобразует аргумент в кортеж: 
```python
In [13]: tuple([1,2,3,4])
Out[13]: (1, 2, 3, 4)

In [14]: tuple({1,2,3,4})
Out[14]: (1, 2, 3, 4)

In [15]: tuple("string")
Out[15]: ('s', 't', 'r', 'i', 'n', 'g')
```

Это может пригодиться в том случае, если нужно получить неизменяемый объект.

---
### ```str()```

Функция ```str()``` преобразует аргумент в строку: 
```python
In [16]: str(10)
Out[16]: '10'
```


---
### Проверка типов

---
### Проверка типов

При преобразовании типов данных могут возникнуть ошибки такого рода:
```python
In [1]: int('a')
------------------------------------------------------
ValueError           Traceback (most recent call last)
<ipython-input-42-b3c3f4515dd4> in <module>()
----> 1 int('a')

ValueError: invalid literal for int() with base 10: 'a'
```

---
### ```isdigit()```

В Python такие методы есть. Например, чтобы проверить, состоит ли строка из одних цифр, можно использовать метод ```isdigit()```:
```python
In [2]: "a".isdigit()
Out[2]: False

In [3]: "a10".isdigit()
Out[3]: False

In [4]: "10".isdigit()
Out[4]: True
```

---
### ```isalpha()```

Метод ```isalpha()``` позволяет проверить, состоит ли строка из одних букв:
```python
In [7]: "a".isalpha()
Out[7]: True

In [8]: "a100".isalpha()
Out[8]: False

In [9]: "a--  ".isalpha()
Out[9]: False

In [10]: "a ".isalpha()
Out[10]: False
```

---
### ```isalnum()```

Метод ```isalnum()``` позволяет проверить, состоит ли строка из  букв и цифр:
```python
In [11]: "a".isalnum()
Out[1]: True

In [12]: "a10".isalnum()
Out[12]: True
```

---
### ```type()```

Иногда, в зависимости от результата, библиотека или функция может выводить разные типы объектов. Например, если объект один, возращается строка, если несколько, то возвращается кортеж.

Нам же надо построить ход программы по-разному, в зависимости от того, была ли возвращена строка или кортеж.

В этом может помочь функция ```type()```:
```python
In [13]: type("string")
Out[13]: str

In [14]: type("string") == str
Out[14]: True
```

---
### ```type()```

Аналогично с кортежем (и другими типами данных):
```python
In [15]: type((1, 2, 3))
Out[15]: tuple

In [16]: type((1, 2, 3)) == tuple
Out[16]: True

In [17]: type((1, 2, 3)) == list
Out[17]: False
```

