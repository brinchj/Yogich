import time, pygame


def prepare_file(path):
    file(path).read()

def init():
    pygame.init()
    pygame.mixer.init(44100)

def play_file(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def wait():
    while pygame.mixer.music.get_busy():
        time.sleep(1)

