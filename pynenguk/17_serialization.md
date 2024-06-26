# Python для мережевих інженерів 

---

# Серіалізація даних

---
### Серіалізація даних

Серіалізація даних — це зберігання даних у певному форматі.
Найчастіше це збереження даних в якомусь структурованому форматі.

Наприклад, це можуть бути:
* файли у форматі YAML, JSON, XML
* файли у форматі CSV
* база даних

---
### Серіалізація даних

Чим формати YAML, JSON, CSV можуть бути корисними:
* у вас можуть бути дані про IP-адреси та подібна інформація, яку потрібно обробити в таблицях
  * таблицю можна експортувати у формат CSV і обробити за допомогою Python
* програмне забезпечення може повертати дані у форматі JSON. 
* YAML дуже зручно використовувати для опису параметрів
  * наприклад, це можуть бути налаштування для різних об'єктів (IP-адреси, VLAN тощо)

---
## csv

```
"status","network","netmask","nexthop","metric","locprf","weight","path","origin"
"*","1.0.0.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 15169","i"
"*>","1.0.0.0","24","200.219.145.23",NA,NA,0,"53242 7738 15169","i"
"*","1.0.4.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 1299 7545 56203","i"
"*>","1.0.4.0","24","200.219.145.23",NA,NA,0,"53242 12956 174 7545 56203","i"
"*","1.0.5.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 1299 7545 56203","i"
"*>","1.0.5.0","24","200.219.145.23",NA,NA,0,"53242 12956 174 7545 56203","i"
"*","1.0.6.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 2828 4826 38803 56203","i"
"*>","1.0.6.0","24","200.219.145.23",NA,NA,0,"53242 7738 6939 4826 38803 56203","i"
"*","1.0.7.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 2828 4826 38803 56203","i"
"*>","1.0.7.0","24","200.219.145.23",NA,NA,0,"53242 7738 6939 4826 38803 56203","i"
"*","1.0.11.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 10026 18046","i"
"*>","1.0.11.0","24","200.219.145.23",NA,NA,0,"53242 12956 174 10026 18046","i"
"*","1.0.12.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 10026 18046","i"
"*>","1.0.12.0","24","200.219.145.23",NA,NA,0,"53242 12956 174 10026 18046","i"
"*","1.0.13.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 10026 18046","i"
"*>","1.0.13.0","24","200.219.145.23",NA,NA,0,"53242 12956 174 10026 18046","i"
"*","1.0.20.0","23","200.219.145.45",NA,NA,0,"28135 18881 3549 6762 10026 2519","i"
"*>","1.0.20.0","23","200.219.145.23",NA,NA,0,"53242 12956 2516 2519","i"
"*","1.0.22.0","23","200.219.145.45",NA,NA,0,"28135 18881 3549 6762 10026 2519","i"
"*>","1.0.22.0","23","200.219.145.23",NA,NA,0,"53242 12956 2516 2519","i"
"*","1.0.24.0","23","200.219.145.45",NA,NA,0,"28135 18881 3549 6762 10026 2519","i"
"*>","1.0.24.0","23","200.219.145.23",NA,NA,0,"53242 12956 2516 2519","i"
"*","1.0.26.0","23","200.219.145.45",NA,NA,0,"28135 18881 3549 6762 10026 2519","i"
"*>","1.0.26.0","23","200.219.145.23",NA,NA,0,"53242 12956 2516 2519","i"
"*","1.0.28.0","22","200.219.145.45",NA,NA,0,"28135 18881 3549 6762 10026 2519","i"
"*>","1.0.28.0","22","200.219.145.23",NA,NA,0,"53242 12956 2516 2519","i"
```
---
## yaml

```yaml
---

- name: Run cfg commands on routers
  hosts: cisco-routers
  gather_facts: false
  connection: local

  tasks:

    - name: Config line vty
      ios_config:
        parents:
          - line vty 0 4
        lines:
          - login local
          - transport input ssh
        provider: "{{ cli }}"
      notify: save config

    - name: Send config commands
      ios_config:
        lines:
          - service password-encryption
          - no ip http server
          - no ip http secure-server
          - no ip domain lookup
        provider: "{{ cli }}"
      notify: save config
```

---
## json

```json
{
     "login": "pyneng",
     "id": 28531730,
     "node_id": "MDQ6VXNlcjI4NTMxNzMw",
     "avatar_url": "https://avatars.githubusercontent.com/u/28531730?v=4",
     "gravatar_id": "",
     "url": "https://api.github.com/users/pyneng",
     "html_url": "https://github.com/pyneng",
     "followers_url": "https://api.github.com/users/pyneng/followers",
     "following_url": "https://api.github.com/users/pyneng/following{/other_user}",
     "gists_url": "https://api.github.com/users/pyneng/gists{/gist_id}",
     "starred_url": "https://api.github.com/users/pyneng/starred{/owner}{/repo}",
     "subscriptions_url": "https://api.github.com/users/pyneng/subscriptions",
     "organizations_url": "https://api.github.com/users/pyneng/orgs",
     "repos_url": "https://api.github.com/users/pyneng/repos",
     "events_url": "https://api.github.com/users/pyneng/events{/privacy}",
     "received_events_url": "https://api.github.com/users/pyneng/received_events",
     "type": "User",
     "site_admin": false,
     "name": "Наташа Самойленко",
     "company": null,
     "blog": "https://pyneng.github.io/",
     "location": null,
     "email": null,
     "hireable": null,
     "bio": null,
     "twitter_username": "natenka_says",
     "public_repos": 32,
     "public_gists": 0,
     "followers": 194,
     "following": 12,
     "created_at": "2017-05-08T11:02:10Z",
     "updated_at": "2021-07-19T12:20:57Z"
}
```
---

## Робота з файлами CSV

---

### Робота з файлами CSV

__CSV (comma-separated value)__ - це формат представлення табличних даних (наприклад, це можуть бути дані з таблиці або дані з бази даних).

У цьому форматі кожен рядок файлу є рядком таблиці.
Незважаючи на назву формату, роздільником може бути не тільки кома.

Формати з іншим роздільником можуть мати власну назву, наприклад, TSV (tab separated values), однак назва  CSV зазвичай означає будь-які роздільники.

---

### Робота з файлами CSV

Приклад файлу CSV (sw_data.csv):
```
hostname,vendor,model,location
sw1,Cisco,3750,London
sw2,Cisco,3850,Liverpool
sw3,Cisco,3650,Liverpool
sw4,Cisco,3650,London
```

У стандартній бібліотеці Python є модуль csv, який дозволяє працювати з файлами у форматі CSV.

---

### Читання файлів CSV

Приклад використання модуля csv (файл csv_read.py):
```python
import csv

with open('sw_data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

Результат буде таким:
```
$ python csv_read.py
['hostname', 'vendor', 'model', 'location']
['sw1', 'Cisco', '3750', 'London']
['sw2', 'Cisco', '3850', 'Liverpool']
['sw3', 'Cisco', '3650', 'Liverpool']
['sw4', 'Cisco', '3650', 'London']
```

---

### Читання файлів CSV

```python
In [1]: import csv

In [2]: with open('sw_data.csv') as f:
   ...:     reader = csv.reader(f)
   ...:     print reader
   ...:
<_csv.reader object at 0x10385b050>
```

---

### Читання файлів CSV

Заголовки стовпців зручніше отримати окремим об'єктом (файл csv_read_headers.py):
```py
import csv

with open('sw_data.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)
    print(f'Headers: {headers}')
    for row in reader:
        print(row)
```


---

### Читання файлів CSV

DictReader дозволяє отримувати словники, в яких ключами є імена стовпців, а значеннями є значення стовпців (файл csv_read_dict.py):
```python
import csv

with open('sw_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(row['hostname'], row['model'])

```

---

### Читання файлів CSV

Результат буде таким:
```
$ python csv_read_dict.py
{'hostname': 'sw1', 'vendor': 'Cisco', 'model': '3750', 'location': 'London'}
sw1 3750
{'hostname': 'sw2', 'vendor': 'Cisco', 'model': '3850', 'location': 'Liverpool'}
sw2 3850
{'hostname': 'sw3', 'vendor': 'Cisco', 'model': '3650', 'location': 'Liverpool'}
sw3 3650
{'hostname': 'sw4', 'vendor': 'Cisco', 'model': '3650', 'location': 'London'}
sw4 3650
```

---

### Запис файлів у форматі CSV

Використовуючи модуль csv, можна записати файл у форматі CSV (файл csv_write.py):

```python
import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]

with open('sw_data_new.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
```

---

### Запис файлів у форматі CSV

Файл sw_data_new.csv буде таким:
```
hostname,vendor,model,location
sw1,Cisco,3750,"London, Best str"
sw2,Cisco,3850,"Liverpool, Better str"
sw3,Cisco,3650,"Liverpool, Better str"
sw4,Cisco,3650,"London, Best str"
```

Зверніть увагу: останнє значення взято в лапки, а решта рядків – ні.

---

### Запис файлів у форматі CSV

Для того щоб усі рядки були записані у файл csv із лапками, потрібно змінити скрипт таким чином (файл csv_write_quoting.py):


```python
import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]

with open('sw_data_new.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        writer.writerow(row)
```

---

### Запис файлів у форматі CSV

Тепер всі значення взяті в лапки. І, оскільки номер моделі вказано у вигляді рядка в оригінальному списку, він також узятий у лапки.
```
"hostname","vendor","model","location"
"sw1","Cisco","3750","London, Best str"
"sw2","Cisco","3850","Liverpool, Better str"
"sw3","Cisco","3650","Liverpool, Better str"
"sw4","Cisco","3650","London, Best str"
```

---

### Запис файлів у форматі CSV

Крім методу writerow, підтримується метод writerows (файл csv_writerows.py):

```python
import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]

with open('sw_data_new.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(data)
```

---
### DictWriter

За допомогою DictWriter можна записати словники у форматі csv.

Загалом DictWriter працює так само, як writer,
але необхідно додатково вказати, у якому порядку стовпці відображатимуться у файлі.
Для цього використовується параметр fieldnames.


---
### DictWriter

Файл csv_write_dict.py:
```python
import csv

data = [{'hostname': 'sw1',
         'location': 'London',
         'model': '3750',
         'vendor': 'Cisco'},
        {'hostname': 'sw2',
         'location': 'Liverpool',
         'model': '3850',
         'vendor': 'Cisco'},
        {'hostname': 'sw3',
         'location': 'Liverpool',
         'model': '3650',
         'vendor': 'Cisco'},
        {'hostname': 'sw4',
         'location': 'London',
         'model': '3650',
         'vendor': 'Cisco'}]

with open('csv_write_dictwriter.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=list(data[0].keys()),
                            quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for d in data:
        writer.writerow(d)
```

---

### Використання іншого роздільника

Наприклад, якщо файл використовує роздільник ```;``` (файл sw_data2.csv):
```
hostname;vendor;model;location
sw1;Cisco;3750;London
sw2;Cisco;3850;Liverpool
sw3;Cisco;3650;Liverpool
sw4;Cisco;3650;London
```

Треба вказати роздільник в reader (файл csv_read_delimiter.py):
```python
import csv

with open('sw_data2.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)
```


---

### Робота з файлами JSON

---

### Робота з файлами JSON

__JSON (JavaScript Object Notation)__ - це текстовий формат для зберігання та обміну даними.


Синтаксис [JSON](https://en.wikipedia.org/wiki/JSON) дуже схожий на деякі типи даних в Python і, хоча назви елементів відрізняються, ця схожість допомогає зрозуміти структуру об'єктів JSON.

Як і з CSV, в стандартній бібліотеці Python є модуль, який дозволяє записувати та читати дані у форматі JSON.


---

### Читання

Файл sw_templates.json:
```json
{
  "access": [
    "switchport mode access", 
    "switchport access vlan", 
    "switchport nonegotiate", 
    "spanning-tree portfast", 
    "spanning-tree bpduguard enable"
  ], 
  "trunk": [
    "switchport trunk encapsulation dot1q", 
    "switchport mode trunk", 
    "switchport trunk native vlan 999", 
    "switchport trunk allowed vlan"
  ]
}
```

---

### Читання. json.load()

Читання файлу JSON в об’єкт Python (файл json_read_load.py):
```python
import json
from pprint import pprint


with open('sw_templates.json') as f:
    templates = json.load(f)

pprint(templates)
```

---

### Читання. json.load()

Результат буде таким:
```python
$ python json_read_load.py
{'access': ['switchport mode access',
            'switchport access vlan',
            'switchport nonegotiate',
            'spanning-tree portfast',
            'spanning-tree bpduguard enable'],
 'trunk': ['switchport trunk encapsulation dot1q',
           'switchport mode trunk',
           'switchport trunk native vlan 999',
           'switchport trunk allowed vlan']}
```

---

### Читання. json.loads()

Читання рядка в форматі JSON в об’єкт Python (файл json_read_loads.py):
```python
import json

with open('sw_templates.json') as f:
    file_content = f.read()
    templates = json.loads(file_content)

print(templates)

for section, commands in templates.items():
    print(section)
    print('\n'.join(commands))

```


---
### Запис. json.dumps()

Перетворення об’єкта на рядок JSON (json_write_dumps.py):
```python
import json


trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk native vlan 999',
                  'switchport trunk allowed vlan']

access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

to_json = {'trunk': trunk_template, 'access': access_template}

with open('sw_templates.json', 'w') as f:
    f.write(json.dumps(to_json))

with open('sw_templates.json') as f:
    print(f.read())

```

---
### Запис. json.dump()

Запис об’єкта Python у файл у форматі JSON (файл json_write_dump.py):
```python
import json


trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk native vlan 999',
                  'switchport trunk allowed vlan']

access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

to_json = {'trunk': trunk_template, 'access': access_template}

with open('sw_templates.json', 'w') as f:
    json.dump(to_json, f)

with open('sw_templates.json') as f:
    print(f.read())

```

---
### Запис

Більш читабельний вивід (файл json_write_indent.py):
```python
import json


trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk native vlan 999',
                  'switchport trunk allowed vlan']

access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

to_json = {'trunk':trunk_template, 'access':access_template}

with open('sw_templates.json', 'w') as f:
    json.dump(to_json, f, sort_keys=True, indent=2)

with open('sw_templates.json') as f:
    print(f.read())
``` 


---
### Зміна типу даних

Під час роботи з форматом JSON дані не завжди будуть того самого типу, що й вихідні дані в Python.

Наприклад, кортежі, записані в JSON, перетворюються на списки:
```python

In [1]: import json

In [2]: trunk_template = ('switchport trunk encapsulation dot1q',
   ...:                   'switchport mode trunk',
   ...:                   'switchport trunk native vlan 999',
   ...:                   'switchport trunk allowed vlan')

In [3]: print type(trunk_template)
<type 'tuple'>

In [4]: with open('trunk_template.json', 'w') as f:
   ...:     json.dump(trunk_template, f, sort_keys=True, indent=2)
   ...:
```

---
### Зміна типу даних

```python

In [5]: cat trunk_template.json
[
  "switchport trunk encapsulation dot1q",
  "switchport mode trunk",
  "switchport trunk native vlan 999",
  "switchport trunk allowed vlan"
]
In [6]: templates = json.load(open('trunk_template.json'))

In [7]: type(templates)
Out[7]: list

In [8]: print(templates)
['switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk native vlan 999', 'switchport trunk allowed vlan']
```

---
### Конвертація даних Python у JSON

|  Python     | JSON  |
|:-----------:|:-----:|
|  dict       | object|
| list, tuple | array |
| str         | string|
| int, float  | number|
| True        | true  |
| False       | false |
| None        | null  |

---
### Конвертація JSON у дані Python

| JSON  |  Python |
|:-----:|:-------:|
| object| dict
| array | list
| string| str
| number (int) | int
| number (real)| float
| true  | True
| false | False
| null  | None



---
### Ключі словника

У формат JSON не можна записати словник, у якого ключі - кортежі:
```python
In [9]: to_json = {('trunk', 'cisco'): trunk_template, 'access': access_template}

In [10]: with open('sw_templates.json', 'w') as f:
    ...:     json.dump(to_json, f)
    ...:
...
TypeError: key ('trunk', 'cisco') is not a string
```

---
### Ключі словника

Спеціальний параметр дозволяє ігнорувати такі ключі:
```python
In [11]: with open('sw_templates.json', 'w') as f:
    ...:     json.dump(to_json, f, skipkeys=True)
    ...:
    ...:

In [12]: cat sw_templates.json
{"access": ["switchport mode access", "switchport access vlan", "switchport nonegotiate",
"spanning-tree portfast", "spanning-tree bpduguard enable"]}
```

---

### Робота з файлами YAML

---

### Робота з файлами YAML

__YAML (YAML Ain't Markup Language)__ - ще один текстовий формат для запису даних.

YAML більш читабельний, ніж JSON, тому його часто використовують для опису сценаріїв у програмному забезпеченні.
Наприклад, в Ansible.

---

### Синтаксис YAML

---
### Синтаксис YAML

Як і Python, YAML використовує відступи для позначення структури документа.
Але в YAML можна використовувати лише пробіли та не можна використовувати табуляції.

---

#### Список

Список можна записати в один рядок:
```yaml
[switchport mode access, switchport access vlan, switchport nonegotiate, spanning-tree portfast, spanning-tree bpduguard enable]
```

Або кожен елемент списку в окремому рядку:
```yaml
- switchport mode access
- switchport access vlan
- switchport nonegotiate
- spanning-tree portfast
- spanning-tree bpduguard enable
```

Коли список записується в такому блоці, кожен рядок повинен починатися з ```- ``` (знак мінус і пробіл). І всі рядки в списку повинні мати однаковий рівень відступу.

---

#### Словник

Словник також можна записати в один рядок:
```yaml
{ vlan: 100, name: IT }
```

Або блоком:
```yaml
vlan: 100
name: IT
```
---

#### Рядки

Рядки в YAML не потрібно брати в лапки.
Це зручно, але іноді все ж потрібно використовувати лапки.
Наприклад, коли в рядку використовується якийсь спеціальний символ (спеціальний для YAML).

Такий рядок, наприклад, потрібно взяти в лапки, щоб YAML правильно інтерпретував його:
```yaml
command: "sh interface | include Queueing strategy:"
```
---

#### Комбінація елементів

Словник, що містить два ключі: access та trunk.
Значення, які відповідають цим ключам, є списками команд:
```yaml
access:
- switchport mode access
- switchport access vlan
- switchport nonegotiate
- spanning-tree portfast
- spanning-tree bpduguard enable

trunk:
- switchport trunk encapsulation dot1q
- switchport mode trunk
- switchport trunk native vlan 999
- switchport trunk allowed vlan
```

---

#### Комбінація елементів

Список словників:
```yaml
- BS: 1550
  IT: 791
  id: 11
  name: Liverpool
  to_id: 1
  to_name: LONDON
- BS: 1510
  IT: 793
  id: 12
  name: Bristol
  to_id: 1
  to_name: LONDON
- BS: 1650
  IT: 892
  id: 14
  name: Coventry
  to_id: 2
  to_name: Manchester
```

---

### Модуль PyYAML

---

### Модуль PyYAML

Для роботи з YAML в Python використовується модуль PyYAML.
Він не входить до стандартної бібліотеки модулів, тому його потрібно встановити:

```
pip install pyyaml
```

---

#### Читання з YAML

Файл info.yaml:
```yaml
- BS: 1550
  IT: 791
  id: 11
  name: Liverpool
  to_id: 1
  to_name: LONDON
- BS: 1510
  IT: 793
  id: 12
  name: Bristol
  to_id: 1
  to_name: LONDON
- BS: 1650
  IT: 892
  id: 14
  name: Coventry
  to_id: 2
  to_name: Manchester
```

---

#### Читання з YAML

Читання з YAML (файл yaml_read.py):
```python
import yaml
from pprint import pprint

with open('info.yaml') as f:
    templates = yaml.load(f)

pprint(templates)

```

---

#### Читання з YAML

Результат:
```python
$ python yaml_read.py
[{'BS': 1550,
  'IT': 791,
  'id': 11,
  'name': 'Liverpool',
  'to_id': 1,
  'to_name': 'LONDON'},
 {'BS': 1510,
  'IT': 793,
  'id': 12,
  'name': 'Bristol',
  'to_id': 1,
  'to_name': 'LONDON'},
 {'BS': 1650,
  'IT': 892,
  'id': 14,
  'name': 'Coventry',
  'to_id': 2,
  'to_name': 'Manchester'}]

```


---

#### Запис в YAML

Запис об’єктів Python у YAML (файл yaml_write.py):
```python
import yaml

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk native vlan 999',
                  'switchport trunk allowed vlan']

access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

to_yaml = {'trunk': trunk_template, 'access': access_template}

with open('sw_templates.yaml', 'w') as f:
    yaml.dump(to_yaml, f)

with open('sw_templates.yaml') as f:
    print(f.read())

```

---

#### Запис в YAML

Файл sw_templates.yaml виглядає так:
```yaml
access: [switchport mode access, switchport access vlan, switchport nonegotiate, spanning-tree
    portfast, spanning-tree bpduguard enable]
trunk: [switchport trunk encapsulation dot1q, switchport mode trunk, switchport trunk
    native vlan 999, switchport trunk allowed vlan]
```

---

#### Запис в YAML

Параметр ```default_flow_style=False``` (файл yaml_write_default_flow_style.py):
```python
import yaml

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk native vlan 999',
                  'switchport trunk allowed vlan']

access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

to_yaml = {'trunk': trunk_template, 'access': access_template}

with open('sw_templates.yaml', 'w') as f:
    yaml.dump(to_yaml, f, default_flow_style=False)

with open('sw_templates.yaml') as f:
    print f.read()
```

---

#### Запис в YAML

Тепер вміст файлу sw_templates.yaml виглядає так:
```yaml
access:
- switchport mode access
- switchport access vlan
- switchport nonegotiate
- spanning-tree portfast
- spanning-tree bpduguard enable
trunk:
- switchport trunk encapsulation dot1q
- switchport mode trunk
- switchport trunk native vlan 999
- switchport trunk allowed vlan
```

