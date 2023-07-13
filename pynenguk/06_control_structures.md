# Контроль перебігу програми

* if/elif/else
* for
* while
* try/except

---

## if/elif/else

---
### if/elif/else

* Перевірка if завжди йде першою
* Після оператора if має бути якась умова: якщо ця умова виконується, дії в блоці if виконуються
* За допомогою elif можна зробити кілька розгалужень, тобто перевіряти вхідні дані на різні умови
* Блоків elif може бути багато
* Блок else виконується у тому випадку, якщо жодна з умов if або elif не була істинною


```python
if expression:
    ...


if expression:
    ...
else:
    ...


if expression:
    ...
elif expression:
    ...
elif expression:
    ...
else:
    ...
```

---
### if/elif/else

```python
if expression:
    ...
elif expression:
    ...
elif expression:
    ...
```


---
### if/elif/else

```python
if expression:
    ...
if expression:
    ...
if expression:
    ...
```

---
### if/elif/else

```python
number = int(input("Enter number: "))

if number == 10:
    print('number дорівнює 10')
elif numer < 10:
    print('number менше 10')
else:
    print('number більше 10')
```


---
### if/elif/else

```python
number = int(input("Enter number: "))

if number == 10:
    print('number дорівнює 10')
elif numer < 10:
    print('number менше 10')
elif numer > 10:
    print('number більше 10')
else:
    print("Кінець")
```


---
### if/elif/else

```python
In [7]: 5 > 3
Out[7]: True

In [8]: 5 == 5
Out[8]: True

In [9]: 'vlan' in 'switchport trunk allowed vlan 10,20'
Out[9]: True

In [10]: 1 in [1, 2, 3]
Out[10]: True

In [11]: 0 in [1, 2, 3]
Out[11]: False
```

---
### True и False

У Python, крім очевидних значень True і False, усі інші об'єкти також
мають хибне або істинне значення:

* істинне:
    * будь-яке ненульове число
    * будь-який непорожній рядок
    * будь-який непорожній об'єкт

* хибне:
    * 0
    * None
    * порожній рядок
    * порожній об'єкт (список, словник, множина тощо)



---
### True и False

```python
list_to_test = [1, 2, 3]

if list_to_test:
    print("У списку є об'єкти")


if len(list_to_test) != 0:
    print("У списку є об'єкти")
```

---
## Оператори порівняння

Оператори порівняння, які можна використовувати в умовах:

```python
In [3]: 5 > 6
Out[3]: False

In [4]: 5 > 2
Out[4]: True

In [5]: 5 < 2
Out[5]: False

In [6]: 5 == 2
Out[6]: False

In [7]: 5 == 5
Out[7]: True

In [8]: 5 >= 5
Out[8]: True

In [9]: 5 <= 10
Out[9]: True

In [10]: 8 != 10
Out[10]: True
```

---
### Оператор in

Оператор `in` дозволяє виконувати перевірку на наявність елемента у
послідовності (наприклад, елемента у списку або підрядка в рядку):
```python
In [8]: 'Fast' in 'FastEthernet'
Out[8]: True

In [9]: 'Gigabit' in 'FastEthernet'
Out[9]: False

In [10]: vlan = [10, 20, 30, 40]

In [11]: 10 in vlan
Out[11]: True

In [12]: 50 in vlan
Out[12]: False
```

---
### Оператор in

При використанні зі словниками `in` перевіряє ключі словника:
```python
r1 = {
    'ios': '15.4',
    'ip': '10.255.0.1',
    'hostname': 'london_r1',
    'location': '21 New Globe Walk',
    'model': '4451',
    'vendor': 'Cisco'
}

In [16]: 'ios' in r1
Out[16]: True

In [17]: '4451' in r1
Out[17]: False
```

---
### Оператори and, or

```python
r1 = {
    'ios': '15.4',
    'ip': '10.255.0.1',
    'hostname': 'london_r1',
    'location': '21 New Globe Walk',
    'model': '4451',
    'vendor': 'Cisco'
}

In [18]: vlan = [10, 20, 30, 40]

In [19]: 'ios' in r1 and 10 in vlan
Out[19]: True

In [21]: '4451' in r1 or 10 in vlan
Out[21]: True
```

---
### Оператор and

У Python оператор and повертає не булеве значення, а значення одного з
виразів/елементів.

Якщо обидва елементи істинні, результатом виразу буде останнє значення:

```python
In [24]: 'string1' and 'string2'
Out[24]: 'string2'

In [25]: 'string1' and 'string2' and 'string3'
Out[25]: 'string3'
```

---
### Оператор or

Оператор or, як і оператор and, повертає значення одного з елементів.

Під час обчислення елементів повертається перший істинний елемент:

```python
In [28]: '' or 'string1'
Out[28]: 'string1'

In [29]: '' or [] or 'string1'
Out[29]: 'string1'

In [30]: 'string1' or 'string2'
Out[30]: 'string1'
```

---
### Логічні оператори and, or, not

| Вираз | Результат
|----------------|-----------|
| True and True  | True |
| True and False | False |
| False and True | False | 
| False and False | False |
| | |
| True or True | True |
| True or False | True |
| False or True | True |
| False or False | False |
| | |
| not True | False |
| not False | True |



---
### Логічні оператори and, or, not

Логічні операції, упорядковані за зростанням пріоритету

| Операція | Результат |
|----------|-----------|
| `a or b` | якщо a істинне, то a, інакше b |
| `a and b`| якщо a хибне, то a, інакше b |
| `not a`  | якщо a хибне, то True, інакше False |

---
### Логічні оператори and, or, not

Логічні операції, упорядковані за зростанням пріоритету

| Операція | Результат | Примітка |
|----------|-----------|----------|
| `a or b` | якщо a істинне, то a, інакше b | b обчислюється тільки якщо a хибне |
| `a and b`| якщо a хибне, то a, інакше b | b обчислюється тільки якщо a істинне |
| `not a`  | якщо a хибне, то True, інакше False |  |

---

### Обчислення за короткою схемою ([Short-Circuit evaluation](https://en.wikipedia.org/wiki/Short-circuit_evaluation))

```python
In [1]: True and print(10)
10

In [2]: False and print(10)
Out[2]: False

In [3]: False or print(10)
10

In [4]: False or print(10) or True
10
Out[4]: True
```

---
### [Пріоритет операторів](https://docs.python.org/3/reference/expressions.html#operator-precedence)

* ``x[index] x[i:j] x(arg1, arg2, ...) x.attr``
* ``* / %``
* ``+ -``
* ``in``, ``not in``, ``is``, ``is not``, ``< <= > >= != ==``
* ``not x``
* ``and``
* ``or``

---
### Приклад використання конструкції if/elif/else

```python
username = input('Введіть ім'я користувача: ")
password = input('Введіть пароль: ")

if len(password) < 8:
    print("Пароль надто короткий")
elif username in password:
    print("Пароль містить ім'я користувача")
else:
    print(f"Пароль для користувача {username} встановлено")
```


---
### Перевірка скрипту:

```
$ python check_password.py
Введіть ім'я користувача: nata
Введіть пароль: nata1234
Пароль містить ім'я користувача

$ python check_password.py
Введіть ім'я користувача: nata 
Введіть пароль: 123nata123
Пароль містить ім'я користувача

$ python check_password.py
Введіть ім'я користувача: nata
Введіть пароль: 1234
Пароль надто короткий

$ python check_password.py
Введіть ім'я користувача: nata
Введіть пароль: 123456789
Пароль для користувача nata встановлено
```

---
## for

---
### for

Цикл for перебирає елементи вказаної послідовності один за одним і
виконує дії, вказані в блоці for для кожного елемента.

Приклади послідовностей елементів, по яким цикл for може виконувати ітерацію:

* рядок
* список
* словник
* range
* будь-який ітерований об'єкт

```python
vlans = [10, 20, 30, 40, 100]

for vlan in vlans:
    print(vlan)
```

---
### for

```python
In [1]: for letter in 'Test string':
   ...:     print(letter)
   ...:     
T
e
s
t

s
t
r
i
n
g
```

---
### for


```python
In [2]: for i in range(10):
   ...:     print('interface FastEthernet0/{}'.format(i))
   ...:     
interface FastEthernet0/0
interface FastEthernet0/1
interface FastEthernet0/2
interface FastEthernet0/3
interface FastEthernet0/4
interface FastEthernet0/5
interface FastEthernet0/6
interface FastEthernet0/7
interface FastEthernet0/8
interface FastEthernet0/9
```

---
### for

У цьому прикладі цикл проходить за списком VLAN, тому змінну можна назвати vlan:

```python
vlans = [10, 20, 30, 40, 100]
for vlan in vlans:
    print('vlan {}'.format(vlan))
    print(' name VLAN_{}'.format(vlan))
    

vlan 10
 name VLAN_10
vlan 20
 name VLAN_20
vlan 30
 name VLAN_30
vlan 40
 name VLAN_40
vlan 100
 name VLAN_100
```

---
### for

Коли цикл for проходить через словник, він виконує ітерацію за ключами:

```python
r1 = {
    'ios': '15.4',
    'ip': '10.255.0.1',
    'hostname': 'london_r1',
    'location': '21 New Globe Walk',
    'model': '4451',
    'vendor': 'Cisco',
}

In [6]: for k in r1:
   ....:     print(k)
   ....:     
vendor
ip
hostname
ios
location
model
```

---
### for

Якщо потрібно вивести пари ключ-значення в циклі, можна зробити так:

```python
In [7]: for key in r1:
   ....:     print(key + ' => ' + r1[key])
   ....:     
vendor => Cisco
ip => 10.255.0.1
hostname => london_r1
ios => 15.4
location => 21 New Globe Walk
model => 4451
```

---
### for

Або скористатися методом items, який дозволяє отримати пару ключ-значення:

```python
In [8]: for key, value in r1.items():
   ....:     print(key + ' => ' + value)
   ....:     
vendor => Cisco
ip => 10.255.0.1
hostname => london_r1
ios => 15.4
location => 21 New Globe Walk
model => 4451
```

---
### Вкладені for

```python
In [7]: commands = ['switchport mode access', 'spanning-tree portfast', 'spanning-tree bpduguard enable']
In [8]: fast_int = ['0/1', '0/3', '0/4', '0/7']

In [9]: for intf in fast_int:
   ...:     print(f'interface FastEthernet {intf}')
   ...:     for command in commands:
   ...:         print(f' {command}')
   ...:
interface FastEthernet 0/1
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet 0/3
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet 0/4
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
...
```

---
### Комбінування for і if

Файл generate_access_port_config.py:
```python
access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

access = {'0/12': 10, '0/14': 11, '0/16': 17, '0/17': 150}

for intf, vlan in access.items():
    print(f'interface FastEthernet{intf}')
    for command in access_template:
        if command.endswith('access vlan'):
            print(f' {command} {vlan}')
        else:
            print(' {command}')

```

---
### Комбінування for і if

```
$ python generate_access_port_config.py
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
interface FastEthernet0/17
 switchport mode access
 switchport access vlan 150
 spanning-tree portfast
 spanning-tree bpduguard enable
```

---
## while

---
### while

Цикл while - це ще один різновид циклу в Python.

У циклі while, як і в if, треба писати умову. Якщо умова є істинною,
виконуються дії всередині блоку while. Але, на відміну від if, після
виконання коду в блоці, while повертається на початок циклу.

Під час використання циклів while слід звертати увагу  на те, чи буде досягнуто
такий стан, за якого умова циклу буде хибною.


```python
while not ping_ip(server_ip):
    time.sleep(pause)
```

---
### while

```python
while not ping_ip(server_ip):
    time.sleep(pause)
```

---
### while

```python
output = ""
while True:
    time.sleep(pause)
    try:
        part = ssh.recv(max_read)
        output += part
    except OSError:
        break
```

---
### while

```python
In [1]: a = 5

In [2]: while a > 0:
   ...:     print(num1)
   ...:     a -= 1
   ...:     
5
4
3
2
1
```

---
### while

```python
username = input("Введіть ім'я користувача: ")
password = input("Введіть пароль: ")

password_correct = False

while not password_correct:
    if len(password) < 8:
        print("Пароль надто короткий\n")
        password = input("Введіть пароль ще раз: ")
    elif username in password:
        print("Пароль містить ім'я користувача\n")
        password = input("Введіть пароль ще раз: ")
    else:
        print(f"Пароль для користувача {username} встановлено")
        password_correct = True
```

---
### while

```
$ python check_password_with_while.py
Введіть ім'я користувача: nata
Введіть пароль: nata
Пароль надто короткий

Введіть пароль ще раз: natanata
Пароль містить ім'я користувача

Введіть пароль ще раз: 123345345345
Пароль для користувача nata встановлено
```

---
## break, continue, pass

---
### Оператор break

Оператор break дозволяє достроково перервати цикл:

* break перериває поточний цикл і продовжує виконання наступних виразів
* якщо використовується кілька вкладених циклів, break перериває внутрішній цикл і продовжує виконувати вирази, що йдуть за блоком
* break може використовуватися в циклах for та while

---
### Оператор break

```python
In [1]: for num in range(10):
   ...:     if num < 7:
   ...:         print(num)
   ...:     else:
   ...:         break
   ...:     
0
1
2
3
4
5
6
```

---
### Оператор break

```python
In [2]: i = 0
In [3]: while i < 10:
   ...:     if i == 5:
   ...:         break
   ...:     else:
   ...:         print(i)
   ...:         i += 1
   ...:         
0
1
2
3
4
```

---
### Оператор break

```python
username = input("Введіть ім'я користувача: ")
password = input("Введіть пароль: ")

while True:
    if len(password) < 8:
        print("Пароль надто короткий\n")
    elif username in password:
        print("Пароль містить ім'я користувача\n")
    else:
        print("Пароль для користувача {} встановлено".format(username))
        # завершує цикл while
        break
    password = input("Введіть пароль ще раз: ")
```

---
### Оператор continue

Оператор continue повертає керування на початок циклу. Тобто, continue дозволяє
"перестрибнути" вирази, що залишилися в циклі і перейти до наступної ітерації.

```python
In [4]: for num in range(5):
   ...:     if num == 3:
   ...:         continue
   ...:     else:
   ...:         print(num)
   ...:         
0
1
2
4
```

---
### Оператор continue

```python
i = 0

while i < 6:
    i += 1
    if i == 3:
        print("Пропускаємо 3")
        continue
        print("Це ніхто не побачить")
    else:
        print("Поточне значення: ", i)
```

```
Поточне значення:  1
Поточне значення:  2
Пропускаємо 3
Поточне значення:  4
Поточне значення:  5
Поточне значення:  6
```

---
### Оператор continue

```python
username = input("Введіть ім'я користувача: ")
password = input("Введіть пароль: ")

password_correct = False

while not password_correct:
    if len(password) < 8:
        print("Пароль надто короткий\n")
    elif username in password:
        print("Пароль містить ім'я користувача\n")
    else:
        print("Пароль для користувача {} встановлено'.format(username))
        password_correct = True
        continue
    password = input("Введіть пароль ще раз: ")
```

```
$ python check_password_with_while_continue.py
Введіть ім'я користувача: nata
Введіть пароль: nata12
Пароль надто короткий

Введіть пароль ще раз: natalksdjflsdjf
Пароль містить ім'я користувача

Введіть пароль ще раз: asdfsujljhdflaskjdfh
Пароль для користувача nata встановлено
```

---
### Оператор pass

Оператор pass нічого не робить. Фактично це така заглушка для блоків коду.

Наприклад, pass може допомогти ситуації, коли потрібно прописати структуру
скрипта. Його можна ставити у циклах, функціях, класах. І це не впливатиме на
виконання коду.

Приклад використання pass:

```python
for num in range(5):
    if num < 3:
        pass
    else:
        print(num)
```

Результат
```
3
4
```

---
## Робота з винятками try/except/else/finally

---
### try/except

Приклади винятків:
```python
In [1]: 2/0
-----------------------------------------------------
ZeroDivisionError: division by zero

In [2]: 'test' + 2
-----------------------------------------------------
TypeError: must be str, not int
```

---
### try/except

Для роботи з винятками використовується конструкція try/except:
```python
In [3]: try:
   ...:     2/0
   ...: except ZeroDivisionError:
   ...:     print("You can't divide by zero")
   ...:     
You can't divide by zero
```

---
### Конструкція try працює таким чином

* спочатку виконуються вирази, які записані в блоці try
* якщо під час виконання блоку try не виникло жодних винятків, блок except пропускається, і виконується подальший код
* якщо під час виконання блоку try в якомусь місці виник виняток, частина блоку try, що залишилася, пропускається
* якщо в блоці except зазначено виняток, який виник, виконується код у блоці except
* якщо виняток, який виник, не вказано в блоці except, виконання програми переривається та генерується виняток

---
### try/except

```python
In [4]: try:
   ...:     print("Let's divide some numbers")
   ...:     2/0
   ...:     print('Cool!')
   ...: except ZeroDivisionError:
   ...:     print("You can't divide by zero")
   ...:     
Let's divide some numbers
You can't divide by zero
```

---
### try/except

У конструкції try/except може бути багато except, якщо потрібні різні дії,
залежно від типу помилки.

Наприклад, скрипт divide.py ділить два числа введених користувачем:

```python
num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")

try:
    print("Результат: ", int(num1) / int(num2))
except ValueError:
    print("Вводьте лише числа")
except ZeroDivisionError:
    print("На нуль ділити не можна")
```

---
### try/except

Приклади виконання скрипту:

```
$ python divide.py
Введіть перше число: 3
Введіть друге число: 1
Результат:  3

$ python divide.py
Введіть перше число: 5
Введіть друге число: 0
На нуль ділити не можна

$ python divide.py
Введіть перше число: qewr
Введіть друге число: 3
Вводьте лише числа
```

---
### try/except

Якщо немає потреби виводити різні повідомлення на помилки ValueError та
ZeroDivisionError, можна зробити так:

```python
num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")

try:
    print("Результат: ", int(num1)/int(num2))
except (ValueError, ZeroDivisionError):
    print("Щось пішло не так...")
```

---
### try/except

```python
$ python divide_ver2.py
Введіть перше число: wer
Введіть друге число: 4
Щось пішло не так...

$ python divide_ver2.py
Введіть перше число: 5
Введіть друге число: 0
Щось пішло не так...
```

---
### try/except/else

У конструкції try/except є опціональний блок else. Він виконується у тому
випадку, якщо не було винятку.

Наприклад, якщо необхідно виконувати надалі якісь операції з даними, які ввів
користувач, можна записати їх у блоці else:

```python
num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")

try:
    result = int(num1)/int(num2)
except (ValueError, ZeroDivisionError):
    print("Щось пішло не так...")
else:
    print("Результат: ", result)
```

---
### try/except/else

```python
$ python divide_ver3.py
Введіть перше число: 10
Введіть друге число: 2
Результат:  5

$ python divide_ver3.py
Введіть перше число: werq
Введіть друге число: 3
Щось пішло не так...
```

---
### try/except/finally

Блок finally – це ще один опціональний блок у конструкції try. Він виконується
завжди, незалежно від того, чи був виняток чи ні.

Сюди ставляться дії, які треба виконати у будь-якому випадку. Наприклад, це
може бути закриття файлу, вивільнення якихось ресурсів.

Приклад із блоком finally:

```python
num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")

try:
    result = int(num1)/int(num2)
except (ValueError, ZeroDivisionError):
    print("Щось пішло не так...")
else:
    print("Результат: ", result**2)
finally:
    print("The End")
```

---
### try/except/finally

```python
$ python divide_ver4.py
Введіть перше число: 10
Введіть друге число: 2
Результат:  5
The End

$ python divide_ver4.py
Введіть перше число: qwerewr
Введіть друге число: 3
Щось пішло не так...
The End

$ python divide_ver4.py
Введіть перше число: 4
Введіть друге число: 0
Щось пішло не так...
The End
```

---
## Коли використовувати винятки

Як правило, той самий код можна написати і з використанням винятків, і без них.
Наприклад, цей варіант коду:

```python
while True:
    num1 = input("Введіть перше число: ")
    num2 = input("Введіть друге число: ")
    try:
        result = int(num1)/int(num2)
    except ValueError:
        print("Підтримуються лише числа")
    except ZeroDivisionError:
        print("На нуль ділити не можна")
    else:
        print(result)
        break
```

---
## Коли використовувати винятки

Можна переписати код таким чином без try/except:

```python
while True:
    a = input("Введите число: ")
    b = input("Введите второе число: ")
    if num1.isdigit() and num2.isdigit():
        if int(num2) == 0:
            print("На ноль делить нельзя")
        else:
            print(int(num1)/int(num2))
            break
    else:
        print("Поддерживаются только числа")

```

---
## Коли використовувати винятки

Важливо в кожній конкретній ситуації оцінювати, який варіант коду зрозуміліший,
компактніший і універсальніший - з винятками або без.

Якщо ви раніше використовували якусь іншу мову програмування, є ймовірність, що
використання винятків вважалося поганим тоном. У Python це не так.

---
### LBYL vs EAFP

* LBYL - look before you leap
* EAFP - easier to ask forgiveness than permission 

---
### LBYL vs EAFP

EAFP - easier to ask forgiveness than permission 

```python
num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")

try:
    result = int(num1) / int(num2)
except ValueError:
    print("Вводьте лише числа")
except ZeroDivisionError:
    print("На нуль ділити не можна")
else:
    print(result)
```

LBYL - look before you leap

```python
num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")

if num1.isdigit() and num2.isdigit():
    if int(num2) == 0:
		print("На нуль ділити не можна")
    else:
        print(int(num1) / int(num2))
else:
    print("Вводьте лише числа")
```

---
### for/else, while/else

В циклах for и while опционально может использоваться блок else.

for/else

* блок else выполняется в том случае, если цикл завершил итерацию списка
* но else не выполняется, если в цикле был выполнен break

while/else

* блок else выполняется в том случае, если условие в while ложно
* else не выполняется, если в цикле был выполнен break

