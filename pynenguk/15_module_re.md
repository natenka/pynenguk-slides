# Python для мережевих інженерів 

---
# Регулярні вирази

---
## Модуль re

---
## Модуль re

Основні функції модуля __re__:

* search - шукає перший збіг з шаблоном
* findall - шукає всі збіги з шаблоном. Повертає збіги у вигляді списку рядків
* finditer - шукає всі збіги з шаблоном. Повертає ітератор із збігами (об’єкти Match)
* match - шукає збіг на початку рядка
* fullmatch - весь рядок повинен відповідати описаному регулярному виразу
* compile - компілює регулярний вираз. Потім можна застосувати всі перелічені функції до отриманого об’єкту


---
## Модуль re

Крім функцій пошуку збігів, модуль має наступні функції:

* ```re.sub``` - для заміни в рядках
* ```re.split``` - для розділення рядків на частини

---
## raw string

У Python для роботи з регулярними виразами використовується модуль re.
Відповідно, для початку роботи з регулярними виразами треба його
імпортувати.

У Python деякі символи рядка треба екранувати, щоб вони сприймалися
правильно. До таких символів відноситься, наприклад, ``\``. Щоб написати правильно
рядок, в якому знаходяться два символи ``\\``, обидва символи треба екранувати і в
результаті вийде рядок виду: ``\\\\data``. Натомість, можна використовувати
raw-рядок і тоді кожен символ буде сприйматися як написано. Raw-рядки
відрізняються від звичайних тим, що при створенні рядка, на початку пишеться літера r:

```python
In [3]: r"\\data"
Out[3]: '\\\\data'
```


Так як у регулярних виразах постійно використовується ``\``, завжди
використовуйте raw-рядки для опису регулярних виразів. Деякі вирази
правильно відпрацюють і без raw-рядків, але, використання raw-рядків для
регулярних виразів це гарний тон.

---
## Об'єкт Match

---
### Об'єкт Match

У модулі re кілька функцій повертають об'єкт Match, якщо знайдено збіг:
* search
* match
* finditer повертає ітератор з об'єктами Match

---
### Об'єкт Match

Приклад об'єкту Match:
```python
In [1]: log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'

In [2]: match = re.search('Host (\S+) in vlan (\d+) .* port (\S+) and port (\S+)', log)

In [3]: match
Out[3]: <_sre.SRE_Match object; span=(47, 124), match='Host f03a.b216.7ad7 in vlan 10 is flapping betwee>

```

Вивід у 3 рядку просто відображає інформацію про об'єкт.
Тому не варто покладатися на те, що відображається в частині match, так як рядок, що відображається, обрізається за фіксованою кількістю знаків.

---
### group()

Метод group повертає підрядок, який збігся з шаблоном або з виразом у групі.

Якщо метод викликається без аргументів, відображається весь підрядок:
```python
In [4]: match.group()
Out[4]: 'Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'

```

---
### group()

Фактично, у цьому випадку метод group викликається з групою 0:

```python
In [13]: match.group(0)
Out[13]: 'Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
```

---
### group()

Інші номери відображають лише вміст відповідної групи:
```python
In [14]: match.group(1)
Out[14]: 'f03a.b216.7ad7'

In [15]: match.group(2)
Out[15]: '10'

In [16]: match.group(3)
Out[16]: 'Gi0/5'

In [17]: match.group(4)
Out[17]: 'Gi0/15'
```

---
### group()

Якщо викликати метод group з номером групи, який перевищує кількість існуючих груп, виникне помилка:
```python
In [18]: match.group(5)
-----------------------------------------------------------------
IndexError                      Traceback (most recent call last)
<ipython-input-18-9df93fa7b44b> in <module>()
----> 1 match.group(5)

IndexError: no such group
```

---
### group()

Якщо викликати метод із кількома номерами груп, результатом буде кортеж рядків, які відповідають збігам:

```python
In [19]: match.group(1, 2, 3)
Out[19]: ('f03a.b216.7ad7', '10', 'Gi0/5')
```

---
### group()

Якщо група описує частину шаблону та збігів було кілька, метод відобразить останній збіг:
```python
In [1]: log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'

In [44]: match = re.search('Host (\w{4}\.)+', log)

In [45]: match.group(1)
Out[46]: 'b216.'
```

Такий вивід був отриманий через те, що вираз у дужках описує 4 літери або цифри, а після них стоїть плюс.
Відповідно, спочатку перша частина MAC-адреси відповідала виразу в дужках, потім друга.
Але запам'ятовується і повертається тільки останній збіг з групою.

---
### group()

Якщо у виразі використовувалися іменовані групи, методу group можна передати ім'я групи та отримати відповідний підрядок:
```python
In [1]: log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'

In [55]: match = re.search('Host (?P<mac>\S+) '
    ...:                   'in vlan (?P<vlan>\d+) .* '
    ...:                   'port (?P<int1>\S+) '
    ...:                   'and port (?P<int2>\S+)',
    ...:                   log)
    ...:

In [53]: match.group('mac')
Out[53]: 'f03a.b216.7ad7'

In [54]: match.group('int2')
Out[54]: 'Gi0/15'
```

---
### group()

Але ці групи доступні і за номером:
```python
In [58]: match.group(3)
Out[58]: 'Gi0/5'

In [59]: match.group(4)
Out[59]: 'Gi0/15'
```


---
### groups()

Метод groups() повертає кортеж з рядками, в якому елементи - це ті підрядки, які потрапили до відповідних груп:
```python
In [63]: log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'

In [64]: match = re.search('Host (\S+) '
    ...:                   'in vlan (\d+) .* '
    ...:                   'port (\S+) '
    ...:                   'and port (\S+)',
    ...:                   log)
    ...:

In [65]: match.groups()
Out[65]: ('f03a.b216.7ad7', '10', 'Gi0/5', 'Gi0/15')

```

---
### groups()

Метод груп має необов'язковий параметр - default. Це працює в ситуації, коли все, що потрапляє в групу, є необов’язковим.

Наприклад, з таким рядком буде збіг і в першій групі, і в другій:

```python
In [76]: line = '100     aab1.a1a1.a5d3    FastEthernet0/1'

In [77]: match = re.search('(\d+) +(\w+)?', line)

In [78]: match.groups()
Out[78]: ('100', 'aab1')
```

---
### groups()

Якщо після пробілу в рядку нічого немає, нічого не буде включено до групи.
Але збіг буде, оскільки регулярний вираз описує, що група необов’язкова:

```python
In [80]: line = '100     '

In [81]: match = re.search('(\d+) +(\w+)?', line)

In [82]: match.groups()
Out[82]: ('100', None)
```

Відповідно, для другої групи значення буде None.

---
### groups()

Но если передать методу groups аргумент, он будет возвращаться вместо None:
```python
In [83]: line = '100     '

In [84]: match = re.search('(\d+) +(\w+)?', line)

In [85]: match.groups(0)
Out[85]: ('100', 0)

In [86]: match.groups('No match')
Out[86]: ('100', 'No match')
```

---
### groupdict()

Але якщо передати методу groups аргумент, він повертатиметься замість None:
```python
In [63]: log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'

In [88]: match = re.search('Host (?P<mac>\S+) '
    ...:                   'in vlan (?P<vlan>\d+) .* '
    ...:                   'port (?P<int1>\S+) '
    ...:                   'and port (?P<int2>\S+)',
    ...:                   log)
    ...:

In [89]: match.groupdict()
Out[89]: {'int1': 'Gi0/5', 'int2': 'Gi0/15', 'mac': 'f03a.b216.7ad7', 'vlan': '10'}
```



---
## ```re.search```

---
### ```re.search```

Функція ``search``:
* використовується для пошуку підрядка, який відповідає шаблону
* повертає об'єкт Match, якщо підрядок знайдено
* повертає ``None``, якщо підрядок не знайдено

Функція search підходить у тому випадку, коли треба знайти лише один збіг у рядку.


---
### ```re.search```


```python
import re

regex = ('Host \S+ '
         'in vlan (\d+) '
         'is flapping between port '
         '(\S+) and port (\S+)')

ports = set()

with open('log.txt') as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            vlan = match.group(1)
            ports.add(match.group(2))
            ports.add(match.group(3))

print('Петля між портами {} у VLAN {}'.format(', '.join(ports), vlan))
```

---
## ```re.finditer```

---
### ```re.finditer```

Функція ```finditer```:
* використовується для пошуку всіх неперекриваючих збігів у шаблоні
* повертає ітератор з об’єктами Match

Функція finditer чудово підходить для обробки тих команд, вивід яких відображається у стовпцях.
Наприклад, sh ip int br, sh mac address-table тощо.
У цьому випадку його можна застосувати до всього виводу команди.


---
### ```re.finditer()```

Приклад  sh ip int br:
```python
In [8]: sh_ip_int_br = '''
R1#show ip interface brief
Interface             IP-Address      OK? Method Status           Protocol
FastEthernet0/0       15.0.15.1       YES manual up               up
FastEthernet0/1       10.0.12.1       YES manual up               up
FastEthernet0/2       10.0.13.1       YES manual up               up
FastEthernet0/3       unassigned      YES unset  up               up
Loopback0             10.1.1.1        YES manual up               up
Loopback100           100.0.0.1       YES manual up               up
'''
```

---
### ```re.finditer()```

Регулярний вираз для обробки виводу:
```python
In [9]: result = re.finditer('(\S+) +'
   ...:                      '([\d.]+) +'
   ...:                      '\w+ +\w+ +'
   ...:                      '(up|down|administratively down) +'
   ...:                      '(up|down)',
   ...:                      sh_ip_int_br)
   ...:
```

---
### ```re.finditer()```

Змінна результату містить ітератор:
```python
In [12]: result
Out[12]: <callable_iterator at 0xb583f46c>
```

---
### ```re.finditer()```

Ітератор містить об’єкти Match:
```python
In [16]: groups = []

In [18]: for match in result:
    ...:     print(match)
    ...:     groups.append(match.groups())
    ...:
<_sre.SRE_Match object; span=(103, 171), match='FastEthernet0/0       15.0.15.1       YES manual >
<_sre.SRE_Match object; span=(172, 240), match='FastEthernet0/1       10.0.12.1       YES manual >
<_sre.SRE_Match object; span=(241, 309), match='FastEthernet0/2       10.0.13.1       YES manual >
<_sre.SRE_Match object; span=(379, 447), match='Loopback0             10.1.1.1        YES manual >
<_sre.SRE_Match object; span=(448, 516), match='Loopback100           100.0.0.1       YES manual >
```

---
### ```re.finditer()```

Тепер у списку groups знаходяться кортежі з рядками, які потрапили до груп:
```python
In [19]: groups
Out[19]:
[('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
 ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
 ('Loopback0', '10.1.1.1', 'up', 'up'),
 ('Loopback100', '100.0.0.1', 'up', 'up')]

```

---
### ```re.finditer()```

Такий результат можна отримати за допомогою генератора списків:
```python
In [20]: regex = '(\S+) +([\d.]+) +\w+ +\w+ +(up|down|administratively down) +(up|down)'

In [21]: result = [match.groups() for match in re.finditer(regex, sh_ip_int_br)]

In [22]: result
Out[22]:
[('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
 ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
 ('Loopback0', '10.1.1.1', 'up', 'up'),
 ('Loopback100', '100.0.0.1', 'up', 'up')]

```

---
## ```re.findall()```


---
### ```re.findall()```

Функція ```findall()'':
* використовується для пошуку всіх неперекриваючих збігів у шаблоні
* повертає:
  * список рядків, які описуються регулярним виразом, якщо в регулярному виразі немає груп
  * список рядків, які відповідають регулярному виразу в групі, якщо в регулярному виразі є одна група
  * список кортежів, що містять рядки, які відповідають виразу в групі, якщо груп декілька


---
### ```re.findall()```

```python
In [2]: mac_address_table = open('CAM_table.txt').read()

In [3]: print(mac_address_table)
sw1#sh mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
 100    a1b2.ac10.7000    DYNAMIC     Gi0/1
 200    a0d4.cb20.7000    DYNAMIC     Gi0/2
 300    acb4.cd30.7000    DYNAMIC     Gi0/3
 100    a2bb.ec40.7000    DYNAMIC     Gi0/4
 500    aa4b.c550.7000    DYNAMIC     Gi0/5
 200    a1bb.1c60.7000    DYNAMIC     Gi0/6
 300    aa0b.cc70.7000    DYNAMIC     Gi0/7

```

---
### ```re.findall()```

Первый пример - регулярное выражение без групп.
В этом случае findall возвращает список строк, которые совпали с регулярным выражением.

Например, с помощью findall можно получить список строк с соответствиями vlan - mac - interface и избавиться от заголовка в выводе команды:


Перший приклад — регулярний вираз без груп.
У цьому випадку findall повертає список рядків, які відповідають регулярному виразу.

Наприклад, використовуючи findalд, можна отримати список рядків з зіставленням vlan – mac – interface і позбутися заголовка у виведенні команди:

```python
In [4]: re.findall('\d+ +\S+ +\w+ +\S+', mac_address_table)
Out[4]:
['100    a1b2.ac10.7000    DYNAMIC     Gi0/1',
 '200    a0d4.cb20.7000    DYNAMIC     Gi0/2',
 '300    acb4.cd30.7000    DYNAMIC     Gi0/3',
 '100    a2bb.ec40.7000    DYNAMIC     Gi0/4',
 '500    aa4b.c550.7000    DYNAMIC     Gi0/5',
 '200    a1bb.1c60.7000    DYNAMIC     Gi0/6',
 '300    aa0b.cc70.7000    DYNAMIC     Gi0/7']
```


---
### ```re.findall()```

Якщо вираз використовує одну групу, findall повертає список рядків, які відповідають виразу в групі:
```python
In [5]: re.findall('\d+ +(\S+) +\w+ +\S+', mac_address_table)
Out[5]:
['a1b2.ac10.7000',
 'a0d4.cb20.7000',
 'acb4.cd30.7000',
 'a2bb.ec40.7000',
 'aa4b.c550.7000',
 'a1bb.1c60.7000',
 'aa0b.cc70.7000']
```

У цьому випадку findall шукає збіг всього рядка, але повертає результат, подібний до методу groups() об’єкта Match.

---
### ```re.findall()```

Якщо є кілька груп, findall поверне список кортежів:
```python
In [6]: re.findall('(\d+) +(\S+) +\w+ +(\S+)', mac_address_table)
Out[6]:
[('100', 'a1b2.ac10.7000', 'Gi0/1'),
 ('200', 'a0d4.cb20.7000', 'Gi0/2'),
 ('300', 'acb4.cd30.7000', 'Gi0/3'),
 ('100', 'a2bb.ec40.7000', 'Gi0/4'),
 ('500', 'aa4b.c550.7000', 'Gi0/5'),
 ('200', 'a1bb.1c60.7000', 'Gi0/6'),
 ('300', 'aa0b.cc70.7000', 'Gi0/7')]

```

Якщо такі особливості функції findall заважають отримати бажаний результат, то краще скористатися функцією finditer.
Але іноді така поведінка є доречною та зручною у використанні.

---
## Прапори

---
### Прапори

Під час використання функцій або створення скомпільованого регулярного виразу можна вказати додаткові позначки, які впливають на поведінку регулярного виразу.

Модуль re підтримує наступні прапори (у дужках наведено коротку версію позначення прапора):
* re.ASCII (re.A)
* re.IGNORECASE (re.I)
* re.MULTILINE (re.M)
* re.DOTALL (re.S)
* re.VERBOSE (re.X)
* re.LOCALE (re.L)
* re.DEBUG


---
## re.split

---
### re.split

Функція split працює подібно до методу split на рядках.  
Але у функції re.split ви можете використовувати регулярні вирази, що означає, що ви можете розділити рядок на частини відповідно до складніших умов.

Наприклад, рядок ospf_route має бути розбитий на елементи пробілами (як у методі str.split):

```python
In [1]: ospf_route = 'O     10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

In [2]: re.split(' +', ospf_route)
Out[2]:
['O',
 '10.0.24.0/24',
 '[110/41]',
 'via',
 '10.0.13.3,',
 '3d18h,',
 'FastEthernet0/0']
```

---
### re.split

Подібним чином можна позбутися ком:

```python
In [3]: re.split('[ ,]+', ospf_route)
Out[3]:
['O',
 '10.0.24.0/24',
 '[110/41]',
 'via',
 '10.0.13.3',
 '3d18h',
 'FastEthernet0/0']
```

---
### re.split

Функція split має особливість роботи з групами (вирази в круглих дужках).  
Якщо вказати те ж таки вираз за допомогою круглих дужок, у кінцевий список потраплять і роздільники.

Наприклад, у виразі як роздільник додано слово via:

```python
In [5]: re.split('(via|[ ,\[\]])+', ospf_route)
Out[5]:
['O',
 ' ',
 '10.0.24.0/24',
 '[',
 '110/41',
 ' ',
 '10.0.13.3',
 ' ',
 '3d18h',
 ' ',
 'FastEthernet0/0']
```

---
### re.split

Для відключення такої поведінки треба зробити групу не Capture.  
Тобто відключити запам'ятовування елементів групи:


```python
In [6]: re.split('(?:via|[ ,\[\]])+', ospf_route)
Out[6]: ['O', '10.0.24.0/24', '110/41', '10.0.13.3', '3d18h', 'FastEthernet0/0']
```

---
## re.sub

---
### re.sub

Функція re.sub працює подібно до методу replace у рядках.  
Але у функції re.sub ви можете використовувати регулярні вирази, що означає, що ви можете робити заміни на основі складніших умов.

Замініть коми, квадратні дужки та слово via пробілом у рядку ospf_route:


```python
In [7]: ospf_route = 'O    10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

In [8]: re.sub('(via|[,\[\]])', ' ', ospf_route)
Out[8]: 'O        10.0.24.0/24  110/41    10.0.13.3  3d18h  FastEthernet0/0'
```

---
### re.sub

```python
In [9]: mac_table = '''
   ...:  100    aabb.cc10.7000    DYNAMIC     Gi0/1
   ...:  200    aabb.cc20.7000    DYNAMIC     Gi0/2
   ...:  300    aabb.cc30.7000    DYNAMIC     Gi0/3
   ...:  100    aabb.cc40.7000    DYNAMIC     Gi0/4
   ...:  500    aabb.cc50.7000    DYNAMIC     Gi0/5
   ...:  200    aabb.cc60.7000    DYNAMIC     Gi0/6
   ...:  300    aabb.cc70.7000    DYNAMIC     Gi0/7
   ...: '''

In [4]: print(re.sub(' *(\d+) +'
   ...:              '([a-f0-9]+)\.'
   ...:              '([a-f0-9]+)\.'
   ...:              '([a-f0-9]+) +\w+ +'
   ...:              '(\S+)',
   ...:              r'\1 \2:\3:\4 \5',
   ...:              mac_table))
   ...:

100 aabb:cc10:7000 Gi0/1
200 aabb:cc20:7000 Gi0/2
300 aabb:cc30:7000 Gi0/3
100 aabb:cc40:7000 Gi0/4
500 aabb:cc50:7000 Gi0/5
200 aabb:cc60:7000 Gi0/6
300 aabb:cc70:7000 Gi0/7
```

