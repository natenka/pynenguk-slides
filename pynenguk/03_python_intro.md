# Початок роботи з Python

---
## Терміни

* об'єкт
* функція
* атрибут
* метод
* клас
* модуль

---
### Імена змінних

У Python є рекомендації щодо іменування функцій, класів та змінних:

* імена змінних зазвичай пишуться повністю великими чи маленькими літерами: ``DB_NAME``, ``db_name``
* імена функцій задаються маленькими літерами, з підкресленням між словами: ``get_names``
* імена класів задаються словами з великими літерами: ``JuniperDevice``

---
### Типи даних у Python

| Назва    | Назва        | Літерал |
|-------------|-----------------|--------------|
| String      | рядок          | ``"interface Gi0/0"`` |
|             |                 |
| List        | список          | ``[1, 2, 3]`` |
|             |                 |
| Dictionary  | словник         | ``{"username": "user1", "permissions": 100}`` |
|             |                 |
| Tuple       | кортеж          | ``("line console 0", "login local")`` |
|             |                 |
| Set         | множина       | ``{3, 10, 100, 4, 5}`` |
|             |                 |


---
## Клас

```python
user_id = str(100)
file = open("README.md")
```

```python
In [1]: import subprocess

In [2]: result = subprocess.run('ls')

In [3]: result
Out[3]: CompletedProcess(args='ls', returncode=0)
```

---
## Клас

```python
from netmiko import Netmiko


r1 = Netmiko(host="192.168.100.1", username="cisco", password="cisco", device_type="cisco_ios")
r1.enable()
output = r1.send_command(command)
```

---
## Клас

```python
class IPAddress:
    def __init__(self, ip, mask):
        self.address = ip
        self.mask = mask

    def to_bin(self):
        octets = [f"{int(octet):08b}" for octet in self.address.split(".")]
        return "".join(octets)


ip1 = IPAddress("10.1.1.1", 24)
ip2 = IPAddress("10.2.2.2", 24)
```

---
## Клас

```python
import ipaddress


class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask

    def __int__(self):
        int_ip = int(ipaddress.ip_address(self.ip))
        return int_ip

    def __str__(self):
        return f"{self.ip}/{self.mask}"

    def __repr__(self):
        return f"IPAddress('{self.ip}', {self.mask})"

    def __lt__(self, second_ip):
        if type(second_ip) != IPAddress:
            raise TypeError(f"'<' not supported between instances of 'IPAddress'"
                            f" and '{type(second_ip).__name__}'")
        return (int(self), self.mask) < (int(second_ip), second_ip.mask)

    def __eq__(self, second_ip):
        if type(second_ip) != IPAddress:
            raise TypeError(f"'==' not supported between instances of 'IPAddress'"
                            f" and '{type(second_ip).__name__}'")
        return (int(self), self.mask) == (int(second_ip), second_ip.mask)


ip1 = IPAddress("10.1.1.1", 25)
ip2 = IPAddress("10.2.2.2", 25)
```
