# A simple implementation of Priority Queue 
# using Queue. 
class RegularQueue(object): 
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
        item = self.queue[0]
        del self.queue[0]
        return item
