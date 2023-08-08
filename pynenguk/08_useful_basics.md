# Розпакування змінних


---
### Розпакування змінних

Розпакування змінних — це спеціальний синтаксис, який дозволяє призначати
елементи ітерованого об'єкта змінним.

```python
interface = ['FastEthernet0/1', '10.1.1.1', 'up', 'up']

intf, ip, status, protocol = interface
```

> Досить часто цей функціонал називають розпакуванням кортежів (tuple unpacking),
> але розпакування працює з будь-яким ітерованим об'єктом, а не лише з кортежами.



---
### Розпакування змінних

```python
In [1]: interface = ['FastEthernet0/1', '10.1.1.1', 'up', 'up']

In [2]: intf, ip, status, protocol = interface

In [3]: intf
Out[3]: 'FastEthernet0/1'

In [4]: ip
Out[4]: '10.1.1.1'
```

Такий варіант набагато зручніше використовувати, ніж використання індексів:

```python
In [5]: intf, ip, status, protocol = interface[0], interface[1], interface[2], interface[3]
```

---
### Розпакування змінних

При розпаковуванні змінних кожен елемент списку потрапляє у відповідну змінну.
Важливо враховувати, що змінних зліва має бути рівно стільки, скільки елементів
у списку.

Якщо змінних більше або менше, виникне виняток:

```python
In [6]: intf, ip, status = interface
------------------------------------------------------------
ValueError                 Traceback (most recent call last)
<ipython-input-11-a304c4372b1a> in <module>()
----> 1 intf, ip, status = interface

ValueError: too many values to unpack (expected 3)

In [7]: intf, ip, status, protocol, other = interface
------------------------------------------------------------
ValueError                 Traceback (most recent call last)
<ipython-input-12-ac93e78b978c> in <module>()
----> 1 intf, ip, status, protocol, other = interface

ValueError: not enough values to unpack (expected 5, got 4)
```

---
## Заміна непотрібних елементів `_`

Часто з усіх елементів ітерованого об'єкту потрібні лише деякі. У цьому випадку
синтаксис розпакування вимагає від вас вказати рівно стільки змінних, скільки є
елементів у ітерованому об'єкті.

Якщо, наприклад, з рядка line треба отримати лише VLAN, MAC та інтерфейс, треба
все одно вказати змінну для типу запису:

```python
In [8]: line = '100    01bb.c580.7000    DYNAMIC     Gi0/1'

In [9]: vlan, mac, item_type, intf = line.split()

In [10]: vlan
Out[10]: '100'

In [11]: intf
Out[11]: 'Gi0/1'
```

---
## Заміна непотрібних елементів `_`

Якщо тип запису не потрібний надалі, можна замінити змінну `item_type` нижнім підкресленням:

```python
vlan, mac, _, intf = line.split()
```

Таким чином, явно вказується, що цей елемент не потрібен.


---
## Заміна непотрібних елементів `_`

Підкреслення можна використовувати кілька разів:

```python
In [13]: dhcp = '00:09:BB:3D:D6:58   10.1.10.2        86250       dhcp-snooping   10    FastEthernet0/1'

In [14]: mac, ip, _, _, vlan, intf = dhcp.split()

In [15]: mac
Out[15]: '00:09:BB:3D:D6:58'

In [16]: vlan
Out[16]: '10'

```

---
## Використання `*`

Розпакування змінних підтримує спеціальний синтаксис, який дозволяє
розпаковувати кілька елементів на один.  Якщо поставити `*` перед іменем
змінної, до неї запишуться всі елементи, крім присвоєних явно.

Наприклад, так можна отримати перший елемент змінну `first`, а інші в `rest`:

```python
In [18]: vlans = [10, 11, 13, 30]

In [19]: first, *rest = vlans

In [20]: first
Out[20]: 10

In [21]: rest
Out[21]: [11, 13, 30]
```

---
## Використання `*`

При цьому змінна із зірочкою завжди буде списком:

```python
In [22]: vlans = (10, 11, 13, 30)

In [22]: first, *rest = vlans

In [23]: first
Out[23]: 10

In [24]: rest
Out[24]: [11, 13, 30]
```

---
## Використання `*`

Якщо елемент лише один, розпакування все одно відпрацює:

```python
In [25]: first, *rest = vlans

In [26]: first
Out[26]: 55

In [27]: rest
Out[27]: []
```

---
## Використання `*`

У виразі розпакування може бути лише одна змінна із зірочкою.

```python
In [28]: vlans = (10, 11, 13, 30)

In [29]: first, *rest, *others = vlans
  File "<ipython-input-37-dedf7a08933a>", line 1
    first, *rest, *others = vlans
                                 ^
SyntaxError: two starred expressions in assignment
```

---
## Використання `*`

Змінна із зірочкою може бути не тільки в кінці виразу:

```python
In [30]: vlans = (10, 11, 13, 30)

In [31]: *rest, last = vlans

In [32]: rest
Out[32]: [10, 11, 13]

In [33]: last
Out[33]: 30
```

---
## Використання `*`

Таким чином можна вказати, що потрібен перший, другий та останній елемент:

```python
In [34]: cdp = 'SW1      Eth 0/0     140     S I      WS-C3750-  Eth 0/1'

In [35]: name, l_intf, *other, r_intf = cdp.split()

In [36]: name
Out[36]: 'SW1'

In [37]: l_intf
Out[37]: 'Eth'

In [38]: r_intf
Out[38]: '0/1'
```

---
### Примеры распаковки

---
### Распаковка итерируемых объектов

Эти примеры показывают, что распаковывать можно не только списки, кортежи и строки, но и любой другой итерируемый объект.

Распаковка range:
```python
In [39]: first, *rest = range(1,6)

In [40]: first
Out[40]: 1

In [41]: rest
Out[41]: [2, 3, 4, 5]
```

---
### Распаковка итерируемых объектов

Распаковка zip:
```python
In [42]: a = [1, 2, 3, 4, 5]

In [43]: b = [100, 200, 300, 400, 500]

In [45]: list(zip(a, b))
Out[45]: [(1, 100), (2, 200), (3, 300), (4, 400), (5, 500)]

In [46]: first, *rest, last = zip(a, b)

In [47]: first
Out[47]: (1, 100)

In [48]: rest
Out[48]: [(2, 200), (3, 300), (4, 400)]

In [49]: last
Out[49]: (5, 500)
```

---
### Пример распаковки в цикле for

Пример цикла, который проходится по ключам:
```python
access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
access = {'0/12':10, '0/14':11, '0/16':17}

In [52]: for intf in access:
    ...:     print('interface FastEthernet' + intf)
    ...:     for command in access_template:
    ...:         if command.endswith('access vlan'):
    ...:             print(' {} {}'.format(command, access[intf]))
    ...:         else:
    ...:             print(' {}'.format(command))
    ...:
interface FastEthernet0/12
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet0/14
 switchport mode access
 switchport access vlan 11
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet0/16
 switchport mode access
 switchport access vlan 17
 spanning-tree portfast
 spanning-tree bpduguard enable

```

---
### Распаковка итерируемых объектов

Вместо этого можно проходиться по парам ключ-значение и сразу же распаковывать их в разные переменные:
```python
for intf, vlan in access.items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))

```

---
### Распаковка итерируемых объектов

Пример распаковки элементов списка в цикле:
```python
In [54]: table
Out[54]:
[['100', 'a1b2.ac10.7000', 'DYNAMIC', 'Gi0/1'],
 ['200', 'a0d4.cb20.7000', 'DYNAMIC', 'Gi0/2'],
 ['300', 'acb4.cd30.7000', 'DYNAMIC', 'Gi0/3'],
 ['100', 'a2bb.ec40.7000', 'DYNAMIC', 'Gi0/4'],
 ['500', 'aa4b.c550.7000', 'DYNAMIC', 'Gi0/5'],
 ['200', 'a1bb.1c60.7000', 'DYNAMIC', 'Gi0/6'],
 ['300', 'aa0b.cc70.7000', 'DYNAMIC', 'Gi0/7']]


In [55]: for line in table:
    ...:     vlan, mac, _, intf = line
    ...:     print(vlan, mac, intf)
    ...:
100 a1b2.ac10.7000 Gi0/1
200 a0d4.cb20.7000 Gi0/2
300 acb4.cd30.7000 Gi0/3
100 a2bb.ec40.7000 Gi0/4
500 aa4b.c550.7000 Gi0/5
200 a1bb.1c60.7000 Gi0/6
300 aa0b.cc70.7000 Gi0/7
```

---
### Распаковка итерируемых объектов

Но еще лучше сделать так:
```python
In [56]: for vlan, mac, _, intf in table:
    ...:     print(vlan, mac, intf)
    ...:
100 a1b2.ac10.7000 Gi0/1
200 a0d4.cb20.7000 Gi0/2
300 acb4.cd30.7000 Gi0/3
100 a2bb.ec40.7000 Gi0/4
500 aa4b.c550.7000 Gi0/5
200 a1bb.1c60.7000 Gi0/6
300 aa0b.cc70.7000 Gi0/7
```

---
## Спискові, словникові, множинні вирази

---
## Спискові, словникові, множинні вирази

Python підтримує спеціальні вирази, які дозволяють компактно створювати списки,
словники та множини.

```python
[int(vl) for vl in vlans]
{int(vl) for vl in vlans}
{key.lower(): value for key, value in r1.items()}
```


Англійською ці вирази називаються, відповідно:

-  List comprehensions (спискові вирази)
-  Dict comprehensions (словникові вирази)
-  Set comprehensions (множинні вирази)

Ці вирази не тільки дозволяють компактніше створювати відповідні об'єкти, але й
створюють їх швидше. І хоча спочатку вони вимагають певної звички використання
та розуміння, вони часто використовуються.

---
## Синтаксис

Синтаксис спискового виразу (синтаксис словникових та множинних виразів
відрізняється тільки дужками):

```python
[expression for item1 in iterable1 if condition1
            for item2 in iterable2 if condition2
            ...
            for itemN in iterableN if conditionN]
```

В найпростішому варіанті (один цикл без умови)

```python
[expression for item in iterable]
```

Цикл з умовою:

```python
[expression for item in iterable if condition]
```

---
## Спискові вирази (list comprehensions)

Списковий вираз дозволяє записати код:

```python
items = ["10", "20", "30", "1", "11", "100"]

vlans = []
for vl in items:
    vlans.append(int(vl))
```

Таким списковим виразом:

```python
items = ["10", "20", "30", "1", "11", "100"]
vlans = [int(vl) for vl in items]
```

Результат буде однаковим, список vlans:

```python
[10, 20, 30, 1, 11, 100]
```

---
## Спискові вирази (list comprehensions)

У спискових виразах можна використовувати умови if. Таким чином можна додавати
до списку лише деякі елементи з ітерованого об'єкту.

```python
items = ['10', '20', 'a', '30', 'b', '40']

only_digits = []

for item in items:
    if item.isdigit():
        only_digits.append(int(item))
```

Аналогічний варіант як списковий вираз:

```python
items = ['10', '20', 'a', '30', 'b', '40']
only_digits = [int(item) for item in items if item.isdigit()]
```

Результат
```python
[10, 20, 30, 40]
```



---
## Спискові вирази (list comprehensions)

Приклад використання спискового виразу для отримання значень із вкладених словників:

```python
london_co = {
    "r1": {
        "hostname": "london_r1",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "hostname": "london_r2",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "hostname": "london_sw1",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
    },
}

In [14]: [london_co[device]['ios'] for device in london_co]
Out[14]: ['15.4', '15.4', '3.6.XE']

In [15]: [london_co[device]['ip'] for device in london_co]
Out[15]: ['10.255.0.1', '10.255.0.2', '10.255.0.101']
```

---
## Спискові вирази (list comprehensions)

У списковому виразі можна використовувати кілька for.
Наприклад, у списку vlans є кілька вкладених списків з VLAN'ами:

```python
vlans = [[10, 21, 35], [101, 115, 150], [111, 40, 50]]
```

З цього списку потрібно сформувати один плоский список із номерами VLAN. Перший
варіант із циклами for:

```python
result = []

for vlan_list in vlans:
    for vlan in vlan_list:
        result.append(vlan)
```

Аналогічний варіант із списковим виразом:

```python
result = [vlan for vlan_list in vlans for vlan in vlan_list]
```

Результат:

```python
[10, 21, 35, 101, 115, 150, 111, 40, 50]
```


---
## Dict comprehensions (генераторы словарей)


---
### Dict comprehensions (генераторы словарей)

Генераторы словарей аналогичны генераторам списков, но они используются для создания словарей.

Например, такое выражение:
```python
d = {}

for num in range(1, 11):
    d[num] = num**2

In [29]: print(d)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```

---
### Dict comprehensions (генераторы словарей)

Можно заменить генератором словаря:
```python
d = {num: num**2 for num in range(1, 11)}

In [31]: print(d)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```

---
### Dict comprehensions (генераторы словарей)

Еще один пример, в котором надо преобразовать существующий словарь и перевести все ключи в нижний регистр.
Для начала, вариант решения без генератора словаря:
```python
r1 = {
	'IOS': '15.4',
	'IP': '10.255.0.1',
	'hostname': 'london_r1',
	'location': '21 New Globe Walk',
	'model': '4451',
	'vendor': 'Cisco',
}

lower_r1 = {}
for key, value in r1.items():
    lower_r1[str.lower(key)] = value

In [35]: lower_r1
Out[35]:
{'hostname': 'london_r1',
 'ios': '15.4',
 'ip': '10.255.0.1',
 'location': '21 New Globe Walk',
 'model': '4451',
 'vendor': 'Cisco'}

```

---
### Dict comprehensions (генераторы словарей)

Аналогичный вариант с помощью генератора словаря:
```python
r1 = {
	'IOS': '15.4',
	'IP': '10.255.0.1',
	'hostname': 'london_r1',
	'location': '21 New Globe Walk',
	'model': '4451',
	'vendor': 'Cisco',
}

lower_r1 = {str.lower(key): value for key, value in r1.items()}

In [38]: lower_r1
Out[38]:
{'hostname': 'london_r1',
 'ios': '15.4',
 'ip': '10.255.0.1',
 'location': '21 New Globe Walk',
 'model': '4451',
 'vendor': 'Cisco'}

```

---
### Dict comprehensions (генераторы словарей)

Как и list comprehensions, dict comprehensions можно делать вложенными.
Попробуем аналогичным образом преобразовать ключи во вложенных словарях:

```python
london_co = {
    'r1': {'IOS': '15.4',
           'IP': '10.255.0.1',
           'hostname': 'london_r1',
           'location': '21 New Globe Walk',
           'model': '4451',
           'vendor': 'Cisco'},
    'r2': {'IOS': '15.4',
           'IP': '10.255.0.2',
           'hostname': 'london_r2',
           'location': '21 New Globe Walk',
           'model': '4451',
           'vendor': 'Cisco'},
    'sw1': {'IOS': '3.6.XE',
            'IP': '10.255.0.101',
            'hostname': 'london_sw1',
            'location': '21 New Globe Walk',
            'model': '3850',
            'vendor': 'Cisco'},
}

In [40]: lower_london_co = {}

In [41]: for device, params in london_co.items():
    ...:     lower_london_co[device] = {}
    ...:     for key, value in params.items():
    ...:         lower_london_co[device][str.lower(key)] = value
    ...:

In [44]: pprint(lower_london_co)
{'r1': {'hostname': 'london_r1',
        'ios': '15.4',
        'ip': '10.255.0.1',
        'location': '21 New Globe Walk',
        'model': '4451',
        'vendor': 'Cisco'},
 'r2': {'hostname': 'london_r2',
        'ios': '15.4',
        'ip': '10.255.0.2',
        'location': '21 New Globe Walk',
        'model': '4451',
        'vendor': 'Cisco'},
 'sw1': {'hostname': 'london_sw1',
         'ios': '3.6.XE',
         'ip': '10.255.0.101',
         'location': '21 New Globe Walk',
         'model': '3850',
         'vendor': 'Cisco'}}
```

---
### Dict comprehensions (генераторы словарей)

Аналогичное преобразование с dict comprehensions:
```python
result = {
    device: {str.lower(key): value for key, value in params.items()}
    for device, params in london_co.items()
}

In [44]: pprint(result)
{'r1': {'hostname': 'london_r1',
        'ios': '15.4',
        'ip': '10.255.0.1',
        'location': '21 New Globe Walk',
        'model': '4451',
        'vendor': 'Cisco'},
 'r2': {'hostname': 'london_r2',
        'ios': '15.4',
        'ip': '10.255.0.2',
        'location': '21 New Globe Walk',
        'model': '4451',
        'vendor': 'Cisco'},
 'sw1': {'hostname': 'london_sw1',
         'ios': '3.6.XE',
         'ip': '10.255.0.101',
         'location': '21 New Globe Walk',
         'model': '3850',
         'vendor': 'Cisco'}}
```

---
## Set comprehensions (генераторы множеств)

---
### Set comprehensions (генераторы множеств)

Генераторы множеств в целом аналогичны генераторам списков.

Например, надо получить множество с уникальными номерами VLAN'ов:
```python
vlans = [10, '30', 30, 10, '56']
unique_vlans = {int(vlan) for vlan in vlans}

In [47]: unique_vlans
Out[47]: {10, 30, 56}
```

---
### Set comprehensions (генераторы множеств)

Аналогичное решение, без использования set comprehensions:
```python
vlans = [10, '30', 30, 10, '56']
unique_vlans = set()

for vlan in vlans:
    unique_vlans.add(int(vlan))

In [51]: unique_vlans
Out[51]: {10, 30, 56}

```

