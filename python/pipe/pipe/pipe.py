class Pipe(object):
    def __init__(self, fn):
        self.fn = fn

    def __ror__(self, data):
        return self.fn(data)


def add():
    return Pipe(sum)
