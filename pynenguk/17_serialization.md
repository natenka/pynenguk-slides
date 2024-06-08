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

__YAML (YAML Ain't Markup Language)__ - еще один текстовый формат для записи данных.

YAML более приятен для восприятия человеком, чем JSON, поэтому его часто используют для описания сценариев в ПО.
Например, в Ansible.

---

### Синтаксис YAML

---
### Синтаксис YAML

Как и Python, YAML использует отступы для указания структуры документа.
Но в YAML можно использовать только пробелы и нельзя использовать знаки табуляции.

Еще одна схожесть с Python: комментарии начинаются с символа # и продолжаются до конца строки.

---

#### Список

Список может быть записан в одну строку:
```yaml
[switchport mode access, switchport access vlan, switchport nonegotiate, spanning-tree portfast, spanning-tree bpduguard enable]
```

Или каждый элемент списка в своей строке:
```yaml
- switchport mode access
- switchport access vlan
- switchport nonegotiate
- spanning-tree portfast
- spanning-tree bpduguard enable
```

Когда список записан таким блоком, каждая строка должна начинаться с ```- ``` (минуса и пробела). И все строки в списке должны быть на одном уровне отступа.

---

#### Словарь

Словарь также может быть записан в одну строку:
```yaml
{ vlan: 100, name: IT }
```

Или блоком:
```yaml
vlan: 100
name: IT
```
---

#### Строки

Строки в YAML не обязательно брать в кавычки.
Это удобно, но иногда всё же следует использовать кавычки.
Например, когда в строке используется какой-то специальный символ (специальный для YAML).

Такую строку, например, нужно взять в кавычки, чтобы она была корректно воспринята YAML:
```yaml
command: "sh interface | include Queueing strategy:"
```
---

#### Комбинация элементов

Словарь, в котором есть два ключа: access и trunk.
Значения, которые соответствуют этим ключам - списки команд:
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

#### Комбинация элементов

Список словарей:
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
Для работы с YAML в Python используется модуль PyYAML.
Он не входит в стандартную библиотеку модулей, поэтому его нужно установить:
```
pip install pyyaml
```

Работа с ним аналогична модулям csv и json.

---

#### Читання из YAML

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

#### Читання из YAML

Чтение из YAML (файл yaml_read.py):
```python
import yaml
import pprint

with open('info.yaml') as f:
    templates = yaml.load(f)

pprint.pprint(templates)

```

---

#### Читання из YAML
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

Запись объектов Python в YAML (файл yaml_write.py):
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

to_yaml = {'trunk':trunk_template, 'access':access_template}

with open('sw_templates.yaml', 'w') as f:
    yaml.dump(to_yaml, f)

with open('sw_templates.yaml') as f:
    print(f.read())

```

---

#### Запис в YAML

Файл sw_templates.yaml выглядит таким образом:
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

to_yaml = {'trunk':trunk_template, 'access':access_template}

with open('sw_templates.yaml', 'w') as f:
    yaml.dump(to_yaml, f, default_flow_style=False)

with open('sw_templates.yaml') as f:
    print f.read()
```

---

#### Запис в YAML

Теперь содержимое файла sw_templates.yaml выглядит таким образом:
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

