import random
import numpy as np

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Task:
    def __init__(self, start, time):
        self.start = start
        self.end = None
        self.time = time


class Washing:
    def __init__(self):
        self.tasks = Queue()
        self.prob_task = 400
        self.prob_time = (300, 600)
        self.current_task = None

    def simulation(self, max_time):
        waiting = []
        for t in range(max_time):
            if random.randrange(1, self.prob_task + 1) == self.prob_task:
                time = random.randrange(self.prob_time[0], self.prob_time[1] + 1)
                self.tasks.enqueue(Task(t, time))
            if not self.current_task and not self.tasks.isEmpty():
                new_task = self.tasks.dequeue()
                new_task.end = t
                waiting.append(new_task.end - new_task.start)
                self.current_task = new_task
            if self.current_task:
                self.current_task.time -= 1
                if self.current_task.time == 0:
                    self.current_task = None
        return round(np.array(waiting).mean(), 1), self.tasks.size()


if __name__ == '__main__':
    for i in range(10):
        w = Washing()
        t = w.simulation(3600)
        print(f'mean: {t[0]}\t\tremaining: {t[1]}')
