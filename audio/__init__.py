import time, pygame, cStringIO


def prepare_file(path):
    file(path).read()

def init(path):
    pygame.mixer.init(44100)
    return pygame.mixer.Sound(cStringIO.StringIO(file(path).read()))

def play_file(sound, clock):
    print 'Play called at:', clock()
    sound.play()
    print 'Starting playback at:', clock()

def wait(clock):
    while pygame.mixer.get_busy():
        print clock()
        time.sleep(1)

