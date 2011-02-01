import subprocess


def prepare_file(path):
    file(path).read()


def play_file(path):
    subprocess.call(['mplayer', path])
