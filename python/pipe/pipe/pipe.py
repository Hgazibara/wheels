import functools
import operator
import subprocess


class Pipe(object):
    def __init__(self, fn):
        self.fn = fn

    def __ror__(self, data):
        return self.fn(data)


def add():
    return Pipe(sum)


def multiply():
    return Pipe(functools.partial(reduce, operator.mul))


def process(command):
    def work(data):
        p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = p.communicate(input=data)
        return stdout
    return Pipe(work)
