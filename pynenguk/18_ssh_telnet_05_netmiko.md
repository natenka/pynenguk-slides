# Python для мережевих інженерів 


---

# Підключення до обладнання

---

## Модуль netmiko

---
### Модуль netmiko

Netmiko это модуль, который позволяет упростить использование paramiko для сетевых устройств.

Грубо говоря, netmiko это такая "обертка" для paramiko.

Сначала netmiko нужно установить:
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

Пример использования netmiko (файл 4_netmiko.py):
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

* device_params - это словарь, в котором указываются параметры устройства
 * device_type - это предопределенные значения, которые понимает netmiko
    * в данном случае, так как подключение выполняется к устройству с Cisco IOS, используется значение 'cisco_ios'

---
### Модуль netmiko

* ```ssh = ConnectHandler(**device_params)``` - устанавливается соединение с устройством, на основе параметров, которые находятся в словаре
* ```ssh.enable()``` - переход в режим enable
 * пароль передается автоматически
 * используется значение ключа secret, который указан в словаре device_params
* ```result = ssh.send_command(command)``` - отправка команды и получение вывода

В этом примере не передается команда terminal length, так как netmiko по умолчанию, выполняет эту команду.

---
### Модуль netmiko

Так выглядит результат выполнения скрипта:
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
## Поддерживаемые типы устройств

Netmiko поддерживает несколько типов устройств:
* Arista vEOS
* Cisco ASA
* Cisco IOS
* Cisco IOS-XR
* Cisco SG300
* HP Comware7
* HP ProCurve
* Juniper Junos
* Linux
* и другие

Актуальный список можно посмотреть в [репозитории](https://github.com/ktbyers/netmiko) модуля.

---

## Словарь, определяющий параметры устройств

В словаре могут указываться такие параметры:
```python
cisco_router = {'device_type': 'cisco_ios',
                'ip': '192.168.1.1',
                'username': 'user',
                'password': 'userpass',
                'secret': 'enablepass',
                'port': 20022,
                 }
```

---
## Подключение по SSH

```python
ssh = ConnectHandler(**cisco_router)
```

---
## Режим enable

Перейти в режим enable:
```python
ssh.enable()
```

Выйти из режима enable:
```python
ssh.exit_enable_mode()
```

---
## Отправка команд

В netmiko есть несколько способов отправки команд:
* ```send_command``` - отправить одну команду
* ```send_config_set``` - отправить список команд
* ```send_config_from_file``` - отправить команды из файла (использует внутри метод ```send_config_set```)
* ```send_command_timing``` - отправить команду и подождать вывод на основании таймера

---
### ```send_command```

Метод send_command позволяет отправить одну команду на устройство.

Например:
```python
result = ssh.send_command("show ip int br")
```

---
### ```send_command```

Метод работает таким образом:
* отправляет команду на устройство и получает вывод до строки с приглашением или до указанной строки
 * приглашение определяется автоматически
 * если на вашем устройстве оно не определилось, можно просто указать строку, до которой считывать вывод
 * ранее так работал метод ```send_command_expect```, но с версии 1.0.0 так работает ```send_command```, а метод ```send_command_expect``` оставлен для совместимости
* метод возвращает вывод команды

---
### ```send_command```

Методу можно передавать такие параметры:

* ```command_string``` - команда
* ```expect_string``` - до какой строки считывать вывод
* ```delay_factor``` - параметр позволяет увеличить задержку до начала поиска строки
* ```max_loops``` - количество итераций, до того как метод выдаст ошибку (исключение). По умолчанию 500
* ```strip_prompt``` - удалить приглашение из вывода. По умолчанию удаляется
* ```strip_command``` - удалить саму команду из вывода

В большинстве случаев, достаточно будет указать только команду.

---
### ```send_config_set```

Метод ```send_config_set``` позволяет отправить несколько команд конфигурационного режима.

Пример использования:
```python
commands = ["router ospf 1",
            "network 10.0.0.0 0.255.255.255 area 0",
            "network 192.168.100.0 0.0.0.255 area 1"]

result = ssh.send_config_set(commands)
```

---
### ```send_config_set```

Метод работает таким образом:
* заходит в конфигурационный режим,
* затем передает все команды
* и выходит из конфигурационного режима 
 * в зависимости от типа устройства, выхода из конфигурационного режима может и не быть. Например, для IOS-XR выхода не будет, так как сначала надо закомитить изменения

---
### ```send_config_from_file```

Метод ```send_config_from_file``` отправляет команды из указанного файла в конфигурационный режим.

Пример использования:
```python
result = ssh.send_config_from_file("config_ospf.txt")
```

Метод открывает файл, считывает команды и передает их методу ```send_config_set```.

---
### Дополнительные методы

Кроме перечисленных методов для отправки команд, netmiko поддерживает такие методы:
* ```config_mode``` - перейти в режим конфигурации
 * ```ssh.config_mode()```
* ```exit_config_mode``` - выйти из режима конфигурации
 * ```ssh.exit_config_mode()```

---
### Дополнительные методы

* check_config_mode - проверить находится ли netmiko в режиме конфигурации (возвращает True, если в режиме конфигурации и False - если нет)
 * ```ssh.check_config_mode()```
* ```find_prompt``` - возвращает текущее приглашение устройства
 * ```ssh.find_prompt()```
* ```commit``` - выполнить commit на IOS-XR и Juniper
 * ```ssh.commit()```
* ```disconnect``` - завершить соединение SSH


---
### Telnet

С версии 1.0.0 netmiko поддерживает подключения по Telnet.
Пока что, только для Cisco IOS устройств.

Внутри, netmiko использует telnetlib, для подключения по Telnet. Но, при этом, предоставляет тот же интерфейс для работы, что и подключение по SSH.

---
### Telnet
Для того, чтобы подключиться по Telnet, достаточно в словаре, который определяет параметры подключения, указать тип устройства 'cisco_ios_telnet':
```python
device_params = {'device_type': 'cisco_ios_telnet',
                 'ip': ip,
                 'username':user,
                 'password':password,
                 'secret':enable_pass }
```

---
### Telnet
В остальном, методы, которые применимы к SSH, применимы и к Telnet. Пример, аналогичный примеру с SSH (файл 4_netmiko_telnet.py):
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

```

---
### Telnet

Файл 4_netmiko_telnet.py:
```python
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

---
### Telnet

Аналогично подключению через SSH, работают и методы:
* ```send_command_timing()```
* ```find_prompt()```
* ```send_config_set()```
* ```send_config_from_file()```
* ```check_enable_mode()```
* ```disconnect()```

