# Python для мережевих інженерів 


---

# Підключення до обладнання

## Модуль scrapli
---

### Модуль scrapli

Scrapli це модуль, який
дозволяє підключатися до мережевого обладнання за допомогою Telnet, SSH або NETCONF.

Як і netmiko, scrapli може використовувати paramiko та інші модулі для самого підключення, але в той же час забезпечує той самий
робочий інтерфейс для різних типів підключення та різного обладнання.

---
### Додаткові модулі

* [nornir_scrapli](https://carlmontanari.github.io/more_scrapli/nornir_scrapli)
* [scrapli_community](https://carlmontanari.github.io/more_scrapli/scrapli_community)
* [scrapli_cfg](https://carlmontanari.github.io/more_scrapli/scrapli_cfg)
* [scrapli_replay](https://carlmontanari.github.io/more_scrapli/scrapli_replay)
* [scrapli_netconf](https://carlmontanari.github.io/more_scrapli/scrapli_netconf)

---

### Встановлення scrapli

```
pip install scrapli
pip install scrapli[full]
```

Installation extras:

* paramiko
* ssh2
* asyncssh
* textfsm (textfsm and ntc-templates)
* ttp (ttp template parser)
* genie (genie/pyats)
* netconf (scrapli_netconf)
* community (scrapli_community)

---
### Основні компоненти скраплі

* transport - це специфічний спосіб підключення до обладнання
* channel - наступний рівень над транспортом, який відповідає за відправку команд, отримання вихідних даних та інші взаємодії з обладнанням
* driver — це інтерфейс, який надається користувачеві для роботи зі scrapli.
  Існують спеціальні драйвери, такі як ``IOSXEDriver``, які розуміють
  як взаємодіяти з обладнанням конкретного типу, і основний
  драйвер Driver, який забезпечує мінімальний інтерфейс для роботи через SSH/Telnet.


---

### Доступні варіанти транспорту

* system - використовується вбудований клієнт SSH, тобто використання клієнта на Linux/MacOS
* paramiko - модуль paramiko
* ssh2 - використовує модуль ssh2-python (обгортка навколо бібліотеки C libssh2)
* telnet - використовуватиметься telnetlib
* asyncssh - модуль asyncssh
* asynctelnet - клієнт telnet, написаний за допомогою asyncio

---
### Підтримувані платформи

* Cisco IOS-XE
* Cisco NX-OS
* Juniper JunOS
* Cisco IOS-XR
* Arista EOS

Крім цих платформ, існують ще платформи [scrapli_community](https://github.com/scrapli/scrapli_community).
І одна з переваг scrapli полягає в тому, що додавати платформи відносно легко.

---

### Створення підключення

У scrapli глобально є два варіанти підключення: використовуючи клас Scrapli,
який вибирає потрібний driver за параметром platform або конкретний driver,
наприклад, IOSXEDriver. При цьому параметри передаються ті самі і конкретному
драйверу та Scrapli.

Якщо у scrapli (або scrapli community) немає підтримки необхідної платформи, можна додати платформу до scrapli community або використовувати:
* [Driver](https://carlmontanari.github.io/scrapli/user_guide/advanced_usage/#using-driver-directly)
* [GenericDriver](https://carlmontanari.github.io/scrapli/user_guide/advanced_usage/#using-the-genericdriver)
* [NetworkDriver](https://carlmontanari.github.io/scrapli/user_guide/advanced_usage/)

---

### Параметри підключення

* host - IP-адреса або ім'я хоста
* auth_username - ім'я користувача
* auth_password - пароль
* auth_secondary - пароль для включення
* auth_strict_key - контролює перевірку SSH ключів сервера, а саме дозволяти
  чи підключатися до серверів ключ яких не збережено у ssh/known_hosts.
  False – дозволити підключення (за замовчуванням значення True)
* platform - потрібно вказувати при використанні Scrapli
* transport - який транспорт використовувати
* transport_options - опції для конкретного транспорту


---
### Підключення

Процесс подключения немного отличается в зависимости от того используется
менеджер контекста или нет. При подключении без менеджера контекста, сначала надо
передать параметры драйверу или Scrapli, а затем вызвать метод open:

Процес підключення дещо відрізняється залежно від того, використовується менеджер контексту чи ні. Підключаючись без менеджера контексту, потрібно спочатку передати параметри драйверу або Scrapli, а потім викликати метод `open`:

```python
from scrapli import Scrapli

r1 = {
   "host": "192.168.100.1",
   "auth_username": "cisco",
   "auth_password": "cisco",
   "auth_secondary": "cisco",
   "auth_strict_key": False,
   "platform": "cisco_iosxe"
}

In [2]: ssh = Scrapli(**r1)

In [3]: ssh.open()

In [4]: ssh.get_prompt()
Out[4]: 'R1#'

In [5]: ssh.close()
```

---
### Підключення з менеджером контексту

При використанні менеджера контексту open викликати не треба:

```python
In [8]: with Scrapli(**r1_driver) as ssh:
   ...:     print(ssh.get_prompt())
   ...:
R1#
```

---
### Використання драйвера

| Обладнання  | Драйвер      | Параметр platform |
|--------------|--------------|-------------------|
| Cisco IOS-XE | IOSXEDriver  | cisco_iosxe       |
| Cisco NX-OS  | NXOSDriver   | cisco_nxos        |
| Cisco IOS-XR | IOSXRDriver  | cisco_iosxr       |
| Arista EOS   | EOSDriver    | arista_eos        |
| Juniper JunOS| JunosDriver  | juniper_junos     |

---
### Приклад підключення за допомогою драйвера IOSXEDriver

```python
In [11]: from scrapli.driver.core import IOSXEDriver

In [12]: r1_driver = {
    ...:    "host": "192.168.100.1",
    ...:    "auth_username": "cisco",
    ...:    "auth_password": "cisco",
    ...:    "auth_secondary": "cisco",
    ...:    "auth_strict_key": False,
    ...: }

In [13]: with IOSXEDriver(**r1_driver) as ssh:
    ...:     print(ssh.get_prompt())
    ...:
R1#
```

---

### Відправлення команд

У scrapli є кілька методів для відправки команд:

* ``send_command`` - відправити одну show команду
* ``send_commands`` - надіслати список show команд
* ``send_commands_from_file`` - відправити show команди з файлу
* ``send_config`` - надіслати одну команду в конфігураційному режимі
* ``send_configs`` - надіслати список команд у конфігураційному режимі
* ``send_configs_from_file`` - відправити команди з файлу в конфігураційному режимі
* ``send_interactive``

Всі ці методи повертають об'єкт Response, а не вивід команди у вигляді рядка.


---
### Об'єкт Response

Метод send_command та інші методи для надсилання команд на обладнання
повертають об'єкт Response (не вивід команди).
Response дозволяє отримати не тільки вивід команди, а й такі речі як
час роботи команди, виконалася команда з помилками або без, структурований
результат за допомогою textfsm тощо.

```python
In [15]: reply = ssh.send_command("sh clock")

In [16]: reply
Out[16]: Response <Success: True>
```

---
### Об'єкт Response

Ви можете отримати вивід команди, звернувшись до атрибута result:

```python
In [17]: reply.result
Out[17]: '*17:31:54.232 UTC Wed Mar 31 2021'
```

Атрибут raw_result містить байтовий рядок із повним результатом:

```python
In [18]: reply.raw_result
Out[18]: b'\n*17:31:54.232 UTC Wed Mar 31 2021\nR1#'
```

---

### elapsed_time

Для команд, які виконуються довше за звичайні show, може бути необхідно
знати час виконання команди:

```python
In [18]: r = ssh.send_command("ping 10.1.1.1")

In [19]: r.result
Out[19]: 'Type escape sequence to abort.\nSending 5, 100-byte ICMP Echos to 10.1.1.1, timeout is 2 seconds:\n.....\nSuccess rate is 0 percent (0/5)'

In [20]: r.elapsed_time
Out[20]: 10.047594

In [21]: r.start_time
Out[21]: datetime.datetime(2021, 4, 1, 7, 10, 56, 63697)

In [22]: r.finish_time
Out[22]: datetime.datetime(2021, 4, 1, 7, 11, 6, 111291)
```

---
### Метод send_command

Метод ``send_command`` дозволяє відправити одну команду на пристрій.

```python
In [14]: reply = ssh.send_command("sh clock")
```

---
### Метод send_command

Параметри методу (всі ці параметри треба передавати як ключові):

* ``strip_prompt`` - видалити запрошення з виводу. За замовчуванням видаляється
* ``failed_when_contains`` - якщо вивід містить зазначений рядок або один з
  рядків у списку буде вважатися, що команда виконалася з помилкою
* ``timeout_ops`` - максимальний час на виконання команди, за замовчуванням
  дорівнює 30 секунд для IOSXEDriver

---
### Метод send_command

```python
In [15]: reply = ssh.send_command("sh clock")

In [16]: reply
Out[16]: Response <Success: True>
```

---
### Метод send_command. Параметр timeout_ops

Параметр timeout_ops вказує скільки чекати на виконання команди:

```python
In [19]: ssh.send_command("ping 8.8.8.8", timeout_ops=20)
Out[19]: Response <Success: True>
```

Якщо команда не виконалася за вказаний час, згенерується виняток
ScrapliTimeout (вивід скорочений):

```python
In [20]: ssh.send_command("ping 8.8.8.8", timeout_ops=2)
---------------------------------------------------------------------------
ScrapliTimeout                            Traceback (most recent call last)
<ipython-input-20-e062fb19f0e6> in <module>
----> 1 ssh.send_command("ping 8.8.8.8", timeout_ops=2)
```

---
### TextFSM

Окрім отримання звичайного виводу команд, scrapli також дозволяє отримати
структурований результат, наприклад, за допомогою методу textfsm_parse_output:

```python
In [21]: reply = ssh.send_command("sh ip int br")

In [22]: reply.textfsm_parse_output()
Out[22]:
[{'intf': 'Ethernet0/0',
  'ipaddr': '192.168.100.1',
  'status': 'up',
  'proto': 'up'},
 {'intf': 'Ethernet0/1',
  'ipaddr': '192.168.200.1',
  'status': 'up',
  'proto': 'up'},
 {'intf': 'Ethernet0/2',
  'ipaddr': 'unassigned',
  'status': 'up',
  'proto': 'up'},
 {'intf': 'Ethernet0/3',
  'ipaddr': '192.168.130.1',
  'status': 'up',
  'proto': 'up'}]
```

---
### Виявлення помилок

Методы для отправки команд автоматически проверяют вывод на наличие ошибок.
Для каждого вендора/типа оборудования это свои ошибки, плюс можно самостоятельно
указать наличие каких строк в выводе будет считаться ошибкой.
По умолчанию для IOSXEDriver ошибками будут считаться такие строки:

Методи надсилання команд автоматично перевіряють вивід на наявність помилок.
У кожного типу обладнання є свої помилки, крім того, можна самостійно вказати, наявність яких рядків у виведених даних буде вважатися помилкою.
За замовчуванням для IOSXEDriver такі рядки вважатимуться помилками:

```python
In [21]: ssh.failed_when_contains
Out[21]:
['% Ambiguous command',
 '% Incomplete command',
 '% Invalid input detected',
 '% Unknown command']
```

---
### Виявлення помилок

Атрибут failed у об'єкта Response повертає True, якщо команда відпрацювала з
помилкою та False, якщо без помилки

```python
In [23]: reply = ssh.send_command("sh clck")

In [24]: reply.result
Out[24]: "        ^\n% Invalid input detected at '^' marker."

In [25]: reply
Out[25]: Response <Success: False>

In [26]: reply.failed
Out[26]: True
```

---
### Метод send_config

Метод ``send_config`` дозволяє відправити одну команду конфігураційного режиму.

```python
In [33]: r = ssh.send_config("username user1 password password1")
```

---
### Метод send_config

За замовчуванням при використанні ``send_config``, атрибут result міститиме порожній рядок (якщо не було помилки, коли виконання команд):
```python
In [34]: r.result
Out[34]: ''
```

Параметр ``strip_prompt=False``:

```python
In [37]: r = ssh.send_config("username user1 password password1", strip_prompt=False)

In [38]: r.result
Out[38]: 'R1(config)#'
```

---
### Методи send_commands, send_configs

Методи send_commands, send_configs відрізняються від send_command, send_config тим, що можна надсилати декілька команд.
Крім того, ці методи повертають не Response, а MultiResponse, який можна сприймати як список Response, по одній для кожної команди.

```python
In [44]: reply = ssh.send_commands(["sh clock", "sh ip int br"])

In [45]: reply
Out[45]: MultiResponse <Success: True; Response Elements: 2>

In [46]: for r in reply:
    ...:     print(r)
    ...:     print(r.result)
    ...:
Response <Success: True>
*08:38:20.115 UTC Thu Apr 1 2021
Response <Success: True>
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
Ethernet0/2                unassigned      YES NVRAM  up                    up
Ethernet0/3                192.168.130.1   YES NVRAM  up                    up

In [47]: reply.result
Out[47]: 'sh clock\n*08:38:20.115 UTC Thu Apr 1 2021sh ip int br\nInterface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up\nEthernet0/2                unassigned      YES NVRAM  up                    up\nEthernet0/3                192.168.130.1   YES NVRAM  up                    up'

In [48]: reply[0]
Out[48]: Response <Success: True>

In [49]: reply[1]
Out[49]: Response <Success: True>

In [50]: reply[0].result
Out[50]: '*08:38:20.115 UTC Thu Apr 1 2021'
```

---
### stop_on_failed


Якщо вказати ``stop_on_failed=True``, scrapli зупинить виконання команд, після першої помилки в якійсь команді, наступні команди не виконуватимуться:

```python
In [59]: reply = ssh.send_commands(["ping 192.168.100.2", "sh clck", "sh ip int br"], stop_on_failed=True)

In [60]: reply
Out[60]: MultiResponse <Success: False; Response Elements: 2>

In [61]: reply.result
Out[61]: "ping 192.168.100.2\nType escape sequence to abort.\nSending 5, 100-byte ICMP Echos to 192.168.100.2, timeout is 2 seconds:\n!!!!!\nSuccess rate is 100 percent (5/5), round-trip min/avg/max = 1/2/6 mssh clck\n        ^\n% Invalid input detected at '^' marker."

In [62]: for r in reply:
    ...:     print(r)
    ...:     print(r.result)
    ...:
Response <Success: True>
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.100.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/6 ms
Response <Success: False>
        ^
% Invalid input detected at '^' marker.
```

---
## Підключення Telnet

---
### Підключення Telnet

Для подключения к оборудовани по Telnet надо указать transport равным
telnet и обязательно указать параметр port равным 23 (или тому порту который
используется у вас для подключения по Telnet):

Для підключення до обладнання через Telnet необхідно вказати транспорт рівний telnet і обов’язково вказати параметр ``port=23`` (або той порт, який
використовується для підключення через Telnet):


```python
from scrapli.driver.core import IOSXEDriver
from scrapli.exceptions import ScrapliException
import socket

r1 = {
    "host": "192.168.100.1",
    "auth_username": "cisco",
    "auth_password": "cisco2",
    "auth_secondary": "cisco",
    "auth_strict_key": False,
    "transport": "telnet",
    "port": 23,  # port
}


def send_show(device, show_command):
    try:
        with IOSXEDriver(**r1) as ssh:
            reply = ssh.send_command(show_command)
            return reply.result
    except socket.timeout as error:
        print(error)
    except ScrapliException as error:
        print(error, device["host"])


if __name__ == "__main__":
    output = send_show(r1, "sh ip int br")
    print(output)
```
