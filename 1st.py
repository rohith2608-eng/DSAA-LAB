class Arraystack():    
    def __init__(self):
        self.data=[]        
    def __len__(self):            
            return len(self.data)   
    def is_empty(self):        
        return len(self.data)==0    
    def push(self,e):        
        self.data.append(e)        
    def top(self):            
        if self.is_empty():                
            raise Empty(Stack is empty)            
        return self.data[-1]        
    def pop(self):           
         if self.is_empty():                
            raise Empty(Stack is empty)            
         return self.data.pop()
        
S=Arraystack()
S.push(90)
S.push(37)
print(len(S))
print(S.pop())
print(S.is_empty())
print(S.pop())
print(S.is_empty())
S.push(67)
S.push(39)
print(S.top())
S.push(45)
print(len(S))
print(S.pop())
S.push(67)

