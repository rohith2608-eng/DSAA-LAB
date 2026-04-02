class Arrayqueue:
    DEFAULT_CAPACITY=5
    def __init__(self):
        self.data=[None]
        self.size=0
        self.front=0
    def __len__(self):
        return self.size()
    def is_empty(self):
        return self.size==0
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front]
    def display(self):
        for i in self.data:
            print(i)
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        answer=self.data[self.front]
        self.data[self.front]=None
        self.front=(self.front+1)%len(self.data)
        self.size-=1
        return answer
    def enqueue(self,e):
        if self.size==len(self.data):
            self.resize(2*len(self.data))
        avail=(self.front+self.size)%len(self.data)
        self.data[avail]=e
        self.size+=1
    def resize(self,cap):
        old=self.data
        self.data=[None]*cap
        walk=self.front
        for k in range(self.size):
            self.data[k]=old[walk]
            walk=(1+walk)%len(old)
        self.front=0
q=Arrayqueue()
q.enqueue(64)
q.enqueue(77)
q.enqueue(69)
print(q.dequeue())
print(q.is_empty())
print(q.first())
q.display()
