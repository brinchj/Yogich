import time, pygame


def prepare_file(path):
    file(path).read()

def init(path):
    pygame.init()
    pygame.mixer.init(44100)
    pygame.mixer.music.load(path)

def play_file(clock):
    print 'Play called at:', clock()
    pygame.mixer.music.play()
    print 'Starting playback at:', clock()

def wait(clock):
    while pygame.mixer.music.get_busy():
        print clock(), pygame.mixer.music.get_pos()
        time.sleep(1)

