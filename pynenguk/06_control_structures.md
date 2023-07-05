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

Цикл while - это еще одна разновидность цикла в Python. 

В цикле while, как и в выражении if, надо писать условие.
Если условие истинно, выполняются действия внутри блока while. 
В отличии от if, после выполнения while возвращается в начало цикла.

При использовании циклов while необходимо обращать внимание на то, будет ли достигнуто такое состояние, при котором условие цикла будет ложным.

---
### while

```python
In [1]: a = 5

In [2]: while a > 0:
   ...:     print(a)
   ...:     a -= 1 # Эта запись равнозначна a = a - 1
   ...:     
5
4
3
2
1
```

---
### while

Файл check_password_with_while.py:
```python
username = input('Введите имя пользователя: ' )
password = input('Введите пароль: ' )

password_correct = False

while not password_correct:
    if len(password) < 8:
        print('Пароль слишком короткий\n')
        password = input('Введите пароль еще раз: ' )
    elif username in password:
        print('Пароль содержит имя пользователя\n')
        password = input('Введите пароль еще раз: ' )
    else:
        print('Пароль для пользователя {} установлен'.format( username ))
        password_correct = True

```

---
### while

```
$ python check_password_with_while.py
Введите имя пользователя: nata
Введите пароль: nata
Пароль слишком короткий

Введите пароль еще раз: natanata
Пароль содержит имя пользователя

Введите пароль еще раз: 123345345345
Пароль для пользователя nata установлен
```

---
## break, continue, pass

---
### Оператор break

__Оператор break__ позволяет досрочно прервать цикл:
* break прерывает текущий цикл и продолжает выполнение следующих выражений
* если используется несколько вложенных циклов, break прерывает внутренний цикл и продолжает выполнять выражения, следующие за блоком
* break может использоваться в циклах for и while

---
### Оператор break

Пример с циклом for:
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

Пример с циклом while:
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

Файл check_password_with_while_break.py:
```python
username = input('Введите имя пользователя: ' )
password = input('Введите пароль: ' )

while True:
    if len(password) < 8:
        print('Пароль слишком короткий\n')
    elif username in password:
        print('Пароль содержит имя пользователя\n')
    else:
        print('Пароль для пользователя {} установлен'.format(username))
        # завершает цикл while
        break
    password = input('Введите пароль еще раз: ')
```

---
### Оператор continue

Оператор continue возвращает управление в начало цикла. То есть, continue позволяет "перепрыгнуть" оставшиеся выражения в цикле и перейти к следующей итерации.

Пример с циклом for:
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

Пример с циклом while:
```python
In [5]: i = 0
In [6]: while i < 6:
   ....:     i += 1
   ....:     if i == 3:
   ....:         print("Пропускаем 3")
   ....:         continue
   ....:         print("Это никто не увидит")
   ....:     else:
   ....:         print("Текущее значение: ", i)
   ....:         
Текущее значение:  1
Текущее значение:  2
Пропускаем 3
Текущее значение:  4
Текущее значение:  5
Текущее значение:  6
```

---
### Оператор continue

Файл check_password_with_while_continue.py:
```python
username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')

password_correct = False

while not password_correct:
    if len(password) < 8:
        print('Пароль слишком короткий\n')
    elif username in password:
        print('Пароль содержит имя пользователя\n')
    else:
        print(f'Пароль для пользователя {username} установлен')
        password_correct = True
        continue
    password = input('Введите пароль еще раз: ')

```

---
### Оператор continue

Результат выполнения будет таким:
```
$ python check_password_with_while_continue.py
Введите имя пользователя: nata
Введите пароль: nata12
Пароль слишком короткий

Введите пароль еще раз: natalksdjflsdjf
Пароль содержит имя пользователя

Введите пароль еще раз: asdfsujljhdflaskjdfh
Пароль для пользователя nata установлен
```

---
### Оператор pass

Оператор ```pass``` ничего не делает. Фактически, это такая заглушка для объектов.

Например, ```pass``` может помочь в ситуации, когда нужно прописать структуру скрипта.
Его можно ставить в циклах, функциях, классах. И это не будет влиять на исполнение кода.

Пример использования pass:
```python
In [6]: for num in range(5):
   ....:     if num < 3:
   ....:         pass
   ....:     else:
   ....:         print(num)
   ....:         
3
4
```

---
## Работа с исключениями try/except/else/finally

---
### try/except

Примеры исключений:
```python
In [1]: 2/0
-----------------------------------------------------
ZeroDivisionError: division by zero

In [2]: 'test' + 2
-----------------------------------------------------
TypeError: must be str, not int
```

Когда в программе возникает исключение, она сразу завершает работу.

---
### try/except

Для работы с исключениями используется конструкция ```try/except```:
```python
In [3]: try:
   ...:     2/0
   ...: except ZeroDivisionError:
   ...:     print("You can't divide by zero")
   ...:     
You can't divide by zero
```

---
### Конструкция try работает таким образом

* сначала выполняются выражения, которые записаны в блоке try
* если при выполнения блока try не возникло никаких исключений, блок except пропускается, и выполняется дальнейший код
* если во время выполнения блока try в каком-то месте возникло исключение, оставшаяся часть блока try пропускается
 * если в блоке except указано исключение, которое возникло, выполняется код в блоке except
 * если исключение, которое возникло, не указано в блоке except, выполнение программы прерывается и выдается ошибка

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

В конструкции try/except может быть много except, если нужны разные действия в зависимости от типа ошибки.

```python
try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    print("Результат: ", int(a)/int(b))
except ValueError:
    print("Пожалуйста, вводите только числа")
except ZeroDivisionError:
    print("На ноль делить нельзя")
```

---
### try/except

Примеры выполнения скрипта:
```
$ python divide.py
Введите первое число: 3
Введите второе число: 1
Результат:  3

$ python divide.py
Введите первое число: 5
Введите второе число: 0
На ноль делить нельзя

$ python divide.py
Введите первое число: qewr
Введите второе число: 3
Пожалуйста, вводите только числа
```

---
### try/except

Если нет необходимости выводить различные сообщения на ошибки ValueError и ZeroDivisionError, можно сделать так (файл divide_ver2.py):
```python
try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    print("Результат: ", int(a)/int(b))
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так...")

```

---
### try/except

```python
$ python divide_ver2.py
Введите первое число: wer
Введите второе число: 4
Что-то пошло не так...

$ python divide_ver2.py
Введите первое число: 5
Введите второе число: 0
Что-то пошло не так...
```

---
### try/except/else

В конструкции try/except есть опциональный блок else. Он выполняется в том случае, если не было исключения.

Например, если необходимо выполнять в дальнейшем какие-то операции с данными, которые ввел пользователь, можно записать их в блоке else (файл divide_ver3.py): 
```python
try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    result = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так...")
else:
    print("Результат в квадрате: ", result**2)
```

---
### try/except/else

Пример выполнения:
```python
$ python divide_ver3.py
Введите первое число: 10
Введите второе число: 2
Результат в квадрате:  25

$ python divide_ver3.py
Введите первое число: werq
Введите второе число: 3
Что-то пошло не так...
```

---
### try/except/finally

Блок finally - это еще один опциональный блок в конструкции try. Он выполняется __всегда__, независимо от того, было ли исключение или нет.

Сюда ставятся действия, которые надо выполнить в любом случае. Например, это может быть закрытие файла.

Файл divide_ver4.py с блоком finally:
```python
a = input("Введите первое число: ")
b = input("Введите второе число: ")
try:
    result = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так...")
else:
    print("Результат в квадрате: ", result**2)
finally:
    print("Вот и сказочке конец, а кто слушал - молодец.")

```

---
### try/except/finally

```python
$ python divide_ver4.py
Введите первое число: 10
Введите второе число: 2
Результат в квадрате:  25
Вот и сказочке конец, а кто слушал - молодец.

$ python divide_ver4.py
Введите первое число: qwerewr
Введите второе число: 3
Что-то пошло не так...
Вот и сказочке конец, а кто слушал - молодец.

$ python divide_ver4.py
Введите первое число: 4
Введите второе число: 0
Что-то пошло не так...
Вот и сказочке конец, а кто слушал - молодец.
```

---
### Когда использовать исключения

Как правило, один и тот же код можно написать и с использованием исключений, и без них.

```python
while True:
    a = input("Введите число: ")
    b = input("Введите второе число: ")
    try:
        result = int(a)/int(b)
    except ValueError:
        print("Поддерживаются только числа")
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    else:
        print(result)
        break

```

---
### Когда использовать исключения

Можно переписать таким образом без try/except (файл try_except_divide.py):
```python
while True:
    a = input("Введите число: ")
    b = input("Введите второе число: ")
    if a.isdigit() and b.isdigit():
        if int(b) == 0:
            print("На ноль делить нельзя")
        else:
            print(int(a)/int(b))
            break
    else:
        print("Поддерживаются только числа")

```

---
### Когда использовать исключения

Важно в каждой конкретной ситуации оценивать, какой вариант кода более понятный, компактный и универсальный - с исключениями или без.

Если вы раньше использовали какой-то другой язык программирования, есть вероятность, что в нем использование исключений считалось плохим тоном.
В Python этот не так.

---
### LBYL vs EAFP

* LBYL - look before you leap
* EAFP - easier to ask forgiveness than permission 

---
### LBYL vs EAFP

EAFP - easier to ask forgiveness than permission 
```python
a = input("Введите число: ")
b = input("Введите второе число: ")
try:
    result = int(a) / int(b)
except ValueError:
    print("Поддерживаются только числа")
except ZeroDivisionError:
    print("На ноль делить нельзя")
else:
    print(result)
```

LBYL - look before you leap

```python
a = input("Введите число: ")
b = input("Введите второе число: ")
if a.isdigit() and b.isdigit():
    if int(b) == 0:
        print("На ноль делить нельзя")
    else:
        print(int(a) / int(b))
else:
    print("Поддерживаются только числа")
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

