from time import time, strftime
from tasks import *


class CalculatingGame:
    def __init__(self, operations):
        self.operations = operations
        self.paused = False
        self.tasks = []
        self.prevtime = 0
        self.fname = strftime('stats/%Y%m%d-%H%M%S.log')

    def log(self, text):
        with open(self.fname, "a") as f:
            f.write(text)
            f.write("\n")

    def getTasks(self):
        return self.tasks

    def processValue(self, val):
        remaining = []
        for task in self.tasks:
            if str(task.getResult()) != val:
                remaining.append(task)
            else:
                self.log("{} died at age: {}".format(str(task), task.getAge()))

        self.tasks = remaining

    def createNewTask(self, num):
        if num == '*':
            self.tasks.append(MultiplyTask())
        elif num == '-':
            self.tasks.append(SubtractionTask())
        elif num == '/':
            self.tasks.append(DivisionTask())
        elif num == '%':
            self.tasks.append(ModulusTask())
        elif num == '+':
            self.tasks.append(AddingTask())
        else:
            assert(False)

    def stepTimer(self):
        if not self.paused:
            remaining = []
            for task in self.tasks:
                task.move()
                if task.getPositionY() < 550:
                    remaining.append(task)
                else:
                    self.log("{} failed".format(str(task)))
            self.tasks = remaining

        curr_time = int(time())
        if curr_time > self.prevtime + 1:
            self.prevtime = curr_time
            index = int(random() * len(self.operations))
            self.createNewTask(self.operations[index])
