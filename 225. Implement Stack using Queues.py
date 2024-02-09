class MyStack(object):

    def __init__(self):
        self.q = [] #constructor initializes instance of the class 

    def push(self, x):
    
        self.q.append(x)  # append the element to the end of the queue
        for i in range(len(self.q)-1):  #iterate through the whole queue
            self.q.append(self.q.pop(0)) #rotate the queue to put the element to be removed at the end 
        print(self.q[len(self.q)-1])  #remove the element from the queue

    def pop(self):
    
        return self.q.pop(0)

    def top(self):
    
        return self.q[0]
        

    def empty(self):

        if len(self.q)==0:
            return True
        else:
            return False
        
