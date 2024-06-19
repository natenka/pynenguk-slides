# Python для мережевих інженерів 

---

## Об'єктно-орієнтоване програмування (ООП)

---

## Об'єктно-орієнтоване програмування (ООП)

Об'єктно-орієнтоване програмування (ООП) - методологія програмування, заснована на представленні програми у вигляді сукупності об'єктів, кожен із яких є екземпляром певного класу, а класи утворюють ієрархію наслідування

---
### Терміни

* Клас (Class) – елемент програми, який описує якийсь тип даних. Клас описує шаблон для створення об'єктів, як правило, вказує змінні цього об'єкта та дії, які можна виконувати застосовно до об'єкта.
* Екземпляр  класу (Instance) – об'єкт, який є представником класу.
* Метод (Method) - функція, яка визначена всередині класу та описує якусь дію, яка підтримує клас
* Змінна екземпляра (instance variable, а іноді й instance attribute) - дані, що належать до об'єкта
* Змінна класу (class variable) - дані, що відносяться до класу та поділяються всіма екземплярами класу
* Атрибут екземпляра (instance attribute) - змінні та методи, що відносяться до об'єктів (екземплярів), створених на підставі класу. Кожен об'єкт має свою копію атрибутів.

---
### Створення класу

---
### Створення класу


```python
In [1]: class Switch:
   ...:     pass
   ...:

In [2]: sw1 = Switch()
```

---
### Атрибути

```python
In [3]: sw1 = Switch()
In [4]: sw2 = Switch()

In [5]: sw1.hostname = 'sw1'
In [6]: sw1.model = 'Cisco 3850'

In [7]: sw2.hostname = 'sw2'
In [8]: sw2.model = 'Cisco 3750'
```

---
### Атрибуты

```python
In [13]: sw1.model
Out[13]: 'Cisco 3850'

In [14]: sw2.model
Out[14]: 'Cisco 3750'
```


---
### Методи

```python
In [15]: class Switch:
    ...:     def info(self):
    ...:         print('Hostname: {}\nModel: {}'.format(self.hostname, self.model))
    ...:
```

---
### Методи

```python
In [16]: sw1 = Switch()

In [17]: sw1.hostname = 'sw1'

In [18]: sw1.model = 'Cisco 3850'

In [19]: sw1.info()
Hostname: sw1
Model: Cisco 3850
```

---
### `__init__`

```python
In [32]: class Switch:
    ...:     def __init__(self, hostname, model):
    ...:         self.hostname = hostname
    ...:         self.model = model
    ...:
    ...:     def info(self):
    ...:         print('Hostname: {}\nModel: {}'.format(self.hostname, self.model))
    ...:
```

---
### `__init__`

```python
In [33]: sw1 = Switch('sw1', 'Cisco 3850')

In [36]: sw1.info()
Hostname: sw1
Model: Cisco 3850

In [37]: sw1.hostname
Out[37]: 'sw1'
```

---
### self

Ці варіанти рівнозначні:
```python
In [38]: Switch.info(sw1)
Hostname: sw1
Model: Cisco 3850

In [39]: sw1.info()
Hostname: sw1
Model: Cisco 3850
```

---
### self

```python
In [40]: class Switch:
    ...:     def __init__(self, hostname, model):
    ...:         self.hostname = hostname
    ...:         self.model = model
    ...:

In [41]: def info(sw_obj):
    ...:     print('Hostname: {}\nModel: {}'.format(sw_obj.hostname, sw_obj.model))
    ...:

In [42]: sw1 = Switch('sw1', 'Cisco 3850')

In [43]: info(sw1)
Hostname: sw1
Model: Cisco 3850
```


---
### Спеціальні методи

---
### Одне підкреслення перед ім'ям

Одне підкреслення перед ім'ям вказує, що ім'я використовується як внутрішнє, що цей об'єкт є внутрішньою особливістю реалізації і його не варто використовувати безпосередньо

```python
class Switch:
    def _get_display_str(self):
        hostname = getattr(self, 'hostname', None)
        model = getattr(self, 'model', None)
        return 'Hostname: {}, Model: {}'.format(hostname, model)

    def __str__(self):
        return self._get_display_str()
```

---
### Два підкреслення перед ім'ям

Два підкреслення перед ім'ям методу чи аргументу використовуються не просто як домовленість. Такі імена трансформуються у формат "ім'я класу + ім'я методу". Це дозволяє створювати унікальні методи та атрибути класів.

> Таке перетворення виконується лише в тому випадку, якщо наприкінці менше двох підкреслень чи ні підкреслень



---
### Два підкреслення перед ім'ям

```python
class Switch:
    def __get_display_str(self):
        hostname = getattr(self, 'hostname', None)
        model = getattr(self, 'model', None)
        return 'Hostname: {}, Model: {}'.format(hostname, model)

    def __str__(self):
        return self.__get_display_str()
```

---
### Два підкреслення перед ім'ям

```python
In [1]: sw1 = Switch()

In [2]: dir(sw1)
Out[2]:
['_Switch__get_display_str',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
...
 '__weakref__']

In [3]: print(sw1)
Hostname: None, Model: None

```

---
### Два підкреслення перед і після імені

Таким чином позначаються спеціальні змінні та методи.

Ці методи викликаються при використанні функцій та операторів Python та дозволяють реалізувати певний функціонал.

Як правило, такі методи не потрібно викликати безпосередньо. Але, наприклад, при створенні свого класу може знадобитися описати такий метод, щоб об'єкт підтримував якісь операції в Python.


---
### Два підкреслення перед і після імені

```python
class Switch:
    def __init__(self, hostname, model):
        self.hostname = hostname
        self.model = model

    def __str__(self):
        return 'Hostname: {}, Model: {}'.format(self.hostname, self.model)

    def __del__(self):
        print("Я умираю....")
```

```python
In [2]: sw1 = Switch('sw1', 'cisco')

In [3]: del sw1
Я умираю....

In [4]: sw1
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-4-924218d7093c> in <module>()
----> 1 sw1

NameError: name 'sw1' is not defined
```

---
### `__str__`

---
### `__str__`

```python
In [45]: class Switch:
    ...:     def __init__(self, hostname, model):
    ...:         self.hostname = hostname
    ...:         self.model = model
    ...:

In [46]: sw1 = Switch('sw1', 'Cisco 3850')

In [47]: print(sw1)
<__main__.Switch object at 0xb4e47d8c>
```

---
### `__str__`

```python
In [52]: class Switch:
    ...:     def __init__(self, hostname, model):
    ...:         self.hostname = hostname
    ...:         self.model = model
    ...:
    ...:     def __str__(self):
    ...:         return 'Hostname: {}, Model: {}'.format(self.hostname, self.model)
    ...:

In [53]: sw1 = Switch('sw1', 'Cisco 3850')

In [54]: print(sw1)
Hostname: sw1, Model: Cisco 3850

In [55]: str(sw1)
Out[55]: 'Hostname: sw1, Model: Cisco 3850'
```

---
### `__add__`

---
### `__add__`

Метод __add__ викликається, коли у виразі використовується +.
Наприклад, вираз `a + b` перетворюється на `a.__add__(b)`

```python
In [5]: class MyNum:
   ...:     def __init__(self, num):
   ...:         self.num = num
   ...:
   ...:     def __add__(self, other):
   ...:         return MyNum(self.num + other.num)
   ...:

In [6]: a = MyNum(5)

In [7]: b = MyNum(10)

In [8]: c = a + b

In [9]: c.num
Out[9]: 15
```
