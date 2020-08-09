from queue import PriorityQueue, Queue

class Workers:
    def __init__(self, numOfWorkers):
        self.all_p = PriorityQueue()

        self.remote_jobs = PriorityQueue()
        self.in_person_job = PriorityQueue()

        self.doing_job = PriorityQueue()

        self.numWorkers = numOfWorkers
        self.current_time = 0
        self.workers = [{'status': 0, 'current': 0, 'current_to_finish': 0, 'type': 0, 'start_time': 0} for i in range(0, self.numWorkers)]
        self.needToDo = []
        self.doneInStore = []
        self.doneOutStor = []
    
    def add(self, val, time, time_to_do):
        if val == 'R':
            self.remote_jobs.put( (time, time_to_do) ) 
        else:
            self.in_person_job.put((time, time_to_do))
            
        
    
    def add_job_to_worker(self, timeToComplete, val):
        added = False
        for worker in self.workers:
            if worker['status'] == 0:
                worker['status'] = 1
                worker['current_to_finish'] = timeToComplete
                worker['current'] = 0
                worker['type'] = val
                worker['start_time'] = self.current_time
                added = True
                return True
        print('error')
        return False

    def can_take(self):
        stat = False
        for worker in self.workers:
            if(worker['status'] == 0):
                stat = True
        return stat

    def update(self):
        print('updated')
        print('workers: ' +str(self.workers))

        if self.can_take():
            if not self.in_person_job.empty():
                self.add_job_to_worker()

        self.current_time = self.current_time + 1

        for worker in self.workers:
            if worker['status'] == 1 or worker['status'] == -1:
                worker['current'] = worker['current'] +1
                if worker['current'] >= worker['current_to_finish']:
                    if worker['type'] == -1:
                        self.doneInStore.append( self.current_time - worker["start_time"] )
                    if worker['type'] == 1:
                        self.doneOutStor.append( self.current_time - worker["start_time"] )
                    
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
        print(inStore / len(self.doneInStore),outStore / len(self.doneOutStor) )


    def isWorking(self):
        if(not self.remote_jobs.empty() or not self.remote_jobs.empty()):
            return True
        isWorking = False
        for worker in self.workers:
            if worker['status'] == 1:
                isWorking = True
        return isWorking
            



line_1 = input()

numOfPrecsriptions =  int(line_1.split()[0])
numOfworkers = int(line_1.split()[1])

x=1
all_p = PriorityQueue()
workers = Workers(numOfworkers)

while x <= numOfPrecsriptions:
    line = input()
    inputs = line.split()
    workers.add( inputs[1], int(inputs[0]), int(inputs[2]) )
    x=x+1

print('done taking input')

while workers.isWorking():
    workers.update()

workers.print_stuff()