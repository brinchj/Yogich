#!/usr/bin/env python

import sys, subprocess
import ntp, clock, audio
from decimal import Decimal

timestamp, path = sys.argv[1:]
timestamp = Decimal(timestamp)

diff = ntp.get_time_more_exact()
real_clock = clock.build_clock(diff)

#audio.prepare_file(path)
#sound = audio.init(path)

CMD = ['mplayer', path]

def player():
    #sound.play()
    subprocess.call(CMD)
    audio.wait(real_clock)

clock.run_at(timestamp, player, real_clock)

