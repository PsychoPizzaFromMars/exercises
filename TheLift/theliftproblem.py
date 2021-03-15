class Dinglemouse(object):
    def __init__(self, queues, capacity):
        self.queues = [list(i) for i in queues]
        self.capacity = capacity
        self.passengers = []
        self.path = [0]

    def theLift(self):
        while [el for i in self.queues for el in i if el != self.queues.index(i)]:
            # Go up
            for i, floor in enumerate(self.queues):
                up_queue = list(filter(lambda x: x > i, floor))
                if up_queue or i in self.passengers:
                    if i != self.path[-1]:
                        self.path.append(i)
                    # People go out at first.
                    on_exit = list(filter(lambda x: x == i, self.passengers))
                    self.queues[i].extend(on_exit)
                    self.passengers = list(
                        filter(lambda x: x != i, self.passengers))
                    # People who goes up enter the elevator.
                    up_queue = up_queue[:(
                        self.capacity - len(self.passengers))]
                    self.passengers.extend(up_queue)
                    for el in up_queue:
                        self.queues[i].remove(el)
            # Go down
            for i, floor in list(enumerate(self.queues))[::-1]:
                down_queue = list(filter(lambda x: x < i, floor))
                if down_queue or i in self.passengers:
                    if i != self.path[-1]:
                        self.path.append(i)
                    # People go out at first.
                    on_exit = list(filter(lambda x: x == i, self.passengers))
                    self.queues[i].extend(on_exit)
                    self.passengers = list(
                        filter(lambda x: x != i, self.passengers))
                    # People who goes down enter the elevator.
                    down_queue = down_queue[:(
                        self.capacity - len(self.passengers))]
                    self.passengers.extend(down_queue)
                    for el in down_queue:
                        self.queues[i].remove(el)
        if self.path[-1] != 0:
            self.path.append(0)
        return self.path


lift = Dinglemouse(((),   (),    (5, 5, 5), (),   (),    (),    ()), 5)
print(lift.theLift(), lift.queues)
