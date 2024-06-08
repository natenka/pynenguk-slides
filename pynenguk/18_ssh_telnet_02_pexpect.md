# Python для мережевих інженерів 


---
## Модуль pexpect

---
### Модуль pexpect

Модуль pexpect дозволяє автоматизувати такі інтерактивні з’єднання, як:
* telnet
* ssh
* ftp


Спочатку потрібно встановити модуль pexpect:
```
pip install pexpect
```

---
### Модуль pexpect

Логіка pexpect полягає в наступному:
* запускається якась програма
* pexpect очікує певного результату (підказка, запит пароля тощо)
* після отримання виводу він надсилає команди/дані
* останні два кроки повторюються стільки, скільки потрібно

При цьому сам pexpect не реалізує різні утиліти, а використовує вже готові.

---
### Модуль pexpect

pexpect має два основних інструменти:
* функція ```run```
* клас ```spawn```

---
### ```pexpect.run```

Функція ``run`` дозволяє викликати програму та повернути її результат.

```python
In [1]: import pexpect

In [2]: output = pexpect.run('ls -ls')

In [3]: print(output)
b'total 44\r\n4 -rw-r--r-- 1 vagrant vagrant 3203 Jul 14 07:15 1_pexpect.py\r\n4 -rw-r--r-- 1 vagrant vagrant 3393 Jul 14 07:15 2_telnetlib.py\r\n4 -rw-r--r-- 1 vagrant vagrant 3452 Jul 14 07:15 3_paramiko.py\r\n'

In [4]: print(output.decode('utf-8'))
total 44
4 -rw-r--r-- 1 vagrant vagrant 3203 Jul 14 07:15 1_pexpect.py
4 -rw-r--r-- 1 vagrant vagrant 3393 Jul 14 07:15 2_telnetlib.py
4 -rw-r--r-- 1 vagrant vagrant 3452 Jul 14 07:15 3_paramiko.py

```

---
### ```pexpect.spawn```

Клас ```spawn``` підтримує більше можливостей. Він дозволяє взаємодіяти з викликаною програмою, надсилаючи дані та очікуючи певні відповіді.

```python
s = pexpect.spawn('ssh user@10.1.1.1')
 
s.expect('Password:')
s.sendline('userpass')
s.expect('>')
```

---
### ```pexpect.spawn```

Наприклад, таким чином можна ініціювати з'єднання SSH:
```python
In [5]: ssh = pexpect.spawn('ssh cisco@192.168.100.1')
```


---
### pexpect.expect

У pexpect.expect як шаблон можна використовувати:
* регулярний вираз
* EOF - цей шаблон дозволяє реагувати на виняток EOF
* TIMEOUT - виняток timeout (значення за замовчуванням timeout = 30 секунд)
* compiled re

```python
In [6]: ssh.expect('[Pp]assword')
Out[6]: 0
```

Рядок, який очікує pexpect: ```[Pp]assword``` - це регулярний вираз, який описує рядок `password` або `Password`.


---
### pexpect.expect

Метод expect повернув число 0 в результаті своєї роботи.
Це число вказує на те, що знайдено збіг і що це елемент з нульовим індексом.
Індекс з’являється тут, оскільки expect можна передавати список рядків.

Наприклад, ви можете передати список з двох елементів:
```python
In [7]: ssh = pexpect.spawn('ssh cisco@192.168.100.1')

In [8]: ssh.expect(['password', 'Password'])
Out[8]: 1
```

---
### pexpect.sendline

Для надсилання команд використовуйте команду sendline:
```python
In [9]: ssh.sendline('cisco')
Out[9]: 6
```

Команда sendline надсилає рядок, автоматично додає новий рядок на основі значення os.linesep, а потім повертає число, яке вказує кількість записаних байтів.

---
### expect-sendline

Щоб перейти в режим enable, повторюється цикл очікування-надсилання (expect-sendline):
```python
In [10]: ssh.expect('[>#]')
Out[10]: 0

In [11]: ssh.sendline('enable')
Out[11]: 7

In [12]: ssh.expect('[Pp]assword')
Out[12]: 0

In [13]: ssh.sendline('cisco')
Out[13]: 6

In [14]: ssh.expect('[>#]')
Out[14]: 0
```

---
### Надсилання команди

Тепер можна відправити команду:
```python
In [15]: ssh.sendline('sh ip int br')
Out[15]: 13
```

Після надсилання команди pexpect треба вказати, до якого моменту читати вихідні дані.
Вказуємо, що потрібно дочекатися `#`:
```python
In [16]: ssh.expect('#')
Out[16]: 0
```

---
### Отримання виводу з before

Результат команди знаходиться в атрибуті before:
```python
In [17]: ssh.before
Out[17]: b'sh ip int br\r\nInterface                  ip-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                19.1.1.1        YES NVRAM  up                    up      \r\nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \r\nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      \r\nR1'
```

---
### Отримання виводу з before

Оскільки результат виводиться як послідовність байтів, нам потрібно перетворити його на рядок:
```python
In [18]: show_output = ssh.before.decode('utf-8')

In [19]: print(show_output)
sh ip int br
Interface                  ip-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
Ethernet0/2                19.1.1.1        YES NVRAM  up                    up
Ethernet0/3                192.168.230.1   YES NVRAM  up                    up
Ethernet0/3.100            10.100.0.1      YES NVRAM  up                    up
Ethernet0/3.200            10.200.0.1      YES NVRAM  up                    up
Ethernet0/3.300            10.30.0.1       YES NVRAM  up                    up
R1
```

---
### Закриття сесії

Сесія завершується викликом методу close:
```python
In [20]: ssh.close()
```

---
### Спеціальні символи в shell

Pexpect не інтерпретує спеціальні символи shell, такі як ``>``, ``|``, ``*``.

Для того, щоб, наприклад, команда ``ls -ls | grep SUMMARY`` спрацювала, потрібно запустити shell так:

```python
In [1]: import pexpect

In [2]: p = pexpect.spawn('/bin/bash -c "ls -ls | grep pexpect"')

In [3]: p.expect(pexpect.EOF)
Out[3]: 0

In [4]: print(p.before)
b'4 -rw-r--r-- 1 vagrant vagrant 3203 Jul 14 07:15 1_pexpect.py\r\n'

In [5]: print(p.before.decode('utf-8'))
4 -rw-r--r-- 1 vagrant vagrant 3203 Jul 14 07:15 1_pexpect.py

```

---
### pexpect.EOF

У попередньому прикладі використовувався pexpect.EOF.

Це спеціальне значення, яке дозволяє реагувати на завершення команди або сеансу, який було запущено в spawn.

Під час виклику команди ``ls -ls`` pexpect не отримує інтерактивний сеанс.
Команда виконана і все, її робота завершена.

Тому якщо запустити її та вказати в expect запрошення, виникне помилка:
```python
In [5]: p = pexpect.spawn('/bin/bash -c "ls -ls | grep SUMMARY"')

In [6]: p.expect('nattaur')
---------------------------------------------------------------------------
EOF                                       Traceback (most recent call last)
<ipython-input-9-9c71777698c2> in <module>()
----> 1 p.expect('nattaur')
...
```

Але якщо передати в expect EOF, помилки не буде.

---
### Метод pexpect.expect

У pexpect.expect як шаблон можна використовувати:
* регулярний вираз
* EOF - дозволяє реагувати на виняток EOF
* TIMEOUT - виняток timeout (значення за замовчуванням timeout = 30 секунд)
* compiled re

---
### Метод pexpect.expect


Ще одна дуже корисна можливість pexpect.expect можна передавати не одне значення, а список:

```python
In [7]: p = pexpect.spawn('/bin/bash -c "ls -ls | grep netmiko"')

In [8]: p.expect(['py3_convert', pexpect.TIMEOUT, pexpect.EOF])
Out[8]: 2

```

---
### Метод pexpect.expect

Тут є кілька важливих моментів:
* коли pexpect.expect викликається зі списком, можна вказати різні очікувані рядки
* крім рядків, можете вказати винятки
* pexpect.expect повертає номер елемента списку, який ініціював
  * у цьому випадку номер 2, оскільки виняток EOF є номером два у списку
* завдяки цьому формату можна робити розгалуження в програмі в залежності від того, з яким елементом був збіг

---
### Приклад використання pexpect

Приклад використання pexpect для підключення до обладнання та надсилання команди show (файл 1_pexpect.py):

```python
import pexpect
import getpass
import sys

command = sys.argv[1]
user = input("Username: ")
password = getpass.getpass()
enable_pass = getpass.getpass(prompt='Enter enable password: ')

devices_ip = ['192.168.100.1','192.168.100.2','192.168.100.3']
```

---
### Приклад використання pexpect

Файл 1_pexpect.py:
```python
for ip in devices_ip:
    print("Connection to device {}".format(ip))
    t = pexpect.spawn('ssh {}@{}'.format(user, ip))

    t.expect('Password:')
    t.sendline(password)

    t.expect('>')
    t.sendline('enable')

    t.expect('Password:')
    t.sendline(enable_pass)

    t.expect('#')
    t.sendline("terminal length 0")

    t.expect('#')
    t.sendline(command)

    t.expect('#')
    print(t.before.decode('utf-8'))

```

---
### Приклад використання pexpect

Виконання скрипта виглядає так:
```python
$ python 1_pexpect.py "sh ip int br"
Username: cisco
Password:
Enter enable secret:
Connection to device 192.168.100.1
sh ip int br
Interface              ip-Address      OK? Method Status                Protocol
FastEthernet0/0        192.168.100.1   YES NVRAM  up                    up
FastEthernet0/1        unassigned      YES NVRAM  up                    up
FastEthernet0/1.10     10.1.10.1       YES manual up                    up
FastEthernet0/1.20     10.1.20.1       YES manual up                    up
FastEthernet0/1.30     10.1.30.1       YES manual up                    up
FastEthernet0/1.40     10.1.40.1       YES manual up                    up
FastEthernet0/1.50     10.1.50.1       YES manual up                    up
FastEthernet0/1.60     10.1.60.1       YES manual up                    up
FastEthernet0/1.70     10.1.70.1       YES manual up                    up
R1
Connection to device 192.168.100.2
sh ip int br
Interface              ip-Address      OK? Method Status                Protocol
FastEthernet0/0        192.168.100.2   YES NVRAM  up                    up
FastEthernet0/1        unassigned      YES NVRAM  up                    up
FastEthernet0/1.10     10.2.10.1       YES manual up                    up
FastEthernet0/1.20     10.2.20.1       YES manual up                    up
FastEthernet0/1.30     10.2.30.1       YES manual up                    up
FastEthernet0/1.40     10.2.40.1       YES manual up                    up
FastEthernet0/1.50     10.2.50.1       YES manual up                    up
FastEthernet0/1.60     10.2.60.1       YES manual up                    up
FastEthernet0/1.70     10.2.70.1       YES manual up                    up
R2
Connection to device 192.168.100.3
sh ip int br
Interface              ip-Address      OK? Method Status                Protocol
FastEthernet0/0        192.168.100.3   YES NVRAM  up                    up
FastEthernet0/1        unassigned      YES NVRAM  up                    up
FastEthernet0/1.10     10.3.10.1       YES manual up                    up
FastEthernet0/1.20     10.3.20.1       YES manual up                    up
FastEthernet0/1.30     10.3.30.1       YES manual up                    up
FastEthernet0/1.40     10.3.40.1       YES manual up                    up
FastEthernet0/1.50     10.3.50.1       YES manual up                    up
FastEthernet0/1.60     10.3.60.1       YES manual up                    up
FastEthernet0/1.70     10.3.70.1       YES manual up                    up
R3
```

