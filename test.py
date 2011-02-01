#!/usr/bin/env python

import sys
import ntp
import clock
import audio
from decimal import Decimal

timestamp, path = sys.argv[1:]
timestamp = Decimal(timestamp)

diff = ntp.get_time_more_exact()
real_clock = clock.build_clock(diff)


def player():
    audio.play_file(path, real_clock)


clock.run_at(timestamp, player, real_clock)
