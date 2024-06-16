# Python для мережевих інженерів 

---
# Регулярні вирази

---
## Модуль re

---
## Модуль re

Основні функції модуля __re__:

* search - шукає перший збіг з шаблоном
* findall - шукає всі збіги з шаблоном. Повертає збіги у вигляді списку рядків
* finditer - шукає всі збіги з шаблоном. Повертає ітератор із збігами (об’єкти Match)
* match - шукає збіг на початку рядка
* fullmatch - весь рядок повинен відповідати описаному регулярному виразу
* compile - компілює регулярний вираз. Потім можна застосувати всі перелічені функції до отриманого об’єкту


---
## Модуль re

Крім функцій пошуку збігів, модуль має наступні функції:

* ```re.sub``` - для заміни в рядках
* ```re.split``` - для розділення рядків на частини

---
## raw string

У Python для роботи з регулярними виразами використовується модуль re.
Відповідно, для початку роботи з регулярними виразами треба його
імпортувати.

У Python деякі символи рядка треба екранувати, щоб вони сприймалися
правильно. До таких символів відноситься, наприклад, ``\``. Щоб написати правильно
рядок, в якому знаходяться два символи ``\\``, обидва символи треба екранувати і в
результаті вийде рядок виду: ``\\\\data``. Натомість, можна використовувати
raw-рядок і тоді кожен символ буде сприйматися як написано. Raw-рядки
відрізняються від звичайних тим, що при створенні рядка, на початку пишеться літера r:

```python
In [3]: r"\\data"
Out[3]: '\\\\data'
```


Так як у регулярних виразах постійно використовується ``\``, завжди
використовуйте raw-рядки для опису регулярних виразів. Деякі вирази
правильно відпрацюють і без raw-рядків, але, використання raw-рядків для
регулярних виразів це гарний тон.

---
## Об'єкт Match

---
### Об'єкт Match

У модулі re кілька функцій повертають об'єкт Match, якщо знайдено збіг:
* search
* match
* finditer повертає ітератор з об'єктами Match

---
### Об'єкт Match

Приклад об'єкту Match:
```python
In [1]: log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'

In [2]: match = re.search('Host (\S+) in vlan (\d+) .* port (\S+) and port (\S+)', log)

In [3]: match
Out[3]: <_sre.SRE_Match object; span=(47, 124), match='Host f03a.b216.7ad7 in vlan 10 is flapping betwee>

```

Вивід у 3 рядку просто відображає інформацію про об'єкт.
Тому не варто покладатися на те, що відображається в частині match, так як рядок, що відображається, обрізається за фіксованою кількістю знаків.

---
### group()

Метод group повертає підрядок, який збігся з шаблоном або з виразом у групі.

Якщо метод викликається без аргументів, відображається весь підрядок:
```python
In [4]: match.group()
Out[4]: 'Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'

```

---
### group()

Фактично, у цьому випадку метод group викликається з групою 0:

```python
In [13]: match.group(0)
Out[13]: 'Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
```

---
### group()

Інші номери відображають лише вміст відповідної групи:
```python
In [14]: match.group(1)
Out[14]: 'f03a.b216.7ad7'

In [15]: match.group(2)
Out[15]: '10'

In [16]: match.group(3)
Out[16]: 'Gi0/5'

In [17]: match.group(4)
Out[17]: 'Gi0/15'
```

---
### group()

Якщо викликати метод group з номером групи, який перевищує кількість існуючих груп, виникне помилка:
```python
In [18]: match.group(5)
-----------------------------------------------------------------
IndexError                      Traceback (most recent call last)
<ipython-input-18-9df93fa7b44b> in <module>()
----> 1 match.group(5)

IndexError: no such group
```

---
### group()

Якщо викликати метод із кількома номерами груп, результатом буде кортеж рядків, які відповідають збігам:

```python
In [19]: match.group(1, 2, 3)
Out[19]: ('f03a.b216.7ad7', '10', 'Gi0/5')
```

---
### group()

Якщо група описує частину шаблону та збігів було кілька, метод відобразить останній збіг:
```python
In [1]: log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'

In [44]: match = re.search('Host (\w{4}\.)+', log)

In [45]: match.group(1)
Out[46]: 'b216.'
```

Такий вивід був отриманий через те, що вираз у дужках описує 4 літери або цифри, а після них стоїть плюс.
Відповідно, спочатку перша частина MAC-адреси відповідала виразу в дужках, потім друга.
Але запам'ятовується і повертається тільки останній збіг з групою.

---
### group()

Якщо у виразі використовувалися іменовані групи, методу group можна передати ім'я групи та отримати відповідний підрядок:
```python
In [1]: log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'

In [55]: match = re.search('Host (?P<mac>\S+) '
    ...:                   'in vlan (?P<vlan>\d+) .* '
    ...:                   'port (?P<int1>\S+) '
    ...:                   'and port (?P<int2>\S+)',
    ...:                   log)
    ...:

In [53]: match.group('mac')
Out[53]: 'f03a.b216.7ad7'

In [54]: match.group('int2')
Out[54]: 'Gi0/15'
```

---
### group()

Але ці групи доступні і за номером:
```python
In [58]: match.group(3)
Out[58]: 'Gi0/5'

In [59]: match.group(4)
Out[59]: 'Gi0/15'
```


---
### groups()

Метод groups() повертає кортеж з рядками, в якому елементи - це ті підрядки, які потрапили до відповідних груп:
```python
In [63]: log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'

In [64]: match = re.search('Host (\S+) '
    ...:                   'in vlan (\d+) .* '
    ...:                   'port (\S+) '
    ...:                   'and port (\S+)',
    ...:                   log)
    ...:

In [65]: match.groups()
Out[65]: ('f03a.b216.7ad7', '10', 'Gi0/5', 'Gi0/15')

```

---
### groups()

Метод груп має необов'язковий параметр - default. Це працює в ситуації, коли все, що потрапляє в групу, є необов’язковим.

Наприклад, з таким рядком буде збіг і в першій групі, і в другій:

```python
In [76]: line = '100     aab1.a1a1.a5d3    FastEthernet0/1'

In [77]: match = re.search('(\d+) +(\w+)?', line)

In [78]: match.groups()
Out[78]: ('100', 'aab1')
```

---
### groups()

Якщо після пробілу в рядку нічого немає, нічого не буде включено до групи.
Але збіг буде, оскільки регулярний вираз описує, що група необов’язкова:

```python
In [80]: line = '100     '

In [81]: match = re.search('(\d+) +(\w+)?', line)

In [82]: match.groups()
Out[82]: ('100', None)
```

Відповідно, для другої групи значення буде None.

---
### groups()

Но если передать методу groups аргумент, он будет возвращаться вместо None:
```python
In [83]: line = '100     '

In [84]: match = re.search('(\d+) +(\w+)?', line)

In [85]: match.groups(0)
Out[85]: ('100', 0)

In [86]: match.groups('No match')
Out[86]: ('100', 'No match')
```

---
### groupdict()

Але якщо передати методу groups аргумент, він повертатиметься замість None:
```python
In [63]: log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'

In [88]: match = re.search('Host (?P<mac>\S+) '
    ...:                   'in vlan (?P<vlan>\d+) .* '
    ...:                   'port (?P<int1>\S+) '
    ...:                   'and port (?P<int2>\S+)',
    ...:                   log)
    ...:

In [89]: match.groupdict()
Out[89]: {'int1': 'Gi0/5', 'int2': 'Gi0/15', 'mac': 'f03a.b216.7ad7', 'vlan': '10'}
```



---
## ```re.search()```

---
### ```re.search()```

Функция ```search()```:
* используется для поиска подстроки, которая соответствует шаблону
* возвращает объект Match, если подстрока найдена
* возвращает ```None```, если подстрока не найдена

Функция search подходит в том случае, когда надо найти только одно совпадение в строке, например, когда регулярное выражение описывает всю строку или часть строки.


---
### ```re.search()```

В файле log.txt находятся лог-сообщения с информацией о том, что один и тот же MAC слишком быстро переучивается то на одном, то на другом интерфейсе.
Одна из причин таких сообщений - петля в сети.

Содержимое файла log.txt:
```
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/24 and port Gi0/19
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/24 and port Gi0/16
```

---
### ```re.search()```

При этом, MAC-адрес может прыгать между несколькими портами.
В таком случае очень важно знать, с каких портов прилетает MAC.
И, если это вызвано петлей, выключить все порты, кроме одного.

Попробуем вычислить, между какими портами и в каком VLAN образовалась проблема.

---
### ```re.search()```

Проверка регулярного выражения с одной строкой из log-файла:
```python
In [1]: import re

In [2]: log = '%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24'

In [3]: match = re.search('Host \S+ '
   ...:                   'in vlan (\d+) '
   ...:                   'is flapping between port '
   ...:                   '(\S+) and port (\S+)', log)
   ...:

```

---
### ```re.search()```

Регулярное выражение для удобства чтения разбито на части.
В нем есть три группы:
* ```(\d+)``` - описывает номер VLAN
* ```(\S+) and port (\S+)``` - в это выражение попадают номера портов

---
### ```re.search()```

В итоге, в группы попали такие части строки:
```python
In [4]: match.groups()
Out[4]: ('10', 'Gi0/16', 'Gi0/24')
```

---
### ```re.search()```

В итоговом скрипте файл log.txt обрабатывается построчно, и из каждой строки собирается информация о портах.
Так как порты могут дублироваться, сразу добавляем их в множество, чтобы получить подборку уникальных интерфейсов (файл parse_log_search.py):
```python
import re

regex = ('Host \S+ '
         'in vlan (\d+) '
         'is flapping between port '
         '(\S+) and port (\S+)')

ports = set()

with open('log.txt') as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            vlan = match.group(1)
            ports.add(match.group(2))
            ports.add(match.group(3))

print('Петля между портами {} в VLAN {}'.format(', '.join(ports), vlan))

```

---
### ```re.search()```

Результат выполнения скрипта такой:
```
$ python parse_log_search.py
Петля между портами Gi0/19, Gi0/24, Gi0/16 в VLAN 10
```

---
### Обработка вывода show cdp neighbors detail

Попробуем получить параметры устройств из вывода sh cdp neighbors detail.

Пример вывода информации для одного соседа:
```
SW1#show cdp neighbors detail
-------------------------
Device ID: SW2
Entry address(es):
  IP address: 10.1.1.2
Platform: cisco WS-C2960-8TC-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/0/16,  Port ID (outgoing port): GigabitEthernet0/1
Holdtime : 164 sec

Version :
Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Mon 03-Mar-14 22:53 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
  IP address: 10.1.1.2

```

---
### Обработка вывода show cdp neighbors detail

Задача получить такие поля:
* имя соседа (Device ID: SW2)
* IP-адрес соседа (IP address: 10.1.1.2)
* платформу соседа (Platform: cisco WS-C2960-8TC-L)
* версию IOS (Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9, RELEASE SOFTWARE (fc1))

---
### Обработка вывода show cdp neighbors detail

И, для удобства, надо получить данные в виде словаря.
Пример итогового словаря для коммутатора SW2:
```python
{'SW2': {'ip': '10.1.1.2',
         'platform': 'cisco WS-C2960-8TC-L',
         'ios': 'C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9'}}
```


---
### Обработка вывода show cdp neighbors detail

Файл parse_sh_cdp_neighbors_detail_ver1.py
```python
import re
from pprint import pprint


def parse_cdp(filename):
    result = {}

    with open(filename) as f:
        for line in f:
            if line.startswith('Device ID'):
                neighbor = re.search('Device ID: (\S+)', line).group(1)
                result[neighbor] = {}
            elif line.startswith('  IP address'):
                ip = re.search('IP address: (\S+)', line).group(1)
                result[neighbor]['ip'] = ip
            elif line.startswith('Platform'):
                platform = re.search('Platform: (\S+ \S+),', line).group(1)
                result[neighbor]['platform'] = platform
            elif line.startswith('Cisco IOS Software'):
                ios = re.search('Cisco IOS Software, (.+), RELEASE', line).group(1)
                result[neighbor]['ios'] = ios

    return result

pprint(parse_cdp('sh_cdp_neighbors_sw1.txt'))

```

---
### Обработка вывода show cdp neighbors detail

Результат выглядит так:
```python
$ python parse_sh_cdp_neighbors_detail_ver1.py
{'R1': {'ios': '3800 Software (C3825-ADVENTERPRISEK9-M), Version 12.4(24)T1',
        'ip': '10.1.1.1',
        'platform': 'Cisco 3825'},
 'R2': {'ios': '2900 Software (C3825-ADVENTERPRISEK9-M), Version 15.2(2)T1',
        'ip': '10.2.2.2',
        'platform': 'Cisco 2911'},
 'SW2': {'ios': 'C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9',
         'ip': '10.1.1.2',
         'platform': 'cisco WS-C2960-8TC-L'}}

```

---
### Обработка вывода show cdp neighbors detail

Файл parse_sh_cdp_neighbors_detail_ver2.py:
```python
import re
from pprint import pprint


def parse_cdp(filename):
    regex = ('Device ID: (?P<device>\S+)'
             '|IP address: (?P<ip>\S+)'
             '|Platform: (?P<platform>\S+ \S+),'
             '|Cisco IOS Software, (?P<ios>.+), RELEASE')

    result = {}

    with open('sh_cdp_neighbors_sw1.txt') as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                if match.lastgroup == 'device':
                    device = match.group(match.lastgroup)
                    result[device] = {}
                elif device:
                    result[device][match.lastgroup] = match.group(match.lastgroup)

    return result

pprint(parse_cdp('sh_cdp_neighbors_sw1.txt'))

```

---
### Обработка вывода show cdp neighbors detail

Пояснения ко второму варианту:
* в регулярном выражении описаны все варианты строк через знак или ```|```
* без проверки строки ищется совпадение
* если совпадение найдено, проверяется метод lastgroup
  * метод lastgroup возвращает имя последней именованной группы в регулярном выражении, для которой было найдено совпадение
  * если было найдено совпадение для группы device, в переменную device записывается значение, которое попало в эту группу
  * иначе в словарь записывается соответствие 'имя группы': соответствующее значение

---
### Обработка вывода show cdp neighbors detail

У этого решения ограничение в том, что подразумевается, что в каждой строке может быть только одно совпадение. И в регулярных выражениях, которые записаны через знак ```|```, может быть только одна группа.
Это можно исправить, расширив решение.

---
### Обработка вывода show cdp neighbors detail

Результат будет таким же:
```python
$ python parse_sh_cdp_neighbors_detail_ver2.py
{'R1': {'ios': '3800 Software (C3825-ADVENTERPRISEK9-M), Version 12.4(24)T1',
        'ip': '10.1.1.1',
        'platform': 'Cisco 3825'},
 'R2': {'ios': '2900 Software (C3825-ADVENTERPRISEK9-M), Version 15.2(2)T1',
        'ip': '10.2.2.2',
        'platform': 'Cisco 2911'},
 'SW2': {'ios': 'C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9',
         'ip': '10.1.1.2',
         'platform': 'cisco WS-C2960-8TC-L'}}

```


---
## ```re.match()```

---
### ```re.match()```

Функция ```match()```:
* используется для поиска в начале строки подстроки, которая соответствует шаблону
* возвращает объект Match, если подстрока найдена
* возвращает ```None```, если подстрока не найдена

---
### ```re.match()```

Функция match отличается от search тем, что match всегда ищет совпадение в начале строки.
Например, если повторить пример, который использовался для функции search, но уже с match:
```python
In [2]: import re

In [3]: log = '%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24'

In [4]: match = re.match('Host \S+ '
   ...:                  'in vlan (\d+) '
   ...:                  'is flapping between port '
   ...:                  '(\S+) and port (\S+)', log)
   ...:
```

---
### ```re.match()```

Результатом будет None:
```python
In [6]: print(match)
None

```

Так получилось из-за того, что match ищет слово Host в начале строки.
Но это сообщение находится в середине.

---
### ```re.match()```

В данном случае можно легко исправить выражение, чтобы функция match находила совпадение:
```python
In [4]: match = re.match('\S+: Host \S+ '
   ...:                  'in vlan (\d+) '
   ...:                  'is flapping between port '
   ...:                  '(\S+) and port (\S+)', log)
   ...:

```

---
### ```re.match()```

Перед словом Host добавлено выражение ```\S+: ```. Теперь совпадение будет найдено:
```python
In [11]: print(match)
<_sre.SRE_Match object; span=(0, 104), match='%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in >

In [12]: match.groups()
Out[12]: ('10', 'Gi0/16', 'Gi0/24')
```

---
### ```re.match()```

Пример аналогичен тому, который использовался в функции search, с небольшими изменениями (файл parse_log_match.py):
```python
import re

regex = ('\S+: Host \S+ '
         'in vlan (\d+) '
         'is flapping between port '
         '(\S+) and port (\S+)')

ports = set()

with open('log.txt') as f:
    for line in f:
        match = re.match(regex, line)
        if match:
            vlan = match.group(1)
            ports.add(match.group(2))
            ports.add(match.group(3))

print('Петля между портами {} в VLAN {}'.format(', '.join(ports), vlan))

```

---
### ```re.match()```

Результат:
```
$ python parse_log_match.py
Петля между портами Gi0/19, Gi0/24, Gi0/16 в VLAN 10
```


---
## ```re.finditer()```

---
### ```re.finditer()```

Функция ```finditer()```:
* используется для поиска всех непересекающихся совпадений в шаблоне
* возвращает итератор с объектами Match

Функция finditer отлично подходит для обработки тех команд, вывод которых отображается столбцами.
Например, sh ip int br, sh mac address-table и др.
В этом случае его можно применять ко всему выводу команды.

---
### ```re.finditer()```

Пример вывода sh ip int br:
```python
In [8]: sh_ip_int_br = '''
   ...: R1#show ip interface brief
   ...: Interface             IP-Address      OK? Method Status           Protocol
   ...: FastEthernet0/0       15.0.15.1       YES manual up               up
   ...: FastEthernet0/1       10.0.12.1       YES manual up               up
   ...: FastEthernet0/2       10.0.13.1       YES manual up               up
   ...: FastEthernet0/3       unassigned      YES unset  up               up
   ...: Loopback0             10.1.1.1        YES manual up               up
   ...: Loopback100           100.0.0.1       YES manual up               up
   ...: '''
```

---
### ```re.finditer()```

Регулярное выражение для обработки вывода:
```python
In [9]: result = re.finditer('(\S+) +'
   ...:                      '([\d.]+) +'
   ...:                      '\w+ +\w+ +'
   ...:                      '(up|down|administratively down) +'
   ...:                      '(up|down)',
   ...:                      sh_ip_int_br)
   ...:
```

---
### ```re.finditer()```

В переменной result находится итератор:
```python
In [12]: result
Out[12]: <callable_iterator at 0xb583f46c>
```

---
### ```re.finditer()```

В итераторе находятся объекты Match:
```python
In [16]: groups = []

In [18]: for match in result:
    ...:     print(match)
    ...:     groups.append(match.groups())
    ...:
<_sre.SRE_Match object; span=(103, 171), match='FastEthernet0/0       15.0.15.1       YES manual >
<_sre.SRE_Match object; span=(172, 240), match='FastEthernet0/1       10.0.12.1       YES manual >
<_sre.SRE_Match object; span=(241, 309), match='FastEthernet0/2       10.0.13.1       YES manual >
<_sre.SRE_Match object; span=(379, 447), match='Loopback0             10.1.1.1        YES manual >
<_sre.SRE_Match object; span=(448, 516), match='Loopback100           100.0.0.1       YES manual >
```

---
### ```re.finditer()```

Теперь в списке groups находятся кортежи со строками, которые попали в группы:
```python
In [19]: groups
Out[19]:
[('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
 ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
 ('Loopback0', '10.1.1.1', 'up', 'up'),
 ('Loopback100', '100.0.0.1', 'up', 'up')]

```

---
### ```re.finditer()```

Аналогичный результат можно получить с помощью генератора списков:
```python
In [20]: regex = '(\S+) +([\d.]+) +\w+ +\w+ +(up|down|administratively down) +(up|down)'

In [21]: result = [match.groups() for match in re.finditer(regex, sh_ip_int_br)]

In [22]: result
Out[22]:
[('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
 ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
 ('Loopback0', '10.1.1.1', 'up', 'up'),
 ('Loopback100', '100.0.0.1', 'up', 'up')]

```

---
### ```re.finditer()```

Теперь разберем тот же лог-файл, который использовался в подразделах search и match.

В этом случае вывод можно не перебирать построчно, а передать все содержимое файла (файл parse_log_finditer.py): 
```python
import re

regex = ('Host \S+ '
         'in vlan (\d+) '
         'is flapping between port '
         '(\S+) and port (\S+)')

ports = set()

with open('log.txt') as f:
    for m in re.finditer(regex, f.read()):
        vlan = m.group(1)
        ports.add(m.group(2))
        ports.add(m.group(3))

print('Петля между портами {} в VLAN {}'.format(', '.join(ports), vlan))

```

---
### ```re.finditer()```

> В реальной жизни log-файл может быть очень большим. В таком случае, его лучше обрабатывать построчно. 

Вывод будет таким же:
```
$ python parse_log_finditer.py
Петля между портами Gi0/19, Gi0/24, Gi0/16 в VLAN 10
```

---
### Обработка вывода show cdp neighbors detail

Файл parse_sh_cdp_neighbors_detail_finditer.py:
```python
import re
from pprint import pprint

def parse_cdp(filename):
    regex = ('Device ID: (?P<device>\S+)'
             '|IP address: (?P<ip>\S+)'
             '|Platform: (?P<platform>\S+ \S+),'
             '|Cisco IOS Software, (?P<ios>.+), RELEASE')

    result = {}

    with open('sh_cdp_neighbors_sw1.txt') as f:
        match_iter = re.finditer(regex, f.read())
        for match in match_iter:
            if match.lastgroup == 'device':
                device = match.group(match.lastgroup)
                result[device] = {}
            elif device:
                result[device][match.lastgroup] = match.group(match.lastgroup)
    return result

pprint(parse_cdp('sh_cdp_neighbors_sw1.txt'))
```

---
### Обработка вывода show cdp neighbors detail

Теперь совпадения ищутся во всем файле, а не в каждой строке отдельно:
```python
    with open('sh_cdp_neighbors_sw1.txt') as f:
        match_iter = re.finditer(regex, f.read())
```

Затем перебираются совпадения:
```python
    with open('sh_cdp_neighbors_sw1.txt') as f:
        match_iter = re.finditer(regex, f.read())
        for match in match_iter:

```

---
### Обработка вывода show cdp neighbors detail

Результат будет таким:
```python
$ python parse_sh_cdp_neighbors_detail_finditer.py
{'R1': {'ios': '3800 Software (C3825-ADVENTERPRISEK9-M), Version 12.4(24)T1',
        'ip': '10.1.1.1',
        'platform': 'Cisco 3825'},
 'R2': {'ios': '2900 Software (C3825-ADVENTERPRISEK9-M), Version 15.2(2)T1',
        'ip': '10.2.2.2',
        'platform': 'Cisco 2911'},
 'SW2': {'ios': 'C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9',
         'ip': '10.1.1.2',
         'platform': 'cisco WS-C2960-8TC-L'}}

```

---
### Обработка вывода show cdp neighbors detail

Хотя результат аналогичный, с finditer больше возможностей, так как можно указывать не только то, что должно находиться в нужной строке, но и в строках вокруг.

---
### Обработка вывода show cdp neighbors detail

Например, можно точнее указать, какой именно IP-адрес надо взять:
```
Device ID: SW2
Entry address(es):
  IP address: 10.1.1.2
Platform: cisco WS-C2960-8TC-L,  Capabilities: Switch IGMP

...

Native VLAN: 1
Duplex: full
Management address(es):
  IP address: 10.1.1.2
```

---
### Обработка вывода show cdp neighbors detail

Например, если нужно взять первый IP-адрес, можно так дополнить регулярное выражение:
```python
regex = ('Device ID: (?P<device>\S+)'
         '|Entry address.*\n +IP address: (?P<ip>\S+)'
         '|Platform: (?P<platform>\S+ \S+),'
         '|Cisco IOS Software, (?P<ios>.+), RELEASE')
```



---
## ```re.findall()```


---
### ```re.findall()```

Функция ```findall()```:
* используется для поиска всех непересекающихся совпадений в шаблоне
* возвращает:
  * список строк, которые описаны регулярным выражением, если в регулярном выражении нет групп
  * список строк, которые совпали с регулярным выражением в группе, если в регулярном выражении одна группа
  * список кортежей, в которых находятся строки, которые совпали с выражением в группе, если групп несколько

---
### ```re.findall()```

Рассмотрим работу findall на примере вывода команды sh mac address-table:
```python
In [2]: mac_address_table = open('CAM_table.txt').read()

In [3]: print(mac_address_table)
sw1#sh mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
 100    a1b2.ac10.7000    DYNAMIC     Gi0/1
 200    a0d4.cb20.7000    DYNAMIC     Gi0/2
 300    acb4.cd30.7000    DYNAMIC     Gi0/3
 100    a2bb.ec40.7000    DYNAMIC     Gi0/4
 500    aa4b.c550.7000    DYNAMIC     Gi0/5
 200    a1bb.1c60.7000    DYNAMIC     Gi0/6
 300    aa0b.cc70.7000    DYNAMIC     Gi0/7

```

---
### ```re.findall()```

Первый пример - регулярное выражение без групп.
В этом случае findall возвращает список строк, которые совпали с регулярным выражением.

Например, с помощью findall можно получить список строк с соответствиями vlan - mac - interface и избавиться от заголовка в выводе команды:
```python
In [4]: re.findall('\d+ +\S+ +\w+ +\S+', mac_address_table)
Out[4]:
['100    a1b2.ac10.7000    DYNAMIC     Gi0/1',
 '200    a0d4.cb20.7000    DYNAMIC     Gi0/2',
 '300    acb4.cd30.7000    DYNAMIC     Gi0/3',
 '100    a2bb.ec40.7000    DYNAMIC     Gi0/4',
 '500    aa4b.c550.7000    DYNAMIC     Gi0/5',
 '200    a1bb.1c60.7000    DYNAMIC     Gi0/6',
 '300    aa0b.cc70.7000    DYNAMIC     Gi0/7']
```

---
### ```re.findall()```

Обратите внимание, что findall возвращает список строк, а не объект Match.

Но как только в регулярном выражении появляется группа, findall ведет себя по-другому.

---
### ```re.findall()```

Если в выражении используется одна группа, findall возвращает список строк, которые совпали с выражением в группе:
```python
In [5]: re.findall('\d+ +(\S+) +\w+ +\S+', mac_address_table)
Out[5]:
['a1b2.ac10.7000',
 'a0d4.cb20.7000',
 'acb4.cd30.7000',
 'a2bb.ec40.7000',
 'aa4b.c550.7000',
 'a1bb.1c60.7000',
 'aa0b.cc70.7000']
```

При этом findall ищет совпадение всей строки, но возвращает результат, похожий на метод groups() в объекте Match.

---
### ```re.findall()```

Если же групп несколько, findall вернет список кортежей:
```python
In [6]: re.findall('(\d+) +(\S+) +\w+ +(\S+)', mac_address_table)
Out[6]:
[('100', 'a1b2.ac10.7000', 'Gi0/1'),
 ('200', 'a0d4.cb20.7000', 'Gi0/2'),
 ('300', 'acb4.cd30.7000', 'Gi0/3'),
 ('100', 'a2bb.ec40.7000', 'Gi0/4'),
 ('500', 'aa4b.c550.7000', 'Gi0/5'),
 ('200', 'a1bb.1c60.7000', 'Gi0/6'),
 ('300', 'aa0b.cc70.7000', 'Gi0/7')]

```

Если такие особенности работы функции findall мешают получить необходимый результат, то лучше использовать фукнцию finditer.
Но иногда такое поведение подходит и удобно использовать.

---
### ```re.findall()```


Пример использования findall в разборе лог-файла (файл parse_log_findall.py):
```python
import re

regex = ('Host \S+ '
         'in vlan (\d+) '
         'is flapping between port '
         '(\S+) and port (\S+)')

ports = set()

with open('log.txt') as f:
    result = re.findall(regex, f.read())
    for vlan, port1, port2 in result:
        ports.add(port1)
        ports.add(port2)

print('Петля между портами {} в VLAN {}'.format(', '.join(ports), vlan))
```

---
### ```re.findall()```

Результат:
```
$ python parse_log_findall.py
Петля между портами Gi0/19, Gi0/16, Gi0/24 в VLAN 10

```


---
## ```re.compile()```

---
### ```re.compile()```

В Python есть возможность заранее скомпилировать регулярное выражение, а затем использовать его. Это особенно полезно в тех случаях, когда регулярное выражение много используется в скрипте.

Использование компилированного выражения может ускорить обработку, и, как правило, такой вариант удобней использовать, так как в программе разделяется создание регулярного выражения и его использование.
Кроме того, при использовании функции re.compile создается объект RegexObject, у которого есть несколько дополнительных возможностей, которых нет в объекте MatchObject.

---
### ```re.compile()```

Для компиляции регулярного выражения используется функция re.compile:
```python
In [52]: regex = re.compile('\d+ +\S+ +\w+ +\S+')

```

---
### ```re.compile()```

Она возвращает объект RegexObject:
```python
In [53]: regex
Out[53]: re.compile(r'\d+ +\S+ +\w+ +\S+', re.UNICODE)

```

---
### ```re.compile()```

У объекта RegexObject доступны такие методы и атрибуты:
```python
In [55]: [ method for method in dir(regex) if not method.startswith('_')]
Out[55]:
['findall',
 'finditer',
 'flags',
 'fullmatch',
 'groupindex',
 'groups',
 'match',
 'pattern',
 'scanner',
 'search',
 'split',
 'sub',
 'subn']
```

---
### ```re.compile()```

Обратите внимание, что у объекта Regex доступны методы search, match, finditer, findall. Это те же функции, которые доступны в модуле глобально, но теперь их надо применять к объекту.

Пример использования метода search:
```python
In [67]: line = ' 100    a1b2.ac10.7000    DYNAMIC     Gi0/1'

In [68]: match = regex.search(line)
```

Теперь search надо вызывать как метод объекта regex.
И передать как аргумент строку.

---
### ```re.compile()```

Результатом будет объект Match:
```python
In [69]: match
Out[69]: <_sre.SRE_Match object; span=(1, 43), match='100    a1b2.ac10.7000    DYNAMIC     Gi0/1'>

In [70]: match.group()
Out[70]: '100    a1b2.ac10.7000    DYNAMIC     Gi0/1'

```

---
### ```re.compile()```

Пример компиляции регулярного выражения и его использования на примере разбора лог-файла (файл parse_log_compile.py):
```python
import re

regex = re.compile('Host \S+ '
                   'in vlan (\d+) '
                   'is flapping between port '
                   '(\S+) and port (\S+)')

ports = set()

with open('log.txt') as f:
    for m in regex.finditer(f.read()):
        vlan = m.group(1)
        ports.add(m.group(2))
        ports.add(m.group(3))

print('Петля между портами {} в VLAN {}'.format(', '.join(ports), vlan))

```

---
### ```re.compile()```

Это модифицированный пример с использованием finditer.
Тут изменилось описание регулярного выражения:
```python
regex = re.compile('Host \S+ '
                   'in vlan (\d+) '
                   'is flapping between port '
                   '(\S+) and port (\S+)')
```


И вызов finditer теперь выполняется как метод объекта regex:
```python
    for m in regex.finditer(f.read()):
```

---
### Параметры, которые доступны только при использовании re.compile

При использовании функции re.compile в методах search, match, findall, finditer и fullmatch появляются дополнительные параметры:
* pos - позволяет указывать индекс в строке, с которого надо начать искать совпадение
* endpos - указывает, до какого индекса надо выполнять поиск

Их использование аналогично выполнению среза строки.

---
### Параметры, которые доступны только при использовании re.compile

Например, таким будет результат без указания параметров pos, endpos:
```python
In [75]: regex = re.compile(r'\d+ +\S+ +\w+ +\S+')

In [76]: line = ' 100    a1b2.ac10.7000    DYNAMIC     Gi0/1'

In [77]: match = regex.search(line)

In [78]: match.group()
Out[78]: '100    a1b2.ac10.7000    DYNAMIC     Gi0/1'

```

---
### Параметры, которые доступны только при использовании re.compile

В этом случае указывается начальная позиция поиска:
```
In [79]: match = regex.search(line, 2)

In [80]: match.group()
Out[80]: '00    a1b2.ac10.7000    DYNAMIC     Gi0/1'
```

---
### Параметры, которые доступны только при использовании re.compile

Указание начальной позиции аналогично срезу строки:
```python
In [81]: match = regex.search(line[2:])

In [82]: match.group()
Out[82]: '00    a1b2.ac10.7000    DYNAMIC     Gi0/1'

```

---
### Параметры, которые доступны только при использовании re.compile

И последний пример, с указанием двух индексов:
```python
In [90]: line = ' 100    a1b2.ac10.7000    DYNAMIC     Gi0/1'

In [91]: regex = re.compile(r'\d+ +\S+ +\w+ +\S+')

In [92]: match = regex.search(line, 2, 40)

In [93]: match.group()
Out[93]: '00    a1b2.ac10.7000    DYNAMIC     Gi'

```

---
### Параметры, которые доступны только при использовании re.compile

И аналогичный срез строки:
```python
In [94]: match = regex.search(line[2:40])

In [95]: match.group()
Out[95]: '00    a1b2.ac10.7000    DYNAMIC     Gi'

```

В методах  match, findall, finditer и fullmatch параметры pos и endpos работают аналогично.




---
## Флаги

---
### Флаги

При использовании функций или создании скомпилированного регулярного выражения можно указывать дополнительные флаги, которые влияют на поведение регулярного выражения.

Модуль re поддерживает такие флаги (в скобках короткий вариант обозначения флага):
* re.ASCII (re.A)
* re.IGNORECASE (re.I)
* re.MULTILINE (re.M)
* re.DOTALL (re.S)
* re.VERBOSE (re.X)
* re.LOCALE (re.L)
* re.DEBUG

---
### re.DOTALL

С помощью регулярных выражений можно работать и с многострочной строкой.

Например, из строки table надо получить только строки с соответствиями VLAN-MAC-interface:

```python
In [11]: table = '''
    ...: sw1#sh mac address-table
    ...:           Mac Address Table
    ...: -------------------------------------------
    ...:
    ...: Vlan    Mac Address       Type        Ports
    ...: ----    -----------       --------    -----
    ...:  100    aabb.cc10.7000    DYNAMIC     Gi0/1
    ...:  200    aabb.cc20.7000    DYNAMIC     Gi0/2
    ...:  300    aabb.cc30.7000    DYNAMIC     Gi0/3
    ...:  100    aabb.cc40.7000    DYNAMIC     Gi0/4
    ...:  500    aabb.cc50.7000    DYNAMIC     Gi0/5
    ...:  200    aabb.cc60.7000    DYNAMIC     Gi0/6
    ...:  300    aabb.cc70.7000    DYNAMIC     Gi0/7
    ...: '''
```

---
### re.DOTALL

В этом выражении описана строка с MAC-адресом:

```python
In [12]: m = re.search(' *\d+ +[a-f0-9.]+ +\w+ +\S+', table)
```

В результат попадет первая строка с MAC-адресом:

```python
In [13]: m.group()
Out[13]: ' 100    aabb.cc80.7000    DYNAMIC     Gi0/1'
```

---
### re.DOTALL

Учитывая то, что по умолчанию регулярные выражения жадные, можно получить все соответствия таким образом:

```python
In [14]: m = re.search('( *\d+ +[a-f0-9.]+ +\w+ +\S+\n)+', table)

In [15]: print(m.group())
 100    aabb.cc10.7000    DYNAMIC     Gi0/1
 200    aabb.cc20.7000    DYNAMIC     Gi0/2
 300    aabb.cc30.7000    DYNAMIC     Gi0/3
 100    aabb.cc40.7000    DYNAMIC     Gi0/4
 500    aabb.cc50.7000    DYNAMIC     Gi0/5
 200    aabb.cc60.7000    DYNAMIC     Gi0/6
 300    aabb.cc70.7000    DYNAMIC     Gi0/7
```

---
### re.DOTALL

Тут описана строка с MAC-адресом, перевод строки, и указано, что это выражение должно повторяться, как минимум, один раз.

Получается, что в данном случае надо получить все строки, начиная с первого соответствия VLAN-MAC-интерфейс.

Это можно описать таким образом:

```python
In [16]: m = re.search(' *\d+ +[a-f0-9.]+ +\w+ +\S+.*', table)

In [17]: print(m.group())
 100    aabb.cc10.7000    DYNAMIC     Gi0/1
```

---
### re.DOTALL

Пока что в результате только одна строка, так как по умолчанию точка не включает в себя перевод строки.  
Но, если добавить специальный флаг, re.DOTALL, точка будет включать и перевод строки, и в результат попадут все соответствия:

```python
In [18]: m = re.search(' *\d+ +[a-f0-9.]+ +\w+ +\S+.*', table, re.DOTALL)

In [19]: print(m.group())
 100    aabb.cc10.7000    DYNAMIC     Gi0/1
 200    aabb.cc20.7000    DYNAMIC     Gi0/2
 300    aabb.cc30.7000    DYNAMIC     Gi0/3
 100    aabb.cc40.7000    DYNAMIC     Gi0/4
 500    aabb.cc50.7000    DYNAMIC     Gi0/5
 200    aabb.cc60.7000    DYNAMIC     Gi0/6
 300    aabb.cc70.7000    DYNAMIC     Gi0/7
```

---
## re.split

---
### re.split

Функция split работает аналогично методу split в строках.  
Но в функции re.split можно использовать регулярные выражения, а значит, разделять строку на части по более сложным условиям.

Например, строку ospf\_route надо разбить на элементы по пробелам \(как в методе str.split\):

```python
In [1]: ospf_route = 'O     10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

In [2]: re.split(' +', ospf_route)
Out[2]:
['O',
 '10.0.24.0/24',
 '[110/41]',
 'via',
 '10.0.13.3,',
 '3d18h,',
 'FastEthernet0/0']
```

---
### re.split

Аналогичным образом можно избавиться и от запятых:

```python
In [3]: re.split('[ ,]+', ospf_route)
Out[3]:
['O',
 '10.0.24.0/24',
 '[110/41]',
 'via',
 '10.0.13.3',
 '3d18h',
 'FastEthernet0/0']
```

---
### re.split

И, если нужно, от квадратных скобок:

```python
In [4]: re.split('[ ,\[\]]+', ospf_route)
Out[4]: ['O', '10.0.24.0/24', '110/41', 'via', '10.0.13.3', '3d18h', 'FastEthernet0/0']
```

---
### re.split

У функции split есть особенность работы с группами \(выражения в круглых скобках\).  
Если указать то же выражение с помощью круглых скобок, в итоговый список попадут и разделители.

Например, в выражении как разделитель добавлено слово via:

```python
In [5]: re.split('(via|[ ,\[\]])+', ospf_route)
Out[5]:
['O',
 ' ',
 '10.0.24.0/24',
 '[',
 '110/41',
 ' ',
 '10.0.13.3',
 ' ',
 '3d18h',
 ' ',
 'FastEthernet0/0']
```

---
### re.split

Для отключения такого поведения надо сделать группу noncapture.  
То есть, отключить запоминание элементов группы:

```python
In [6]: re.split('(?:via|[ ,\[\]])+', ospf_route)
Out[6]: ['O', '10.0.24.0/24', '110/41', '10.0.13.3', '3d18h', 'FastEthernet0/0']
```

---
## re.sub

---
### re.sub

Функция re.sub работает аналогично методу replace в строках.  
Но в функции re.sub можно использовать регулярные выражения, а значит, делать замены по более сложным условиям.

Заменим запятые, квадратные скобки и слово via на пробел в строке ospf\_route:

```python
In [7]: ospf_route = 'O    10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

In [8]: re.sub('(via|[,\[\]])', ' ', ospf_route)
Out[8]: 'O        10.0.24.0/24  110/41    10.0.13.3  3d18h  FastEthernet0/0'
```

---
### re.sub

С помощью re.sub можно трансформировать строку.  
Например, преобразовать строку mac\_table таким образом:

```python
In [9]: mac_table = '''
   ...:  100    aabb.cc10.7000    DYNAMIC     Gi0/1
   ...:  200    aabb.cc20.7000    DYNAMIC     Gi0/2
   ...:  300    aabb.cc30.7000    DYNAMIC     Gi0/3
   ...:  100    aabb.cc40.7000    DYNAMIC     Gi0/4
   ...:  500    aabb.cc50.7000    DYNAMIC     Gi0/5
   ...:  200    aabb.cc60.7000    DYNAMIC     Gi0/6
   ...:  300    aabb.cc70.7000    DYNAMIC     Gi0/7
   ...: '''

In [4]: print(re.sub(' *(\d+) +'
   ...:              '([a-f0-9]+)\.'
   ...:              '([a-f0-9]+)\.'
   ...:              '([a-f0-9]+) +\w+ +'
   ...:              '(\S+)',
   ...:              r'\1 \2:\3:\4 \5',
   ...:              mac_table))
   ...:

100 aabb:cc10:7000 Gi0/1
200 aabb:cc20:7000 Gi0/2
300 aabb:cc30:7000 Gi0/3
100 aabb:cc40:7000 Gi0/4
500 aabb:cc50:7000 Gi0/5
200 aabb:cc60:7000 Gi0/6
300 aabb:cc70:7000 Gi0/7
```

---
### re.sub

Регулярное выражение разделено на группы:

* ```(\d+)``` - первая группа. Сюда попадет номер VLAN
* ```([a-f,0-9]+).([a-f,0-9]+).([a-f,0-9]+)``` - три следующие группы (2, 3, 4) описывают MAC-адрес
* ```(\S+)``` - пятая группа. Описывает интерфейс.

---
### re.sub

Во втором регулярном выражении эти группы используются.  
Для того, чтобы сослаться на группу, используется обратный слеш и номер группы.  
Чтобы не пришлось экранировать обратный слеш, используется raw строка.

В итоге вместо номеров групп будут подставлены соответствующие подстроки.  
Для примера, также изменен формат записи MAC-адреса.
