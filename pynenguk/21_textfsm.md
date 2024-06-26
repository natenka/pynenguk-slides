# Python для мережевих інженерів 

---

# Обробка виводу команд з TextFSM

---
### Обробка виводу команд з TextFSM

TextFSM — це бібліотека, створена Google для обробки виводу команд із мережевих пристроїв.
Вона дозволяє створювати шаблони, за якими буде оброблятися вивід команди.

Шаблонами легше ділитися і знаходити вже створені шаблони.

Спочатку потрібно встановити бібліотеку:
```
pip install textfsm
```

---
### show ip interface brief

```
Value INT (\S+)
Value ADDR (\S+)
Value STATUS (up|down|administratively down)
Value PROTO (up|down)

Start
  ^${INTF}\s+${ADDR}\s+\w+\s+\w+\s+${STATUS}\s+${PROTO} -> Record
```

```
R1#show ip interface brief
Interface        IP-Address      OK? Method Status    Protocol
FastEthernet0/0  15.0.15.1       YES manual up        up
FastEthernet0/1  10.0.12.1       YES manual up        up
FastEthernet0/2  10.0.13.1       YES manual up        up
FastEthernet0/3  unassigned      YES unset  up        up
Loopback0        10.1.1.1        YES manual up        up
Loopback100      100.0.0.1       YES manual up        up
```

---
### Обробка виводу команд з TextFSM

Для використання TextFSM необхідно створити шаблон, за яким буде оброблятися вивід команди.

Приклад результату команди traceroute:
```
r2#traceroute 90.0.0.9 source 33.0.0.2
traceroute 90.0.0.9 source 33.0.0.2
Type escape sequence to abort.
Tracing the route to 90.0.0.9
VRF info: (vrf in name/id, vrf out name/id)
  1 10.0.12.1 1 msec 0 msec 0 msec
  2 15.0.0.5  0 msec 5 msec 4 msec
  3 57.0.0.7  4 msec 1 msec 4 msec
  4 79.0.0.9  4 msec *  1 msec
```

---
### Обробка виводу команд з TextFSM

Наприклад, з результату ви повинні отримати hop, через які пройшов пакет.

У цьому випадку шаблон TextFSM матиме такий вигляд (файл traceroute.template):
```
Value ID (\d+)
Value Hop (\d+(\.\d+){3})

Start
  ^  ${ID} ${Hop} -> Record
```

---
### Обробка виводу команд з TextFSM

Перші два рядки визначають змінні:
* ```Value ID (\d+)```
 * цей рядок визначає змінну ID, яку описує регулярний вираз: ```(\d+)``` - одна або більше цифр
 * номери хопів будуть тут
* ```Value Hop (\d+(\.\d+){3})```
 * цей рядок визначає змінну Hop, яка описує IP-адресу за допомогою цього регулярного виразу: ```(\d+(\.\d+){3})```

---
### Обробка виводу команд з TextFSM

Після рядка Start починається сам шаблон:
* ```^  ${ID} ${Hop} -> Record```
 * спочатку йде символ початку рядка, потім один або два пробіли та змінні ID і Hop
 * у TextFSM змінні описані таким чином: ```${назва змінної}```
 * слово ```Record``` в кінці означає, що рядки, які підпадають під описаний шаблон, будуть оброблені та виведені в результати TextFSM

---
### Обробка виводу команд з TextFSM

Скрипт для обробки результатів команди traceroute за допомогою TextFSM (parse_traceroute.py):
```python
import textfsm

traceroute = """
r2#traceroute 90.0.0.9 source 33.0.0.2
traceroute 90.0.0.9 source 33.0.0.2
Type escape sequence to abort.
Tracing the route to 90.0.0.9
VRF info: (vrf in name/id, vrf out name/id)
  1 10.0.12.1 1 msec 0 msec 0 msec
  2 15.0.0.5  0 msec 5 msec 4 msec
  3 57.0.0.7  4 msec 1 msec 4 msec
  4 79.0.0.9  4 msec *  1 msec
"""

template = open('traceroute.textfsm')
fsm = textfsm.TextFSM(template)
result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)
```

---
### Обробка виводу команд з TextFSM

Результат виконання скрипта:
```
$ python parse_traceroute.py
['ID', 'Hop']
[['1', '10.0.12.1'], ['2', '15.0.0.5'], ['3', '57.0.0.7'], ['4', '79.0.0.9']]
```

Рядки, які відповідають описаному шаблону, повертаються як список списків.
Кожен елемент є списком, який складається з двох елементів: номера адреси та IP-адреси.


---
### Обробка виводу команд з TextFSM

Для роботи з TextFSM потрібен вихід команди та шаблон:
* для різних команд потрібні різні шаблони
* TextFSM повертає результат обробки в табличній формі (як список списків) або як список словників
  * цей результат можна конвертувати у формат csv або список словників

---
## Синтаксис шаблонів TextFSM

---
### Синтаксис шаблонів TextFSM

Шаблон TextFSM описує, як слід обробляти дані.

Будь-який шаблон складається з двох частин:
* визначення змінних
 * ці змінні описують, які стовпці будуть у результаті
* визначення стану


---
### Синтаксис шаблонів TextFSM

Приклад розбору команди traceroute:
```
Value ID (\d+)
Value Hop (\d+(\.\d+){3})


Start
  ^  ${ID} ${Hop} -> Record
```

---
### Визначення змінних

У секції зі змінними повинні йти лише визначення змінних. Єдиний виняток – у цьому розділі можуть бути коментарі.

У цьому розділі не повинно бути порожніх рядків.
Для TextFSM порожній рядок означає кінець розділу визначення змінних.

Формат опису змінних:
```
Value [option[,option...]] name regex
```

---
### Визначення змінних

Синтаксис опису змінних:
* ``Value`` - це ключове слово, яке вказує, що створюється змінна. Його обов'язково потрібно вказувати
* option - опції, які визначають як працювати зі змінною. Якщо потрібно вказати кілька опцій, вони мають бути відокремлені комою, без пробілів.

---
### Визначення змінних

Підтримуються такі опції:
 * __Filldown__ - значення, яке раніше збіглося з регулярним виразом, запам'ятовується до наступної обробки рядка (якщо не було явно очищено або знову збігся регулярний вираз).
   * це означає, що останнє значення стовпця, яке збіглося з регулярним виразом, запам'ятовується і використовується в наступних рядках, якщо в них не був присутній цей стовпець.
 * __Key__ - визначає, що це поле містить унікальний ідентифікатор рядка
 * __Required__ - рядок, який обробляється, буде записано тільки в тому випадку, якщо ця змінна є.
 * __List__ - значення це список і кожен збіг з регулярним виразом буде додавати до списку елемент. За замовчуванням кожен наступний збіг перезаписує попередній.
 * __Fillup__ - працює як Filldown, але заповнює порожні значення вище, доки знайде збіг. Не сумісне з Required.

 
---
### Визначення змінних

* ```name``` - ім'я змінної, яка буде використовуватися як ім'я стовпця. Зарезервовані імена не слід використовувати як назву змінної.
* ```regex``` - це регулярний вираз, який описує змінну. Регулярний вираз має бути в круглих дужках.

---
### Визначення змінних

Після визначення змінних потрібно описати стани:
* кожне визначення стану має бути розділене порожнім рядком (принаймні одним)
* перший рядок - назва стану
* потім є рядки, які описують правила
  * правила мають починатися з пробілу та символу ```^```

---
### Визначення змінних

Початковий стан завжди __Start__.
Вхідні дані порівнюються з поточним станом, але рядок правила може вказувати на необхідність переходу в інший стан.

Перевірка виконується рядок за рядком, поки не буде досягнуто __EOF__ (кінець файлу) або поточний стан не стане __End__.

---
#### Зарезервовані стани

Зарезервовано наступні стани:
* __Start__ - цей стан необхідно вказати. Без нього шаблон працювати не буде.
* __End__ – цей стан завершує обробку вхідних рядків і не виконує стан __EOF__.
* __EOF__ — це неявний стан, який виконується кожного разу, коли обробка досягає кінця файлу. Це виглядає так:

```
 EOF
   ^.* -> Record
```

---
#### Зарезервовані стани

__EOF__ записує поточний рядок, перш ніж обробка завершується. Якщо цю поведінку потрібно змінити, треба явно наприкінці шаблону написати EOF:

```
EOF
```

---
### Правила станів

Кожен стан складається з одного або більше правил:
* TextFSM обробляє вхідні рядки та порівнює їх з правилами
* Якщо правило (регулярний вираз) збігається з рядком, виконуються дії, які описані в правилі і для наступного рядка процес повторюється наново, з початку стану.

Правила мають бути описані у такому форматі:
```
 ^regex [-> action]
```

---
### Правила станів

У правилі:
* кожне правило має починатися з пробілу та символу ``^``
  * символ ``^`` позначає початок рядка і завжди має вказуватися явно
* regex — регулярний вираз, який може використовувати змінні
  * для визначення змінної можна використовувати синтаксис ```$ValueName``` або ```${ValueName}``` (цей формат є кращим)
  * у правилі змінні замінюються регулярними виразами, які вони описують
  * якщо потрібно явно вказати символ кінця рядка, використовується значення ```$$```

---
### Дії в правилах


Після регулярного виразу правило може визначати дії:
* між регулярним виразом і дією має бути символ ```->```
* дії можуть складатися з трьох частин, у форматі __L.R S__
  * __L - Line Action__ - дії, які застосовуються до вхідного рядка
  * __R - Record Action__ - дії, які застосовуються до зібраних значень
  * __S - State Transition__ - перехід в інший стан
* за замовчуванням __Next.NoRecord__

---
#### Line Actions

__Line Actions:__
* __Next__ - обробити рядок, прочитати наступний і почати його перевірку з початку стану. Ця дія використовується за замовчуванням, якщо не вказано інше
* __Continue__ - продовжити обробку правил так, ніби збігу не було, значення присвоюються

---
#### Record Action

__Дія запису__ — необов’язкова дія, яку можна вказати після Line Action. Вони повинні бути розділені крапкою. Види дій:
* __NoRecord__ - нічого не робити. Це дія за замовчуванням, якщо не вказано інше.
* __Record__ - запам'ятати значення, яке відповідає правилу. Усі змінні, крім тих, де вказано параметр Filldown, обнуляються.
* __Clear__ - обнулити всі змінні, крім тих, де вказано опцію Filldown.
* __Clearall__ - обнулити всі змінні.

Відокремлюйте дії крапкою, лише якщо потрібно вказати дії Line і Record. Якщо потрібно вказати лише одну з них, то крапку ставити не потрібно.

---
#### State Transition

Після дії можна вказати новий стан:
* стан має бути одним із зарезервованих або станом, визначеним у шаблоні
* якщо вхідний рядок збігся:
  * всі дії виконуються,
  * зчитується наступний рядок,
  * потім поточний стан змінюється на новий і обробка продовжується в новому стані.

Якщо правило використовує дію __Continue__, то ньому не можна використовувати перехід до іншого стан. Це правило потрібне для того, щоб у послідовності станів не було петель.

---
#### Error Action

Спеціальна дія __Error__ зупиняє обробку всіх рядків, відкидає всі рядки, які були зібрані до цього часу, і повертає виняток.

Синтаксис цієї дії:
```
^regex -> Error [word|"string"]
```

---
## Приклади використання TextFSM

---
### Приклади використання TextFSM

Для обробки виводу команд шаблону використовується скрипт parse_output.py.
Він не прив'язаний до конкретного шаблону та виводу: шаблон та вивід команди будуть передаватися як аргументи:

```python
import sys
import textfsm
from tabulate import tabulate

template = sys.argv[1]
output_file = sys.argv[2]

f = open(template)
output = open(output_file).read()

re_table = textfsm.TextFSM(f)

header = re_table.header
result = re_table.ParseText(output)

print(tabulate(result, headers=header))
```

---
### Приклади використання TextFSM

Приклад запуску скрипту:
```
$ python parse_output.py template command_output
```

Обробка даних за шаблоном завжди виконується однаково.
Тому скрипт буде однаковий і тільки шаблон та дані відрізнятимуться.

---
### show ip interface brief

У випадку, коли потрібно обробити дані, які виведені стовпцями, шаблон TextFSM найбільш зручний.

Шаблон для виводу команди show ip interface brief (файл templates/sh_ip_int_br.template):
```
Value INT (\S+)
Value ADDR (\S+)
Value STATUS (up|down|administratively down)
Value PROTO (up|down)

Start
  ^${INTF}\s+${ADDR}\s+\w+\s+\w+\s+${STATUS}\s+${PROTO} -> Record
```

---
### show ip interface brief

У цьому випадку правило можна описати одним рядком.

Вивід команди (файл output/sh_ip_int_br.txt):
```
R1#show ip interface brief
Interface        IP-Address      OK? Method Status    Protocol
FastEthernet0/0  15.0.15.1       YES manual up        up
FastEthernet0/1  10.0.12.1       YES manual up        up
FastEthernet0/2  10.0.13.1       YES manual up        up
FastEthernet0/3  unassigned      YES unset  up        up
Loopback0        10.1.1.1        YES manual up        up
Loopback100      100.0.0.1       YES manual up        up
```

---
### show ip interface brief

Результат виконання буде таким:
```
$ python parse_output.py templates/sh_ip_int_br.template output/sh_ip_int_br.txt
INT              ADDR        STATUS    PROTO
---------------  ----------  --------  -------
FastEthernet0/0  15.0.15.1   up        up
FastEthernet0/1  10.0.12.1   up        up
FastEthernet0/2  10.0.13.1   up        up
FastEthernet0/3  unassigned  up        up
Loopback0        10.1.1.1    up        up
Loopback100      100.0.0.1   up        up
```


---
### show cdp neighbors detail

Теперь попробуем обработать вывод команды show cdp neighbors detail.

Особенность этой команды в том, что данные находятся не в одной строке, а в разных.

---
### show cdp neighbors detail

В файле output/sh_cdp_n_det.txt находится вывод команды show cdp neighbors detail:
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

-------------------------
Device ID: R1
Entry address(es):
  IP address: 10.1.1.1
Platform: Cisco 3825,  Capabilities: Router Switch IGMP
Interface: GigabitEthernet1/0/22,  Port ID (outgoing port): GigabitEthernet0/0
Holdtime : 156 sec

Version :
Cisco IOS Software, 3800 Software (C3825-ADVENTERPRISEK9-M), Version 12.4(24)T1, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2009 by Cisco Systems, Inc.
Compiled Fri 19-Jun-09 18:40 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Duplex: full
Management address(es):

-------------------------
Device ID: R2
Entry address(es):
  IP address: 10.2.2.2
Platform: Cisco 2911,  Capabilities: Router Switch IGMP
Interface: GigabitEthernet1/0/21,  Port ID (outgoing port): GigabitEthernet0/0
Holdtime : 156 sec

Version :
Cisco IOS Software, 2900 Software (C3825-ADVENTERPRISEK9-M), Version 15.2(2)T1, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2009 by Cisco Systems, Inc.
Compiled Fri 19-Jun-09 18:40 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Duplex: full
Management address(es):


```

---
### show cdp neighbors detail

Из вывод команды надо получить такие поля:
* LOCAL_HOST - имя устройства из приглашения
* DEST_HOST - имя соседа
* MGMNT_IP - IP-адрес соседа
* PLATFORM - модель соседнего устройства
* LOCAL_PORT - локальный интерфейс, который соединен с соседом
* REMOTE_PORT - порт соседнего устройства
* IOS_VERSION - версия IOS соседа

---
### show cdp neighbors detail

Шаблон выглядит таким образом (файл templates/sh_cdp_n_det.template):
```
Value LOCAL_HOST (\S+)
Value DEST_HOST (\S+)
Value MGMNT_IP (.*)
Value PLATFORM (.*)
Value LOCAL_PORT (.*)
Value REMOTE_PORT (.*)
Value IOS_VERSION (\S+)

Start
  ^${LOCAL_HOST}[>#].
  ^Device ID: ${DEST_HOST}
  ^.*IP address: ${MGMNT_IP}
  ^Platform: ${PLATFORM},
  ^Interface: ${LOCAL_PORT},  Port ID \(outgoing port\): ${REMOTE_PORT}
  ^.*Version ${IOS_VERSION},
```

---
### show cdp neighbors detail

Результат выполнения скрипта:
```
$ python parse_output.py templates/sh_cdp_n_det.template output/sh_cdp_n_det.txt
LOCAL_HOST    DEST_HOST    MGMNT_IP    PLATFORM    LOCAL_PORT             REMOTE_PORT         IOS_VERSION
------------  -----------  ----------  ----------  ---------------------  ------------------  -------------
SW1           R2           10.2.2.2    Cisco 2911  GigabitEthernet1/0/21  GigabitEthernet0/0  15.2(2)T1
```

---
### show cdp neighbors detail

Несмотря на то, что правила с переменными описаны в разных строках, и, соответственно, работают с разными строками, TextFSM собирает их в одну строку таблицы.
То есть, переменные, которые определены в начале шаблона, задают строку итоговой таблицы.

Обратите внимание, что в файле sh_cdp_n_det.txt находится вывод с тремя соседями, а в таблице только один сосед, последний.

---
#### Record
Так получилось из-за того, что в шаблоне не указано действие __Record__.
И в итоге, в финальной таблице осталась только последняя строка.

Исправленый шаблон:
```
Value LOCAL_HOST (\S+)
Value DEST_HOST (\S+)
Value MGMNT_IP (.*)
Value PLATFORM (.*)
Value LOCAL_PORT (.*)
Value REMOTE_PORT (.*)
Value IOS_VERSION (\S+)

Start
  ^${LOCAL_HOST}[>#].
  ^Device ID: ${DEST_HOST}
  ^.*IP address: ${MGMNT_IP}
  ^Platform: ${PLATFORM},
  ^Interface: ${LOCAL_PORT},  Port ID \(outgoing port\): ${REMOTE_PORT}
  ^.*Version ${IOS_VERSION}, -> Record
```

---
#### Record

Теперь результат запуска скрипта выглядит так:
```
$ python parse_output.py templates/sh_cdp_n_det.template output/sh_cdp_n_det.txt
LOCAL_HOST    DEST_HOST    MGMNT_IP    PLATFORM              LOCAL_PORT             REMOTE_PORT         IOS_VERSION
------------  -----------  ----------  --------------------  ---------------------  ------------------  -------------
SW1           SW2          10.1.1.2    cisco WS-C2960-8TC-L  GigabitEthernet1/0/16  GigabitEthernet0/1  12.2(55)SE9
              R1           10.1.1.1    Cisco 3825            GigabitEthernet1/0/22  GigabitEthernet0/0  12.4(24)T1
              R2           10.2.2.2    Cisco 2911            GigabitEthernet1/0/21  GigabitEthernet0/0  15.2(2)T1
```

Вывод получен со всех трёх устройств.
Но, переменная LOCAL_HOST отображается не в каждой строке, а только в первой.

---
#### Filldown

Это связано с тем, что приглашение, из которого взято значение переменной, появляется только один раз.
И, для того, чтобы оно появлялось и в последующих строках, надо использовать действие __Filldown__ для переменной LOCAL_HOST:
```
Value Filldown LOCAL_HOST (\S+)
Value DEST_HOST (\S+)
Value MGMNT_IP (.*)
Value PLATFORM (.*)
Value LOCAL_PORT (.*)
Value REMOTE_PORT (.*)
Value IOS_VERSION (\S+)

Start
  ^${LOCAL_HOST}[>#].
  ^Device ID: ${DEST_HOST}
  ^.*IP address: ${MGMNT_IP}
  ^Platform: ${PLATFORM},
  ^Interface: ${LOCAL_PORT},  Port ID \(outgoing port\): ${REMOTE_PORT}
  ^.*Version ${IOS_VERSION}, -> Record
```

---
#### Filldown

Теперь мы получили такой вывод:
```
$ python parse_output.py templates/sh_cdp_n_det.template output/sh_cdp_n_det.txt
LOCAL_HOST    DEST_HOST    MGMNT_IP    PLATFORM              LOCAL_PORT             REMOTE_PORT         IOS_VERSION
------------  -----------  ----------  --------------------  ---------------------  ------------------  -------------
SW1           SW2          10.1.1.2    cisco WS-C2960-8TC-L  GigabitEthernet1/0/16  GigabitEthernet0/1  12.2(55)SE9
SW1           R1           10.1.1.1    Cisco 3825            GigabitEthernet1/0/22  GigabitEthernet0/0  12.4(24)T1
SW1           R2           10.2.2.2    Cisco 2911            GigabitEthernet1/0/21  GigabitEthernet0/0  15.2(2)T1
SW1
```

Теперь значение переменной LOCAL_HOST появилось во всех трёх строках. Но появился ещё один странный эффект - последняя строка, в которой заполнена только колонка LOCAL_HOST.

---
#### Required

Дело в том, что все переменные, которые мы определили, опциональны.
К тому же, одна переменная с параметром Filldown.
И, чтобы избавиться от последней строки, нужно сделать хотя бы одну переменную обязательной, с помощью параметра __Required__:
```
Value Filldown LOCAL_HOST (\S+)
Value Required DEST_HOST (\S+)
Value MGMNT_IP (.*)
Value PLATFORM (.*)
Value LOCAL_PORT (.*)
Value REMOTE_PORT (.*)
Value IOS_VERSION (\S+)

Start
  ^${LOCAL_HOST}[>#].
  ^Device ID: ${DEST_HOST}
  ^.*IP address: ${MGMNT_IP}
  ^Platform: ${PLATFORM},
  ^Interface: ${LOCAL_PORT},  Port ID \(outgoing port\): ${REMOTE_PORT}
  ^.*Version ${IOS_VERSION}, -> Record
```

---
#### Required

Теперь мы получим корректный вывод:
```
$ python parse_output.py templates/sh_cdp_n_det.template output/sh_cdp_n_det.txt
LOCAL_HOST    DEST_HOST    MGMNT_IP    PLATFORM              LOCAL_PORT             REMOTE_PORT         IOS_VERSION
------------  -----------  ----------  --------------------  ---------------------  ------------------  -------------
SW1           SW2          10.1.1.2    cisco WS-C2960-8TC-L  GigabitEthernet1/0/16  GigabitEthernet0/1  12.2(55)SE9
SW1           R1           10.1.1.1    Cisco 3825            GigabitEthernet1/0/22  GigabitEthernet0/0  12.4(24)T1
SW1           R2           10.2.2.2    Cisco 2911            GigabitEthernet1/0/21  GigabitEthernet0/0  15.2(2)T1
```
---
### show ip route ospf

Рассмотрим случай, когда нам нужно обработать вывод команды show ip route ospf и в таблице маршрутизации есть несколько маршрутов к одной сети.

Для маршрутов к одной и той же сети, вместо нескольких строк, где будет повторяться сеть, будет создана одна запись, в которой все доступные next-hop адреса собраны в список.


---
### show ip route ospf

Пример вывода команды show ip route ospf (файл output/sh_ip_route_ospf.txt):
```
R1#sh ip route ospf
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       + - replicated route, % - next hop override

Gateway of last resort is not set

      10.0.0.0/8 is variably subnetted, 10 subnets, 2 masks
O        10.0.24.0/24 [110/20] via 10.0.12.2, 1w2d, Ethernet0/1
O        10.0.34.0/24 [110/20] via 10.0.13.3, 1w2d, Ethernet0/2
O        10.2.2.2/32 [110/11] via 10.0.12.2, 1w2d, Ethernet0/1
O        10.3.3.3/32 [110/11] via 10.0.13.3, 1w2d, Ethernet0/2
O        10.4.4.4/32 [110/21] via 10.0.13.3, 1w2d, Ethernet0/2
                     [110/21] via 10.0.12.2, 1w2d, Ethernet0/1
                     [110/21] via 10.0.14.4, 1w2d, Ethernet0/3
O        10.5.35.0/24 [110/20] via 10.0.13.3, 1w2d, Ethernet0/2


```

---
### show ip route ospf

Для этого примера упрощаем задачу и считаем, что маршруты могут быть только OSPF и с обозначением, только O (то есть, только внутризональные маршруты).

Первая версия шаблона выглядит так:
```
Value Network (([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}))
Value Mask (\/\d{1,2})
Value Distance (\d+)
Value Metric (\d+)
Value NextHop ([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})

Start
  ^O +${Network}${Mask}\s\[${Distance}\/${Metric}\]\svia\s${NextHop}, -> Record
```

---
### show ip route ospf

Результат получился такой:
```
Network    Mask      Distance    Metric  NextHop
---------  ------  ----------  --------  ---------
10.0.24.0  /24            110        20  10.0.12.2
10.0.34.0  /24            110        20  10.0.13.3
10.2.2.2   /32            110        11  10.0.12.2
10.3.3.3   /32            110        11  10.0.13.3
10.4.4.4   /32            110        21  10.0.13.3
10.5.35.0  /24            110        20  10.0.13.3
```

---
#### List

Всё нормально, но потерялись варианты путей для маршрута 10.4.4.4/32.
Это логично, ведь нет правила, которое подошло бы для такой строки.


Воспользуемся опцией __List__ для переменной NextHop:
```
Value Network (([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}))
Value Mask (\/\d{1,2})
Value Distance (\d+)
Value Metric (\d+)
Value List NextHop ([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})

Start
  ^O +${Network}${Mask}\s\[${Distance}\/${Metric}\]\svia\s${NextHop}, -> Record
```

---
#### List

Теперь вывод получился таким:
```
Network    Mask      Distance    Metric  NextHop
---------  ------  ----------  --------  -------------
10.0.24.0  /24            110        20  ['10.0.12.2']
10.0.34.0  /24            110        20  ['10.0.13.3']
10.2.2.2   /32            110        11  ['10.0.12.2']
10.3.3.3   /32            110        11  ['10.0.13.3']
10.4.4.4   /32            110        21  ['10.0.13.3']
10.5.35.0  /24            110        20  ['10.0.13.3']
```

---
#### List

Изменилось то, что в столбце NextHop отображается список, но пока с одним элементом.

Так как, перед записью маршрута, для которого есть несколько путей, надо добавить к нему все доступные адреса NextHop, надо перенести действие __Record__.


---
#### List

Для этого, запись переносится на момент, когда встречается следующая строка с маршрутом.
В этот момент надо записать предыдущую строку и только после этого, уже записывать текущую.
Для этого, используется такая запись:
```
  ^O -> Continue.Record
```

---
#### List

В ней действие __Record__ говорит, что надо записать текущее значение переменных.
А, так как в этом правиле нет переменных, записывается то, что было в предыдущих значениях.

Действие __Continue__ говорит, что надо продолжить работать с текущей строкой так, как-будто совпадения не было.
Засчет этого, сработает следующая строка.

Остается добавить правило, которое будет описывать дополнительные маршруты к сети (в них нет сети и маски):
```
  ^\s+\[${Distance}\/${Metric}\]\svia\s${NextHop},
```

---
#### List

Итоговый шаблон выглядит так (файл templates/sh_ip_route_ospf.template):
```
Value Network (([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}))
Value Mask (\/\d{1,2})
Value Distance (\d+)
Value Metric (\d+)
Value List NextHop ([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})

Start
  ^O -> Continue.Record
  ^O +${Network}${Mask}\s\[${Distance}\/${Metric}\]\svia\s${NextHop},
  ^\s+\[${Distance}\/${Metric}\]\svia\s${NextHop},
```

---
#### List

В результате, мы получим такой вывод:
```
Network    Mask      Distance    Metric  NextHop
---------  ------  ----------  --------  ---------------------------------------
10.0.24.0  /24            110        20  ['10.0.12.2']
10.0.34.0  /24            110        20  ['10.0.13.3']
10.2.2.2   /32            110        11  ['10.0.12.2']
10.3.3.3   /32            110        11  ['10.0.13.3']
10.4.4.4   /32            110        21  ['10.0.13.3', '10.0.12.2', '10.0.14.4']
10.5.35.0  /24            110        20  ['10.0.13.3']
```

---
### show etherchannel summary

---
### show etherchannel summary

TextFSM удобно использовать для разбора вывода, который отображается столбцами или для обработки вывода, который находится в разных строках.
Менее удобными получаются шаблоны, когда надо получить несколько однотипных элементов из одной строки.

---
### show etherchannel summary

Пример вывода команды show etherchannel summary (файл output/sh_etherchannel_summary.txt):
```
sw1# sh etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port


Number of channel-groups in use: 2
Number of aggregators:           2

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP      Fa0/1(P)   Fa0/2(P)   Fa0/3(P)
3      Po3(SU)          -        Fa0/11(P)   Fa0/12(P)   Fa0/13(P)   Fa0/14(P)
```

---
### show etherchannel summary

В данном случае, нужно получить:
* имя и номер port-channel. Например, Po1
* список всех портов в нем. Например, ['Fa0/1', 'Fa0/2', 'Fa0/3']

Сложность тут в том, что порты находятся в одной строке, а в TextFSM нельзя указывать одну и ту же переменную несколько раз в строке.
Но, есть возможность несколько раз искать совпадение в строке.



---
### show etherchannel summary

Первая версия шаблона выглядит так:
```
Value CHANNEL (\S+)
Value List MEMBERS (\w+\d+\/\d+)

Start
  ^\d+ +${CHANNEL}\(\S+ +[\w-]+ +[\w ]+ +${MEMBERS}\( -> Record
```

---
### show etherchannel summary

В шаблоне две переменные:
* CHANNEL - имя и номер агрегированного порта
* MEMBERS - список портов, которые входят в агрегированный порт. Для этой переменной указан тип - List

Результат:
```
CHANNEL    MEMBERS
---------  ----------
Po1        ['Fa0/1']
Po3        ['Fa0/11']
```

---
### show etherchannel summary

Пока что в выводе только первый порт, а нужно чтобы попали все порты.
В данном случае, надо продолжить обработку строки с портами, после найденного совпадения.
То есть, использовать действие Continue и описать следующее выражение.

Единственная строка, которая есть в шаблоне, описывает первый порт.
Надо добавить строку, которая описывает следующий порт.


---
### show etherchannel summary

Следующая версия шаблона:
```
Value CHANNEL (\S+)
Value List MEMBERS (\w+\d+\/\d+)

Start
  ^\d+ +${CHANNEL}\(\S+ +[\w-]+ +[\w ]+ +${MEMBERS}\( -> Continue
  ^\d+ +${CHANNEL}\(\S+ +[\w-]+ +[\w ]+ +\S+ +${MEMBERS}\( -> Record
```

Вторая строка описывает такое же выражение, но переменная MEMBERS смещается на следующий порт.


---
### show etherchannel summary

Результат:
```
CHANNEL    MEMBERS
---------  --------------------
Po1        ['Fa0/1', 'Fa0/2']
Po3        ['Fa0/11', 'Fa0/12']
```


---
### show etherchannel summary

Аналогично надо дописать в шаблон строки, которые описывают третий и четвертый порт.
Но, так как в выводе может быть переменное количество портов, надо перенести правило Record на отдельную строку, чтобы оно не было привязано к конкретному количеству портов в строке.

Если Record будет находиться, например, после строки, в которой описаны четыре порта, для ситуации когда портов в строке меньше, запись не будет выполняться.


---
### show etherchannel summary

Итоговый шаблон (файл templates/sh_etherchannel_summary.txt):
```
Value CHANNEL (\S+)
Value List MEMBERS (\w+\d+\/\d+)

Start
  ^\d+.* -> Continue.Record
  ^\d+ +${CHANNEL}\(\S+ +[\w-]+ +[\w ]+ +\S+ +${MEMBERS}\( -> Continue
  ^\d+ +${CHANNEL}\(\S+ +[\w-]+ +[\w ]+ +(\S+ +){2} +${MEMBERS}\( -> Continue
  ^\d+ +${CHANNEL}\(\S+ +[\w-]+ +[\w ]+ +(\S+ +){3} +${MEMBERS}\( -> Continue
```

---
### show etherchannel summary

Результат обработки:
```
CHANNEL    MEMBERS
---------  ----------------------------------------
Po1        ['Fa0/1', 'Fa0/2', 'Fa0/3']
Po3        ['Fa0/11', 'Fa0/12', 'Fa0/13', 'Fa0/14']
```

---
### show etherchannel summary

Возможен ещё один вариант вывода команды sh etherchannel summary (файл output/sh_etherchannel_summary2.txt):
```
sw1# sh etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port


Number of channel-groups in use: 2
Number of aggregators:           2

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP      Fa0/1(P)   Fa0/2(P)   Fa0/3(P)
3      Po3(SU)          -        Fa0/11(P)   Fa0/12(P)   Fa0/13(P)   Fa0/14(P)
                                 Fa0/15(P)   Fa0/16(P)
```

---
### show etherchannel summary

Для того чтобы шаблон обрабатывал и этот вариант, надо его модифицировать (файл templates/sh_etherchannel_summary2.txt):
```
Value CHANNEL (\S+)
Value List MEMBERS (\w+\d+\/\d+)

Start
  ^\d+.* -> Continue.Record
  ^\d+ +${CHANNEL}\(\S+ +[\w-]+ +[\w ]+ +${MEMBERS}\( -> Continue
  ^\d+ +${CHANNEL}\(\S+ +[\w-]+ +[\w ]+ +\S+ +${MEMBERS}\( -> Continue
  ^\d+ +${CHANNEL}\(\S+ +[\w-]+ +[\w ]+ +(\S+ +){2} +${MEMBERS}\( -> Continue
  ^\d+ +${CHANNEL}\(\S+ +[\w-]+ +[\w ]+ +(\S+ +){3} +${MEMBERS}\( -> Continue
  ^ +${MEMBERS} -> Continue
  ^ +\S+ +${MEMBERS} -> Continue
  ^ +(\S+ +){2} +${MEMBERS} -> Continue
  ^ +(\S+ +){3} +${MEMBERS} -> Continue
```

Результат будет таким:
```
CHANNEL    MEMBERS
---------  ------------------------------------------------------------
Po1        ['Fa0/1', 'Fa0/2', 'Fa0/3']
Po3        ['Fa0/11', 'Fa0/12', 'Fa0/13', 'Fa0/14', 'Fa0/15', 'Fa0/16']
```


---

## TextFSM CLI Table

---
### TextFSM CLI Table

Благодаря TextFSM, можно обрабатывать вывод команд и получать структурированный результат. 
Но, всё ещё надо вручную прописывать каким шаблоном обрабатывать команды show, каждый раз, когда используется TextFSM.

Было бы намного удобней иметь какое-то соответствие между командой и шаблоном.
Чтобы можно было написать общий скрипт, который выполняет подключения к устройствам, отправляет команды, сам выбирает шаблон и парсит вывод в соответствиее с шаблоном.

---
### TextFSM CLI Table

В TextFSM есть такая возможность.

Для того, чтобы ей можно было воспользоваться, надо создать файл в котором описаны соответствия между командами и шаблонами. В TextFSM он называется index.

---
### TextFSM CLI Table

Файл index должен находится в каталоге с шаблонами и должен иметь такой формат:
* первая строка - названия колонок
* каждая следующая строка - это соответствие шаблона команде

---
### TextFSM CLI Table

* обязательные колонки, местоположение которых фиксировано (должны быть обязательно первой и последней, соответственно):
 * первая колонка - имена шаблонов
 * последняя колонка - соответствующая команда
   * в этой колонке используется специальный формат, чтобы описать то, что команда может быть написана не полностью

---
### TextFSM CLI Table

* остальные колонки могут быть любыми
 * например, в примере ниже будут колонки Hostname, Vendor. Они позволяют уточнить информацию об устройстве, чтобы определить какой шаблон использовать.
   * например, команда show version может быть у оборудования Cisco и HP. Соответственно, только команды недостаточно, чтобы определить какой шаблон использовать. В таком случае, можно передать информацию о том, какой тип оборудования используется, вместе с командой, и тогда получится определить правильный шаблон.
* во всех столбцах, кроме первого, поддерживаются регулярные выражения
 * в командах, внутри ```[[]]``` регулярные выражения не поддерживаются

---
### TextFSM CLI Table

Пример файла index:
```
Template, Hostname, Vendor, Command
sh_cdp_n_det.template, .*, Cisco, sh[[ow]] cdp ne[[ighbors]] de[[tail]]
sh_clock.template, .*, Cisco, sh[[ow]] clo[[ck]]
sh_ip_int_br.template, .*, Cisco, sh[[ow]] ip int[[erface]] br[[ief]]
sh_ip_route_ospf.template, .*, Cisco, sh[[ow]] ip rou[[te]] o[[spf]]
```

---
### TextFSM CLI Table

Обратите внимание на то, как записаны команды:
* ```sh[[ow]] ip int[[erface]] br[[ief]]```
 * эта запись будет преобразована в выражение sh((ow)?)? ip int((erface)?)? br((ief)?)?
 * это значит, что TextFSM сможет определить какой шаблон использовать, даже если команда набрана не полностью
 * например, такие варианты команды сработают:
     * sh ip int br
     * show ip inter bri

---
### Как использовать CLI table

Посмотрим как пользоваться классом clitable и файлом index.

В каталоге templates такие шаблоны и файл index:
```
sh_cdp_n_det.template
sh_clock.template
sh_ip_int_br.template
sh_ip_route_ospf.template
index
```

---
### Как использовать CLI table

Сначала попробуем поработать с CLI Table в ipython, чтобы посмотреть какие возможности есть у этого класса, а затем посмотрим на финальный скрипт.

Для начала, импортируем класс clitable:
```python
In [1]: import clitable
```

---
### Как использовать CLI table

Проверять работу clitable будем на последнем примере из прошлого раздела - выводе команды show ip route ospf. Считываем вывод, который хранится в файле output/sh_ip_route_ospf.txt, в строку:
```python
In [2]: output_sh_ip_route_ospf = open('output/sh_ip_route_ospf.txt').read()
```

---
### Как использовать CLI table

Сначала надо инициализировать класс, передав ему имя файла, в котором хранится соответствие между шаблонами и командами, и указать имя каталога, в котором хранятся шаблоны:
```python
In [3]: cli_table = clitable.CliTable('index', 'templates')
```

---
### Как использовать CLI table

Надо указать какая команда передается и указать дополнительные атрибуты, которые помогут идентифицировать шаблон.
Для этого, нужно создать словарь, в котором ключи - имена столбцов, которые определены в файле index.
В данном случае, не обязательно указывать название вендора, так как команде sh ip route ospf соответствет только один шаблон. 
```python
In [4]: attributes = {'Command': 'show ip route ospf' , 'Vendor': 'Cisco'}
```

---
### Как использовать CLI table

Методу ParseCmd надо передать вывод команды и словарь с параметрами:
```python
In [5]: cli_table.ParseCmd(output_sh_ip_route_ospf, attributes)
```

В результате, в объекте cli_table, получаем обработанный вывод команды sh ip route ospf.

---
### Как использовать CLI table

Методы cli_table (чтобы посмотреть все методы, надо вызвать dir(cli_table)):
```python
In [6]: cli_table.
cli_table.AddColumn        cli_table.NewRow           cli_table.index            cli_table.size
cli_table.AddKeys          cli_table.ParseCmd         cli_table.index_file       cli_table.sort
cli_table.Append           cli_table.ReadIndex        cli_table.next             cli_table.superkey
cli_table.CsvToTable       cli_table.Remove           cli_table.raw              cli_table.synchronised
cli_table.FormattedTable   cli_table.Reset            cli_table.row              cli_table.table
cli_table.INDEX            cli_table.RowWith          cli_table.row_class        cli_table.template_dir
cli_table.KeyValue         cli_table.extend           cli_table.row_index
cli_table.LabelValueTable  cli_table.header           cli_table.separator
```

---
### Как использовать CLI table

Например, если вызвать ```print cli_table```, получим такой вывод:
```python
In [7]: print(cli_table)
Network, Mask, Distance, Metric, NextHop
10.0.24.0, /24, 110, 20, ['10.0.12.2']
10.0.34.0, /24, 110, 20, ['10.0.13.3']
10.2.2.2, /32, 110, 11, ['10.0.12.2']
10.3.3.3, /32, 110, 11, ['10.0.13.3']
10.4.4.4, /32, 110, 21, ['10.0.13.3', '10.0.12.2', '10.0.14.4']
10.5.35.0, /24, 110, 20, ['10.0.13.3']
```

---
### Как использовать CLI table

Метод FormattedTable позволяет получить вывод в виде таблицы:
```python
In [8]: print(cli_table.FormattedTable())
 Network    Mask  Distance  Metric  NextHop
====================================================================
 10.0.24.0  /24   110       20      10.0.12.2
 10.0.34.0  /24   110       20      10.0.13.3
 10.2.2.2   /32   110       11      10.0.12.2
 10.3.3.3   /32   110       11      10.0.13.3
 10.4.4.4   /32   110       21      10.0.13.3, 10.0.12.2, 10.0.14.4
 10.5.35.0  /24   110       20      10.0.13.3
```

Такой вывод это просто строка, который может пригодится для отображения информации.

---
### Как использовать CLI table

Чтобы получить из объекта cli_table структурированный вывод, например, список списков, надо обратиться к объекту таким образом:
```python
In [9]: data_rows = [list(row) for row in cli_table]

In [11]: data_rows
Out[11]:
[['10.0.24.0', '/24', '110', '20', ['10.0.12.2']],
 ['10.0.34.0', '/24', '110', '20', ['10.0.13.3']],
 ['10.2.2.2', '/32', '110', '11', ['10.0.12.2']],
 ['10.3.3.3', '/32', '110', '11', ['10.0.13.3']],
 ['10.4.4.4', '/32', '110', '21', ['10.0.13.3', '10.0.12.2', '10.0.14.4']],
 ['10.5.35.0', '/24', '110', '20', ['10.0.13.3']]]

```

---
### Как использовать CLI table

Отдельно можно получить названия столбцов:
```python
In [12]: header = list(cli_table.header)

In [14]: header
Out[14]: ['Network', 'Mask', 'Distance', 'Metric', 'NextHop']
```

Теперь вывод аналогичен тому, который был получен в прошлом разделе.


---
### Как использовать CLI table

Соберем всё в один скрипт (файл textfsm_clitable.py):
```python
import clitable

output_sh_ip_route_ospf = open('output/sh_ip_route_ospf.txt').read()

cli_table = clitable.CliTable('index', 'templates')

attributes = {'Command': 'show ip route ospf' , 'Vendor': 'Cisco'}

cli_table.ParseCmd(output_sh_ip_route_ospf, attributes)
print("CLI Table output:\n", cli_table)

print("Formatted Table:\n", cli_table.FormattedTable())

data_rows = [list(row) for row in cli_table]
header = list(cli_table.header)

print(header)
for row in data_rows:
    print(row)

```

---
### Как использовать CLI table


Вывод будет таким:
```
$ python textfsm_clitable.py
CLI Table output:
Network, Mask, Distance, Metric, NextHop
10.0.24.0, /24, 110, 20, ['10.0.12.2']
10.0.34.0, /24, 110, 20, ['10.0.13.3']
10.2.2.2, /32, 110, 11, ['10.0.12.2']
10.3.3.3, /32, 110, 11, ['10.0.13.3']
10.4.4.4, /32, 110, 21, ['10.0.13.3', '10.0.12.2', '10.0.14.4']
10.5.35.0, /24, 110, 20, ['10.0.13.3']

Formatted Table:
 Network    Mask  Distance  Metric  NextHop
====================================================================
 10.0.24.0  /24   110       20      10.0.12.2
 10.0.34.0  /24   110       20      10.0.13.3
 10.2.2.2   /32   110       11      10.0.12.2
 10.3.3.3   /32   110       11      10.0.13.3
 10.4.4.4   /32   110       21      10.0.13.3, 10.0.12.2, 10.0.14.4
 10.5.35.0  /24   110       20      10.0.13.3

['Network', 'Mask', 'Distance', 'Metric', 'NextHop']
['10.0.24.0', '/24', '110', '20', ['10.0.12.2']]
['10.0.34.0', '/24', '110', '20', ['10.0.13.3']]
['10.2.2.2', '/32', '110', '11', ['10.0.12.2']]
['10.3.3.3', '/32', '110', '11', ['10.0.13.3']]
['10.4.4.4', '/32', '110', '21', ['10.0.13.3', '10.0.12.2', '10.0.14.4']]
['10.5.35.0', '/24', '110', '20', ['10.0.13.3']]

```

