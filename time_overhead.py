#!/usr/bin/env python

import sys
import subprocess
import ntp
import clock


path = sys.argv[1]
diff = ntp.get_time_more_exact()
real_clock = clock.build_clock(diff)

CMD = ['mplayer', '-endpos', '5', path]


def player():
    print 'play:', real_clock()
    subprocess.call(CMD)
    print 'done:', real_clock()

clock.run_at(real_clock(), player, real_clock)
