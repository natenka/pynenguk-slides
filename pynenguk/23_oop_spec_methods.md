# Python для мережевих інженерів 

---

## Об'єктно-орієнтоване програмування
### Спеціальні методи

---
### Спеціальні методи

Спеціальні методи Python - це методи, які відповідають за "стандартні" можливості об'єктів і викликаються автоматично під час використання цих можливостей.

Наприклад, вираз ``a + b``, де a і b це числа, перетворюється на такий виклик
``a.__add__(b)``, тобто спеціальний метод __add__ відповідає за операцію додавання.
Усі спеціальні методи починаються і закінчуються подвійним підкресленням, тому
англійською їх часто називають dunder методи, скорочено від "double underscore".


Спеціальні методи відповідають за такі можливості, як робота в менеджерах контексту, створення ітераторів та об'єктів, що ітеруються, операції складання, множення та інші.
Додаючи спеціальні методи до об'єктів, створених користувачем, ми робимо
їх схожими на вбудовані об'єкти.


---
### Одне підкреслення перед ім'ям

Одне підкреслення перед ім'ям методу вказує, що метод є 
внутрішньою особливістю реалізації та його не варто використовувати безпосередньо.

```python
class CiscoSSH:
    def __init__(self, ip, username, password, enable, disable_paging=True):
        self._client = paramiko.SSHClient()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self._client.connect(
            hostname=ip,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False)

        self._ssh = self._client.invoke_shell()
        self._ssh.send('enable\n')
        self._ssh.send(enable + '\n')
        if disable_paging:
            self._ssh.send('terminal length 0\n')
        time.sleep(1)
        self._ssh.recv(1000)

    def send_show_command(self, command):
        self._ssh.send(command + '\n')
        time.sleep(2)
        result = self._ssh.recv(5000).decode('ascii')
        return result
```



---
### Два підкреслення перед ім'ям

Таким чином позначаються спеціальні змінні та методи.

* ``__name__`` - ця змінна дорівнює рядку ``__main__``, коли скрипт
  запускається безпосередньо, і дорівнює імені модуля, коли імпортується
* ``__file__`` - ця змінна дорівнює імені скрипта, який був запущений
  безпосередньо, і дорівнює повному шляху до модуля, коли він імпортується


Крім того, таким чином Python позначаються спеціальні методи. Ці
методи викликаються при використанні функцій та операторів Python та
дозволяють реалізувати певний функціонал.

Як правило, такі методи не потрібно викликати безпосередньо, але, наприклад, при
створення свого класу може знадобитися описати такий метод, щоб
об'єкт підтримував якісь операції у Python.

---
## Методи __str__, __repr__

---
### Методи __str__, __repr__

Специальные методы __str__ и __repr__ отвечают за строковое представления объекта. При этом используются они в разных местах.

Спеціальні методи __str__ та __repr__ відповідають за представлення об'єкта. Ці методи икористовуються у різних місцях.

```python
In [1]: from datetime import datetime

In [2]: now = datetime.now()

In [3]: str(now)
Out[3]: '2021-08-22 06:48:39.978094'

In [4]: repr(now)
Out[4]: 'datetime.datetime(2021, 8, 22, 6, 48, 39, 978094)'
```

---
### `__str__`

Метод `__str__` відповідає за рядкове відображення інформації про об'єкт. Він викликається під час використання str і print:

```python
class Switch:
    def __init__(self, hostname, model):
        self.hostname = hostname
        self.model = model

    def __str__(self):
        return 'Switch: {}'.format(self.hostname)

In [5]: sw1 = Switch('sw1', 'Cisco 3850')

In [6]: print(sw1)
Switch: sw1

In [7]: str(sw1)
Out[7]: 'Switch: sw1'
```

---
## Протоколи

---
### Протоколи

Спеціальні методи відповідають не лише за підтримку операцій типу додавання,
порівняння, а й за підтримку протоколів. Протокол - це набір методів, які
повинні бути реалізовані в об'єкті, щоб він підтримував певну поведінку.
Наприклад, у Python є такі протоколи: ітерації, менеджер контексту,
контейнери та інші. Після створення в об'єкті певних методів,
об'єкт поводитиметься як вбудований і використовувати інтерфейс зрозумілий усім, хто пише на Python.


---
### Протокол ітерації


Ітерований об'єкт (iterable) - це об'єкт, який здатний повертати елементи по одному.
Для Python це будь-який об'єкт у якого є метод ``__iter__`` або метод ``__getitem__``.

Ітерований об'єкт перетворюється на ітератор викликом ``iter(name)``,
де name - ім'я об'єкта, що ітерується.

Ітератор (iterator) – це об'єкт, який повертає свої елементи по одному за один раз.
З точки зору Python - це будь-який об'єкт, який має метод ``__next__``. Цей метод повертає наступний елемент, якщо він є, або повертає виняток ``StopIteration``, коли елементи закінчилися.
Крім того, ітератор запам'ятовує, на якому об'єкті зупинився в останню ітерацію.
Також у кожного ітератора є метод ``__iter__`` - тобто, будь-який ітератор є об'єктом, що ітерується. Цей метод повертає сам ітератор.


---
### Протокол послідовності

У самому базовому варіанті протокол послідовності (sequence) включає
два методи: ``__len__`` та ``__getitem__``. У більш повному варіанті також методи: ``__contains__``, ``__iter__``, ``__reversed__``, ``index`` та ``count``. Якщо послідовність змінювани, додаються ще кілька методів.

```python
class Network:
    def __init__(self, network):
        self.network = network
        subnet = ipaddress.ip_network(self.network)
        self.addresses = [str(ip) for ip in subnet.hosts()]

    def __iter__(self):
        return iter(self.addresses)

    def __len__(self):
        return len(self.addresses)

    def __getitem__(self, index):
        return self.addresses[index]
```

---
### Менеджер контексту

---
### Менеджер контексту

Для використання об'єкта в менеджері контексту, у класі мають бути визначені методи ``__enter__`` та ``__exit__``:

* ``__enter__`` виконується на початку блоку with і якщо метод повертає значення, воно присвоюється в змінну, яка стоїть після as.
* ``__exit__`` гарантовано викликається після блоку with, навіть якщо у блоці виник виняток.


---
### Менеджер контексту

```python
class CiscoSSH:
    def __init__(self, **device_params):
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()
        print('CiscoSSH __init__ called')

    def __enter__(self):
        print('CiscoSSH __enter__ called')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('CiscoSSH __exit__ called')
        self.ssh.disconnect()
```

---
### Менеджер контексту

```python
In [8]: with CiscoSSH(**DEVICE_PARAMS) as r1:
   ...:     print('Inside with')
   ...:     print(r1.ssh.send_command('sh ip int br'))
   ...:
CiscoSSH __init__ called
CiscoSSH __enter__ called
Inside with
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
Ethernet0/2                190.16.200.1    YES NVRAM  up                    up
Ethernet0/3                192.168.230.1   YES NVRAM  up                    up
Ethernet0/3.100            10.100.0.1      YES NVRAM  up                    up
Ethernet0/3.200            10.200.0.1      YES NVRAM  up                    up
Ethernet0/3.300            10.30.0.1       YES NVRAM  up                    up
CiscoSSH __exit__ called
```

---
### Менеджер контексту

Якщо всередині блоку з'являється виняток, він буде згенерований після виконання методу ``__exit__``:

```python
In [10]: with CiscoSSH(**DEVICE_PARAMS) as r1:
    ...:     print('Inside with')
    ...:     print(r1.ssh.send_command('sh ip int br'))
    ...:     raise ValueError('Error')
    ...:
CiscoSSH __init__ called
CiscoSSH __enter__ called
Inside with
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
Ethernet0/2                190.16.200.1    YES NVRAM  up                    up
Ethernet0/3                192.168.230.1   YES NVRAM  up                    up
Ethernet0/3.100            10.100.0.1      YES NVRAM  up                    up
Ethernet0/3.200            10.200.0.1      YES NVRAM  up                    up
Ethernet0/3.300            10.30.0.1       YES NVRAM  up                    up
CiscoSSH __exit__ called
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-10-4e8b17370785> in <module>()
      2     print('Inside with')
      3     print(r1.ssh.send_command('sh ip int br'))
----> 4     raise ValueError('Error')

ValueError: Error
```


