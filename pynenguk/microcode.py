text = """
### Оператори and, or, not

```python
r1 = {
    'ios': '15.4',
    'ip': '10.255.0.1',
    'hostname': 'london_r1',
    'location': '21 New Globe Walk',
    'model': '4451',
    'vendor': 'Cisco'
}
vlan = [10, 20, 30, 40]


In [19]: 'ios' in r1 and 10 in vlan
Out[19]: True

In [20]: '4451' in r1 and 10 in vlan
Out[20]: False

In [21]: '4451' in r1 or 10 in vlan
Out[21]: True

In [23]: '4451' not in r1
Out[23]: True

```

"""
from rich.console import Console
from rich.markdown import Markdown
from rich.padding import Padding


console = Console()
md = Markdown(text)
console.clear()
console.print(Padding(md, (0, 8)))

