#!/usr/bin/env python

from lib import clock, ntp
import time
import sys

diff = ntp.get_time_more_exact()
clck = clock.build_clock(diff)

print 'click:',
sys.stdin.readline()

for i in xrange(10):
    print clck()
    time.sleep(1)
