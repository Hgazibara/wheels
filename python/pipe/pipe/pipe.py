import subprocess


class Pipe(object):
    def __init__(self, fn):
        self.fn = fn

    def __ror__(self, data):
        return self.fn(data)


def add():
    return Pipe(sum)


def mul():
    return Pipe(lambda data: reduce(lambda x, y: x*y, data, 1))


def process(command):
    def work(data):
        p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = p.communicate(input=data)
        return stdout
    return Pipe(work)
