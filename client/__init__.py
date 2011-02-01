from threading import Thread
import struct
import time

from lib.audio import play_file, prepare_file
from lib.clock import run_at, build_clock
from lib.ntp import get_time_more_exact

from socket import socket, AF_INET, SOCK_DGRAM, \
     SOL_SOCKET, SO_BROADCAST

now = build_clock(get_time_more_exact())
nowi = lambda: int(now())


class Downloader(Thread):
    def __init__(self, playlist):
        Thread.__init__(self)
        self.daemon = True
        self.playlist = playlist

    def run(self):
        pass


class Player(Thread):
    def __init__(self, playlist):
        Thread.__init__(self)
        self.daemon = True
        self.playlist = playlist

    def run(self):
        while True:
            if not self.playlist or self.playlist[0][0] < nowi() + 5:
                time.sleep(1)
                continue

            def play():
                play_file('sailor')
            prepare_file('sailor')
            run_at(self.playlist[0][0], play, now)


class Listener(Thread):
    def __init__(self, playlist, port=13131):
        Thread.__init__(self)
        self.daemon = True
        self.playlist = playlist
        self.port = port
        self.socket = None

    def update(self, buf):
        l = len(buf) / 8
        data = struct.unpack('!' + ('q' * l), buf)
        lst = []
        for i in xrange(0, len(data), 2):
            lst.append(tuple(data[i:i + 2]))
        self.playlist[:] = lst

    def run(self):
        while True:
            self.socket = socket(AF_INET, SOCK_DGRAM)
            self.socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
            self.socket.bind(('', self.port))
            buf, _ = self.socket.recvfrom(4096)
            self.update(buf)


class Client:
    def __init__(self):
        self.playlist = []
        self.downloader = Downloader(self.playlist)
        self.listener = Listener(self.playlist)
        self.player = Player(self.playlist)

    def start(self):
        for i in (self.downloader, self.listener, self.player):
            i.start()
