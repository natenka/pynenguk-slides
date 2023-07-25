# Робота з файлами

---
## Робота з файлами

При роботі з мережевим обладнанням (і не тільки) файлами можуть бути:

* конфігурації (прості, не структуровані текстові файли) - робота з ними розглядається в цьому розділі
* шаблони конфігурацій - зазвичай це якийсь спеціальний формат файлів
* файли з параметрами підключень. Як правило, це структуровані файли, в певному форматі: YAML, JSON, CSV


---
### Робота з файлами

У роботі з файлами є кілька аспектів:

* відкриття/закриття
* читання
* запис

---
### Робота з файлами

```
R1#show ip interface brief
Interface                  IP-Address      OK? Method Status           Protocol
FastEthernet0/0            15.0.15.1       YES manual up               up
FastEthernet0/1            10.0.12.1       YES manual up               up
FastEthernet0/2            10.0.13.1       YES manual up               up
FastEthernet0/3            unassigned      YES unset  up               down
Loopback0                  10.1.1.1        YES manual up               up
Loopback100                100.0.0.1       YES manual up               up
```

```
Ethernet0/0 is up, line protocol is up
  Internet address is 192.168.100.1/24
  Broadcast address is 255.255.255.255
  Address determined by non-volatile memory
  MTU is 1500 bytes
  Helper address is not set
  ...
Ethernet0/1 is up, line protocol is up
  Internet address is 192.168.200.1/24
  Broadcast address is 255.255.255.255
  Address determined by non-volatile memory
  MTU is 1500 bytes
  Helper address is not set
  ...
Ethernet0/2 is up, line protocol is up
  Internet address is 19.1.1.1/24
  Broadcast address is 255.255.255.255
  Address determined by non-volatile memory
  MTU is 1500 bytes
  Helper address is not set
  ...
```

---
### Робота з файлами

```
Current configuration : 2033 bytes
!
! Last configuration change at 13:11:59 UTC Thu Feb 25 2016
!
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname sw1
!
!
!
interface FastEthernet0/0
 switchport mode access
 switchport access vlan 10
!
interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100,200
 switchport mode trunk
!
interface FastEthernet0/2
 switchport mode access
 switchport access vlan 20
!         
interface FastEthernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100,300,400,500,600
 switchport mode trunk
!         
interface FastEthernet1/0
 switchport mode access
 switchport access vlan 20
!
interface FastEthernet1/1
 switchport mode access
 switchport access vlan 30
!
interface FastEthernet1/2
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 400,500,600
 switchport mode trunk
!
interface Vlan100
 ip address 10.0.100.1 255.255.255.0
!
!
alias configure sh do sh 
alias exec ospf sh run | s ^router ospf
alias exec vc sh mpls l2tr vc
!
line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
line aux 0
line vty 0 4
 login
 transport input all
!
end
```

---
## Відкриття файлів

Для початку роботи з файлом його треба відкрити.

Для відкриття файлів найчастіше використовується функція open:

```python
file = open('file_name.txt', 'r')
```

У функції open:

* `'file_name.txt'` - ім'я файлу. Тут можна вказувати ім'я файлу або шлях (абсолютний чи відносний)
* `'r'` - режим відкриття файлу


---
### Режими відкриття файлів

| Символ | Значення |
|--------|-----------|
| `"r"` | відкритий для читання (за замовчуванням) |
| `"w"` | відкрити для запису, спочатку видаливши вміст файлу |
| `"x"` | відкрити для ексклюзивного створення, якщо файл уже існує, виникає виняток FileExistsError |
| `"а"` | відкрити для запису, додаючи в кінець файлу, якщо він існує |
| `"b"` | двійковий режим |
| `"t"` | текстовий режим (за замовчуванням) |
| `"+"` | відкритий для оновлення (читання та запис) |


Python розрізняє двійковий і текстовий ввід-вивід.  Файли, відкриті в
двійковому режимі (із буквою `b` в аргументі mode), повертають вміст як об'єкти
байти (bytes) без будь-якого декодування. У текстовому режимі (за
замовчуванням, або коли `t` включено в аргумент режиму), вміст файлу
повертається як рядок, відповідно байти були спочатку декодовані з
використанням кодування.

---
### Режими відкриття файлів

* `r` - відкрити файл тільки для читання (за замовчуванням)
* `w` - відкрити файл для запису
    * якщо файл існує, його вміст видаляється
    * якщо файл не існує, то створюється новий
* `x` – відкрити файл для ексклюзивного створення:
    * якщо файл існує, запис не відбувається
    * якщо файл не існує, то створюється новий
* `a` – відкрити файл для доповнення запису. Дані додаються до кінця файлу


---
### Режими відкриття файлів

| Режим відкриття            | r | r+ | w | w+ | a | a+ | x | x+ |
|----------------------------|---|----|---|----|---|----|---|----|
| читання                    | + | +  |   | +  |   | +  |   | +  |
| запис                      |   | +  | + | +  | + | +  | + | +  |
| створення нового файлу     |   |    | + | +  | + | +  | + | +  |
| відкриття існуючого файлу  |   |    | + | +  | + | +  |   |    |
| вміст файлу видаляється    |   |    | + | +  |   |    |   |    |
| позиція на початку         | + | +  | + | +  |   |    | + | +  |
| позиція в кінці            |   |    |   |    | + | +  |   |    |
| запис після seek           |   | +  | + | +  |   |    | + | +  |


---
## Читання файлів

У Python є кілька варіантів читання файлу:

* перебирати файл у циклі for
* метод `read` - зчитує вміст файлу в рядок
* метод `readline` - зчитує один рядок
* метод `readlines` - зчитує рядки файлу та створює список із рядків

---
## Блок with

У Python існує більш зручний спосіб роботи з файлами, ніж ті, які
використовувалися досі - конструкція with.  Конструкція with називається
менеджер контексту.


```python
with open('r1.txt', 'r') as f:
    for line in f:
        print(line)
```


---
## Запис файлів

При записі в файл дуже важливо визначитися з режимом відкриття файлу, щоб
випадково не видалити вміст файлу:

* `w` - відкрити файл для запису. Якщо файл існує, то його вміст видаляється
* `a` - відкрити файл для доповнення запису. Дані додаються в кінці файлу
* `x` - відкрити файл для запису. Якщо файл існує, запис не виконується

Всі режими створюють файл, якщо він не існує.

Для запису в файл використовуються такі методи:

* write - записати один рядок у файл
* writelines - дозволяє передавати список рядків як аргумент

