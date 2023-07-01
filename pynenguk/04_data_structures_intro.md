## Типи даних у Python

---
### Типи даних у Python

У Python є кілька базових типів даних:

* Numbers (числа)
* Strings (рядки)
* Lists (списки)
* Dictionaries (словники)
* Tuples (кортежі)
* Sets (множини)
* Boolean (логічний тип даних)

Ці типи даних можна класифікувати за кількома ознаками:

* змінювані (списки, словники та множини)
* незмінні (числа, рядки та кортежі)
* упорядковані (списки, кортежі, рядки та словники)
* невпорядковані (множини)

---
### Типи даних у Python

Змінювані

* списки
* словники
* множини

Незмінні

* числа
* рядки
* кортежі

---
### Типи даних у Python

Упорядковані

* списки
* кортежі
* рядки
* словники

Невпорядковані

* множини

---
### Типи даних у Python

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
| Boolean     | логічний тип даних | ``True, False`` |

---
### Типи даних у Python

|             |               |
|-------------|--------------|
| String      | Для зберігання тексту та довільних даних, для яких у Python немає типу |
| List        | Набір даних, часто однотипних даних: список вланів, команд, рядків файлу |
| Dictionary  | Використовується для даних типу поле: значення |
| Tuple       | Незмінний набір даних, який часто повертається із зовнішніх джерел - БД, CSV.
|             | Також використовується коли дані є набір значень: ``(x, y)`` |
| Set         | Для збереження унікальних даних. Плюс часто використовується |
|             | для операцій з множинами |
| Boolean     | Вказує, що якесь значення є справжнім або хибним |
| None        | Використовується, коли потрібно вказати, що тут немає ніякого значення |


|             |              |
|-------------|--------------|
| String      | "interface Gi0/0" |
| List        | [1, 2, 3] |
| Dictionary  | {"username": "user1", "permissions": 100} |
| Tuple       | ("line console 0", "login local") |
| Set         | {3, 10, 100, 4, 5} |
| Boolean     | True, False |


---
## Список

```python
interfaces = [
    ['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up'],
    ['FastEthernet0/1', '10.0.1.1', 'YES', 'manual', 'up', 'up'],
    ['FastEthernet0/2', '10.0.2.1', 'YES', 'manual', 'up', 'down'],
]

interfaces = [
    {'address': '192.168.100.1', 'intf': 'Ethernet0/0', 'protocol': 'up', 'status': 'up'},
    {'address': '192.168.200.1', 'intf': 'Ethernet0/1', 'protocol': 'up', 'status': 'up'},
]

```

---
### Словник

```python
london = {
    'id': 1,
    'name': 'London',
    'it_vlan': 320,
    'user_vlan': 1010,
    'mngmt_vlan': 99,
    'to_name': None,
    'to_id': None,
    'routing': False,
    'port': 'G1/0/11',
}
```


---
## Змінні

---
### Змінні

Змінні в Python:

* не вимагають оголошення типу змінної
* є посиланнями на область пам'яті

```python
In [1]: native_vlan = 3

In [2]: hostname = "sw1_london"

In [3]: number = 100 * 5
```


---
### Змінні


Правила іменування змінних:

* ім'я змінної може складатися тільки з літер, цифр та знака підкреслення
* ім'я не може починатися з цифри
* ім'я не може містити спеціальних символів @, $, %

Приклади

* ``get_names``
* ``JuniperDevice``
* ``DB_NAME``


---
### Імена змінних

У Python є рекомендації щодо іменування функцій, класів та змінних:

* імена змінних зазвичай пишуться повністю великими чи маленькими літерами: ``DB_NAME``, ``db_name``
* імена функцій задаються маленькими літерами, з підкресленням між словами: ``get_names``
* імена класів задаються словами з великими літерами: ``JuniperDevice``


---
## Числа

---
### Числа

```python
In [1]: 1 + 2
Out[1]: 3

In [2]: 1.0 + 2
Out[2]: 3.0

In [3]: 10 - 4
Out[3]: 6

In [4]: 2**3
Out[4]: 8
```

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
### Методи для роботи з рядками

```python
In [1]: line = "test"

In [2]: line.
          capitalize   find         isdecimal    istitle      partition    rstrip       translate
          casefold     format       isdigit      isupper      replace      split        upper
          center       format_map   isidentifier join         rfind        splitlines   zfill
          count        index        islower      ljust        rindex       startswith
          encode       isalnum      isnumeric    lower        rjust        strip
          endswith     isalpha      isprintable  lstrip       rpartition   swapcase
          expandtabs   isascii      isspace      maketrans    rsplit       title
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
## Список (List)

---
### Список

Список у Python це:

* послідовність елементів у квадратних дужках, розділених комою
* змінюваний упорядкований тип даних

```python
In [1]: list1 = [10, 20, 30, 77]

In [2]: list2 = ['one', 'dog', 'seven']

In [3]: list3 = [1, 20, 4.0, 'word']
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
    ['FastEthernet0/2', '10.0.2.1', 'YES', 'manual', 'up', 'down']
]

In [17]: interfaces[0][0]
Out[17]: 'FastEthernet0/0'

In [18]: interfaces[2][0]
Out[18]: 'FastEthernet0/2'

In [19]: interfaces[2][1]
Out[19]: '10.0.2.1'
```

---
### Методи списків

```
In [2]: vlans = [1, 2, 3, 4, 10, 11, 12, 100]

In [3]: vlans.
               append()  count()   insert()  reverse()
               clear()   extend()  pop()     sort()
               copy()    index()   remove()
```

help(list)
```
 |  append(self, object, /)
 |      Append object to the end of the list.
 |
 |  clear(self, /)
 |      Remove all items from list.
 |
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  insert(self, index, object, /)
 |      Insert object before index.
 |
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |
 |      Raises IndexError if list is empty or index is out of range.
 |
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |
 |      The reverse flag can be set to sort in descending order.
 |
```

---
### Методи списків

```
In [26]: inspect(vlans, methods=True)
╭───────────────────────────────────────── <class 'list'> ──────────────────────────────────────────╮
│ Built-in mutable sequence.                                                                        │
│                                                                                                   │
│ ╭───────────────────────────────────────────────────────────────────────────────────────────────╮ │
│ │ [1, 2, 3, 4, 10, 11, 12, 100]                                                                 │ │
│ ╰───────────────────────────────────────────────────────────────────────────────────────────────╯ │
│                                                                                                   │
│  append = def append(object, /): Append object to the end of the list.                            │
│   clear = def clear(): Remove all items from list.                                                │
│    copy = def copy(): Return a shallow copy of the list.                                          │
│   count = def count(value, /): Return number of occurrences of value.                             │
│  extend = def extend(iterable, /): Extend list by appending elements from the iterable.           │
│   index = def index(value, start=0, stop=2147483647, /): Return first index of value.             │
│  insert = def insert(index, object, /): Insert object before index.                               │
│     pop = def pop(index=-1, /): Remove and return item at index (default last).                   │
│  remove = def remove(value, /): Remove first occurrence of value.                                 │
│ reverse = def reverse(): Reverse *IN PLACE*.                                                      │
│    sort = def sort(*, key=None, reverse=False): Sort the list in ascending order and return None. │
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
```

---
## Словник (Dictionary)

---
## Словник (Dictionary)

Словники - це змінюваний упорядкований тип даних:

* дані у словнику - це пари ключ: значение
* доступ до значень здійснюється за ключом
* дані у словнику впорядковані за порядком додавання елементів
* словники можна змінювати, тобто елементи словника можна змінювати, додавати, видаляти
* ключ має бути об'єктом незмінного типу: число, рядок, кортеж
* значення може бути даними будь-якого типу


> В інших мовах програмування тип даних подібний до словника може називатися
> асоціативний масив, хеш або хеш-таблиця.

---
### Словник

Приклад словника:
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

Для того, щоб отримати значення зі словника, треба звернутися по ключу, так
само, як це було в списках, тільки замість номера використовуватиметься ключ:
```python
In [1]: london = {'name': 'London1', 'location': 'London Str'}

In [2]: london['name']
Out[2]: 'London1'

In [3]: london['location']
Out[3]: 'London Str'
```

---
### Словник

Аналогічно можна додати нову пару ключ:значення:
```python
In [4]: london['vendor'] = 'Cisco'

In [5]: print(london)
{'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
```

---
### Словник

У словнику як значення можна використовувати словник:
```python
london_co = {
    'r1': {'hostname': 'london_r1',
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
            'vendor': 'Cisco'},
}
```

---
### Словник

Отримати значення із вкладеного словника можна так:
```python
In [7]: london_co['r1']['ios']
Out[7]: '15.4'

In [8]: london_co['r1']['model']
Out[8]: '4451'

In [9]: london_co['sw1']['ip']
Out[9]: '10.255.0.101'
```

---
### Методи словника


```
In [28]: dict.
               clear()      get()        mro()        setdefault()
               copy()       items()      pop()        update()
               fromkeys()   keys()       popitem()    values()
```

---
### Методи словника


```
In [27]: inspect(dict, methods=True)
╭─────────────────────────────────────────────────────── <class 'dict'> ───────────────────────────────────────────────────────╮
│ def dict(...)                                                                                                                │
│                                                                                                                              │
│ dict() -> new empty dictionary                                                                                               │
│ dict(mapping) -> new dictionary initialized from a mapping object's                                                          │
│     (key, value) pairs                                                                                                       │
│ dict(iterable) -> new dictionary initialized as if via:                                                                      │
│     d = {}                                                                                                                   │
│     for k, v in iterable:                                                                                                    │
│         d[k] = v                                                                                                             │
│ dict(**kwargs) -> new dictionary initialized with the name=value pairs                                                       │
│     in the keyword argument list.  For example:  dict(one=1, two=2)                                                          │
│                                                                                                                              │
│      clear = def clear(...) D.clear() -> None.  Remove all items from D.                                                     │
│       copy = def copy(...) D.copy() -> a shallow copy of D                                                                   │
│   fromkeys = def fromkeys(iterable, value=None, /): Create a new dictionary with keys from iterable and values set to value. │
│        get = def get(self, key, default=None, /): Return the value for key if key is in the dictionary, else default.        │
│      items = def items(...) D.items() -> a set-like object providing a view on D's items                                     │
│       keys = def keys(...) D.keys() -> a set-like object providing a view on D's keys                                        │
│        pop = def pop(...)                                                                                                    │
│              D.pop(k[,d]) -> v, remove specified key and return the corresponding value.                                     │
│              If key is not found, d is returned if given, otherwise KeyError is raised                                       │
│    popitem = def popitem(self, /): Remove and return a (key, value) pair as a 2-tuple.                                       │
│ setdefault = def setdefault(self, key, default=None, /): Insert key with a value of default if key is not in the dictionary. │
│     update = def update(...)                                                                                                 │
│              D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.                                               │
│              If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]                                   │
│              If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v                                 │
│              In either case, this is followed by: for k in F:  D[k] = F[k]                                                   │
│     values = def values(...) D.values() -> an object providing a view on D's values                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```



---
### Операції із множинами

```
                 Union                              Intersection
               Об'єднання                              Перетин
                   _________                              _________
           _______|#########|                     _______|__       |
          |#######|##|######|                    |       |##|      |
          |#######|##|######|                    |       |##|      |
          |#######|##|######|                    |       |##|      |
          |#######|##|######|                    |_______|##|      |
                  |#########|                            |_________|
          
          
                 Difference                      Symmetric difference
                   Різниця                        Симетрична різниця
                   _________                              _________
           _______|__       |                     _______|#########|
          |#######|  |      |                    |#######|  |######|
          |#######|  |      |                    |#######|  |######|
          |#######|  |      |                    |#######|  |######|
          |#######|__|      |                    |#######|__|######|
                  |_________|                            |#########|
```

