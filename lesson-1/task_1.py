"""
1. Написать функцию host_ping(),
в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список,
в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»).
При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
"""
from subprocess import Popen, PIPE, STDOUT
import platform
import chardet
import locale
import socket


def ip_addresses():
    addresses = []
    proc = Popen('curl -sS ifconfig.me/ip'.split(), stdout=PIPE)
    my_public_ip = proc.stdout.read().decode(locale.getpreferredencoding())
    addresses.append(my_public_ip)

    my_local_ip = socket.gethostbyname(socket.gethostname())
    addresses.append(my_local_ip)

    bad_address = '1.2.3.4'
    addresses.append(bad_address)

    return addresses


def host_ping(hosts):
    result_list = []
    PARAM = "-n" if platform.system().lower() == 'windows' else "-c"
    for host in hosts:
        ARGS = ["ping", PARAM, "1", host]
        process = Popen(ARGS, stdout=PIPE, stderr=STDOUT)
        stdout_data, stderr_data = process.communicate()
        result = chardet.detect(stdout_data)
        out = stdout_data.decode(result['encoding'])
        if 'TTL' in out:
            print(f'{host} - Узел доступен')
            result_list.append((host, ''))
        else:
            print(f'{host} - Узел не доступен')
            result_list.append(('', host))

    return result_list


if __name__ == '__main__':
    host_ping(ip_addresses())
