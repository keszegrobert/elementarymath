from time import time, strftime
from random import random


class Task:
    def __init__(self):
        self.left = int(random() * 15)
        self.right = int(random() * 15)
        self.x = int(random() * (800 - 100))
        self.y = 0
        self.deltax = 5
        self.starttime = time()
        self.prevtime = 0

    def move(self):
        self.y += self.deltax

    def getPositionX(self):
        return self.x

    def getPositionY(self):
        return self.y

    def getAge(self):
        return time() - self.starttime


class MultiplyTask(Task):
    def __init__(self):
        Task.__init__(self)

    def __repr__(self):
        return '{} * {}'.format(self.left, self.right)

    def getResult(self):
        return self.left * self.right


class AddingTask(Task):
    def __init__(self):
        Task.__init__(self)

    def __repr__(self):
        return '{} + {}'.format(self.left, self.right)

    def getResult(self):
        return self.left + self.right


class SubtractionTask(Task):
    def __init__(self):
        Task.__init__(self)

    def __repr__(self):
        return '{} - {}'.format(self.left, self.right)

    def getResult(self):
        return self.left - self.right


class DivisionTask(Task):
    def __init__(self):
        Task.__init__(self)
        while self.right == 0:
            self.right = int(random() * 15)

    def __repr__(self):
        return '{} / {}'.format(self.left, self.right)

    def getResult(self):
        return self.left // self.right


class ModulusTask(Task):
    def __init__(self):
        Task.__init__(self)
        while self.right == 0:
            self.right = int(random() * 15)

    def __repr__(self):
        return '{} mod {}'.format(self.left, self.right)

    def getResult(self):
        return self.left % self.right
