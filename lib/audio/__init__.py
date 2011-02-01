import subprocess


def prepare_file(path):
    file(path).read()


def play_file(path, clock):
    print 'Play called at:', clock()
    subprocess.call(['mplayer', path])
    print 'Starting playback at:', clock()
