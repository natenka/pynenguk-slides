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

Здатність змінюватись

* змінювані (списки, словники та множини)
* незмінні (числа, рядки та кортежі)

Впорядкованість

* упорядковані (списки, кортежі, рядки та словники)
* невпорядковані (множини)


| Назва    | Назва        | Приклад |
|-------------|-----------------|--------------|
| String      | рядок          | ``"interface Gi0/0"`` |
|             |                 |
| List        | список          | ``[1, 2, 3]`` |
|             |                 |
| Dictionary  | словник         | ``{"username": "user1", "permissions": 100}`` |
|             |                 |
| Tuple       | кортеж          | ``("line console 0", "login local")`` |
|             |                 |
| Set         | множина       | ``{3, 10, 100, 4, 5}`` |
|             |                 |


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

| Назва    | Назва        | Приклад |
|-------------|-----------------|--------------|
| String      | рядок          | ``"interface Gi0/0"`` |
|             |                 |
| List        | список          | ``[1, 2, 3]`` |
|             |                 |
| Dictionary  | словник         | ``{"username": "user1", "permissions": 100}`` |
|             |                 |
| Tuple       | кортеж          | ``("line console 0", "login local")`` |
|             |                 |
| Set         | множина       | ``{3, 10, 100, 4, 5}`` |
|             |                 |


---
## Типи даних у Python

|             |               |
|-------------|--------------|
| String      | Для зберігання тексту та довільних даних, для яких у Python немає типу |
| List        | Набір даних, часто однотипних даних: список вланів, команд, рядків файлу |
| Dictionary  | Використовується для даних типу поле: значення |
| Tuple       | Незмінний набір даних, який часто повертається із зовнішніх джерел - БД, CSV.
|             | Також використовується коли дані це набір значень: ``(x, y)`` |
| Set         | Для збереження унікальних даних. Плюс часто використовується |
|             | для операцій з множинами |


|             |              |
|-------------|--------------|
| String      | "interface Gi0/0" |
| List        | [1, 2, 3] |
| Dictionary  | {"username": "user1", "permissions": 100} |
| Tuple       | ("line console 0", "login local") |
| Set         | {3, 10, 100, 4, 5} |



---
## Рядки (Strings)

---
### Рядки

Рядок в Python:

* послідовність символів у лапках
* незмінний упорядкований тип даних

```python
In [9]: 'Hello'
Out[9]: 'Hello'

In [10]: "Hello"
Out[10]: 'Hello'
```

---
### Рядки

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
### Дії з рядками

```
In [10]: from rich import inspect

In [13]: inspect(str, methods=True)
╭───────────────────────────────────────────────────────────── <class 'str'> ─────────────────────────────────────────────────────────────╮
│ def str(...)                                                                                                                            │
│                                                                                                                                         │
│ str(object='') -> str                                                                                                                   │
│ str(bytes_or_buffer[, encoding[, errors]]) -> str                                                                                       │
│                                                                                                                                         │
│   capitalize = def capitalize(self, /): Return a capitalized version of the string.                                                     │
│     casefold = def casefold(self, /): Return a version of the string suitable for caseless comparisons.                                 │
│       center = def center(self, width, fillchar=' ', /): Return a centered string of length width.                                      │
│        count = def count(...) S.count(sub[, start[, end]]) -> int                                                                       │
│       encode = def encode(self, /, encoding='utf-8', errors='strict'): Encode the string using the codec registered for encoding.       │
│     endswith = def endswith(...) S.endswith(suffix[, start[, end]]) -> bool                                                             │
│   expandtabs = def expandtabs(self, /, tabsize=8): Return a copy where all tab characters are expanded using spaces.                    │
│         find = def find(...) S.find(sub[, start[, end]]) -> int                                                                         │
│       format = def format(...) S.format(*args, **kwargs) -> str                                                                         │
│   format_map = def format_map(...) S.format_map(mapping) -> str                                                                         │
│        index = def index(...) S.index(sub[, start[, end]]) -> int                                                                       │
│      isalnum = def isalnum(self, /): Return True if the string is an alpha-numeric string, False otherwise.                             │
│      isalpha = def isalpha(self, /): Return True if the string is an alphabetic string, False otherwise.                                │
│      isascii = def isascii(self, /): Return True if all characters in the string are ASCII, False otherwise.                            │
│    isdecimal = def isdecimal(self, /): Return True if the string is a decimal string, False otherwise.                                  │
│      isdigit = def isdigit(self, /): Return True if the string is a digit string, False otherwise.                                      │
│ isidentifier = def isidentifier(self, /): Return True if the string is a valid Python identifier, False otherwise.                      │
│      islower = def islower(self, /): Return True if the string is a lowercase string, False otherwise.                                  │
│    isnumeric = def isnumeric(self, /): Return True if the string is a numeric string, False otherwise.                                  │
│  isprintable = def isprintable(self, /): Return True if the string is printable, False otherwise.                                       │
│      isspace = def isspace(self, /): Return True if the string is a whitespace string, False otherwise.                                 │
│      istitle = def istitle(self, /): Return True if the string is a title-cased string, False otherwise.                                │
│      isupper = def isupper(self, /): Return True if the string is an uppercase string, False otherwise.                                 │
│         join = def join(self, iterable, /): Concatenate any number of strings.                                                          │
│        ljust = def ljust(self, width, fillchar=' ', /): Return a left-justified string of length width.                                 │
│        lower = def lower(self, /): Return a copy of the string converted to lowercase.                                                  │
│       lstrip = def lstrip(self, chars=None, /): Return a copy of the string with leading whitespace removed.                            │
│    maketrans = def maketrans(...) Return a translation table usable for str.translate().                                                │
│    partition = def partition(self, sep, /): Partition the string into three parts using the given separator.                            │
│      replace = def replace(self, old, new, count=-1, /): Return a copy with all occurrences of substring old replaced by new.           │
│        rfind = def rfind(...) S.rfind(sub[, start[, end]]) -> int                                                                       │
│       rindex = def rindex(...) S.rindex(sub[, start[, end]]) -> int                                                                     │
│        rjust = def rjust(self, width, fillchar=' ', /): Return a right-justified string of length width.                                │
│   rpartition = def rpartition(self, sep, /): Partition the string into three parts using the given separator.                           │
│       rsplit = def rsplit(self, /, sep=None, maxsplit=-1): Return a list of the words in the string, using sep as the delimiter string. │
│       rstrip = def rstrip(self, chars=None, /): Return a copy of the string with trailing whitespace removed.                           │
│        split = def split(self, /, sep=None, maxsplit=-1): Return a list of the words in the string, using sep as the delimiter string.  │
│   splitlines = def splitlines(self, /, keepends=False): Return a list of the lines in the string, breaking at line boundaries.          │
│   startswith = def startswith(...) S.startswith(prefix[, start[, end]]) -> bool                                                         │
│        strip = def strip(self, chars=None, /): Return a copy of the string with leading and trailing whitespace removed.                │
│     swapcase = def swapcase(self, /): Convert uppercase characters to lowercase and lowercase characters to uppercase.                  │
│        title = def title(self, /): Return a version of the string where each word is titlecased.                                        │
│    translate = def translate(self, table, /): Replace each character in the string using the given translation table.                   │
│        upper = def upper(self, /): Return a copy of the string converted to uppercase.                                                  │
│        zfill = def zfill(self, width, /): Pad a numeric string with zeros on the left, to fill a field of the given width.              │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

---
### Рядки. Індекс

```python
In [20]: string1 = 'interface FastEthernet1/0'

In [21]: string1[0]
Out[21]: 'i'

In [22]: string1[1]
Out[22]: 'n'

In [23]: string1[-1]
Out[23]: '0'
```

---
### Рядки. Зрізи

```python
In [24]: string1[0:9]
Out[24]: 'interface'

In [25]: string1[10:22]
Out[25]: 'FastEthernet'

In [26]:  string1[10:]
Out[26]: 'FastEthernet1/0'

In [27]: string1[-3:]
Out[27]: '1/0'
```

---
### Рядки

```python
In [28]: a = '0123456789'

In [29]: a[::]
Out[29]: '0123456789'

In [30]: a[::-1]
Out[30]: '9876543210'
```


---
### Рядки

Рядки можна підсумовувати. Тоді вони об'єднуються в один рядок:
```python
In [14]: intf = 'interface'

In [15]: tun = 'Tunnel0'

In [16]: intf + tun
Out[16]: 'interfaceTunnel0'

In [17]: intf + ' ' + tun
Out[17]: 'interface Tunnel0'
```


Рядок можна множити на число. У цьому випадку рядок повторюється вказану
кількість разів:
```python
In [18]: intf * 5
Out[18]: 'interfaceinterfaceinterfaceinterfaceinterface'

In [19]: '#' * 40
Out[19]: '########################################'
```

---
### Корисні методи для роботи з рядками

При автоматизації дуже часто треба буде працювати з рядками, так як
конфігураційний файл, виведення команд і команди, що відправляються - це рядки.
Знання різних методів (тобто дій), які можна застосовувати до рядків, допомагає
ефективніше працювати з ними. Рядки незмінний тип даних, тому всі методи, які
перетворюють рядок повертають новий рядок, а вихідний рядок залишається
незмінним.


---
### Корисні методи для роботи з рядками

|             |  Поділ рядка на частини |
|:------------|:-----------------------------------------------------------------------------|
| split       | Return a list of the words in the string, using sep as the delimiter string. |
| splitlines  | Return a list of the lines in the string, breaking at line boundaries.       |
| partition   | Partition the string into three parts using the given separator.             |
| rpartition  | Partition the string into three parts using the given separator.             |
| rsplit      | Return a list of the words in the string, using sep as the delimiter string. |
|             |  |


| | Видалення символів whitespace |
|:-------|:--------------------------------------------------------------------------|
| strip  | Return a copy of the string with leading and trailing whitespace removed. |
| rstrip | Return a copy of the string with trailing whitespace removed.             |
| lstrip | Return a copy of the string with leading whitespace removed.              |
|        |  |

| |  Перевірка початку/кінця рядка |
|----------------|:-------------------------------------------------------------------------|
| startswith     | Return True if S starts with the specified prefix, False otherwise.      |
| endswith       | Return True if S ends with the specified prefix, False otherwise.      |
|        |  |

---
### Корисні методи для роботи з рядками

|  | Перевірка того, що знаходиться у рядку |
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


|            | Перетворення регістрів |
|:-----------|:---------------------------------------------------------------------------------|
| lower      | Return a copy of the string converted to lowercase.                              |
| capitalize | Return a capitalized version of the string.                                      |
| swapcase   | Convert uppercase characters to lowercase and lowercase characters to uppercase. |
| title      | Return a version of the string where each word is titlecased.                    |
| upper      | Return a copy of the string converted to uppercase.                              |
| casefold   | Return a version of the string suitable for caseless comparisons.                |
|        |  |



---
### Корисні методи для роботи з рядками


|  | Вирівнювання тексту |
|:-------------------------------------|:---------------------------------------------------------------------------------|
| center | Return a centered string of length width.                                        |
| ljust  | Return a left-justified string of length width.                                  |
| rjust  | Return a right-justified string of length width.                                 |
|        |  |


| | Пошук, підрахунок елементів |
|:--------|:-------------------------------------|
| count   | S.count(sub[, start[, end]]) -> int  |
| find    | S.find(sub[, start[, end]]) -> int   |
| index   | S.index(sub[, start[, end]]) -> int  |
| rfind   | S.rfind(sub[, start[, end]]) -> int  |
| rindex  | S.rindex(sub[, start[, end]]) -> int |
|        |  |

| | Інші методи |
|:----------------------------------------|:------------------------------------|
| replace | S.replace(old, new)                  |
| join        | Concatenate any number of strings.                                           |
| zfill                | Pad a numeric string with zeros on the left, to fill a field of the given width. |
| expandtabs | Return a copy where all tab characters are expanded using spaces.       |
| format     | S.format(*args, **kwargs) -> str  |
| format_map | S.format_map(mapping) -> str  |
| maketrans  | Return a translation table usable for str.translate(). |
| translate  | Replace each character in the string using the given translation table. |
| encode   | Encode the string using the codec registered for encoding.              |


---
### ```upper(), lower(), swapcase(), capitalize()```

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
### Рядки - незмінний тип даних

```python
In [31]: string1 = string1.upper()

In [32]: print(string1)
FASTETHERNET
```

---
### ```startswith(), endswith()```

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
### ``replace()``

```python
In [45]: string1 = 'FastEthernet0/1'

In [46]: string1.replace('Fast', 'Gigabit')
Out[46]: 'GigabitEthernet0/1'
```

---
### ``strip()``

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
### ``strip()``

```python
In [51]: ad_metric = '[110/1045]'

In [52]: ad_metric.strip('[]')
Out[52]: '110/1045'
```

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

```python
In [58]: sh_ip_int_br = "FastEthernet0/0       15.0.15.1    YES manual up         up"

In [59]: sh_ip_int_br.split()
Out[59]: ['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up']
```

---
## Форматування рядків

---
## Форматування рядків

* з оператором ``%`` - старіший варіант
* метод ``format`` - відносно новий варіант
* f-рядки – новий варіант, який з'явився у Python 3.6

```python
template = """
IP: {}
Mask: {}
Broadcast: {}
"""

print(template.format(ip, mask, broadcast))
print(template.format("10.1.1.1", 24, "10.1.1.255"))
```

```
IP: 10.1.1.1
Mask: 24
Broadcast: 10.1.1.255
```

---
## Форматування рядків з оператором `%`

```python
In [1]: ip = "10.1.1.1"

In [2]: mask = 24

In [5]: "IP: %s, mask: %d" % (ip, mask)
Out[5]: 'IP: 10.1.1.1, mask: 24'
```

Можна зустріти в налаштуваннях logging:

```python
logging.basicConfig(
    format='%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
)
```

---
## Форматування рядків із методом format

```python
In [1]: ip = "10.1.1.1"

In [2]: mask = 24

In [4]: "IP: {}, mask: {}".format(ip, mask)
Out[4]: 'IP: 10.1.1.1, mask: 24'

In [5]: template = "IP: {}, mask: {}"

In [6]: template.format(ip, mask)
Out[6]: 'IP: 10.1.1.1, mask: 24'
```

---
## Форматування рядків із методом format

```python
template = """
IP: {}
Mask: {}
Broadcast: {}
"""

print(template.format(ip, mask, broadcast))
print(template.format("10.1.1.1", 24, "10.1.1.255"))
```

```
IP: 10.1.1.1
Mask: 24
Broadcast: 10.1.1.255
```

---
## f-рядки

```python
In [1]: ip = "10.1.1.1"

In [2]: mask = 24

In [3]: f"IP: {ip}, mask: {mask}"
Out[3]: 'IP: 10.1.1.1, mask: 24'
```

Порівняння з format:

```python
In [3]: f"IP: {ip}, mask: {mask}"
Out[3]: 'IP: 10.1.1.1, mask: 24'

In [4]: "IP: {}, mask: {}".format(ip, mask)
Out[4]: 'IP: 10.1.1.1, mask: 24'
```

---
## Jinja2

```jinja
hostname {{ name }}

interface Loopback0
 ip address 10.0.0.{{ id }} 255.255.255.255

{% for vlan_id in vlans %}
vlan {{ vlan_id }}
{% endfor %}
```


```python
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader("."))
templ = env.get_template("cfg_template.txt")

liverpool = {"id": "11", "name": "Liverpool", "vlans": [1, 2, 10, 30]}
print(templ.render(liverpool))
```


---
## Форматування рядків із методом format

---
## Форматування рядків із методом format

`{}` вказує на те, що сюди підставиться значення, яке
передається методу format. При цьому кожна пара фігурних дужок позначає одне
місце для підстановки значення.

```python
template = """
IP: {}
Mask: {}
Broadcast: {}
"""

print(template.format(ip, mask, broadcast))
print(template.format("10.1.1.1", 24, "10.1.1.255"))
```

```
IP: 10.1.1.1
Mask: 24
Broadcast: 10.1.1.255
```

---
## Форматування рядків із методом format

```python
In [1]: "interface FastEthernet0/{}".format('1')
Out[1]: 'interface FastEthernet0/1'
```


---
## Форматування рядків

```python
In [3]: print('{}'.format('10.1.1.1'))
10.1.1.1

In [4]: print('{}'.format(100))
100

In [5]: print('{}'.format([10, 1, 1, 1]))
[10, 1, 1, 1]
```

---
## Форматування рядків

За допомогою форматування рядків можна виводити результат стовпцями. У
форматуванні рядків можна вказувати, скільки символів виділено на дані. Якщо
кількість символів у даних менша, ніж виділена кількість символів, відсутні
символи заповнюються пробілами.

---
### Форматування рядків

```python
In [3]: vlan, mac, intf = ['100', 'aabb.cc80.7000', 'Gi0/1']

In [4]: print("{:>15} {:>15} {:>15}".format(vlan, mac, intf))
            100  aabb.cc80.7000           Gi0/1

In [5]: print("{:15} {:15} {:15}".format(vlan, mac, intf))
100             aabb.cc80.7000  Gi0/1
```

---
### Форматування рядків

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
### Форматування рядків

```python
In [9]: print("{:.3f}".format(10.0/3))
3.333
```

---
### Форматування рядків

```python
In [11]: '{:b} {:b} {:b} {:b}'.format(192, 100, 1, 1)
Out[11]: '11000000 1100100 1 1'

In [12]: '{:8b} {:8b} {:8b} {:8b}'.format(192, 100, 1, 1)
Out[12]: '11000000  1100100        1        1'
```

---
### Форматування рядків

```python
In [13]: '{:08b} {:08b} {:08b} {:08b}'.format(192, 100, 1, 1)
Out[13]: '11000000 01100100 00000001 00000001'
```

---
### Форматування рядків

```python
In [15]: '{ip}/{mask}'.format(mask=24, ip='10.1.1.1')
Out[15]: '10.1.1.1/24'
```

---
### Форматування рядків

```python
In [16]: '{1}/{0}'.format(24, '10.1.1.1')
Out[16]: '10.1.1.1/24'
```

---
### Форматування рядків

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
### Форматування рядків

```python
ip_template = '''
IP address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

In [22]: print(ip_template.format(192, 100, 1, 1))

IP address:
192      100      1        1
11000000 01100100 00000001 00000001
```


---
## Об'єднання літералів рядків 

---
## Об'єднання літералів рядків

```python
In [1]: s = ('Test' 'String')

In [2]: s
Out[2]: 'TestString'

In [3]: s = 'Test' 'String'

In [4]: s
Out[4]: 'TestString'
```

---
## Об'єднання літералів рядків

```python
In [5]: s = ('Test'
   ...: 'String')

In [6]: s
Out[6]: 'TestString'
```

---
## Об'єднання літералів рядків

```python
regex = ('(\S+) +(\S+) +'
         '\w+ +\w+ +'
         '(up|down|administratively down) +'
         '(\w+)')
```

---
## Об'єднання літералів рядків

```python
regex = ('(\S+) +(\S+) +' # interface and IP
         '\w+ +\w+ +'
         '(up|down|administratively down) +' # Status
         '(\w+)') # Protocol
```


---
## Список (List)

---
### Список

Список у Python це:


* послідовність елементів у квадратних дужках, розділених комою
* змінюваний упорядкований тип даних

```python
vlans = [10, 20, 30, 77]
words = ['one', 'dog', 'seven']
commands = ["interface Gi0/1", "ip address 10.1.1.1 255.255.255.0"]
items = [1, 20, 4.0, 'word']
```

---
### Список

```python
interfaces = [
    ['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up'],
    ['FastEthernet0/1', '10.0.1.1', 'YES', 'manual', 'up', 'up'],
    ['FastEthernet0/2', '10.0.2.1', 'YES', 'manual', 'up', 'down'],
]
```

---
### Список

Так як список - це впорядкований тип даних, то, як і в рядках, у списках можна
звертатися до елемента за номером, робити зрізи:
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

Оскільки список є змінним типом даних, елементи списку можна змінювати:
```python
In [13]: list3
Out[13]: [1, 20, 4.0, 'word']

In [14]: list3[0] = 'test'

In [15]: list3
Out[15]: ['test', 20, 4.0, 'word']
```

---
### Список

Можна також створювати список списків. І, як і у звичайному списку, можна
звертатися до елементів у вкладених списках:
```python
interfaces = [
    ['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up'],
    ['FastEthernet0/1', '10.0.1.1', 'YES', 'manual', 'up', 'up'],
    ['FastEthernet0/2', '10.0.2.1', 'YES', 'manual', 'up', 'down'],
]

In [17]: interfaces[0][0]
Out[17]: 'FastEthernet0/0'

In [18]: interfaces[2][0]
Out[18]: 'FastEthernet0/2'

In [19]: interfaces[2][1]
Out[19]: '10.0.2.1'
```

---
### Список

len

```python
In [1]: items = [1, 2, 3]

In [2]: len(items)
Out[2]: 3
```

sorted

```python
In [1]: names = ['John', 'Michael', 'Antony']

In [2]: sorted(names)
Out[2]: ['Antony', 'John', 'Michael']
```


---
### Корисні методи для роботи зі списками

---
### Корисні методи для роботи зі списками

Список є змінним типом даних, тому важливо звернути увагу на те, що більшість
методів списку змінюють список на місці, не повертаючи нічого.

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
### ``join()``

```python
In [16]: vlans = ['10', '20', '30']

In [17]: ','.join(vlans)
Out[17]: '10,20,30'
```

---
### ``append()``

```python
In [18]: vlans = ['10', '20', '30', '100-200']

In [19]: vlans.append('300')

In [20]: vlans
Out[20]: ['10', '20', '30', '100-200', '300']
```


---
### ``extend()``

```python
In [21]: vlans = ['10', '20', '30', '100-200']

In [22]: vlans2 = ['300', '400', '500']

In [23]: vlans.extend(vlans2)

In [24]: vlans
Out[24]: ['10', '20', '30', '100-200', '300', '400', '500']
```

---
### Додавання списків

```python
In [27]: vlans = ['10', '20', '30', '100-200']

In [28]: vlans2 = ['300', '400', '500']

In [29]: vlans + vlans2
Out[29]: ['10', '20', '30', '100-200', '300', '400', '500']
```

---
### Додавання списків

```python
In [30]: result = vlans + vlans2

In [31]: result
Out[31]: ['10', '20', '30', '100-200', '300', '400', '500']
```

---
### ``pop()``

```python
In [28]: vlans = ['10', '20', '30', '100-200']

In [29]: vlans.pop(-1)
Out[29]: '100-200'

In [30]: vlans
Out[30]: ['10', '20', '30']
```


---
### ``remove()``

```python
In [31]: vlans = ['10', '20', '30', '100-200']

In [32]: vlans.remove('20')

In [33]: vlans
Out[33]: ['10', '30', '100-200']
```

---
### ``remove()``

```python
In [34]: vlans.remove(-1)
-------------------------------------------------
ValueError      Traceback (most recent call last)
<ipython-input-32-f4ee38810cb7> in <module>()
----> 1 vlans.remove(-1)

ValueError: list.remove(x): x not in list
```

---
### ``index()``

```python
In [35]: vlans = ['10', '20', '30', '100-200']

In [36]: vlans.index('30')
Out[36]: 2
```

---
### ``insert()``

```python
In [37]: vlans = ['10', '20', '30', '100-200']

In [38]: vlans.insert(1,'15')

In [39]: vlans
Out[39]: ['10', '15', '20', '30', '100-200']
```

---
## Словник (Dictionary)

---
### Словник

Словники - це змінюваний упорядкований тип даних:

* дані у словнику - це пари ключ: значення
* доступ до значень здійснюється за ключом
* дані у словнику впорядковані за порядком додавання елементів
* словники можна змінювати, тобто елементи словника можна змінювати, додавати, видаляти
* ключ має бути хешованим об'єктом: число, рядок, кортеж
* значення може бути даними будь-якого типу


> В інших мовах програмування тип даних подібний до словника може називатися
> асоціативний масив, хеш або хеш-таблиця.

```python
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
```

---
### Словник

```python
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

london = {
        'id': 1,
        'name': 'London',
        'it_vlan': 320,
        'user_vlan': 1010,
        'mngmt_vlan': 99,
        'to_name': None,
        'to_id': None,
        'port': 'G1/0/11',
}
```

---
### Словник

```python
In [1]: london = {'name': 'London1', 'location': 'London Str'}

In [2]: london['name']
Out[2]: 'London1'

In [3]: london['location']
Out[3]: 'London Str'
```

---
### Словник

```python
In [4]: london['vendor'] = 'Cisco'

In [5]: print(london)
{'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
```

---
### Словник

```python
london = {
    "r1": {
        "hostname": "london_r1",
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "hostname": "london_r2",
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "hostname": "london_sw1",
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
    },
}
```

---
### Словник

```python
In [7]: london_co['r1']['ios']
Out[7]: '15.4'

In [8]: london_co['r1']['model']
Out[8]: '4451'

In [9]: london_co['sw1']['ip']
Out[9]: '10.255.0.101'
```

---
### sorted

```python
In [1]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

In [2]: sorted(london)
Out[2]: ['location', 'name', 'vendor']
```


---
### Корисні методи для роботи зі словниками

|   | Методи |
|----------|-------------------------------------------|
| get      | Return the value for key if key is in the dictionary, else default.
| update   | Update D from dict/iterable E and F.
| keys     | Return  a set-like object providing a view on D's keys
| values   | Return an object providing a view on D's values
| items    | Return a set-like object providing a view on D's items
| pop      | remove specified key and return the corresponding value.
|          | If key is not found, d is returned if given, otherwise KeyError is raised
| popitem  | Remove and return a (key, value) pair as a 2-tuple.
| setdefault | Insert key with a value of default if key is not in the dictionary.
| clear    | Remove all items from D.
| copy     |  a shallow copy of D
| fromkeys | Create a new dictionary with keys from iterable and values set to value.

---
### ``clear()``

```python
In [1]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco', 'model': '4451', 'ios': '15.4'}

In [2]: london.clear()

In [3]: london
Out[3]: {}
```

---
### ``copy()``

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
### ``copy()``

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
### ``get()``

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
### ``get()``

```python
In [18]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

In [19]: print(london.get('ios'))
None

In [20]: print(london.get('ios', 'Ooops'))
Ooops
```

---
### ``setdefault()``

```python
In [21]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

In [22]: ios = london.setdefault('ios')

In [23]: print(ios)
None

In [24]: london
Out[24]: {'ios': None, 'location': 'London Str', 'name': 'London1', 'vendor': 'Cisco'}

In [25]: london.setdefault('name')
Out[25]: 'London1'
```

---
### ``setdefault()``

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
### ``setdefault()``

```python
if key in london:
    value = london[key]
else:
    london[key] = 'somevalue'
    value = london[key]

```


---
### ``keys(), values(), items()``

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

Всі три методи повертають спеціальні об'єкти view, які відображають ключі,
значення та пари ключ-значення словника відповідно.

Дуже важлива особливість view полягає в тому, що вони змінюються разом із
зміною словника. І фактично вони лише дають спосіб подивитися на відповідні
об'єкти, але не створюють їхньої копії.

---
### ``keys(), values(), items()``

```python
In [28]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

In [29]: keys = london.keys()

In [30]: print(keys)
dict_keys(['name', 'location', 'vendor'])
```

---
### ``keys(), values(), items()``


```python
In [31]: london['ip'] = '10.1.1.1'

In [32]: keys
Out[32]: dict_keys(['name', 'location', 'vendor', 'ip'])
```

---
### ``keys(), values(), items()``

```python
In [33]: list_keys = list(london.keys())

In [34]: list_keys
Out[34]: ['name', 'location', 'vendor', 'ip']
```

---
### ``del``

```python
In [35]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}

In [36]: del(london['name'])

In [37]: london
Out[37]: {'location': 'London Str', 'vendor': 'Cisco'}
```

---
### ``update``

```python
In [38]: r1 = {'name': 'London1', 'location': 'London Str'}

In [39]: r1.update({'vendor': 'Cisco', 'ios':'15.2'})

In [40]: r1
Out[40]: {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco', 'ios': '15.2'}
```

---
### ``update``


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
## Варіанти створення словника

---
### Літерал

```python
In [1]: r1 = {'model': '4451', 'ios': '15.4'}
```

---
### dict

```python
In [2]: r1 = dict(model='4451', ios='15.4')

In [3]: r1
Out[3]: {'ios': '15.4', 'model': '4451'}
```

---
### dict

```python
In [4]: r1 = dict([('model','4451'), ('ios','15.4')])

In [5]: r1
Out[5]: {'ios': '15.4', 'model': '4451'}
```

---
### dict.fromkeys

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

```python
In [8]: router_models = ['ISR2811', 'ISR2911', 'ISR2921', 'ASR9002']

In [9]: models_count = dict.fromkeys(router_models, 0)

In [10]: models_count
Out[10]: {'ASR9002': 0, 'ISR2811': 0, 'ISR2911': 0, 'ISR2921': 0}

```

---
### dict.fromkeys

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

Кортеж в Python це:

* послідовність елементів у дужках, розділених комою
* незмінний упорядкований тип даних

```python
params = ('hostname', 'location', 'vendor')
```

---
### Кортеж

```python
In [1]: tuple1 = tuple()

In [2]: print(tuple1)
()
```

```python
In [3]: tuple2 = ('password',)
```

---
### Кортеж

```python
In [4]: list_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']

In [5]: tuple_keys = tuple(list_keys)

In [6]: tuple_keys
Out[6]: ('hostname', 'location', 'vendor', 'model', 'IOS', 'IP')
```

```python
In [7]: tuple_keys[0]
Out[7]: 'hostname'
```

---
### Кортеж

```python
In [8]: tuple_keys[1] = 'test'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-1c7162cdefa3> in <module>()
----> 1 tuple_keys[1] = 'test'

TypeError: 'tuple' object does not support item assignment
```

---
### Методи кортежа

|   | Методи кортежа |
|---------|--------------------------------------|
| count   | S.count(sub[, start[, end]]) -> int  |
| index   | S.index(sub[, start[, end]]) -> int  |

---
## Множина (Set)

---
### Множина

Множина́ - це змінюваний невпорядкований тип даних. У множині завжди містяться
тільки унікальні елементи.

Множина в Python - це послідовність елементів у фігурних дужках, які розділені
між собою комою.

```python
vlans = {10, 20, 30, 40, 100, 11}
```

---
### Множина

За допомогою множини можна легко отримати унікальний набір елементів:
```python
In [1]: vlans = [10, 20, 30, 40, 100, 10]

In [2]: set(vlans)
Out[2]: {10, 20, 30, 40, 100}

In [3]: set1 = set(vlans)

In [4]: print(set1)
{40, 100, 10, 20, 30}
```

---
### Варіанти створення множин

Не можна створити порожню множину за допомогою [літералу](/reference/syntax/#literals), оскільки в такому
випадку це буде не множина, а словник:

```python
In [1]: set1 = {}

In [2]: type(set1)
Out[2]: dict
```

порожню множину можна створити таким чином:

```python
In [3]: set2 = set()

In [4]: type(set2)
Out[4]: set
```

Створення множини із рядка/списку:

```python
In [5]: set('long long long long string')
Out[5]: {' ', 'g', 'i', 'l', 'n', 'o', 'r', 's', 't'}

In [6]: set([10, 20, 30, 10, 10, 30])
Out[6]: {10, 20, 30}
```


---
### Корисні методи для роботи з множинами

---
### Методи множин

| Назва                      | Опис |
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
### Методи множин

| Назва                      | Опис |
|-------------------------------|--------------|
| difference                    | Return the difference of two or more sets as a new set. |
| intersection                  | Return the intersection of two sets as a new set. |
| union                         | Return the union of sets as a new set. |
| symmetric_difference          | Return the symmetric difference of two sets as a new set. |
| | |
| difference_update             | Remove all elements of another set from this set. |
| intersection_update           | Update a set with the intersection of itself and another. |
| symmetric_difference_update   | Update a set with the symmetric difference of itself and another. |
| | |
| isdisjoint                    | Return True if two sets have a null intersection. |
| issubset                      | Report whether another set contains this set. |
| issuperset                    | Report whether this set contains another set. |

---
### ```add()```

```python
In [1]: set1 = {10, 20, 30, 40}

In [2]: set1.add(50)

In [3]: set1
Out[3]: {10, 20, 30, 40, 50}
```

---
### ```discard()```

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

```python
In [8]: set1 = {10, 20, 30, 40}

In [9]: set1.clear()

In [10]: set1
Out[10]: set()
```

---
### Операції з множинами

```python
vlans1 = {10, 20, 30, 50, 100}
vlans2 = {100, 101, 102, 102, 200}

In [3]: vlans1.union(vlans2)
Out[3]: {10, 20, 30, 50, 100, 101, 102, 200}

In [4]: vlans1 | vlans2
Out[4]: {10, 20, 30, 50, 100, 101, 102, 200}
```

---
### Операції з множинами

```python
vlans1 = {10, 20, 30, 50, 100}
vlans2 = {100, 101, 102, 200}

In [7]: vlans1.intersection(vlans2)
Out[7]: {100}

In [8]: vlans1 & vlans2
Out[8]: {100}
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

Функция ```set()``` преобразует аргумент в множина: 
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

