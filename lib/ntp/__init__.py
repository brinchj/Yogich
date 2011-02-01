from socket import socket, AF_INET, SOCK_DGRAM, timeout
from decimal import Decimal as Dec
from lib import clock

import struct
import time

TIME1970 = 2208988800L  # NTP


def get_time():
    NTP_SERVER = '130.225.96.8'

    client = socket(AF_INET, SOCK_DGRAM)
    data = '\x1b' + 47 * '\0'
    client.settimeout(1)

    for i in xrange(20):
        try:
            start = clock.now()
            client.sendto(data, (NTP_SERVER, 123))
            data, address = client.recvfrom(1024)
            time_used = clock.now() - start
            break
        except timeout:
            time.sleep(.1 * i)
            continue

    if data:
        s = struct.unpack('!12I', data)
        return start, time_used, Dec(s[10]), Dec(s[11])


def get_time_exact():
    time_used = 1
    while time_used > Dec(str(0.05)):
        time_start, time_used, secs, frac = get_time()
    his = time_start + time_used / 2
    her = secs + (frac / Dec(2 ** 32)) + (time_used / 2) - TIME1970
    return his - her


def get_time_more_exact():
    tries = 10
    msum = Dec(0)
    for n in xrange(tries):
        msum += get_time_exact()
        time.sleep(0.005)
    return msum / tries
