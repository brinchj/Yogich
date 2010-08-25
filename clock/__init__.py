from decimal import Decimal as Dec
from datetime import datetime
import time


def now(diff=0):
    delta = datetime.now() - datetime.fromtimestamp(0)
    now = Dec(delta.days*3600*24) + Dec(delta.seconds) + Dec(delta.microseconds)/1000000
    return now - diff
