from decimal import Decimal as Dec
from datetime import datetime
import time


def now(diff=0):
    delta = datetime.now() - datetime.fromtimestamp(0)
    now = Dec(delta.days*3600*24) + Dec(delta.seconds) + Dec(delta.microseconds)/1000000
    return now - diff

def build_clock(diff):
    return lambda: now(diff)

def run_at(t, fun, clock):
    while clock()+Dec('0.02') < t:
        time.sleep(0.001)

    while clock() < t:
        pass

    fun()

