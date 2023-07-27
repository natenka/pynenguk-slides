
# Функції

---

### Функції

Функція - це блок коду, який виконує певні дії:

* У функції є ім'я, за допомогою якого можна запускати цей блок коду скільки завгодно разів
* запуск коду функції називається викликом функції
* при створенні функції, як правило, визначаються параметри функції
* функції можна передавати аргументи


```python
def sum_numbers(num1, num2):
    """
    Функція обчислює суму двох чисел
    """
    return num1 + num2


In [2]: sum_numbers(100, 42)
Out[2]: 142
```

---
### Створення функцій

---
### Створення функцій


* функції створюються за допомогою зарезервованого слова def
* за def слідують ім'я функції та круглі дужки
* всередині дужок можуть вказуватись параметри, які функція приймає
* після круглих дужок йде двокрапка і з нового рядка, з відступом, йде блок коду, який виконує функція
* першим рядком, опціонально, може бути коментар, так звана docstring
* у функціях може використовуватись оператор return
* він використовується для припинення роботи функції та виходу з неї
* найчастіше оператор return повертає якесь значення

---
### Приклад функції

```python
def open_file(filename):
    """Documentation string"""
    with open(filename) as f:
        print(f.read())

```

---
### Виклик функції

При виклику функції потрібно вказати її ім'я та передати аргументи, якщо потрібно.

* Параметри - це змінні, які використовуються під час створення функції.
* Аргументи - це фактичні значення (дані), що передаються функції під час виклику.


---
### Виклик функції

```python
def open_file(filename):
    """Documentation string"""
    with open(filename) as f:
        print(f.read())


In [2]: open_file('r1.txt')
!
service timestamps debug datetime msec localtime show-timezone year
service timestamps log datetime msec localtime show-timezone year
service password-encryption
service sequence-numbers
!
no ip domain lookup
!
ip ssh version 2
!
```

---
### docstring

Перший рядок у визначенні функції – це docstring, рядок документації. Це
коментар, який використовується як опис функції. Його можна відобразити так:

```python
In [4]: open_file.__doc__
Out[4]: 'Documentation string'
```

---
### Оператор return

Оператор return використовується для припинення роботи функції, виходу з неї і,
як правило, повернення якогось значення. Функція може повертати будь-який
об'єкт Python.


---
### Оператор return

```python
In [5]: result = open_file('ospf.txt')
router ospf 1
 router-id 10.0.0.3
 auto-cost reference-bandwidth 10000
 network 10.0.1.0 0.0.0.255 area 0
 network 10.0.2.0 0.0.0.255 area 2
 network 10.1.1.0 0.0.0.255 area 0

In [6]: print(result)
None
```

---
### Оператор return

Для того, чтобы функция возвращала значение, которое потом можно, например, присвоить переменной, используется оператор ```return```:
```python
def open_file(filename):
    """Documentation string"""
    with open(filename) as f:
        return f.read()


In [8]: result = open_file('r1.txt')

In [9]: print(result)
!
service timestamps debug datetime msec localtime show-timezone year
service timestamps log datetime msec localtime show-timezone year
service password-encryption
service sequence-numbers
!
no ip domain lookup
!
ip ssh version 2
!
```

---
### Оператор return

Выражения, которые идут после return, не выполняются:
```python
In [10]: def open_file(filename):
    ...:     print("Reading file", filename)
    ...:     with open(filename) as f:
    ...:         return f.read()
    ...:         print("Done")
    ...:

In [11]: result = open_file('r1.txt')
Reading file r1.txt

```

---
### Простори імен. Області видимості змінних

---
### Простори імен. Області видимості змінних

* Простір імен (namespace) - це словник імена (як рядки): значення.
* Область видимості (scope) визначає, які простори імен будуть переглядатися та в якому порядку.

Коли ви створюєте змінну, наприклад num1 = 1, ви змінюєте простір імен. Коли ви
звертаєтесь до змінної, наприклад print(num1), Python переглядає список просторів
імен, щоб спробувати знайти той, у якому ім'я є ключем.

Область видимості будь-якого посилання завжди починається з локального простору
імен і просувається назовні, доки не досягне глобального простору імен модуля,
а потім переходить до вбудованих елементів.

* L (local)
* E (enclosing)
* G (global)
* B (built-in)

---
## Пошук змінних

Під час пошуку змінних Python використовує правило LEGB.  Наприклад, якщо
всередині функції виконується звернення до імені змінної, Python шукає змінну в
такому порядку за областями видимості (до першого збігу):

* L (local) - у локальній (всередині функції)
* E (enclosing) - у локальній області видимості вміщуючих функцій (це ті функції, всередині яких знаходиться наша функція)
* G (global) - у глобальній (в скрипті)
* B (built-in) - у вбудованій (зарезервовані значення Python)

---
## Локальні та глобальні змінні

Локальні змінні:

* змінні, визначені всередині функції
* ці змінні стають недоступними після виходу з функції

Глобальні змінні:

* змінні, які визначені поза функцією
* ці змінні "глобальні" лише в межах модуля, щоб вони були доступні в іншому модулі, їх треба імпортувати


---
### Пример локальной и глобальной переменной

```python
In [1]: result = 'test string'

In [2]: def open_file(filename):
   ...:     with open(filename) as f:
   ...:         result = f.read()
   ...:         return result
   ...:

In [3]: open_file('r1.txt')
Out[3]: '!\nservice timestamps debug datetime msec localtime show-timezone year\nservice timestamps log datetime msec localtime show-timezone year\nservice password-encryption\nservice sequence-numbers\n!\nno ip domain lookup\n!\nip ssh version 2\n!\n'

In [4]: result
Out[4]: 'test string'
```

---
## Параметры и аргументы функций

---
### Параметры и аргументы функций

Цель создания функции, как правило, заключается в том, чтобы вынести кусок кода, который выполняет определенную задачу, в отдельный объект.  
Это позволяет использовать этот кусок кода многократно, не создавая его заново в программе.

Как правило, функция должна выполнять какие-то действия с входящими значениями и на выходе выдавать результат.

При работе с функциями важно различать:

* **параметры** - это переменные, которые используются при создании функции.
* **аргументы** - это фактические значения \(данные\), которые передаются функции при вызове.


---
### Параметры и аргументы функций

Для того, чтобы функция могла принимать входящие значения, ее нужно создать с параметрами (файл func_params_args.py):

```python
In [1]: def delete_exclamation_from_cfg(in_cfg, out_cfg):
   ...:     with open(in_cfg) as in_file:
   ...:         result = in_file.readlines()
   ...:     with open(out_cfg, 'w') as out_file:
   ...:         for line in result:
   ...:             if not line.startswith('!'):
   ...:                 out_file.write(line)
   ...:
```

---
### Параметры и аргументы функций

Файл r1.txt будет использоваться как первый аргумент \(in\_cfg\):
```python
In [2]: cat r1.txt
!
service timestamps debug datetime msec localtime show-timezone year
service timestamps log datetime msec localtime show-timezone year
service password-encryption
service sequence-numbers
!
no ip domain lookup
!
ip ssh version 2
!
```

---
### Параметры и аргументы функций

Пример использования функции delete\_exclamation\_from\_cfg:

```python
In [3]: delete_exclamation_from_cfg('r1.txt', 'result.txt')
```

Файл result.txt выглядит так:

```python
In [4]: cat result.txt
service timestamps debug datetime msec localtime show-timezone year
service timestamps log datetime msec localtime show-timezone year
service password-encryption
service sequence-numbers
no ip domain lookup
ip ssh version 2
```

---
### Параметры и аргументы функций

При таком определении функции надо обязательно передать оба аргумента.  
Если передать только один аргумент, возникнет ошибка.
Аналогично, возникнет ошибка, если передать три и больше аргументов.

```python
In [5]: delete_exclamation_from_cfg('r1.txt')
TypeError                                 Traceback (most recent call last)
<ipython-input-12-66ae381f1c4f> in <module>()
-> 1 delete_exclamation_from_cfg('r1.txt')

TypeError: delete_exclamation_from_cfg() missing 1 required positional argument: 'out_cfg'
```


---
## Типы параметров функции

---
### Типы параметров функции

При создании функции можно указать, какие аргументы нужно передавать обязательно, а какие нет.

Функция может быть создана с параметрами:
* __обязательными__
* __необязательными__ (опциональными, параметрами со значением по умолчанию)

---
### Обязательные параметры

__Обязательные параметры__ - определяют, какие аргументы нужно передать функции обязательно.
При этом, их нужно передать ровно столько, сколько указано параметров функции (нельзя указать большее или меньшее количество аргументов)

```python
In [1]: def cfg_to_list(cfg_file, delete_exclamation):
  ....:     result = []
  ....:     with open(cfg_file) as f:
  ....:         for line in f:
  ....:             if delete_exclamation and line.startswith('!'):
  ....:                 pass
  ....:             else:
  ....:                 result.append(line.rstrip())
  ....:     return result
```

---
### Обязательные параметры

Пример вызова функции:
```python
In [2]: cfg_to_list('r1.txt', True)
Out[2]:
['service timestamps debug datetime msec localtime show-timezone year',
 'service timestamps log datetime msec localtime show-timezone year',
 'service password-encryption',
 'service sequence-numbers',
 'no ip domain lookup',
 'ip ssh version 2']
```

Так как аргументу delete_exclamation передано значение True, в итоговом словаре нет строк с восклицательными знаками.

---
### Обязательные параметры

Виклик функції со значением False для аргумента delete_exclamation:
```python
In [3]: cfg_to_list('r1.txt', False)
Out[3]:
['!',
 'service timestamps debug datetime msec localtime show-timezone year',
 'service timestamps log datetime msec localtime show-timezone year',
 'service password-encryption',
 'service sequence-numbers',
 '!',
 'no ip domain lookup',
 '!',
 'ip ssh version 2',
 '!']
```

---
### Необязательные параметры (параметры со значением по умолчанию)

```python
In [4]: def cfg_to_list(cfg_file, delete_exclamation=True):
  ....:     result = []
  ....:     with open( cfg_file ) as f:
  ....:         for line in f:
  ....:             if delete_exclamation and line.startswith('!'):
  ....:                 pass
  ....:             else:
  ....:                 result.append(line.rstrip())
  ....:     return result
  ....:

```

---
### Параметры со значением по умолчанию

Так как теперь у параметра delete_exclamation значение по умолчанию равно True,
соответствующий аргумент можно не указывать при вызове функции, если значение по умолчанию подходит:
```python
In [5]: cfg_to_list('r1.txt')
Out[5]:
['service timestamps debug datetime msec localtime show-timezone year',
 'service timestamps log datetime msec localtime show-timezone year',
 'service password-encryption',
 'service sequence-numbers',
 'no ip domain lookup',
 'ip ssh version 2']
```

---
### Параметры со значением по умолчанию

```python
In [6]: cfg_to_list('r1.txt', False)
Out[6]:
['!',
 'service timestamps debug datetime msec localtime show-timezone year',
 'service timestamps log datetime msec localtime show-timezone year',
 'service password-encryption',
 'service sequence-numbers',
 '!',
 'no ip domain lookup',
 '!',
 'ip ssh version 2',
 '!']

```

---
## Типы аргументов функции

---
### Типы аргументов функции

* __позиционные__ - передаются в том же порядке, в котором они определены при создании функции. То есть, порядок передачи аргументов определяет, какое значение получит каждый
* __ключевые__ - передаются с указанием имени аргумента и его значения. В таком случае, аргументы могут быть указаны в любом порядке, так как их имя указывается явно.

---
### Типы аргументов функции

Позиционные и ключевые аргументы могут быть смешаны при вызове функции.
То есть, можно использовать оба способа при передаче аргументов одной и той же функции.
При этом, сначала должны идти позиционные аргументы, а только потом - ключевые.

---
### Типы аргументов функции

```python
In [1]: def cfg_to_list(cfg_file, delete_exclamation):
  ....:     result = []
  ....:     with open( cfg_file ) as f:
  ....:         for line in f:
  ....:             if delete_exclamation and line.startswith('!'):
  ....:                 pass
  ....:             else:
  ....:                 result.append(line.rstrip())
  ....:     return result
  ....:
```

---
### Позиционные аргументы

Позиционные аргументы при вызове функции надо передать в правильном порядке:
```python
In [2]: cfg_to_list('r1.txt', False)
Out[2]:
['!',
 'service timestamps debug datetime msec localtime show-timezone year',
 'service timestamps log datetime msec localtime show-timezone year',
 'service password-encryption',
 'service sequence-numbers',
 '!',
 'no ip domain lookup',
 '!',
 '',
 '',
 'ip ssh version 2',
 '!']
```

---
### Ключевые аргументы

* передаются с указанием имени аргумента
* за счет этого они могут передаваться в любом порядке

```python
In [4]: cfg_to_list(delete_exclamation=False, cfg_file='r1.txt')
Out[4]:
['!',
 'service timestamps debug datetime msec localtime show-timezone year',
 'service timestamps log datetime msec localtime show-timezone year',
 'service password-encryption',
 'service sequence-numbers',
 '!',
 'no ip domain lookup',
 '!',
 'ip ssh version 2',
 '!']
```

---
### Ключевые аргументы

__Сначала должны идти позиционные аргументы, а затем ключевые.__

Если сделать наоборот, возникнет ошибка:
```python
In [5]: cfg_to_list(delete_exclamation=False, 'r1.txt')
  File "<ipython-input-3-8f3a3aa16a22>", line 1
    cfg_to_list(delete_exclamation=False, 'r1.txt')
                                         ^
SyntaxError: positional argument follows keyword argument

```

---
### Ключевые аргументы

Но в такой комбинации можно:
```python
In [6]: cfg_to_list('r1.txt', delete_exclamation=True)
Out[6]:
['service timestamps debug datetime msec localtime show-timezone year',
 'service timestamps log datetime msec localtime show-timezone year',
 'service password-encryption',
 'service sequence-numbers',
 'no ip domain lookup',
 'ip ssh version 2']

```

---
### Аргументы, которые можно передавать только как ключевые

Аргументы, которые указаны после ``*`` можно передавать только как ключевые при
вызове функции.

```python
def check_passwd(username, password, *, min_length=8, check_username=True):
    if len(password) < min_length:
        print('Пароль слишком короткий')
        return False
    elif check_username and username in password:
        print('Пароль содержит имя пользователя')
        return False
    else:
        print(f'Пароль для пользователя {username} прошел все проверки')
        return True
```

---
### Аргументы, которые можно передавать только как ключевые

При передаче их как позиционных, возникнет исключение:

```python
    In [2]: check_passwd('nata', '12345', min_length=3)
    Пароль для пользователя nata прошел все проверки
    Out[2]: True

    In [3]: check_passwd('nata', '12345', 3)
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-3-4f346c9cf914> in <module>
    ----> 1 check_passwd('nata', '12345', 3)

    TypeError: check_passwd() takes 2 positional arguments but 3 were given
```

---
## Аргументы переменной длины

---
### Аргументы переменной длины

Иногда необходимо сделать так, чтобы функция принимала не фиксированное количество аргументов, а любое.
Для такого случая в Python можно создавать функцию со специальным параметром, который принимает аргументы переменной длины.
Такой параметр может быть как ключевым, так и позиционным.

---
### Позиционные аргументы переменной длины

Параметр, который принимает позиционные аргументы переменной длины, создается добавлением перед именем параметра звездочки.
Имя параметра может быть любым, но, по договоренности, чаще всего, используют имя ```*args```

```python
In [1]: def sum_arg(a, *args):
  ....:     print(a, args)
  ....:     return a + sum(args)
  ....: 
```

---
### Позиционные аргументы переменной длины

Виклик функції с разным количеством аргументов:
```python
In [2]: sum_arg(1, 10, 20, 30)
1 (10, 20, 30)
Out[2]: 61

In [3]: sum_arg(1, 10)
1 (10,)
Out[3]: 11

In [4]: sum_arg(1)
1 ()
Out[4]: 1
```

---
### Позиционные аргументы переменной длины

```python
In [5]: def sum_arg(*args):
  ....:     print(args)
  ....:     return sum(args)
  ....: 

In [6]: sum_arg(1, 10, 20, 30)
(1, 10, 20, 30)
Out[6]: 61

In [7]: sum_arg()
()
Out[7]: 0
```

---
### Ключевые аргументы переменной длины

Параметр, который принимает ключевые аргументы переменной длины, создается добавлением перед именем параметра двух звездочек.
Имя параметра может быть любым, но, по договоренности, чаще всего, используют имя ```**kwargs``` (от keyword arguments).


```python
In [8]: def sum_arg(a, **kwargs):
  ....:     print(a, kwargs)
  ....:     return a + sum(kwargs.values())
  ....: 
```

---
### Ключевые аргументы переменной длины

Виклик функції с разным количеством ключевых аргументов:
```python
In [9]: sum_arg(a=10, b=10, c=20, d=30)
10 {'c': 20, 'b': 10, 'd': 30}
Out[9]: 70

In [10]: sum_arg(b=10, c=20, d=30, a=10)
10 {'c': 20, 'b': 10, 'd': 30}
Out[10]: 70
```

---
### Ключевые аргументы переменной длины

Нельзя указывать позиционный аргумент после ключевого:
```python
In [11]: sum_arg(10, b=10, c=20, d=30)
10 {'c': 20, 'b': 10, 'd': 30}
Out[11]: 70

In [12]: sum_arg(b=10, c=20, d=30, 10)
  File "<ipython-input-14-71c121dc2cf7>", line 1
    sum_arg(b=10,c=20,d=30,10)
                          ^
SyntaxError: positional argument follows keyword argument
```

---
## Распаковка аргументов

---
### Распаковка аргументов

В Python выражения ```*args``` и ```**kwargs``` позволяют выполнять ещё одну задачу - __распаковку аргументов__.

До сих пор мы вызывали все функции вручную.
И, соответственно, передавали все нужные аргументы.

Но в реальной жизни, как правило, данные необходимо передавать в функцию программно.
И часто данные идут в виде какого-то объекта Python.

---
### Распаковка позиционных аргументов

Например, при форматировании строк часто надо передать методу format несколько аргументов.
И часто эти аргументы уже находятся в списке или кортеже.
Чтобы их передать методу format, приходится использовать индексы таким образом:
```python
In [1]: items = [1, 2, 3]

In [2]: print('One: {}, Two: {}, Three: {}'.format(items[0], items[1], items[2]))
One: 1, Two: 2, Three: 3
```

---
### Распаковка позиционных аргументов

Вместо этого, можно воспользоваться распаковкой аргументов и сделать так:
```python
In [4]: items = [1, 2, 3]

In [5]: print('One: {}, Two: {}, Three: {}'.format(*items))
One: 1, Two: 2, Three: 3

```

---
### Распаковка позиционных аргументов

Функция config_interface (файл func_args_unpacking.py): 
```python
def config_interface(intf_name, ip_address, cidr_mask):
    interface = 'interface {}'
    no_shut = 'no shutdown'
    ip_addr = 'ip address {} {}'
    result = []
    result.append(interface.format(intf_name))
    result.append(no_shut)

    mask_bits = int(cidr_mask.split('/')[-1])
    bin_mask = '1'*mask_bits + '0'*(32-mask_bits)
    dec_mask = [str(int(bin_mask[i:i+8], 2)) for i in range(0,25,8)]
    dec_mask_str = '.'.join(dec_mask)

    result.append(ip_addr.format(ip_address, dec_mask_str))
    return result

```

---
### Распаковка позиционных аргументов

```python
In [1]: config_interface('Fa0/1', '10.0.1.1', '/25')
Out[1]: ['interface Fa0/1', 'no shutdown', 'ip address 10.0.1.1 255.255.255.128']

In [2]: config_interface('Fa0/3', '10.0.0.1', '/18')
Out[2]: ['interface Fa0/3', 'no shutdown', 'ip address 10.0.0.1 255.255.192.0']

In [3]: config_interface('Fa0/3', '10.0.0.1', '/32')
Out[3]: ['interface Fa0/3', 'no shutdown', 'ip address 10.0.0.1 255.255.255.255']

In [4]: config_interface('Fa0/3', '10.0.0.1', '/30')
Out[4]: ['interface Fa0/3', 'no shutdown', 'ip address 10.0.0.1 255.255.255.252']

In [5]: config_interface('Fa0/3', '10.0.0.1', '30')
Out[5]: ['interface Fa0/3', 'no shutdown', 'ip address 10.0.0.1 255.255.255.252']
```

---
### Распаковка позиционных аргументов

Например, список interfaces_info, в котором находятся параметры для настройки интерфейсов:
```python
In [6]: interfaces_info = [['Fa0/1', '10.0.1.1', '/24'],
  ....:                    ['Fa0/2', '10.0.2.1', '/24'],
  ....:                    ['Fa0/3', '10.0.3.1', '/24'],
  ....:                    ['Fa0/4', '10.0.4.1', '/24'],
  ....:                    ['Lo0', '10.0.0.1', '/32']]
```

---
### Распаковка позиционных аргументов

Если пройтись по списку в цикле и передавать вложенный список как аргумент функции, возникнет ошибка:
```python
In [7]: for info in interfaces_info:
   ....:     print(config_interface(info))
   ....:
TypeError                                 Traceback (most recent call last)
<ipython-input-5-f7d6a9d80d48> in <module>()
      1 for info in interfaces_info:
----> 2      print(config_interface(info))
      3

TypeError: config_interface() missing 2 required positional arguments: 'ip_address' and 'cidr_mask'

``` 

---
### Распаковка позиционных аргументов

В такой ситуации пригодится распаковка аргументов.
Достаточно добавить ```*``` перед передачей списка как аргумента, и ошибки уже не будет:
```python
In [8]: for info in interfaces_info:
  ....:     print(config_interface(*info))
  ....:
['interface Fa0/1', 'no shutdown', 'ip address 10.0.1.1 255.255.255.0']
['interface Fa0/2', 'no shutdown', 'ip address 10.0.2.1 255.255.255.0']
['interface Fa0/3', 'no shutdown', 'ip address 10.0.3.1 255.255.255.0']
['interface Fa0/4', 'no shutdown', 'ip address 10.0.4.1 255.255.255.0']
['interface Lo0', 'no shutdown', 'ip address 10.0.0.1 255.255.255.255']
```

Python сам 'распакует' список info и передаст в функцию элементы списка как аргументы.

---
### Распаковка ключевых аргументов

---
### Распаковка ключевых аргументов

Аналогичным образом можно распаковывать словарь, чтобы передать его как ключевые аргументы.

Функция config_to_list (файл func_args_unpacking.py):
```python
def config_to_list(cfg_file, delete_excl=True,
                   delete_empty=True, strip_end=True):
    result = []
    with open(cfg_file) as f:
        for line in f:
            if strip_end:
                line = line.rstrip()
            if delete_empty and not line:
                pass
            elif delete_excl and line.startswith('!'):
                pass
            else:
                result.append(line)
    return result
```

---
### Распаковка ключевых аргументов

Пример использования:
```python
In [9]: config_to_list('r1.txt')
Out[9]:
['service timestamps debug datetime msec localtime show-timezone year',
 'service timestamps log datetime msec localtime show-timezone year',
 'service password-encryption',
 'service sequence-numbers',
 'no ip domain lookup',
 'ip ssh version 2']
```

---
### Распаковка ключевых аргументов

Список словарей ```cfg```, в которых указано имя файла и все аргументы:
```python
In [10]: cfg = [dict(cfg_file='r1.txt', delete_excl=True, delete_empty=True, strip_end=True),
   ....:        dict(cfg_file='r2.txt', delete_excl=False, delete_empty=True, strip_end=True),
   ....:        dict(cfg_file='r3.txt', delete_excl=True, delete_empty=False, strip_end=True),
   ....:        dict(cfg_file='r4.txt', delete_excl=True, delete_empty=True, strip_end=False)]
```

---
### Распаковка ключевых аргументов

Если передать словарь функции config_to_list, возникнет ошибка:
```python
In [11]: for d in cfg:
   ....:     print(config_to_list(d))
   ....:
TypeError                                 Traceback (most recent call last)
<ipython-input-4-8d1e8defad71> in <module>()
      1 for d in cfg:
----> 2     print(config_to_list(d))
      3

<ipython-input-1-6337ba2bfe7a> in config_to_list(cfg_file, delete_excl, delete_empty, strip_end)
      2                    delete_empty=True, strip_end=True):
      3     result = []
----> 4     with open( cfg_file ) as f:
      5         for line in f:
      6             if strip_end:

TypeError: expected str, bytes or os.PathLike object, not dict

```

---
### Распаковка ключевых аргументов

Если добавить ```**``` перед передачей словаря функции, функция нормально отработает:
```python
In [12]: for d in cfg:
    ...:     print(config_to_list(**d))
    ...:
['service timestamps debug datetime msec localtime show-timezone year', 'service timestamps log datetime msec localtime show-timezone year', 'service password-encryption', 'service sequence-numbers', 'no ip domain lookup', 'ip ssh version 2']
['!', 'service timestamps debug datetime msec localtime show-timezone year', 'service timestamps log datetime msec localtime show-timezone year', 'service password-encryption', 'service sequence-numbers', '!', 'no ip domain lookup', '!', 'ip ssh version 2', '!']
['service timestamps debug datetime msec localtime show-timezone year', 'service timestamps log datetime msec localtime show-timezone year', 'service password-encryption', 'service sequence-numbers', '', '', '', 'ip ssh version 2', '']
['service timestamps debug datetime msec localtime show-timezone year\n', 'service timestamps log datetime msec localtime show-timezone year\n', 'service password-encryption\n', 'service sequence-numbers\n', 'no ip domain lookup\n', 'ip ssh version 2\n']
```

---
### Пример использования ключевых аргументов переменной длины и распаковки аргументов

---
### Пример использования

С помощью аргументов переменной длины и распаковки аргументов
можно передавать аргументы между функциями.

Функция config_to_list (файл kwargs_example.py):
```python
def config_to_list(cfg_file, delete_excl=True,
                   delete_empty=True, strip_end=True):
    result = []
    with open(cfg_file) as f:
        for line in f:
            if strip_end:
                line = line.rstrip()
            if delete_empty and not line:
                pass
            elif delete_excl and line.startswith('!'):
                pass
            else:
                result.append(line)
    return result
```

---
### Виклик функції в ipython:

```python
In [1]: config_to_list('r1.txt')
Out[1]:
['service timestamps debug datetime msec localtime show-timezone year',
 'service timestamps log datetime msec localtime show-timezone year',
 'service password-encryption',
 'service sequence-numbers',
 'no ip domain lookup',
 'ip ssh version 2']
```

По умолчанию из конфигурации убираются пустые строки, перевод строки в конце строк и строки, которые начинаются на знак восклицания.

---
### Виклик функції

Виклик функції со значением ```delete_empty=False```:
```python
In [2]: config_to_list('r1.txt', delete_empty=False)
Out[2]:
['service timestamps debug datetime msec localtime show-timezone year',
 'service timestamps log datetime msec localtime show-timezone year',
 'service password-encryption',
 'service sequence-numbers',
 'no ip domain lookup',
 '',
 '',
 'ip ssh version 2']

```

---

Сделаем 'оберточную' функцию clear_cfg_and_write_to_file, которая берет файл конфигурации
с помощью функции config_to_list, удаляет лишние строки и затем записывает строки в указанный файл.

Но, при этом, мы не хотим терять возможность управлять тем, какие строки будут отброшены.
То есть, необходимо, чтобы функция clear_cfg_and_write_to_file поддерживала те же параметры, что и функция config_to_list.

---
### Дублирование параметров

Конечно, можно просто продублировать все параметры функции и передать их в функцию config_to_list:
```python
def clear_cfg_and_write_to_file(cfg, to_file, delete_excl=True,
                                delete_empty=True, strip_end=True):

    cfg_as_list = config_to_list(cfg, delete_excl=delete_excl,
                    delete_empty=delete_empty, strip_end=strip_end)
    with open(to_file, 'w') as f:
        f.write('\n'.join(cfg_as_list))
```

---
### Аргументы переменной длины

Но, если воспользоваться возможностью Python принимать аргументы переменной длины, можно сделать функцию clear_cfg_and_write_to_file такой:
```python
def clear_cfg_and_write_to_file(cfg, to_file, **kwargs):
    cfg_as_list = config_to_list(cfg, **kwargs)
    with open(to_file, 'w') as f:
        f.write('\n'.join(cfg_as_list))
```

---
## Есть ли какие-то рекомендации по поводу расположения функций в коде?

В [PEP8](https://pep8.org/) нет рекомендаций по этому поводу.

Если скрипт в одном файле, обычно порядок такой:
1. shebang, file encoding
2. docstring модуля
3. импорт
4. константы
5. все функции в условно произвольном порядке, то есть тут уже самому надо решить как удобнее
6. функции/код для создания CLI если есть
7. Часто, если есть код который надо писать глобально, а не в функции, создают функцию main
8. `if __name__ == "__main__":` и вызов функции main или глобального кода, который вызывает функции


При этом среди функций обычно выбирают для себя какой-то порядок, чтобы он был плюс-минус однотипным
в разных файлах. Например, сначала пишем общие функцие, которые не зависят от других функций в файле,
потом те что зависят. При этом обычно есть какой-то порядок выполнения действий: подключились на оборудование
и считали вывод, парсим его, записали результат в файл - тогда соблюдаем этот порядок в функциях.

> [О структуре больших проектов](https://docs.python-guide.org/writing/structure/). И еще одна ссылка по этой же теме, с [примерами структуры проектов Flask/Django](https://realpython.com/python-application-layouts/).


---
## звездочка

```python
a, *rest = [1, 2, 3, 4, 5]

def func1(*args, **kwargs):
    result = func2(*args, **kwargs)
    return result

items = [100, 200, *rest]
dict1 = {1: 100, 2: 200}
dict2 = {**dict1, 3: 300}

template.format(*items)
```
