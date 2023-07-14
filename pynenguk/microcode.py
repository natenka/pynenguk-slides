text = """
## try/except/else/finally

```python
num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")

try:
    result = int(num1)/int(num2)
except (ValueError, ZeroDivisionError):
    print("Щось пішло не так...")
```

```python
try:
    result = int(num1)/int(num2)
except ValueError:
    print("Вводьте лише числа")
except ZeroDivisionError:
    print("На нуль ділити не можна")
```


```python
try:
    result = int(num1)/int(num2)
except (ValueError, ZeroDivisionError):
    print("Щось пішло не так...")
else:
    print("Результат: ", result**2)
```

```python
try:
    result = int(num1)/int(num2)
except (ValueError, ZeroDivisionError):
    print("Щось пішло не так...")
else:
    print("Результат: ", result**2)
finally:
    print("The End")
```
"""
from rich.console import Console
from rich.markdown import Markdown
from rich.padding import Padding


console = Console()
md = Markdown(text)
console.clear()
console.print(Padding(md, (0, 8)))

