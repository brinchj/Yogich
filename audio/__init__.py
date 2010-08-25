from pygame import mixer


def prepare_file(path):
    file(path).read()

def load_file(path):
    return mixer.music.load(path)

