class ArrayQueue:

    def __init__(self):
        self.data=[]
        self.size=0
        self.front=0
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def first(self):
        if self.is_empty():
            raise empty("queue is empty")
        return self.data[self.front]
    def display(self):
        for i in self.data:
            print (i)
    def dequeue(self):
        if self.is_empty():
            raise empty("queue is empty")
        value=self.data[self.front]
        self.data[self.front] = None
        self.front +=1
        self.size -=1
        return value
    def enqueue(self,e):
        if self.size == len(self.data):
            self.resise(2*len(self.data))
            avail 




q = ArrayQueue()
q.enqueue(64)
q.enqueue(77)
q.enqueue(87)
print(q.dequeue())
print(q.is_empty())
print(q.first())

