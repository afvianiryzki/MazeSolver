# A simple implementation of Priority Queue 
# using Queue. 
class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == [] 
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data)
  
    # for popping an element based on Priority 
    def delete(self): 
        try: 
            min = 0
            for i in range(len(self.queue)): 
                if (self.queue[i].fx < self.queue[min].fx): 
                    min = i 
            item = self.queue[min] 
            del self.queue[min] 
            return item 
        except IndexError: 
            print() 
            exit()

"""if __name__ == '__main__': 
    myQueue = PriorityQueue() 
    myQueue.insert(12) 
    myQueue.insert(1) 
    myQueue.insert(14) 
    myQueue.insert(7) 
    print(myQueue.queue)             
    while not myQueue.isEmpty(): 
        print(myQueue.delete())"""