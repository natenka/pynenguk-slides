# Python для мережевих інженерів 


---

# Unicode

---

### Навіщо потрібне кодування?

---
### Комп'ютери працюють з байтами

Програми, які ми пишемо, не ізольовані самі по собі. Вони завантажують дані з Інтернету, читають і записують дані на диск і передають дані по мережі.

Тому дуже важливо розуміти різницю між тим, як комп'ютер зберігає і передає дані, і тим, як людина сприймає ці дані. Ми сприймаємо текст, але комп'ютер сприймає байти.

---
### Комп'ютери працюють з байтами


У Python 3, відповідно, є дві концепції:

* Рядки - незмінна послідовність Unicode символів. Для зберігання цих символів використовується тип даних рядок (str)
* Байти (байтовий рядок) - незмінна послідовність байтів. Для зберігання використовується тип bytes

Ми отримуємо байти при роботі з:

* мережею
* файлами


---
### Навіщо потрібне кодування?

Для запису символів у байти, потрібна певна домовленість як вони виглядатимуть:

* A - 0x41
* F - 0x46


---
### Стандарт ASCII

ASCII (American standard code for information interchange) - описує відповідність між символом та його числовим кодом. Описує лише 127 символів:

* коди від 32 до 127 описують друковані символи
* коди до 32 описують спеціальні керуючі символи


![ascii](https://upload.wikimedia.org/wikipedia/commons/4/4f/ASCII_Code_Chart.svg)

---

### ISO Latin 1 (ISO 8859-1)

![latin1](http://rabbit.eng.miami.edu/info/asciiiso.gif)

---

### Windows CP1252

![cp1252](http://rabbit.eng.miami.edu/info/cp1252.gif)

---
### Standards

![standards](https://imgs.xkcd.com/comics/standards.png)

---

### Unicode &#129412;


---

### Стандарт Unicode

* 1,114,112 кодів
* Діапазон 0x0 - 0x10FFFF
* стандарт Unicode версії 15.1 визначає 149813 символів
* кожен код – це число, який відповідає певному символу
* стандарт також визначає кодування - спосіб представлення коду символу в байтах


---
### Приклади символів

* U+1F383 JACK-O-LANTERN &#127875;
* U+2615 HOT BEVERAGE  &#9749;
* U+1f600 GRINNING FACE &#128512;

---
### schön в Unicode

### schön

### U+0073 U+0063 U+0068 U+00f6 U+006e


---

### &#8238; Unicode!

![xkcd](https://imgs.xkcd.com/comics/rtl_2x.png)

---
### Кодування

* UTF-8
* UTF-16
* UTF-32

---
### UTF-8

* дозволяє зберігати символи Unicode
* використовує змінну кількість байтів
* символи ASCII позначаються такими ж кодами

---
### Приклади символів

| H | i | &#128704; | &#128640; | &#9731; |
|:-:|:-:|:---------:|:---------:|:-------:|
| 48|69 | 01 f6 c0  | 01 f6 80  | 26 03   |


---
### Unicode в Python

---
### Unicode в Python

У Python 3 є:

* Рядки - незмінна послідовність Unicode символів. Для збереження цих символів використовується тип рядка (str)
* Байти - незмінна послідовність байтів. Для зберігання використовується тип bytes



---
### Рядки

---
### str

Строка в Python 3 - это последовательность кодов Unicode.

```python
In [2]: anteater = "мурахоїд"

In [3]: type(anteater)
Out[3]: str
```

---
### str

Оскільки рядки - це послідовність кодів Юнікод, можна записати рядок у різний спосіб.

Символ Юнікод можна записати, використовуючи його ім'я:
```python
In [1]: "\N{LATIN SMALL LETTER O WITH DIAERESIS}"
Out[1]: 'ö'
```

Або використовуючи такий формат:
```python
In [4]: "\u00F6"
Out[4]: 'ö'
```

---
### str

Рядок можна записати як послідовність кодів Unicode

```python
In [19]: hi1 = 'вітаю'

In [20]: hi2 = '\u0432\u0456\u0442\u0430\u044e'

In [21]: hi2
Out[21]: 'вітаю'

In [22]: hi1 == hi2
Out[22]: True

In [23]: len(hi2)
Out[23]: 6
```


---
### ord

Функція ord повертає значення коду Unicode для символу:
```python
In [7]: ord('п')
Out[7]: 1087

In [8]: hex(ord("a"))
Out[8]: '0x61'
```

---
### chr

Функція chr повертає рядок із символом Unicode, який відповідає переданому коду:

```python
In [9]: chr(1087)
Out[9]: 'п'

In [10]: chr(8364)
Out[10]: '€'

In [11]: chr(9731)
Out[11]: '☃'

```


---
### bytes

---
### bytes

Тип bytes - це незмінна послідовність байтів.

Байти позначаються так само, як рядки, але з додаванням літери "b" перед лапками.

---
### bytes

```python
In [30]: b1 = b'\xd0\xb4\xd0\xb0'

In [31]: b2 = b"\xd0\xb4\xd0\xb0"

In [32]: b3 = b'''\xd0\xb4\xd0\xb0'''

In [36]: type(b1)
Out[36]: bytes

In [37]: len(b1)
Out[37]: 4
```

---
### ASCII в bytes

Python байти, які відповідають символам ASCII, відображаються як ці символи, а не як відповідні їм байти. Це може трохи плутати, але завжди можна розпізнати тип bytes за літерою b:
```python
In [38]: bytes1 = b'hello'

In [39]: bytes1
Out[39]: b'hello'

In [40]: len(bytes1)
Out[40]: 5

In [42]: bytes2 = b'\x68\x65\x6c\x6c\x6f'

In [43]: bytes2
Out[43]: b'hello'
```

---
### Non ASCII

Якщо спробувати написати не ASCII символ у байтовому літералі, виникне помилка:
```python
In [44]: bytes3 = b'вітаю'
  File "<ipython-input-44-dc8b23504fa7>", line 1
    bytes3 = b'вітаю'
            ^
SyntaxError: bytes can only contain ASCII literal characters.
```

---
### bytes

Можна працювати з байтовими рядками, як з unicode рядками:
```python
In [17]: d = {b'hi':'Hello', b'by':'Goodbye'}

In [18]: d[b'hi']
Out[18]: 'Hello'

In [19]: d['hi']
----------------------------------------------------------
KeyError                 Traceback (most recent call last)
<ipython-input-38-259732fc8381> in <module>()
----> 1 d['hi']

KeyError: 'hi'

```



---
### Конвертація між байтами та рядками

---
### encode vs decode

Уникнути роботи з байтами не вийде. Наприклад, під час роботи з мережею чи файловою системою, результат може повертатися в байтах.

Відповідно, треба знати, як виконувати перетворення байтів у рядок і навпаки. За цю конвертацію відповідає кодування.


## str   .encode() ===> bytes
## bytes .decode() ===> str

---
### encode vs decode

Кодування можна розглядати як ключ шифрування, який визначає:

* як "зашифрувати" рядок у байти (str -> bytes). Використовується метод encode (схожий на слово encrypt)
* як "розшифрувати" байти у рядок (bytes -> str). Використовується метод decode (схожий на decrypt)

Для перетворення рядок-байти та байти-рядок необхідно використовувати однакове кодування.


---
### encode

Для перетворення рядка на байти використовується метод encode:
```python
In [1]: hi = 'вітаю'

In [2]: hi.encode('utf-8')
Out[2]: b'\xd0\xb2\xd1\x96\xd1\x82\xd0\xb0\xd1\x8e'

In [3]: hi_bytes = hi.encode('utf-8')
```

---
### decode

Для отримання рядка з байтів, використовується метод decode:
```python
In [4]: hi_bytes
Out[4]: b'\xd0\xb2\xd1\x96\xd1\x82\xd0\xb0\xd1\x8e'

In [5]: hi_bytes.decode('utf-8')
Out[5]: 'вітаю'
```


---
### Як працювати з Юнікод і байтами

---
### Unicode sandwich

Є просте правило, дотримуючись якого можна уникнути, як мінімум, частини проблем. Воно називається "Юнікод сендвіч":

* Байти, які програма зчитує, треба якомога раніше перетворити на юнікод (рядок)
* всередині програми працювати з рядками
* Рядки треба перетворити на байти якомога пізніше, перед передачею


---
### Приклади конвертації між байтами та рядками

---
### subprocess

---
### subprocess

Модуль subprocess повертає результат команди у вигляді байт:
```python
In [1]: import subprocess

In [2]: result = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'],
   ...:                         stdout=subprocess.PIPE)
   ...:

In [3]: result.stdout
Out[3]: b'PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.\n64 bytes from 8.8.8.8: icmp_seq=1 ttl=43 time=59.4 ms\n64 bytes from 8.8.8.8: icmp_seq=2 ttl=43 time=54.4 ms\n64 bytes from 8.8.8.8: icmp_seq=3 ttl=43 time=55.1 ms\n\n--- 8.8.8.8 ping statistics ---\n3 packets transmitted, 3 received, 0% packet loss, time 2002ms\nrtt min/avg/max/mdev = 54.470/56.346/59.440/2.220 ms\n'
```

---
### subprocess

Якщо далі необхідно працювати з цим виводом, треба одразу конвертувати його в рядок:
```python
In [4]: output = result.stdout.decode('utf-8')

In [5]: print(output)
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=43 time=59.4 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=43 time=54.4 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=43 time=55.1 ms

--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2002ms
rtt min/avg/max/mdev = 54.470/56.346/59.440/2.220 ms
```

---
### subprocess encoding

Модуль subprocess підтримує інший варіант перетворення - параметр encoding.

Якщо вказати його під час виклику функції run, результат буде отримано у вигляді рядка:
```python
In [6]: result = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'],
   ...:                         stdout=subprocess.PIPE, encoding='utf-8')
   ...:

In [7]: result.stdout
Out[7]: 'PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.\n64 bytes from 8.8.8.8: icmp_seq=1 ttl=43 time=55.5 ms\n64 bytes from 8.8.8.8: icmp_seq=2 ttl=43 time=54.6 ms\n64 bytes from 8.8.8.8: icmp_seq=3 ttl=43 time=53.3 ms\n\n--- 8.8.8.8 ping statistics ---\n3 packets transmitted, 3 received, 0% packet loss, time 2003ms\nrtt min/avg/max/mdev = 53.368/54.534/55.564/0.941 ms\n'

In [8]: print(result.stdout)
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=43 time=55.5 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=43 time=54.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=43 time=53.3 ms

--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 53.368/54.534/55.564/0.941 ms
```

---
### telnetlib

---
### telnetlib

Залежно від модуля перетворення між рядками і байтами може виконуватися автоматично, а може виконуватися явно.

Наприклад, у модулі telnetlib необхідно передавати байти у методах read_until та write:

```python
import telnetlib
import time

t = telnetlib.Telnet('192.168.100.1')

t.read_until(b'Username:')
t.write(b'cisco\n')

t.read_until(b'Password:')
t.write(b'cisco\n')
t.write(b'sh ip int br\n')

time.sleep(5)

output = t.read_very_eager().decode('utf-8')
print(output)
```

---
### pexpect

---
### pexpect

Модуль pexpect як аргумент чекає на рядок, а повертає байти:
```python
In [9]: import pexpect

In [10]: output = pexpect.run('ls -ls')

In [11]: output
Out[11]: b'total 8\r\n4 drwxr-xr-x 2 vagrant vagrant 4096 Aug 28 12:16 concurrent_futures\r\n4 drwxr-xr-x 2 vagrant vagrant 4096 Aug  3 07:59 iterator_generator\r\n'

In [12]: output.decode('utf-8')
Out[12]: 'total 8\r\n4 drwxr-xr-x 2 vagrant vagrant 4096 Aug 28 12:16 concurrent_futures\r\n4 drwxr-xr-x 2 vagrant vagrant 4096 Aug  3 07:59 iterator_generator\r\n'
```

---
### pexpect encoding

Pexpect також підтримує передачу кодування через параметр encoding:

```python
In [13]: output = pexpect.run('ls -ls', encoding='utf-8')

In [14]: output
Out[14]: 'total 8\r\n4 drwxr-xr-x 2 vagrant vagrant 4096 Aug 28 12:16 concurrent_futures\r\n4 drwxr-xr-x 2 vagrant vagrant 4096 Aug  3 07:59 iterator_generator\r\n'
```

---
### Робота з файлами

---
### Робота з файлами

```python
with open(filename) as f:
    for line in f:
        print(line)
```

---
### Кодування за замовчуванням

Під час читання файлу відбувається конвертація байтів у рядки. І при цьому використовувалося кодування за замовчуванням:
```python
In [1]: import locale

In [2]: locale.getpreferredencoding()
Out[2]: 'UTF-8'
```

---
### Кодування за замовчуванням

Кодування за замовчуванням у файлі:
```python
In [2]: f = open('r1.txt')

In [3]: f
Out[3]: <_io.TextIOWrapper name='r1.txt' mode='r' encoding='UTF-8'>
```

---
### Явне кодування

При роботі з файлами краще явно вказувати кодування, тому що в різних ОС воно може відрізнятися:

```python
In [4]: with open('r1.txt', encoding='utf-8') as f:
   ...:     for line in f:
   ...:         print(line, end='')
   ...:
!
service timestamps debug datetime msec localtime show-timezone year
service timestamps log datetime msec localtime show-timezone year
service password-encryption
service sequence-numbers
!
no ip domain lookup
!
ip ssh version 2
!
```


---
### Помилки при конвертації

---
### Помилки при конвертації

При конвертації між рядками та байтами дуже важливо точно знати, яке кодування використовується, а також знати про можливості різних кодувань.

---
### Помилки

Наприклад, кодування ASCII не може перетворити на байти кирилицю:
```python
In [32]: hi_unicode = 'вітаю'

In [33]: hi_unicode.encode("ascii")
---------------------------------------------------------------------------
UnicodeEncodeError                        Traceback (most recent call last)
Input In [33], in <module>
----> 1 hi_unicode.encode("ascii")

UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-4: ordinal not in range(128)
```

---
### Помилки

Аналогічно, якщо рядок "вітаю" перетворено на байти, і спробувати перетворити байти на рядок за допомогою ascii, теж отримаємо помилку:

```python
In [34]: hi_unicode = 'вітаю'

In [35]: hi_bytes = hi_unicode.encode('utf-8')

In [36]: hi_bytes.decode("ascii")
---------------------------------------------------------------------------
UnicodeDecodeError                        Traceback (most recent call last)
Input In [36], in <module>
----> 1 hi_bytes.decode("ascii")

UnicodeDecodeError: 'ascii' codec can't decode byte 0xd0 in position 0: ordinal not in range(128)
```

---
### Помилки

Ще один варіант помилки, коли використовуються різні кодування для перетворень:
```python
In [37]: de_hi_unicode = 'grüezi'

In [38]: utf_16 = de_hi_unicode.encode('utf-16')

In [39]: utf_16.decode('utf-8')
---------------------------------------------------------------------------
UnicodeDecodeError                        Traceback (most recent call last)
<ipython-input-39-4b4c731e69e4> in <module>()
----> 1 utf_16.decode('utf-8')

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
```

---
### Треба знати яке кодування використовувалося

Насправді попередні помилки - це добре. Вони явно вказують, у чому проблема.

Гірше, коли виходить так:
```python
In [28]: hi_unicode = "вітаю"

In [29]: hi_bytes = hi_unicode.encode("utf-8")

In [30]: hi_bytes
Out[30]: b'\xd0\xb2\xd1\x96\xd1\x82\xd0\xb0\xd1\x8e'

In [31]: hi_bytes.decode("utf-16")
Out[31]: '닐雑苑냐軑'
```

---
### Обробка помилок

---
### Обробка помилок

Методи encode та decode мають режими обробки помилок, які вказують, як реагувати на помилку конвертації.


---
### encode replace

За замовчуванням кодування використовує режим "strict" - якщо виникають помилки кодування, генерується виняток UnicodeError. Приклади такої поведінки були наведені вище.

Режим replace замінить символ знаком питання:
```python
In [44]: de_hi_unicode = 'grüezi'

In [45]: de_hi_unicode.encode('ascii', 'replace')
Out[45]: b'gr?ezi'
```

---
### encode namereplace

Режим namereplace, заміняє символ на ім'я символу:
```python
In [46]: de_hi_unicode = 'grüezi'

In [47]: de_hi_unicode.encode('ascii', 'namereplace')
Out[47]: b'gr\\N{LATIN SMALL LETTER U WITH DIAERESIS}ezi'
```

---
### encode ignore

Крім того, можна повністю ігнорувати символи, які не можна конвертувати:
```python
In [48]: de_hi_unicode = 'grüezi'

In [49]: de_hi_unicode.encode('ascii', 'ignore')
Out[49]: b'grezi'
```

---
### Параметр errors в decode

У методі decode за замовчуванням також використовується режим strict і генерується виняток UnicodeDecodeError.

---
### decode ignore

Якщо змінити режим на ignore, як і в encode, символи просто ігноруватимуться:
```python
In [50]: de_hi_unicode = 'grüezi'

In [51]: de_hi_utf8 = de_hi_unicode.encode('utf-8')

In [52]: de_hi_utf8
Out[52]: b'gr\xc3\xbcezi'

In [53]: de_hi_utf8.decode('ascii', 'ignore')
Out[53]: 'grezi'
```

---
### decode replace

Режим replace замінить символи:
```python
In [54]: de_hi_unicode = 'grüezi'

In [55]: de_hi_utf8 = de_hi_unicode.encode('utf-8')

In [56]: de_hi_utf8.decode('ascii', 'replace')
Out[56]: 'gr��ezi'
```

---


1. &#128013; [Pragmatic Unicode](https://nedbatchelder.com/text/unipain.html)
2. &#129417; [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
3. &#128013; [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)
