# Python для мережевих інженерів 


---

# Підключення до обладнання

---
## Модуль paramiko

---
### Модуль paramiko

Paramiko — це реалізація протоколу SSHv2 на Python.
Paramiko забезпечує функціональність клієнта та сервера.

Оскільки Paramiko не входить до стандартної бібліотеки модулів Python, його потрібно встановити:
```
pip install paramiko
```

---
### Модуль paramiko

Приклад використання Paramiko (файл 3_paramiko.py):
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

Приклад використання Paramiko (файл 3_paramiko.py):
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

* ``client = paramiko.SSHClient()`` - цей клас представляє підключення до SSH-сервера. Він виконує аутентифікацію клієнта.
* ```client.set_missing_host_key_policy(paramiko.AutoAddPolicy())```
  * ```set_missing_host_key_policy``` - встановлює, яку політику використовувати під час підключення до сервера, ключ якого невідомий.
  * ```paramiko.AutoAddPolicy()``` - політика, яка автоматично додає нове ім'я хоста та ключ до локального об'єкта HostKeys.

---
### Модуль paramiko

* ```client.connect``` - метод підключення до SSH-сервера та автентифікації підключення
  * ```hostname``` - ім'я хоста або IP-адреса
  * ```username``` - ім'я користувача
  * ```password``` - пароль
  * ```look_for_keys``` - за замовчуванням paramiko виконує автентифікацію на основі ключа. Щоб вимкнути це, вам потрібно встановити значення False
  * ```allow_agent``` - paramiko може підключатися до локального SSH-агента ОС. Це необхідно при роботі з ключами, а оскільки в даному випадку аутентифікація виконується за логіном/паролем, це потрібно вимкнути.


---
### Модуль paramiko

* ```ssh = client.invoke_shell()``` - після виконання попередньої команди вже є підключення до сервера. Метод ```invoke_shell``` дозволяє встановити інтерактивний сеанс SSH із сервером.


---
### Модуль paramiko

* Всередині встановленого сеансу виконуються команди і отримуються дані:
  * ```ssh.send``` - надсилає вказаний рядок
  * ```ssh.recv``` - отримує дані з сесії. Максимальне значення в байтах, яке можна отримати, вказано в дужках. Цей метод повертає прочитаний рядок
* Крім того, між надсиланням команди та читанням тут і там є рядок ```time.sleep```
  * використовується для створення паузи і вказує скільки часу чекати, перш ніж скрипт продовжить виконання. Це робиться для того, щоб дочекатися виконання команди на обладнанні

---
### Модуль paramiko

Так виглядає результат виконання скрипта:
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

Зауважте, що у вивід потрапив як процес введення пароля enable, так і команда `terminal length`.

Це тому, що paramiko збирає весь вивід у буфер.
І під час виклику методу ```recv``` (наприклад, ```ssh.recv(1000)```) paramiko повертає все, що є в буфері.
Після виконання ```recv``` буфер порожній.

---
### Модуль paramiko

Тому, якщо вам потрібно лише отримати результат команди sh ip int br, тоді вам потрібно залишити ```recv```, але не робити print:
```python
    ssh.send("enable\n")
    ssh.send(enable_pass + '\n')
    time.sleep(1)

    ssh.send("terminal length 0\n")
    time.sleep(1)
    # recv без print
    ssh.recv(1000)

    ssh.send(command + "\n")
    time.sleep(3)
    result = ssh.recv(5000).decode('utf-8')
    print(result)
```

