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

Если в программе есть некое "ожидание": пакетов из сети, запроса пользователя, пауза типа sleep - то в такой программе потоки будут выполняться как будто параллельно, потому что во время таких пауз флаг (GIL) можно передать другому потоку.

Потоки отлично подходят для задач, которые связаны с операциями ввода-вывода:

* Подключение к оборудованию и подключение по сети в целом
* Работа с файловой системой
* Скачивание файлов по сети


---
### Процессы

Процессы позволяют выполнять задачи на разных ядрах компьютера.
Это важно для задач, которые не завязаны на операции ввода-вывода.

Для каждого процесса создается своя копия ресурсов, выделяется память, у каждого процесса свой GIL.
Это же делает процессы более тяжеловесными, по сравнению с потоками.

Кроме того, количество процессов, которые запускаются параллельно, зависит от количества ядер и CPU и обычно исчисляется в десятках, тогда как количество потоков для операций ввода-вывода может исчисляться в сотнях.

---
## Количество потоков

---
### Одна команда

```
Количество устройств: 40
########## Последовательное выполнение ###########
0:05:03.249943
```

---
### Тест 1. От 5 до 30 потоков с шагом 5

```
$ python netmiko_threads_submit_count.py
Количество устройств: 40
################### 5 потоков ####################
0:01:03.416216
################### 10 потоков ###################
0:00:36.339131
################### 15 потоков ###################
0:00:28.748473
################### 20 потоков ###################
0:00:20.728099
################### 25 потоков ###################
0:00:20.889887
################### 30 потоков ###################
0:00:19.441675
```


---
### Тест 2. От 20 до 40 потоков с шагом 5

```
$ python netmiko_threads_submit_count.py
Количество устройств: 40
################### 20 потоков ###################
0:00:22.222185
################### 25 потоков ###################
0:00:20.248397
################### 30 потоков ###################
0:00:19.714420
################### 35 потоков ###################
0:00:18.888092
################### 40 потоков ###################
0:00:15.560998
```


---
### Тест 3. 5000 устройств 30-300 потоков

```
Количество устройств: 5460
################### 30 потоков ###################
0:09:17.187867
################### 50 потоков ###################
0:09:17.604252
################### 70 потоков ###################
0:09:17.117332
################### 90 потоков ###################
0:09:16.693774
################### 100 потоков ##################
0:09:17.083294
################### 120 потоков ##################
0:09:17.945270
################### 140 потоков ##################
0:09:18.114993
################### 200 потоков ##################
0:11:12.951247
################### 300 потоков ##################
0:14:03.790432
```

---
## Потоковая безопасность

Прежде чем разбираться с правилами, надо разобраться с термином «потоковая безопасность». Потоковая безопасность - это концепция, которая описывает работу с многопоточными программами. Код считается потокобезопасным (thread-safe), если он может работать нормально при использовании нескольких потоков.

---
### Рекомендации при работе с потоками

1. Не пишите в один и тот же ресурс из разных потоков, если ресурс или то, чем пишите не предназначено для многопоточной работы. Выяснить это, проще всего, погуглив что-то вроде «python write to file from threads».
2. Если есть воможность, избегайте коммуникаций между потоками в процессе их работы. Это непростая задача и лучше постараться обойтись без нее.
3. Соблюдайте принцип KISS (Keep it simple, stupid) - постарайтесь, чтобы решение было максимально простым.

---
## Модуль logging

Модуль logging - это модуль из стандартной библиотеки Python, который позволяет настраивать логирование из скрипта.

```python
import logging

logging.basicConfig(
    format='%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)
```

* все сообщения будут выводиться на стандартный поток вывода,
* будут выводиться сообщения уровня INFO и выше,
* в каждом сообщении будет информация о потоке, имя логера, уровень сообщения и само сообщение.

---
### Пример скрипта

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
### Результат выполнения скрипта

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

Модуль concurrent.futures предоставляет высокоуровневый интерфейс для работы с процессами и потоками.
При этом и для потоков, и для процессов используется одинаковый интерфейс, что позволяет легко переключаться между ними.
Если сравнивать этот модуль с threading или multiprocessing, то у него меньше возможностей, но с concurrent.futures работать проще и интерфейс более понятный.

---
### Модуль concurrent.futures

Модуль concurrent.futures позволяет решить задачу запуска нескольких потоков/процессов и получения из них данных. Для этого в модуле используются два класса:

* ThreadPoolExecutor - для работы с потоками
* ProcessPoolExecutor - для работы с процессами

Оба класса используют одинаковый интерфейс, поэтому достаточно разобраться с одним и затем просто переключиться на другой при необходимости.

---
### Executor

Создание объекта Executor на примере ThreadPoolExecutor:

```
executor = ThreadPoolExecutor(max_workers=5)
```

После создания объекта Executor, у него есть три метода: shutdown, map и submit. Метод shutdown отвечает за завершение потоков/процессов, а методы map и submit за запуск функций в разных потоках/процессах.

---
### Метод shutdown

Метод shutdown указывает, что объекту Executor надо завершить работу. При этом, если методу shutdown передать значение wait=True (значение по умолчанию), он не вернут результат пока не завершатся все функции, которые запущены в потоках. Если же wait=False, метод shutdown завершает работу мгновенно, но при этом сам скрипт не завершит работу пока все функции не отработают.

Как правило, метод shutdown не используется явно, так как при создании объекта Executor в менеджере контекста, метод shutdown автоматически вызывается в конце блока with c wait равным True.

```
with ThreadPoolExecutor(max_workers=5) as executor:
    ...
```

---
### Схема работы с concurrent.futures

Так как методы map и submit запускают какую-то функцию в потоках или процессах, в коде должна присутствовать, как минимум, функция которая выполняет одно действие и которую надо запустить в разных потоках с разными аргументами функции.

Например, если необходимо пинговать несколько IP-адресов в разных потоках, надо создать функцию, которая будет пинговать один IP-адрес, а затем запустить эту функцию в разных потоках для разных IP-адресов с помощью concurrent.futures.

---
### Метод map

Метод map - работает похоже на встроенную функцию map: применяет функцию func к одному или более итерируемых объектов. При этом, каждый вызов функции запускается в отдельном потоке/процессе. Метод map возвращает итератор с результатами выполнения функции для каждого элемента итерируемого объекта. Результаты расположены в том же порядке, что и элементы в итерируемом объекте.

```
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

Последние 4 строки кода отвечают за подключение к устройствам в отдельных потоках:

```python
with ThreadPoolExecutor(max_workers=3) as executor:
    result = executor.map(send_show, devices, repeat('sh clock'))
    for device, output in zip(devices, result):
        print(device['ip'], output)
```

---
### Метод map

Результат выполнения:
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

* submit запускает в потоке только одну функцию
* с помощью submit можно запускать разные функции с разными несвязанными аргументами, а map надо обязательно запускать с итерируемым объектами в роли аргументов
* submit сразу возвращает результат, не дожидаясь выполнения функции
* submit возвращает специальный объект Future, который представляет выполнение функции.
* submit возвращает результаты в порядке готовности, а не в порядке аргументов
* submit можно передавать ключевые аргументы, а map только позиционные

---
## Future

Метод submit использует объект Future - это объект, который представляет отложенное вычисление. Этот объект можно запрашивать о состоянии (завершена работа или нет), можно получать результаты или исключения, которые возникли в процессе работы, по мере возникновения. Future не нужно создавать вручную, эти объекты создаются методом submit.

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
### Метод submit и работа с futures

* future_list - это список объектов future
* следующий цикл проходится по списку future с помощью функции as_completed. Эта функция возвращает future только когда они завершили работу или были отменены. При этом future возвращаются по мере завершения работы, не в порядке добавления в список future_list

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
### Метод submit и работа с futures

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
