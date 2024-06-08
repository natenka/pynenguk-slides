# Python для мережевих інженерів 


---

# Підключення до обладнання

---

## Модуль netmiko

---
### Модуль netmiko

Netmiko — це модуль, який полегшує використання paramiko для мережевих пристроїв.

Грубо кажучи, netmiko — це «обгортка» для paramiko.

Спочатку потрібно встановити netmiko:
```
pip install netmiko
```

---
### Модуль netmiko

Пример использования netmiko (файл 4_netmiko.py):
```python
from netmiko import ConnectHandler
import getpass
import sys


command = sys.argv[1]
user = input("Username: ")
password = getpass.getpass()
enable_pass = getpass.getpass(prompt='Enter enable password: ')

devices_ip = ['192.168.100.1','192.168.100.2','192.168.100.3']

```

---
### Модуль netmiko

Приклад використання netmiko (файл 4_netmiko.py):
```python
for ip in devices_ip:
    print("Connection to device {}".format(ip))
    device_params = {'device_type': 'cisco_ios',
                     'ip': ip,
                     'username': user,
                     'password': password,
                     'secret': enable_pass}

    ssh = ConnectHandler(**device_params)
    ssh.enable()

    result = ssh.send_command(command)
    print(result)
```

---
### Модуль netmiko

* device_params — це словник, який визначає параметри пристрою
 * device_type — це попередньо визначені значення, які netmiko розуміє
    * у цьому випадку, оскільки підключення здійснюється до пристрою з Cisco IOS, використовується значення `cisco_ios`.
* ```ssh = ConnectHandler(**device_params)``` - з'єднання встановлюється з пристроєм на основі параметрів, які є в словнику
* ```ssh.enable()``` - перейти в режим enable
  * пароль надсилається автоматично
  * використовується значення ключа secret, яке вказано в словнику device_params
* ```result = ssh.send_command(command)``` - відправити команду та отримати вивід

У цьому прикладі команда `terminal length` не передається, оскільки netmiko за замовчуванням виконує цю команду.


---
### Модуль netmiko

Ось так виглядає результат виконання скрипта:
```
$ python 4_netmiko.py "sh ip int br"
Username: cisco
Password:
Enter enable password:
Connection to device 192.168.100.1
Interface              ip-Address      OK? Method Status    Protocol
FastEthernet0/0        192.168.100.1   YES NVRAM  up        up
FastEthernet0/1        unassigned      YES NVRAM  up        up
FastEthernet0/1.10     10.1.10.1       YES manual up        up
FastEthernet0/1.20     10.1.20.1       YES manual up        up
FastEthernet0/1.30     10.1.30.1       YES manual up        up
FastEthernet0/1.40     10.1.40.1       YES manual up        up
FastEthernet0/1.50     10.1.50.1       YES manual up        up
FastEthernet0/1.60     10.1.60.1       YES manual up        up
FastEthernet0/1.70     10.1.70.1       YES manual up        up
Connection to device 192.168.100.2
Interface              ip-Address      OK? Method Status    Protocol
FastEthernet0/0        192.168.100.2   YES NVRAM  up        up
FastEthernet0/1        unassigned      YES NVRAM  up        up
FastEthernet0/1.10     10.2.10.1       YES manual up        up
FastEthernet0/1.20     10.2.20.1       YES manual up        up
FastEthernet0/1.30     10.2.30.1       YES manual up        up
FastEthernet0/1.40     10.2.40.1       YES manual up        up
FastEthernet0/1.50     10.2.50.1       YES manual up        up
FastEthernet0/1.60     10.2.60.1       YES manual up        up
FastEthernet0/1.70     10.2.70.1       YES manual up        up
Connection to device 192.168.100.3
Interface              ip-Address      OK? Method Status    Protocol
FastEthernet0/0        192.168.100.3   YES NVRAM  up        up
FastEthernet0/1        unassigned      YES NVRAM  up        up
FastEthernet0/1.10     10.3.10.1       YES manual up        up
FastEthernet0/1.20     10.3.20.1       YES manual up        up
FastEthernet0/1.30     10.3.30.1       YES manual up        up
FastEthernet0/1.40     10.3.40.1       YES manual up        up
FastEthernet0/1.50     10.3.50.1       YES manual up        up
FastEthernet0/1.60     10.3.60.1       YES manual up        up
FastEthernet0/1.70     10.3.70.1       YES manual up        up
```

---
## Підтримувані типи пристроїв

Netmiko підтримує кілька типів пристроїв:
* Arista vEOS
* Cisco ASA
* Cisco IOS
* Cisco IOS-XR
* Cisco SG300
* HP Comware7
* HP ProCurve
* Juniper Junos
* Linux
* та інші

Поточний список можна переглянути в [репозиторії](https://github.com/ktbyers/netmiko) модуля.

---

## Словник, що визначає параметри пристрою

```python
cisco_router = {'device_type': 'cisco_ios',
                'ip': '192.168.1.1',
                'username': 'user',
                'password': 'userpass',
                'secret': 'enablepass',
                'port': 20022}
```

---
## Підключення через SSH

```python
ssh = ConnectHandler(**cisco_router)
```

---
## Режим enable

Перейти в режим enable:
```python
ssh.enable()
```

Вийти з режиму enable:
```python
ssh.exit_enable_mode()
```

---
## Відправка команд

У Netmiko є кілька способів відправлення команд:
* ```send_command``` - відправити одну команду
* ```send_config_set``` - відправити список команд
* ```send_config_from_file``` - надсилати команди з файлу (використовує внутрішній метод ```send_config_set```)
* ```send_command_timing``` - надіслати команду та очікувати виведення на основі таймера

---
### ```send_command```

Метод send_command дозволяє надсилати на пристрій одну команду.
```python
result = ssh.send_command("show ip int br")
```

---
### ```send_command```

Метод працює так:
* надсилає команду на пристрій і отримує вихідні дані до рядка запрошення або до вказаного рядка
  * запрошення визначається автоматично
  * якщо його не виявлено на пристрої, можна вказати рядок, до якого слід зчитувати вихідні дані
* метод повертає вивід команди

---
### ```send_command```

Методу можна передати такі параметри:

* ```command_string``` - команда
* ```expect_string``` - до якого рядка читати вивід
* ```strip_prompt``` - видалити запрошення з виводу. Видаляється за замовчуванням
* ```strip_command``` - видалити саму команду з виводу

У більшості випадків достатньо буде вказати лише команду.

---
### ```send_config_set```

Метод ```send_config_set``` дозволяє надсилати кілька команд режиму конфігурації.

Приклад використання:
```python
commands = ["router ospf 1",
            "network 10.0.0.0 0.255.255.255 area 0",
            "network 192.168.100.0 0.0.0.255 area 1"]

result = ssh.send_config_set(commands)
```

---
### ```send_config_set```

Метод працює так:

* входить в конфігураційний режим
* передає команди
* виходить з конфігураційного режиму 
  * в залежності від типу пристрою вихід з режиму конфігурації може не бути. Наприклад, для IOS-XR виходу не буде, оскільки спочатку потрібно зробити commit

---
### ```send_config_from_file```

Метод ```send_config_from_file``` надсилає команди з указаного файлу в конфігураційний режим.

Приклад використання:
```python
result = ssh.send_config_from_file("config_ospf.txt")
```

Метод відкриває файл, читає команди та передає їх методу ``send_config_set``.

---
### Додаткові методи

Крім перерахованих методів для відправки команд, Netmiko підтримує такі методи:
* ```config_mode```
* ```ssh.config_mode```
* ```exit_config_mode```
* ```ssh.exit_config_mode```

---
### Додаткові методи

* ```check_config_mode``` - перевірити, чи netmiko знаходиться в режимі конфігурації (повертає True, якщо в режимі конфігурації, і False, якщо ні)
* ```find_prompt``` - повертає підказку поточного пристрою
* ```commit``` - commit на IOS-XR і Juniper
* ```disconnect``` - розірвати з'єднання SSH


---
### Telnet

Для підключення через Telnet достатньо в словнику, який визначає параметри підключення, вказати тип пристрою ``cisco_ios_telnet``:
```python
device_params = {'device_type': 'cisco_ios_telnet',
                 'ip': ip,
                 'username': user,
                 'password': password,
                 'secret': enable_pass}
```

---
### Telnet

```python
from netmiko import ConnectHandler
import getpass
import sys
import time

command = sys.argv[1]
user = input("Username: ")
password = getpass.getpass()
enable_pass = getpass.getpass(prompt='Enter enable password: ')

devices_ip = ['192.168.100.1','192.168.100.2','192.168.100.3']

for ip in devices_ip:
    print("Connection to device {}".format(ip))
    device_params = {'device_type': 'cisco_ios_telnet',
                     'ip': ip,
                     'username':user,
                     'password':password,
                     'secret':enable_pass,
                     'verbose': True}
    ssh = ConnectHandler(**device_params)
    ssh.enable()

    result = ssh.send_command(command)
    print(result)
```
