from queue import PriorityQueue, Queue

class Workers:
    def __init__(self, numOfWorkers):
        self.numWorkers = numOfWorkers
        self.current_time = 0
        self.workers = [{'status': 0, 'current': 0, 'current_to_finish': 0, 'type': 0, 'time_waited': 0} for i in range(0, self.numWorkers)]
        self.needToDo = []
        self.doneInStore = []
        self.doneOutStor = []

    def add_job(self, timeToComplete, val, time_waited):
        added = False
        for worker in self.workers:
            if worker['status'] == 0:
                worker['status'] = 1
                worker['current_to_finish'] = timeToComplete
                worker['current'] = 0
                worker['type'] = val
                worker['time_waited'] = time_waited
                added = True
                return True
        # print('error')
        return False

    def can_take(self):
        stat = False
        for worker in self.workers:
            if(worker['status'] == 0):
                stat = True
        return stat

    def update(self):
        # print('updated')
        # print('workers: ' +str(self.workers))
        self.current_time = self.current_time + 1
        for worker in self.workers:
            if worker['status'] == 1 or worker['status'] == -1:
                worker['current'] = worker['current'] +1
                if worker['current'] >= worker['current_to_finish']:
                    # print("THIS IS TYPE", worker['type'])
                    if worker['type'] == -1:
                        self.doneInStore.append(worker['current_to_finish'] + worker['time_waited'])
                        # worker = {'status': 0, 'current': 0, 'current_to_finish': 0, 'type': 0}
                    if worker['type'] == 1:
                        self.doneOutStor.append(worker['current_to_finish'] + worker['time_waited'])
                        # worker = {'status': 0, 'current': 0, 'current_to_finish': 0, 'type': 0}
                    worker['status'] = 0
                    worker['current_to_finish'] = 0
                    worker['current'] = 0
                    worker['type'] = 0

    def print_stuff(self):
        inStore = 0
        outStore = 0
        for job in self.doneInStore:
            inStore = inStore + job
        for job in self.doneOutStor:
            outStore = outStore + job
        # print(self.doneInStore):
        # print(self.doneOutStor)

        print( self.divideOrZero(inStore , len(self.doneInStore)),  self.divideOrZero( outStore , len(self.doneOutStor) ) )

    def divideOrZero(self, one, two):
        num = 0
        try:
            num = one / two
        except ZeroDivisionError:
            pass
        return num



    def isWorking(self):
        isWorking = False
        for worker in self.workers:
            if worker['status'] == 1:
                isWorking = True
        return isWorking
            



line_1 = input()

numOfPrecsriptions =  int(line_1.split()[0])
numOfworkers = int(line_1.split()[1])

# print(numOfPrecsriptions)
# print(numOfworkers)
# global x
x=1
all_p = PriorityQueue()
workers = Workers(numOfworkers)

num_skipped = 0
last = 1
while x <= numOfPrecsriptions + num_skipped:
    # print(x)
    # print(numOfPrecsriptions)
    line = input()
    inputs = line.split()
    # 1 is remote and -1 is in store
    if inputs[1] == 'R':
        val = 1
    else: 
        val = -1
    last = int(inputs[0])
    all_p.put((val, int(inputs[0]), int(inputs[2])))

    # print(workers.can_take())
    if(workers.can_take()):
        thing = all_p.get()
        workers.add_job(thing[2], thing[0], x - thing[1])
    workers.update()

    if( (x-last) != 0):
        if x-last > 0:
            for i in range(0,(x-last)):
                if(workers.can_take()):
                    thing = all_p.get()
                    workers.add_job(thing[2], thing[0], x - thing[1])
                workers.update()

    x =x+1

# print('done taking input')
while workers.isWorking() or not all_p.empty():
    if(workers.can_take()):
        if(not all_p.empty()):
            thing = all_p.get()
            workers.add_job(thing[2], thing[0], x-thing[1])
    workers.update()
    x = x + 1

workers.print_stuff()