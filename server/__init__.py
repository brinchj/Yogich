
import re
import time
import struct
from subprocess import PIPE, Popen

from socket import socket, SOL_SOCKET, SO_BROADCAST, AF_INET, SOCK_DGRAM
from threading import Thread

from lib.clock import build_clock
from lib.ntp import get_time_more_exact


now = build_clock(get_time_more_exact())
nowi = lambda: int(now())


class Track:
    def __init__(self, path):
        self.path = path
        self.duration = None

    def get_duration(self):
        if self.duration is None:
            proc = Popen([
                'mplayer',
                '-vo', 'null', '-ao', 'null',
                '-frames', '0', '-identify',
                self.path,
                ], stdout=PIPE, stderr=PIPE)
            stdout = proc.communicate()[0]
            match = re.search(r'ID_LENGTH=(\d+(\.\d+)?)', stdout)
            self.duration = float(match.group(1))
        return self.duration

    def id(self):
        return 4  # Random id, chosen by a fair dice roll.


class Playlist:
    def __init__(self):
        self.tracks = None

    def add_next(self, track):
        if self.tracks is None:
            self.tracks = [(int(now()) + 10, track)]
        else:
            prev_t, prev_track = self.tracks[-1]
            next_t = prev_t + prev_track.get_duration() + 5
            self.tracks.append((next_t, track))

    def clean(self):
        while self.tracks and self.tracks[0][0] < nowi():
            self.tracks.pop(0)

    def pack(self):
        self.clean()
        lst = []
        for t, track in self.tracks[0:5]:
            lst.extend([t, track.id()])
        return struct.pack('!' + ('qq' * len(self.tracks)), *lst)


class Server(Thread):
    def __init__(self, port=13131):
        Thread.__init__(self)
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        self.daemon = True
        self.port = port

        self.playlist = Playlist()
        self.playlist.add_next(Track("sailor"))
        self.playlist.add_next(Track("toybox.wav"))

    def run(self):
        while True:
            self.broadcast()
            time.sleep(15)

    def broadcast(self):
        print '> send', len(self.playlist.pack())
        self.socket.sendto(self.playlist.pack(),
                           ('255.255.255.255', self.port))
