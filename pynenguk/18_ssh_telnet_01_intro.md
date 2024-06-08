# Python для мережевих інженерів 


---

# Підключення до обладнання

---

## Модулі для підключення SSH/Telnet

* pexpect
* telnetlib
* paramiko
* netmiko
* scrapli

---

## Введення пароля

---
### Введення пароля

При підключенні до обладнання вручну, як правило, пароль також вводиться вручну.

При автоматизації підключення необхідно визначитися, як буде передаватися пароль:
* запитувати пароль під час запуску сценарію та читати введені користувачем дані
* записати свій логін і пароль у якийсь файл

---
### Модуль getpass

Модуль getpass дозволяє запитувати пароль без відображення введених символів:
```python
In [1]: import getpass

In [2]: password = getpass.getpass()
Password:

In [3]: print(password)
testpass
```

---
### Змінні середовища

Іншим варіантом збереження пароля (і, можливо, пароля) є змінні середовища.

Наприклад, таким чином логін і пароль записуються в змінні:
```
$ export SSH_user=user
$ export SSH_password=userpass
```

А потім в Python значення зчитуються в змінні в скрипті:
```python
import os

username = os.environ.get('SSH_user')
password = os.environ.get('SSH_password')
```

---
### Налаштування інтерфейсу CLI (приклад із click)

```python
@click.command()
@click.argument("command")
@click.argument("ip-list", nargs=-1)
@click.option("--username", "-u", envvar="NET_USER", prompt=True)
@click.option("--password", "-p", envvar="NET_PASSWORD", prompt=True, hide_input=True)
@click.option("--secret", "-s", envvar="NET_SECRET", prompt=True, hide_input=True)
def main(command, ip_list, username, password, secret):
    device_params = {
        "device_type": "cisco_ios",
        "username": username,
        "password": password,
        "secret": secret,
    }

    device_list = [{**device_params, "host": ip} for ip in ip_list]

    result_dict = send_command_to_cisco_devices(device_list, command)
```

