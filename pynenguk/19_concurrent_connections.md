# Python для мережевих інженерів 

---
## Одночасне підключення до кількох пристроїв

---
### Одночасне підключення до кількох пристроїв

Коли потрібно опитувати багато пристроїв, підключення по одному займе досить багато часу.
Для одночасного підключення до пристроїв використовується модуль concurrent.futures.

---
### Вимірювання часу виконання сценарію

Існує кілька варіантів оцінки часу виконання скрипта.
Курс використовує найпростіші варіанти:
* утиліта часу Linux
* модуль Python datetime

При оцінці часу виконання скрипта в даному випадку не важлива висока точність. 
Головне порівняти час виконання скрипта в різних версіях.

---
### ```time```

Утиліта time в Linux дозволяє виміряти час виконання сценарію. Наприклад:
```
$ time python thread_paramiko.py
...
real    0m4.712s
user    0m0.336s
sys     0m0.064s
```

Для використання утиліти time достатньо написати ``time`` перед рядком запуску скрипта.


---
### ```datetime```

Другий варіант — це модуль datetime.
Цей модуль дозволяє працювати з часом і датами в Python.

Приклад використання:
```python
from datetime import datetime
import time

start_time = datetime.now()

time.sleep(5)

print(datetime.now() - start_time)
```

---
### ```datetime```

Результат виконання:
```
$ python test.py
0:00:05.004949
```

---
## Процеси та потоки в Python (CPython)

* процес (process) - це, грубо кажучи, запущена програма. Процесу виділяються окремі ресурси: пам'ять, процесорний час
* потік - одиниця виконання в процесі. Потоки спільно використовують ресурси процесу, до якого вони належать.

---
## Процеси та потоки в Python (CPython)

Python (точніше, CPython, реалізація, яка використовується в курсі) оптимізовано для роботи в однопоточному режимі. Це добре, якщо програма використовує лише один потік.

І, разом з тим, у Python є певні нюанси роботи в багатопоточному режимі. Вони пов’язані з тим, що CPython використовує GIL (global interpreter lock).

---
### GIL

GIL запобігає одночасному виконанню коду Python кількома потоками.
GIL можна розглядати як прапор, який дозволяє потокам виконуватися.
Той, хто має прапор, може зробити роботу.

Прапорець передається або через певну кількість інструкцій Python, або, наприклад, коли виконуються деякі операції вводу/виводу.

Тому виходить, що різні потоки не будуть виконуватися паралельно, а програма просто перемикатиметься між ними, виконуючи їх у різний час.

---
### IO bound task

Якщо в програмі є якесь «очікування» пакетів з мережі, запит користувача, пауза типу сну, то в такій програмі потоки будуть виконуватися ніби паралельно, тому що під час таких пауз GIL може буде передано в інший потік.

Потоки чудово підходять для завдань, які включають операції вводу-виводу:

* Підключення до обладнання та підключення до мережі в цілому
* Робота з файловою системою
* Завантажувати файли через мережу

---
### Процеси

Процеси дозволяють виконувати завдання на різних ядрах комп’ютера.
Це важливо для завдань, які не залежать від операцій введення-виведення.

Для кожного процесу створюється власна копія ресурсів, виділяється пам'ять і кожен процес має власний GIL.
Це також робить процеси більш "важкими" порівняно з потоками.

Крім того, кількість процесів, які виконуються паралельно, залежить від кількості ядер і процесорів і зазвичай обчислюється десятками, тоді як кількість потоків для операцій введення-виведення може обчислюватися сотнями.

---
## Кількість потоків

---
### Одна команда

```
Кількість пристроїв: 40
########## Послідовне виконання ###########
0:05:03.249943
```

---
### Тест 1. Від 5 до 30 потоків з кроком 5

```
$ python netmiko_threads_submit_count.py
Кількість пристроїв: 40
################### 5 потоків ####################
0:01:03.416216
################### 10 потоків ###################
0:00:36.339131
################### 15 потоків ###################
0:00:28.748473
################### 20 потоків ###################
0:00:20.728099
################### 25 потоків ###################
0:00:20.889887
################### 30 потоків ###################
0:00:19.441675
```


---
### Тест 2. Від 20 до 40 потоків з кроком 5

```
$ python netmiko_threads_submit_count.py
Кількість пристроїв: 40
################### 20 потоків ###################
0:00:22.222185
################### 25 потоків ###################
0:00:20.248397
################### 30 потоків ###################
0:00:19.714420
################### 35 потоків ###################
0:00:18.888092
################### 40 потоків ###################
0:00:15.560998
```


---
### Тест 3. 5000 пристроїв 30-300 потоків

```
Кількість пристроїв: 5460
################### 30 потоків ###################
0:09:17.187867
################### 50 потоків ###################
0:09:17.604252
################### 70 потоків ###################
0:09:17.117332
################### 90 потоків ###################
0:09:16.693774
################### 100 потоків ##################
0:09:17.083294
################### 120 потоків ##################
0:09:17.945270
################### 140 потоків ##################
0:09:18.114993
################### 200 потоків ##################
0:11:12.951247
################### 300 потоків ##################
0:14:03.790432
```

---
## Багатопотокова безпека

Перш ніж розуміти правила, потрібно зрозуміти термін «безпека потоку». Багатопотокова безпека - це концепція, яка описує роботу з багатопоточними програмами. Код вважається потокобезпечним (thread-safe), якщо він може працювати нормально під час використання кількох потоків.


---
### Рекомендації при роботі з потоками

1. Не пишіть на той самий ресурс із різних потоків, якщо ресурс або те, що ви пишете, не призначене для багатопотокової роботи. Найпростіший спосіб це з’ясувати — пошукати в Google щось на кшталт «python записувати файл із потоків».
2. Якщо можливо, уникайте спілкування між потоками під час їх роботи. Це непросте завдання і краще спробувати обійтися без нього.
3. Дотримуйтеся принципу KISS (Keep it simple, stupid) - намагайтеся зробити рішення максимально простим.

---
## Модуль logging

Модуль logging - це модуль зі стандартної бібліотеки Python, який дозволяє налаштовувати журналювання зі скрипту.

```python
import logging

logging.basicConfig(
    format='%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)
```

* усі повідомлення будуть виведені на стандартний потік виведення,
* відображатимуться повідомлення рівня INFO і вище,
* кожне повідомлення міститиме інформацію про потік, назву logger, рівень повідомлення та саме повідомлення.


---
### Приклад

```python
from datetime import datetime
import logging
import netmiko
import yaml


logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)


def send_show(device, show):
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received:   {}'
    ip = device["ip"]
    logging.info(start_msg.format(datetime.now().time(), ip))

    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result =  ssh.send_command(show)
        logging.info(received_msg.format(datetime.now().time(), ip))
    return result


if __name__ == "__main__":
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        print(send_show(dev, 'sh clock'))
```

---
### Результат виконання скрипта

```
$ python logging_basics.py
MainThread root INFO: ===> 12:26:12.767168 Connection: 192.168.100.1
MainThread root INFO: <=== 12:26:18.307017 Received:   192.168.100.1
*12:26:18.137 UTC Wed Jun 5 2019
MainThread root INFO: ===> 12:26:18.413913 Connection: 192.168.100.2
MainThread root INFO: <=== 12:26:23.991715 Received:   192.168.100.2
*12:26:23.819 UTC Wed Jun 5 2019
MainThread root INFO: ===> 12:26:24.095452 Connection: 192.168.100.3
MainThread root INFO: <=== 12:26:29.478553 Received:   192.168.100.3
*12:26:29.308 UTC Wed Jun 5 2019
```

---
## Модуль concurrent.futures

Модуль concurrent.futures надає інтерфейс високого рівня для роботи з процесами та потоками.
При цьому і потоки, і процеси використовують однаковий інтерфейс.

Якщо порівнювати цей модуль з threading або multiprocessing, то він має трохи менше можливостей, але з concurrent.futures легше працювати та інтерфейс більш зрозумілий.


---
### Модуль concurrent.futures

Модуль concurrent.futures дозволяє вирішити проблему запуску кількох потоків/процесів і отримання даних з них. Для цього модуль використовує два класи:

* ThreadPoolExecutor - для роботи з потоками
* ProcessPoolExecutor - для роботи з процесами

Обидва класи використовують однаковий інтерфейс роботи.

---
### Executor

Створення об'єкта Executor на прикладі ThreadPoolExecutor:

```
executor = ThreadPoolExecutor(max_workers=5)
```

У об'єкта ``executor`` три методи: shutdown, map і submit. Метод shutdown відповідає за завершення потоків/процесів, а методи map і submit за запуск функцій у різних потоках/процесах.

---
### Метод shutdown

Метод ``shutdown`` вказує на те, що об’єкт Executor має завершити роботу. Водночас, якщо ви передаєте методу shutdown значення ``wait=True`` (значення за замовчуванням), він не поверне результат, доки не завершаться всі функції, що виконуються в потоках. Якщо ``wait=False``, метод shutdown негайно завершується, але сам скрипт не завершиться, доки не завершаться всі функції.

Зазвичай, замість явного виклику методу shutdown, використовується менеджер контексту. В цьому випадку метод shutdown автоматично викликається в кінці блоку with із параметром ``wait=True``.

```python
with ThreadPoolExecutor(max_workers=5) as executor:
    ...
```

---
### Схема роботи з concurrent.futures

Оскільки методи map і submit запускають певну функцію в потоках або процесах, код повинен містити, як мінімум, функцію, яка виконує одну дію і яку потрібно запускати в різних потоках з різними аргументами функції.

Наприклад, якщо вам потрібно виконати перевірку ping кількох IP-адрес у різних потоках, ви повинні створити функцію, яка буде перевіряти одну IP-адресу, а потім запустити цю функцію в різних потоках для різних IP-адрес за допомогою concurrent.futures.

---
### Метод map

Метод map працює подібно до вбудованої функції ``map``: він застосовує func до одного або кількох ітерованих об’єктів. У цьому випадку кожен виклик функції запускається в окремому потоці/процесі. Метод map повертає ітератор із результатами виконання функції для кожного елемента iterable. Результати розташовані в тому ж порядку, що й елементи в iterables.

```python
map(func, *iterables, timeout=None)
```

---
### Метод map

```python
from datetime import datetime
import time
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor
import logging
import netmiko
import yaml


logging.getLogger('paramiko').setLevel(logging.WARNING)
logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)


def send_show(device, show):
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received:   {}'
    ip = device['ip']
    logging.info(start_msg.format(datetime.now().time(), ip))
    if ip == '192.168.100.1':
        time.sleep(5)

    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(show)
        logging.info(received_msg.format(datetime.now().time(), ip))
    return result


with open('devices.yaml') as f:
    devices = yaml.safe_load(f)

with ThreadPoolExecutor(max_workers=3) as executor:
    result = executor.map(send_show, devices, repeat('sh clock'))
    for device, output in zip(devices, result):
        print(device['ip'], output)
```

---
### Метод map

Останні 4 рядки коду відповідають за підключення до пристроїв в окремих потоках:

```python
with ThreadPoolExecutor(max_workers=3) as executor:
    result = executor.map(send_show, devices, repeat('sh clock'))
    for device, output in zip(devices, result):
        print(device['ip'], output)
```

---
### Метод map

Результат виконання:
```
$ python netmiko_threads_map_basics.py
ThreadPoolExecutor-0_0 root INFO: ===> 08:28:55.950254 Connection: 192.168.100.1
ThreadPoolExecutor-0_1 root INFO: ===> 08:28:55.963198 Connection: 192.168.100.2
ThreadPoolExecutor-0_2 root INFO: ===> 08:28:55.970269 Connection: 192.168.100.3
ThreadPoolExecutor-0_1 root INFO: <=== 08:29:11.968796 Received:   192.168.100.2
ThreadPoolExecutor-0_2 root INFO: <=== 08:29:15.497324 Received:   192.168.100.3
ThreadPoolExecutor-0_0 root INFO: <=== 08:29:16.854344 Received:   192.168.100.1
192.168.100.1 *08:29:16.663 UTC Thu Jul 4 2019
192.168.100.2 *08:29:11.744 UTC Thu Jul 4 2019
192.168.100.3 *08:29:15.374 UTC Thu Jul 4 2019
```

---
## Метод submit

---
### Метод submit

* submit запускає одну функцію на потік
* за допомогою submit можна запускати різні функції з різними непов’язаними аргументами, а map має запускатися з ітерованими об’єктами як аргументами
* submit повертає результат негайно, не чекаючи завершення функції
* submit повертає спеціальний об’єкт Future, який представляє виконання функції
* submit в комбінації з ``as_completed`` може повертати результати в порядку готовності, а не в порядку передачі аргументів
* submit можна передавати іменовані аргументи, а map лише позиційні

---
## Future

Метод submit використовує об’єкт Future — це об'єкт, який репрезентує відкладене обчислення. Цей об’єкт можна запитати про статус (чи виконано завдання чи ні), результати або винятки, які виникли під час виконання завдання. Future не потрібно створювати вручну, ці об'єкти створюються методом submit.

---
### Метод submit

Файл netmiko_threads_submit_basics.py:
```python
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from datetime import datetime
import time
import logging

import yaml
from netmiko import ConnectHandler, NetMikoAuthenticationException


logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)
```

---
### Метод submit

Файл netmiko_threads_submit_basics.py:
```python
def send_show(device_dict, command):
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received: {}'
    ip = device_dict['ip']
    logging.info(start_msg.format(datetime.now().time(), ip))
    if ip == '192.168.100.1':
        time.sleep(5)

    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        logging.info(received_msg.format(datetime.now().time(), ip))
    return {ip: result}


with open('devices.yaml') as f:
    devices = yaml.safe_load(f)

with ThreadPoolExecutor(max_workers=2) as executor:
    future_list = []
    for device in devices:
        future = executor.submit(send_show, device, 'sh clock')
        future_list.append(future)
    for f in as_completed(future_list):
        print(f.result())
```

---
### Метод submit та робота з futures

* future_list - список об'єктів future
* наступний цикл проходить за списком future за допомогою функції as_completed. Ця функція повертає future лише тоді, коли вони завершені або скасовані. У цьому випадку future повертаються після завершення роботи, а не в порядку їх додавання до списку future_list

```python
with ThreadPoolExecutor(max_workers=2) as executor:
    future_list = []
    for device in devices:
        future = executor.submit(send_show, device, 'sh clock')
        future_list.append(future)
    for f in as_completed(future_list):
        print(f.result())
```

---
### Метод submit та робота з futures

```
$ python netmiko_threads_submit_basics.py
ThreadPoolExecutor-0_0 root INFO: ===> 17:32:59.088025 Connection: 192.168.100.1
ThreadPoolExecutor-0_1 root INFO: ===> 17:32:59.094103 Connection: 192.168.100.2
ThreadPoolExecutor-0_1 root INFO: <=== 17:33:11.639672 Received: 192.168.100.2
{'192.168.100.2': '*17:33:11.429 UTC Thu Jul 4 2019'}
ThreadPoolExecutor-0_1 root INFO: ===> 17:33:11.849132 Connection: 192.168.100.3
ThreadPoolExecutor-0_0 root INFO: <=== 17:33:17.735761 Received: 192.168.100.1
{'192.168.100.1': '*17:33:17.694 UTC Thu Jul 4 2019'}
ThreadPoolExecutor-0_1 root INFO: <=== 17:33:23.230123 Received: 192.168.100.3
{'192.168.100.3': '*17:33:23.188 UTC Thu Jul 4 2019'}
```
