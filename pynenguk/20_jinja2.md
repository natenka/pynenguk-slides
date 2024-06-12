# Python для мережевих інженерів 

---

# Шаблони конфігурації з Jinja

---

### Шаблони конфігурації з Jinja

Jinja2 це мова шаблонів, що використовується в Python.

Jinja2 використовується для генерації тексту на основі одного або кількох шаблонів.

Приклади використання:
* шаблони для створення HTML-сторінок
* шаблони для створення файлів конфігурації в Unix/Linux
* шаблони для генерації конфігураційних файлів мережевих пристроїв


Ви можете встановити Jinja2 за допомогою pip:
```python
pip install jinja2
```

---

### Шаблони конфігурації з Jinja

Jinja дозволяє розділити дані та шаблон.
Це дозволяє використовувати той самий шаблон, але замінювати в ньому різні дані.

У найпростішому випадку шаблон - це текстовий файл, в якому вказані місця підстановки значень, за допомогою змінних Jinja.

---

### Шаблони конфігурації з Jinja

Приклад шаблону Jinja:
```jinja
hostname {{name}}
!
interface Loopback255
 description Management loopback
 ip address 10.255.{{id}}.1 255.255.255.255
!
interface GigabitEthernet0/0
 description LAN to {{name}} sw1 {{int}}
 ip address {{ip}} 255.255.255.0
!
router ospf 10
 router-id 10.255.{{id}}.1
 auto-cost reference-bandwidth 10000
 network 10.0.0.0 0.255.255.255 area 0
```

---

### Шаблони конфігурації з Jinja

Приклад шаблону Jinja:
```jinja
hostname {{ name }}

interface Loopback0
 ip address 10.0.0.{{ id }} 255.255.255.255

{% for vlan, name in vlans.items() %}
vlan {{ vlan }}
 name {{ name }}
{% endfor %}

{% if ospf %}
router ospf 1
 router-id 10.0.0.{{ id }}
 auto-cost reference-bandwidth 10000
 {% for networks in ospf %}
 network {{ networks.network }} area {{ networks.area }}
 {% endfor %}
{% endif %}

```
---

## Приклад використання Jinja


---

Шаблон templates/router_template.txt — це звичайний текстовий файл:
```
hostname {{name}}
!
interface Loopback255
 description Management loopback
 ip address 10.255.{{id}}.1 255.255.255.255
!
interface GigabitEthernet0/0
 description LAN to {{name}} sw1 {{int}}
 ip address {{ip}} 255.255.255.0
!
router ospf {{ process_id | default(100) }}
 router-id 10.255.{{id}}.1
 auto-cost reference-bandwidth 10000
 network 10.0.0.0 0.255.255.255 area 0
```

---

Файл даних routers_info.yml
```
- id: '11'
  int: Gi1/0/1
  ip: 10.1.1.1
  name: Liverpool
- id: '21'
  int: Gi1/0/2
  ip: 10.2.2.1
  name: London
- int: Gi1/0/3
  ip: 10.3.3.1
  name: Coventry
  process_id: 1
```

---

Скрипт для генерації конфігурацій router_config_generator_ver2.py
```python
from jinja2 import Environment, FileSystemLoader, StrictUndefined
import yaml


env = Environment(
    loader=FileSystemLoader("~/path/to/templates"),
    undefined=StrictUndefined
)
templ = env.get_template("cfg_template.txt")

with open("cfg_data.yaml") as f:
    data = yaml.safe_load(f)

for param in data:
    print(templ.render(param))
```


---
### Jinja2 API

FileSystemLoader

```
loader = FileSystemLoader("templates")
loader = FileSystemLoader(["/override/templates", "/default/templates"])
```

---

## Синтаксис шаблонів Jinja2

---

## Синтаксис шаблонів Jinja2

Поки що приклади шаблонів Jinja2 використовували лише заміну змінних.
Це найпростіший і найзрозуміліший приклад використання шаблонів, але синтаксис шаблону Jinja цим не обмежується.

---

## Синтаксис шаблонів Jinja2

У шаблонах Jinja2 можна використовувати:
* змінні
* умови (if/else)
* цикл (for)
* фільтри — це спеціальні вбудовані методи, які дозволяють трансформувати змінні
* тести - використовуються для перевірки, чи відповідає змінна певній умові

Крім того, Jinja підтримує успадкування між шаблонами.
Це також дозволяє додавати вміст одного шаблону до іншого.

---

## Синтаксис шаблонів Jinja2

Скрипт cfg_gen.py буде використовуватися для створення шаблонів
```python
# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import yaml
import sys

TEMPLATE_DIR, template = sys.argv[1].split('/')
VARS_FILE = sys.argv[2]

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR),
                  trim_blocks=True, lstrip_blocks=True)
template = env.get_template(template)

vars_dict = yaml.load(open(VARS_FILE))

print(template.render(vars_dict))
```

---

## Синтаксис шаблонів Jinja2

```
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), trim_blocks=True)
```

Параметр ```trim_blocks=True``` - видаляє перший порожній рядок після  блоку, якщо встановлено значення True (за замовчуванням False).

Ви також можете додати параметр ```lstrip_blocks=True``` - якщо встановлено значення True, пробіли та табуляції на початку рядка видаляються (за замовчуванням False).

---

## Синтаксис шаблонів Jinja2

Щоб переглянути результат, потрібно викликати скрипт і передати йому два аргументи:
* шаблон
* файл зі змінними у форматі YAML

Результат буде виведено на стандартний потік виведення.

---

## Синтаксис шаблонів Jinja2

Приклад запуску скрипту:
```
$ python cfg_gen.py templates/variables.txt data_files/vars.yml
```

---

## Контроль символів whitespace

---

### trim_blocks


Параметр ```trim_blocks``` видаляє перший порожній рядок після блоку Jinja, якщо його значення True (за замовчуванням False).

Приклад шаблону templates/env_flags.txt:
```
router bgp {{ bgp.local_as }}
 {% for ibgp in bgp.ibgp_neighbors %}
 neighbor {{ ibgp }} remote-as {{ bgp.local_as }}
 neighbor {{ ibgp }} update-source {{ bgp.loopback }}
 {% endfor %}
```

---

### trim_blocks

Якщо скрипт cfg_gen.py виконується без позначок trim_blocks, lstrip_blocks:
```
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
```

Результат буде таким:
```
$ python cfg_gen.py templates/env_flags.txt data_files/router.yml
router bgp 100

 neighbor 10.0.0.2 remote-as 100
 neighbor 10.0.0.2 update-source lo100

 neighbor 10.0.0.3 remote-as 100
 neighbor 10.0.0.3 update-source lo100
```

---

### trim_blocks

При додаванні прапора trim_blocks таким чином:
```python
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), trim_blocks=True)
```

Результат виконання буде таким:
```
$ python cfg_gen.py templates/env_flags.txt data_files/router.yml
router bgp 100
  neighbor 10.0.0.2 remote-as 100
 neighbor 10.0.0.2 update-source lo100
  neighbor 10.0.0.3 remote-as 100
 neighbor 10.0.0.3 update-source lo100

```

---

### lstrip_blocks

Перед рядками ```neighbor ... remote-as`` з'явилися два пробіли.
Це сталося тому, що перед ```{% for ibgp in bgp.ibgp_neighbors %}``` є пробіл.
Після вимкнення додаткового переходу рядка пробіли та табуляції перед блоком додаються до першого рядка блоку.

Але це не впливає на наступні рядки.
Таким чином, рядки з ```neighbor ... update-source``` відображаються через один пробіл.

---

### lstrip_blocks

Параметр ```lstrip_blocks``` контролює, чи видаляються пробіли та символи табуляції від початку рядка до початку блоку (перед відкриваючою фігурною дужкою).

Якщо додати аргумент ```lstrip_blocks=True``` таким чином:
```
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR),
                  trim_blocks=True, lstrip_blocks=True)
```

Результат виконання буде таким:
```
$ python cfg_gen.py templates/env_flags.txt data_files/router.yml
router bgp 100
 neighbor 10.0.0.2 remote-as 100
 neighbor 10.0.0.2 update-source lo100
 neighbor 10.0.0.3 remote-as 100
 neighbor 10.0.0.3 update-source lo100
```


---
## Змінні

---
### Змінні

Змінні в шаблоні вказані в подвійних фігурних дужках:
```
hostname {{ name }}

interface Loopback0
 ip address 10.0.0.{{ id }} 255.255.255.255
```

---
### Змінні

Значення змінних підставляються на основі словника, який передається в шаблон.

Змінна, яка передається в словник, може бути не тільки числом або рядком, але також, наприклад, списком або словником.
Всередині шаблону можна, відповідно, отримати доступ до елемента за номером або ключем.

---
### Змінні

Приклад templates/variables.txt із використанням різних варіантів змінних:
```
hostname {{ name }}

interface Loopback0
 ip address 10.0.0.{{ id }} 255.255.255.255

vlan {{ vlans[0] }}

router ospf 1
 router-id 10.0.0.{{ id }}
 auto-cost reference-bandwidth 10000
 network {{ ospf.network }} area {{ ospf['area'] }}
```

---
### Змінні

І відповідний файл data_files/vars.yml зі змінними:
```
id: 3
name: R3
vlans:
  - 10
  - 20
  - 30
ospf:
  network: 10.0.1.0 0.0.0.255
  area: 0
```

---
### Змінні

Обратите внимание на использование переменной vlans в шаблоне:
* так как переменная vlans это список, можно указывать какой именно элемент из списка нам нужен

Если передается словарь (как в случае с переменной ospf), то внутри шаблона можно обращаться к объектам словаря, используя один из вариантов:
* ospf.network или ospf['network']

Зверніть увагу на використання змінної vlans у шаблоні: оскільки змінна vlan є списком, можна вказати, який елемент зі списку потрібен.

Якщо передано словник (як у випадку зі змінною ospf), то в межах шаблону можна отримати доступ до значень словника за допомогою одного з варіантів:

```python
ospf.network
ospf['network']
```

---
### Змінні

Результат виконання скрипта буде таким:
```
$ python cfg_gen.py templates/variables.txt data_files/vars.yml
hostname R3

interface Loopback0
 ip address 10.0.0.3 255.255.255.255

vlan 10

router ospf 1
 router-id 10.0.0.3
 auto-cost reference-bandwidth 10000
 network 10.0.1.0 0.0.0.255 area 0
```

---
## Цикл for

---
### Цикл for

Цикл for дозволяє вам перебирати елементи послідовності.

Цикл for має бути всередині символів ```{% %}```.
Крім того, потрібно явно вказати кінець циклу:
```
{% for vlan in vlans %}
  vlan {{ vlan }}
{% endfor %}
```

---
### Цикл for

Приклад шаблону templates/for.txt з використанням циклу:
```
hostname {{ name }}

interface Loopback0
 ip address 10.0.0.{{ id }} 255.255.255.255

{% for vlan, name in vlans.items() %}
vlan {{ vlan }}
 name {{ name }}
{% endfor %}

router ospf 1
 router-id 10.0.0.{{ id }}
 auto-cost reference-bandwidth 10000
 {% for networks in ospf %}
 network {{ networks.network }} area {{ networks.area }}
 {% endfor %}
```

---
### Цикл for

Файл data_files/for.yml зі змінними:
```yml
id: 3
name: R3
vlans:
  10: Marketing
  20: Voice
  30: Management
ospf:
  - network: 10.0.1.0 0.0.0.255
    area: 0
  - network: 10.0.2.0 0.0.0.255
    area: 2
  - network: 10.1.1.0 0.0.0.255
    area: 0
```

---
### Цикл for

У циклі for можна перебирати елементи списку (наприклад, список ospf), словники (словник vlan) та інші ітеровані об'єкти.


---
### Цикл for

Результат виконання буде таким:
```
$ python cfg_gen.py templates/for.txt data_files/for.yml
hostname R3

interface Loopback0
 ip address 10.0.0.3 255.255.255.255

vlan 10
 name Marketing
vlan 20
 name Voice
vlan 30
 name Management

router ospf 1
 router-id 10.0.0.3
 auto-cost reference-bandwidth 10000
 network 10.0.1.0 0.0.0.255 area 0
 network 10.0.2.0 0.0.0.255 area 2
 network 10.1.1.0 0.0.0.255 area 0
```

---

##  if/elif/else

---
###  if/elif/else

if дозволяє додати умову до шаблону. Наприклад, ви можете використовувати if, щоб додати деякі частини шаблону, залежно від наявності змінних у словнику даних.


---
###  if/elif/else

Конструкція if також має бути всередині ```{% %}``` і має бути явно вказаний кінець умови:
```
{% if ospf %}
router ospf 1
 router-id 10.0.0.{{ id }}
 auto-cost reference-bandwidth 10000
{% endif %}
```

---
###  if/elif/else

Приклад шаблону templates/if.txt:
```
hostname {{ name }}

interface Loopback0
 ip address 10.0.0.{{ id }} 255.255.255.255

{% for vlan, name in vlans.items() %}
vlan {{ vlan }}
 name {{ name }}
{% endfor %}

{% if ospf %}
router ospf 1
 router-id 10.0.0.{{ id }}
 auto-cost reference-bandwidth 10000
 {% for networks in ospf %}
 network {{ networks.network }} area {{ networks.area }}
 {% endfor %}
{% endif %}
```

---
###  if/elif/else

Вираз ```if ospf``` працює так само, як і в Python: якщо змінна існує і не є порожньою, результатом буде True. Якщо змінної немає або вона порожня, результат буде False.

Тобто в цьому шаблоні конфігурація OSPF генерується, лише якщо змінна ospf існує і є істинною.


---
###  if/elif/else

Конфігурацію буде згенеровано з двома параметрами даних.

По-перше, з файлом data_files/if.yml, який не містить змінної ospf:
```yml
id: 3
name: R3
vlans:
  10: Marketing
  20: Voice
  30: Management
```

Результат буде таким:
```
$ python cfg_gen.py templates/if.txt data_files/if.yml

hostname R3

interface Loopback0
 ip address 10.0.0.3 255.255.255.255

vlan 10
 name Marketing
vlan 20
 name Voice
vlan 30
 name Management
```

---
###  if/elif/else

Тепер той самий шаблон, але з файлом data_files/if_ospf.yml:
```yml
id: 3
name: R3
vlans:
  10: Marketing
  20: Voice
  30: Management
ospf:
  - network: 10.0.1.0 0.0.0.255
    area: 0
  - network: 10.0.2.0 0.0.0.255
    area: 2
  - network: 10.1.1.0 0.0.0.255
    area: 0
```

---
###  if/elif/else

Тепер результат виконання буде таким:
```
hostname R3

interface Loopback0
 ip address 10.0.0.3 255.255.255.255

vlan 10
 name Marketing
vlan 20
 name Voice
vlan 30
 name Management

router ospf 1
 router-id 10.0.0.3
 auto-cost reference-bandwidth 10000
 network 10.0.1.0 0.0.0.255 area 0
 network 10.0.2.0 0.0.0.255 area 2
 network 10.1.1.0 0.0.0.255 area 0
```

---
###  if/elif/else

Як і Python, Jinja дозволяє розгалужуватися в межах умови.

Приклад шаблону templates/if_vlans.txt:
```
{% for intf, params in trunks.items() %}
interface {{ intf }}
 {% if params.action == 'add' %}
 switchport trunk allowed vlan add {{ params.vlans }}
 {% elif params.action == 'delete' %}
 switchport trunk allowed vlan remove {{ params.vlans }}
 {% else %}
 switchport trunk allowed vlan {{ params.vlans }}
 {% endif %}
{% endfor %}
```

---
###  if/elif/else

Файл data_files/if_vlans.yml з даними:
```yml
trunks:
  Fa0/1:
    action: add
    vlans: 10,20
  Fa0/2:
    action: only
    vlans: 10,30
  Fa0/3:
    action: delete
    vlans: 10
```

У цьому прикладі залежно від значення параметра дії генеруються різні команди.

---
###  if/elif/else

Шаблон може також використовувати наступний параметр для доступу до вкладених словників:
```
{% for intf in trunks %}
interface {{ intf }}
 {% if trunks[intf]['action'] == 'add' %}
 switchport trunk allowed vlan add {{ trunks[intf]['vlans'] }}
 {% elif trunks[intf]['action'] == 'delete' %}
 switchport trunk allowed vlan remove {{ trunks[intf]['vlans'] }}
 {% else %}
 switchport trunk allowed vlan {{ trunks[intf]['vlans'] }}
 {% endif %}
{% endfor %}
```

---
###  if/elif/else

В результаті буде згенерована така конфігурація:
```
$ python cfg_gen.py templates/if_vlans.txt data_files/if_vlans.yml
interface Fa0/1
 switchport trunk allowed vlan add 10,20
interface Fa0/3
  switchport trunk allowed vlan remove 10
interface Fa0/2
  switchport trunk allowed vlan 10,30
```

---
###  if/elif/else
Приклад шаблону templates/if_for.txt із умовою в циклі for:
```
{% for vlan, name in vlans.items() if vlan > 15 %}
vlan {{ vlan }}
 name {{ name }}
{% endfor %}
```

---
###  if/elif/else

Файл даних (data_files/if_for.yml):
```yml
vlans:
  10: Marketing
  20: Voice
  30: Management
```

---
###  if/elif/else

Результат виконання:
```
$ python cfg_gen.py templates/if_for.txt data_files/if_for.yml
vlan 20
 name Voice
vlan 30
 name Management
```

---
## Фільтри

---
### Фільтри

У Jinja змінні можна змінювати за допомогою фільтрів.
Фільтри відокремлюються від змінної вертикальною рискою (часточкою ``|``) і можуть містити додаткові аргументи.

Крім того, до змінної можна застосувати декілька фільтрів.
У цьому випадку фільтри записуються послідовно, і кожен з них відокремлюється вертикальною рискою.

```
auto-cost reference-bandwidth {{ ref_bw | default(10000) }}
```

---
### Фільтри

Jinja підтримує велику кількість вбудованих фільтрів.
Ми розглянемо лише деякі з них.
Решту фільтрів можна знайти в [документації](http://jinja.pocoo.org/docs/dev/templates/#builtin-filters).

Крім того, досить легко ви можете створювати власні фільтри.
Ми не розглядатимемо цю можливість, але вона добре описана в [документації](http://jinja.pocoo.org/docs/2.9/api/#custom-filters).

---
### default

Фільтр ``default`` дозволяє вказати значення за замовчуванням для змінної.
Якщо змінну визначено, буде підставлена вона; якщо змінна не визначена, буде підставлено значення, яке вказане у фільтрі default.

---
### default

Приклад шаблону templates/filter_default.txt:
```
router ospf 1
 auto-cost reference-bandwidth {{ ref_bw | default(10000) }}
 {% for networks in ospf %}
 network {{ networks.network }} area {{ networks.area }}
 {% endfor %}
```

Якщо змінна ref_bw визначена в словнику, буде підставлене її значення.
Якщо змінної немає, буде підставлене значення 10000.

---
### default

Файл даних (data_files/filter_default.yml):
```yml
ospf:
  - network: 10.0.1.0 0.0.0.255
    area: 0
  - network: 10.0.2.0 0.0.0.255
    area: 2
  - network: 10.1.1.0 0.0.0.255
    area: 0
```

---
### default

Результат виконання:
```
$ python cfg_gen.py templates/filter_default.txt data_files/filter_default.yml
router ospf 1
 auto-cost reference-bandwidth 10000
 network 10.0.1.0 0.0.0.255 area 0
 network 10.0.2.0 0.0.0.255 area 2
 network 10.1.1.0 0.0.0.255 area 0
```

---
### default

За замовчуванням, якщо змінну визначено, а її значення є порожнім об’єктом, вважатиметься, що змінна та її значення існує.

Якщо ви хочете переконатися, що значення за замовчуванням замінюється навіть тоді, коли змінна порожня (тобто обробляється як False у Python), треба вказати додатковий параметр ``boolean=true``.

---
### default

Наприклад, якщо файл даних такий:
```
ref_bw: ''
ospf:
  - network: 10.0.1.0 0.0.0.255
    area: 0
  - network: 10.0.2.0 0.0.0.255
    area: 2
  - network: 10.1.1.0 0.0.0.255
    area: 0
```

В результаті буде отриманий такий результат:
```
$ python cfg_gen.py templates/filter_default.txt data_files/filter_default.yml
router ospf 1
 auto-cost reference-bandwidth 
 network 10.0.1.0 0.0.0.255 area 0
 network 10.0.2.0 0.0.0.255 area 2
 network 10.1.1.0 0.0.0.255 area 0
```

---
### default

Якщо з тим самим файлом даних, змінити шаблон таким чином:
```
router ospf 1
 auto-cost reference-bandwidth {{ ref_bw | default(10000, boolean=true) }}
{% for networks in ospf %}
 network {{ networks.network }} area {{ networks.area }}
{% endfor %}
```

Результат вже буде таким (буде підставлено значення за замовчуванням):
```
$ python cfg_gen.py templates/filter_default.txt data_files/filter_default.yml
router ospf 1
 auto-cost reference-bandwidth 10000
 network 10.0.1.0 0.0.0.255 area 0
 network 10.0.2.0 0.0.0.255 area 2
 network 10.1.1.0 0.0.0.255 area 0
```

---
### dictsort

Фільтр dictsort дозволяє сортувати словник.
За замовчуванням сортування виконується за ключами.
Однак, змінивши параметри фільтра, можна сортувати за значеннями.

Синтаксис фільтра:
```
dictsort(value, case_sensitive=False, by='key')
```

Після того як dictsort відсортував словник, він повертає список кортежів, а не словник.

---
### dictsort

Приклад templates/filter_dictsort.txt із використанням фільтра dictsort:
```
{% for intf, params in trunks | dictsort %}
interface {{ intf }}
 {% if params.action == 'add' %}
 switchport trunk allowed vlan add {{ params.vlans }}
 {% elif params.action == 'delete' %}
 switchport trunk allowed vlan remove {{ params.vlans }}
 {% else %}
 switchport trunk allowed vlan {{ params.vlans }}
 {% endif %}
{% endfor %}
```

---
### dictsort

Файл даних (data_files/filter_dictsort.yml):
```yml
trunks:
  Fa0/1:
    action: add
    vlans: 10,20
  Fa0/2:
    action: only
    vlans: 10,30
  Fa0/3:
    action: delete
    vlans: 10
```

---
### dictsort

Результат виконання буде таким (інтерфейси впорядковані):
```
$ python cfg_gen.py templates/filter_dictsort.txt data_files/filter_dictsort.yml
interface Fa0/1
  switchport trunk allowed vlan add 10,20
interface Fa0/2
  switchport trunk allowed vlan 10,30
interface Fa0/3
  switchport trunk allowed vlan remove 10
```

---
### join

Фільтр join працює так само, як метод join в Python.

Використовуючи фільтр join, можна об’єднати елементи послідовності в рядок із необов’язковим роздільником між елементами.

---
### join

Приклад шаблону templates/filter_join.txt із використанням фільтра join:
```
{% for intf, params in trunks | dictsort %}
interface {{ intf }}
 {% if params.action == 'add' %}
 switchport trunk allowed vlan add {{ params.vlans | join(',') }}
 {% elif params.action == 'delete' %}
 switchport trunk allowed vlan remove {{ params.vlans | join(',') }}
 {% else %}
 switchport trunk allowed vlan {{ params.vlans | join(',') }}
 {% endif %}
{% endfor %}
```

---
### join

Файл даних (data_files/filter_join.yml):
```yml
trunks:
  Fa0/1:
    action: add
    vlans:
      - 10
      - 20
  Fa0/2:
    action: only
    vlans:
      - 10
      - 30
  Fa0/3:
    action: delete
    vlans:
      - 10
```

---
### join

Результат виконання:
```
$ python cfg_gen.py templates/filter_join.txt data_files/filter_join.yml
interface Fa0/1
  switchport trunk allowed vlan add 10,20
interface Fa0/2
  switchport trunk allowed vlan 10,30
interface Fa0/3
  switchport trunk allowed vlan remove 10

```

---
## Тести

---
### Тести

Окрім фільтрів, Jinja також підтримує тести.
Тести дозволяють перевірити змінні на певну умову.

Jinja підтримує велику кількість вбудованих тестів.
Ми розглянемо лише деякі з них.
Ви можете знайти решту тестів у [документації](http://jinja.pocoo.org/docs/dev/templates/#builtin-tests).

Тести, як і фільтри, можна створювати самостійно.

---
### defined

Тест defined дозволяє перевірити, чи існує змінна в словнику даних.

Приклад шаблону templates/test_defined.txt:
```
router ospf 1
{% if ref_bw is defined %}
 auto-cost reference-bandwidth {{ ref_bw }}
{% else %}
 auto-cost reference-bandwidth 10000
{% endif %}
{% for networks in ospf %}
 network {{ networks.network }} area {{ networks.area }}
{% endfor %}
```

---
### defined

Цей приклад більш громіздкий, ніж використання фільтра за замовчуванням, але цей тест може бути корисним, якщо вам потрібно виконати різні команди залежно від того, визначена змінна чи ні.

Файл даних (data_files/test_defined.yml):

```yml
ospf:
  - network: 10.0.1.0 0.0.0.255
    area: 0
  - network: 10.0.2.0 0.0.0.255
    area: 2
  - network: 10.1.1.0 0.0.0.255
    area: 0
```

---
### defined

Результат виконання:
```
$ python cfg_gen.py templates/test_defined.txt data_files/test_defined.yml
router ospf 1
 auto-cost reference-bandwidth 10000
 network 10.0.1.0 0.0.0.255 area 0
 network 10.0.2.0 0.0.0.255 area 2
 network 10.1.1.0 0.0.0.255 area 0
```

---
## set

---
### set

У межах шаблону можна створювати нові змінні і призначати їм значення.
Це можуть бути нові змінні, або це можуть бути змінені значення змінних, які були передані в шаблон.

Таким чином можна запам'ятати значення, яке, наприклад, було отримано в результаті застосування кількох фільтрів.
І в майбутньому використовувати назву змінної, а не повторювати всі фільтри знову.

---
### set

Приклад шаблону templates/set.txt, у якому вираз set використовується для надання коротших назв параметрів:
```
{% for intf, params in trunks | dictsort %}
 {% set vlans = params.vlans %}
 {% set action = params.action %}

interface {{ intf }}
  {% if action == 'add' %}
 switchport trunk allowed vlan add {{ vlans | join(',') }}
  {% elif action == 'delete' %}
 switchport trunk allowed vlan remove {{ vlans | join(',') }}
  {% else %}
 switchport trunk allowed vlan {{ vlans | join(',') }}
  {% endif %}
{% endfor %}
```

---
### set

Зверніть увагу на другий і третій рядки:
```
  {% set vlans = params.vlans %}
  {% set action = params.action %}
```

Таким чином, створюються нові змінні, і ці нові значення потім використовуються.
Це робить шаблон зрозумілішим.

---
### set

Файл даних (data_files/set.yml):
```json
trunks:
  Fa0/1:
    action: add
    vlans:
      - 10
      - 20
  Fa0/2:
    action: only
    vlans:
      - 10
      - 30
  Fa0/3:
    action: delete
    vlans: 10
```

---
### set

Результат виконання:
```
$ python cfg_gen.py templates/set.txt data_files/set.yml

interface Fa0/1
 switchport trunk allowed vlan add 10,20

interface Fa0/2
 switchport trunk allowed vlan 10,30

interface Fa0/3
 switchport trunk allowed vlan remove 10
```