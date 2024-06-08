# Python для мережевих інженерів 


---

# Підключення до обладнання

---
## Модуль paramiko

---
### Модуль paramiko

Paramiko это реализация протокола SSHv2 на Python.
Paramiko предоставляет функциональность клиента и сервера.

Так как Paramiko не входит в стандартную библиотеку модулей Python, его нужно установить:
```
pip install paramiko
```

---
### Модуль paramiko

Пример использования Paramiko (файл 3_paramiko.py):
```python
import paramiko
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
### Модуль paramiko

Пример использования Paramiko (файл 3_paramiko.py):
```python
for ip in devices_ip:
    print("Connection to device {}".format(ip))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(hostname=ip, username=user, password=password,
                   look_for_keys=False, allow_agent=False)
    ssh = client.invoke_shell()

    ssh.send("enable\n")
    ssh.send(enable_pass + '\n')
    time.sleep(1)

    ssh.send("terminal length 0\n")
    time.sleep(1)
    print(ssh.recv(1000).decode('utf-8'))

    ssh.send(command + "\n")
    time.sleep(2)
    result = ssh.recv(5000).decode('utf-8')
    print(result)

```

---
### Модуль paramiko

* ```client = paramiko.SSHClient()``` - этот класс представляет соединение к SSH-серверу. Он выполняет аутентификацию клиента.
* ```client.set_missing_host_key_policy(paramiko.AutoAddPolicy())```
 * ```set_missing_host_key_policy``` - устанавливает какую политику использовать, когда выполнятся подключение к серверу, ключ которого неизвестен.
 * ```paramiko.AutoAddPolicy()``` - политика, которая автоматически добавляет новое имя хоста и ключ в локальный объект HostKeys.

---
### Модуль paramiko

* ```client.connect``` - метод, который выполняет подключение к SSH-серверу и аутентифицирует подключение
  * ```hostname``` - имя хоста или ip-адрес
  * ```username``` - имя пользователя
  * ```password``` - пароль
  * ```look_for_keys``` - по умолчанию paramiko выполняет аутентификацию по ключам. Чтобы отключить это, надо поставить поставив False
  * ```allow_agent``` - paramiko может подключаться к локальному SSH агенту ОС. Это нужно при работе с ключами, а так как, в данном случае, аутентификация выполняется по логину/паролю, это нужно отключить.

---
### Модуль paramiko

* ```ssh = client.invoke_shell()``` - после выполнения предыдущей команды уже есть подключение к серверу. Метод ```invoke_shell``` позволяет установить интерактивную сессию SSH с сервером.
   
---
### Модуль paramiko

* Внутри установленной сессии выполняются команды и получаются данные:
 * ```ssh.send``` - отправляет указанную строку в сессию
 * ```ssh.recv``` - получает данные из сессии. В скобках указывается максимальное значение в байтах, которое можно получить. Этот метод возвращает считанную строку
* Кроме этого, между отправкой команды и считыванием, кое-где стоит строка ```time.sleep```
 * с помощью неё указывается пауза - сколько времени подождать, прежде чем скрипт продолжит выполняться. Это делается для того, чтобы дождаться выполнения команды на оборудовании

---
### Модуль paramiko

Так выглядит результат выполнения скрипта:
```
$ python 3_paramiko.py "sh ip int br"
Username: cisco
Password:
Enter enable secret:
Connection to device 192.168.100.1

R1>enable
Password:
R1#terminal length 0


R1#
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
R1#
Connection to device 192.168.100.2

R2>enable
Password:
R2#terminal length 0
R2#
sh ip int br
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

R3>enable
Password:
R3#terminal length 0
R3#
sh ip int br
Interface              IP-Address      OK? Method Status                Protocol
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

---
### Модуль paramiko

Обратите внимание, что в вывод попал и процесс ввода пароля enable и команда terminal length.

Это связано с тем, что paramiko собирает весь вывод в буфер.
И, при вызове метода ```recv``` (например, ```ssh.recv(1000)```), paramiko возвращает всё, что есть в буфере.
После выполнения ```recv```, буфер пуст.

---
### Модуль paramiko

Поэтому, если нужно получить только вывод команды sh ip int br, то надо оставить ```recv```, но не делать print:
```python
    ssh.send("enable\n")
    ssh.send(enable_pass + '\n')
    time.sleep(1)

    ssh.send("terminal length 0\n")
    time.sleep(1)
    #Тут мы вызываем recv, но не выводим содержимое буфера
    ssh.recv(1000)

    ssh.send(command + "\n")
    time.sleep(3)
    result = ssh.recv(5000).decode('utf-8')
    print(result)
```

