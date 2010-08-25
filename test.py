#!/usr/bin/env python

import sys
import ntp, clock, audio
from decimal import Decimal

timestamp, path = sys.argv[1:]
timestamp = Decimal(timestamp)

diff = ntp.get_time_more_exact()
real_clock = clock.build_clock(diff)

audio.init()
audio.prepare_file(path)

def player():
    audio.play_file(path)
    audio.wait()

clock.run_at(timestamp, player, real_clock)

