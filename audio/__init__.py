import time, pygame


def prepare_file(path):
    file(path).read()

def init():
    pygame.init()
    pygame.mixer.init(44100)

def play_file(path, clock):
    print 'Play called at:', clock()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    print 'Starting playback at:', clock()

def wait(clock):
    while pygame.mixer.music.get_busy():
        print clock(), pygame.mixer.music.get_pos()
        time.sleep(1)

