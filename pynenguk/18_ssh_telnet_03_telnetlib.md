# Python для мережевих інженерів 


---

# Підключення до обладнання

---

## Модуль telnetlib

---
### telnetlib

Модуль telnetlib входить до стандартної бібліотеки Python (буде видалений в Python 3.13). Це реалізація клієнта Telnet.

Принцип роботи telnetlib подібний до pexpect, але є кілька відмінностей.
Найпомітніша відмінність полягає в тому, що telnetlib вимагає передачі байтового рядка, а не звичайного.


---
### Підключення

Підключення здійснюється наступним чином:

```python
In [1]: telnet = telnetlib.Telnet('192.168.100.1')
```

---
### Метод read_until

Використовуючи метод read_until, вказується до якого рядка читати вивід.
Як аргумент потрібно передати не звичайний рядок, а байти:
```python
In [2]: telnet.read_until(b'Username')
Out[2]: b'\r\n\r\nUser Access Verification\r\n\r\nUsername'
```

Метод read_until повертає все, що він прочитав, до вказаного рядка.

---
### Метод write

Для передачі даних використовується метод write. Йому треба передавати байтовий рядок:
```python
In [3]: telnet.write(b'cisco\n')
```

---
### Введення паролю і команди

```python
In [4]: telnet.read_until(b'Password')
Out[4]: b': cisco\r\nPassword'

In [5]: telnet.write(b'cisco\n')

In [6]: telnet.read_until(b'>')
Out[6]: b': \r\nR1>'

In [7]: telnet.write(b'sh ip int br\n')
```

---
### Отримання результату команди з read_until

Після надсилання команди можна продовжувати використовувати метод read_until:
```python
In [8]: telnet.read_until(b'>')
Out[8]: b'sh ip int br\r\nInterface                  ip-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                19.1.1.1        YES NVRAM  up                    up      \r\nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \r\nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      \r\nR1>'
```

---
### Отримання результату команди від read_very_eager

Використовуючи метод read_very_eager, можна надіслати кілька команд, а потім прочитати весь доступний вивід:
```python
In [9]: telnet.write(b'sh arp\n')

In [10]: telnet.write(b'sh clock\n')

In [11]: telnet.write(b'sh ip int br\n')

In [12]: all_result = telnet.read_very_eager().decode('utf-8')

In [13]: print(all_result)
sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.30.0.1               -   aabb.cc00.6530  ARPA   Ethernet0/3.300
Internet  10.100.0.1              -   aabb.cc00.6530  ARPA   Ethernet0/3.100
Internet  10.200.0.1              -   aabb.cc00.6530  ARPA   Ethernet0/3.200
Internet  19.1.1.1                -   aabb.cc00.6520  ARPA   Ethernet0/2
Internet  192.168.100.1           -   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2         124   aabb.cc00.6600  ARPA   Ethernet0/0
Internet  192.168.100.3         143   aabb.cc00.6700  ARPA   Ethernet0/0
Internet  192.168.100.100       160   aabb.cc80.c900  ARPA   Ethernet0/0
Internet  192.168.200.1           -   0203.e800.6510  ARPA   Ethernet0/1
Internet  192.168.200.100        13   0800.27ac.16db  ARPA   Ethernet0/1
Internet  192.168.230.1           -   aabb.cc00.6530  ARPA   Ethernet0/3
R1>sh clock
*19:18:57.980 UTC Fri Nov 3 2017
R1>sh ip int br
Interface                  ip-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
Ethernet0/2                19.1.1.1        YES NVRAM  up                    up
Ethernet0/3                192.168.230.1   YES NVRAM  up                    up
Ethernet0/3.100            10.100.0.1      YES NVRAM  up                    up
Ethernet0/3.200            10.200.0.1      YES NVRAM  up                    up
Ethernet0/3.300            10.30.0.1       YES NVRAM  up                    up
R1>
```

При використанні методу read_very_eager в скрипті, перед ним обов'язково треба робити паузу, наприклад, за допомогою `time.sleep(2)`. 

---
### Отримання результату з кількох команд за допомогою read_until

З read_until буде дещо інший підхід.
Ви можете запустити ті самі три команди, але потім отримувати вихідні дані по черзі, читаючи до рядка запрошення:

```python
In [14]: telnet.write(b'sh arp\n')

In [15]: telnet.write(b'sh clock\n')

In [16]: telnet.write(b'sh ip int br\n')

In [17]: telnet.read_until(b'>')
Out[17]: b'sh arp\r\nProtocol  Address          Age (min)  Hardware Addr   Type   Interface\r\nInternet  10.30.0.1               -   aabb.cc00.6530  ARPA   Ethernet0/3.300\r\nInternet  10.100.0.1              -   aabb.cc00.6530  ARPA   Ethernet0/3.100\r\nInternet  10.200.0.1              -   aabb.cc00.6530  ARPA   Ethernet0/3.200\r\nInternet  19.1.1.1                -   aabb.cc00.6520  ARPA   Ethernet0/2\r\nInternet  192.168.100.1           -   aabb.cc00.6500  ARPA   Ethernet0/0\r\nInternet  192.168.100.2         126   aabb.cc00.6600  ARPA   Ethernet0/0\r\nInternet  192.168.100.3         145   aabb.cc00.6700  ARPA   Ethernet0/0\r\nInternet  192.168.100.100       162   aabb.cc80.c900  ARPA   Ethernet0/0\r\nInternet  192.168.200.1           -   0203.e800.6510  ARPA   Ethernet0/1\r\nInternet  192.168.200.100        15   0800.27ac.16db  ARPA   Ethernet0/1\r\nInternet  192.168.230.1           -   aabb.cc00.6530  ARPA   Ethernet0/3\r\nR1>'

In [18]: telnet.read_until(b'>')
Out[18]: b'sh clock\r\n*19:20:39.388 UTC Fri Nov 3 2017\r\nR1>'

In [19]: telnet.read_until(b'>')
Out[19]: b'sh ip int br\r\nInterface                  ip-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                19.1.1.1        YES NVRAM  up                    up      \r\nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \r\nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      \r\nR1>'

```

---
### read_until vs read_very_eager

Важлива відмінність між read_until і read_very_eager полягає в тому, як вони реагують на відсутність результату.

Метод read_until очікує на певний рядок. За замовчуванням, якщо його немає, метод зависне.
Додатковий параметр тайм-ауту дозволяє вказати, як довго чекати потрібного рядка:

```python
In [20]: telnet.read_until(b'>', timeout=5)
Out[20]: b''
```

Якщо протягом зазначеного часу не з’являється жоден рядок, повертається порожній рядок.

Метод read_very_eager просто поверне порожній рядок, якщо немає результату:
```python
In [21]: telnet.read_very_eager()
Out[21]: b''
```

---
### Метод expect

Метод expect дозволяє вказати список регулярних виразів.
Він працює подібно до pexpect, але йому завжди потрібно передавати список регулярних виразів модулю telnetlib.
```python
In [22]: telnet.write(b'sh clock\n')

In [23]: telnet.expect([b'[>#]'])
Out[23]:
(0,
 <_sre.SRE_Match object; span=(46, 47), match=b'>'>,
 b'sh clock\r\n*19:35:10.984 UTC Fri Nov 3 2017\r\nR1>')
```

---
### Метод expect

Метод expect возвращает кортеж их трех элементов:
* индекс выражения, которое совпало
* объект Match
* байтовая строка, которая содержит все считанное до регулярного  выражения и включая его


Метод expect повертає кортеж із трьох елементів:
* індекс виразу, з яким був збіг
* об’єкт Match
* байтовий рядок, який містить усе прочитане до регулярного виразу включно


---
### Метод expect

```python
In [24]: telnet.write(b'sh clock\n')

In [25]: regex_idx, match, output = telnet.expect([b'[>#]'])

In [26]: regex_idx
Out[26]: 0

In [27]: match.group()
Out[27]: b'>'

In [28]: match
Out[28]: <_sre.SRE_Match object; span=(46, 47), match=b'>'>

In [29]: match.group()
Out[29]: b'>'

In [30]: output
Out[30]: b'sh clock\r\n*19:37:21.577 UTC Fri Nov 3 2017\r\nR1>'

In [31]: output.decode('utf-8')
Out[31]: 'sh clock\r\n*19:37:21.577 UTC Fri Nov 3 2017\r\nR1>'
```

---
### Закриття з'єднання

Підключення закривається за допомогою методу close:
```python
In [32]: telnet.close()
```

---
### Приклад використання telnetlib

Файл 2_telnetlib.py:
```python
import telnetlib
import time
import getpass
import sys

command = sys.argv[1].encode('utf-8')
user = input("Username: ").encode('utf-8')
password = getpass.getpass().encode('utf-8')
enable_pass = getpass.getpass(prompt='Enter enable password: ').encode('utf-8')

devices_ip = ['192.168.100.1','192.168.100.2','192.168.100.3']

```

---
### Приклад використання telnetlib

Файл 2_telnetlib.py:
```python
for ip in devices_ip:
    print("Connection to device {}".format(ip))
    t = telnetlib.Telnet(ip)

    t.read_until(b"Username:")
    t.write(user + b'\n')

    t.read_until(b"Password:")
    t.write(password + b'\n')
    t.write(b"enable\n")

    t.read_until(b"Password:")
    t.write(enable_pass + b'\n')
    t.write(b"terminal length 0\n")
    t.write(command + b'\n')

    time.sleep(5)

    output = t.read_very_eager().decode('utf-8')
    print(output)
```

---
### Приклад використання telnetlib

Виконання скрипту:
```
$ python 2_telnetlib.py "sh ip int br"
Username: cisco
Password:
Enter enable secret:
Connection to device 192.168.100.1

R1#terminal length 0
R1#sh ip int br
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
R1#
Connection to device 192.168.100.2

R2#terminal length 0
R2#sh ip int br
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
R2#
Connection to device 192.168.100.3

R3#terminal length 0
R3#sh ip int br
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
R3#
```

