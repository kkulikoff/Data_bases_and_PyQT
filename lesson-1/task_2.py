"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""
import ipaddress
from task_1 import host_ping


def host_range_ping():
    addresses = []
    IP1 = ipaddress.ip_address('192.168.1.0')

    for ip in range(10):
        IP1 += 1
        addresses.append(str(IP1))
    # pprint(addresses)
    return host_ping(addresses)


if __name__ == '__main__':
    host_range_ping()