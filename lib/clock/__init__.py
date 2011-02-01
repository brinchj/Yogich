from decimal import Decimal as Dec
from datetime import datetime
import time


def now(*args):
    return now_exact(*args)


def now_exact(diff=0):
    delta = datetime.utcnow() - datetime.utcfromtimestamp(0)
    now = Dec(delta.days * 3600 * 24) + \
          Dec(delta.seconds) + \
          Dec(delta.microseconds) / 1000000
    return now - diff


def build_clock(diff=0):
    return lambda: now(diff)


def run_at(start_time, fun, clock):
    critical = Dec('0.02')
    while clock() + critical < start_time:
        time.sleep(0.001)
    while clock() < start_time:
        pass
    fun()
