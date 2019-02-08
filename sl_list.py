#Made my Moonis Rasheed in the Course Data Strucutres 2
#Follow my Github for more https://github.com/moon18

class SLNode:
    def __init__(self, data):
        self.data = data
        self.front = None # can't use "next" - used by python.

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        pass

class SLList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        temp = self.head
        st ="["
        while(temp):
            st+=str(temp.data)+","
            temp = temp.front
        st+=']'
        return st

    def get(self, i):
        '''SL.get(int) -> value

        Returns the value stored at index, i.
        Returns None if i \notin {0, ..., n-1}.

        Runs in O(1+i) time.
        '''
        if(0<=i<self.size):
            temp = self.head
            count = 0
            while(temp):
                if(count==i):
                    return temp.data
                temp = temp.front
                count+=1
        return None
        

    def set(self, i, x):
        '''SL.set(int, value) -> bool

        Sets the element at index, i, to x and returns True.
        Returns False if i \notin {0, ..., n-1}.

        Runs in O(1+i) time.
        '''
        if(0<=i<self.size):
            temp = self.head
            count = 0
            while(temp):
                if(count==i):
                    temp.data = x
                    self.print()
                    print(self.size)
                    return True
                temp = temp.front
                count+=1
        return False

    def add(self, i, x):
        '''SL.add(int, value) -> bool

        Inserts x at index, i, and returns True.
        Returns False if i \notin {0, ..., n}.

        Runs in O(1+i) time.
        '''
        if(0<=i<=self.size):
            if(i==0):
                if self.head == None:
                    self.head = SLNode(x)
                    self.tail = self.head
                else:
                    temp = self.head
                    self.head = SLNode(x)
                    self.head.front = temp
                
            elif i ==self.size:
                temp = self.tail
                self.tail = SLNode(x)
                temp.front = self.tail
                
            else:
                temp = self.head
                count = 1
                while(temp):
                    if(count==i):
                        newNode = SLNode(x)
                        newNode.front = temp.front
                        temp.front = newNode
                        break
                    temp = temp.front
                    count+=1

            self.size+=1
            self.print()
            print(self.size)
            return True
        return False


    def addMultiple(self,*args):
        for i in args:
            self.add(0,i)
            self.size+=1
    
    def print(self):
        temp = self.head
        print('[',end='')
        while(temp):
            print (temp.data,end=",")
            temp = temp.front
        print(']')           
                            
                        
            
        

    def remove(self, i):
        '''SL.remove(int) -> value

        Removes the element at index, i, and returns it.
        Returns None if i \notin {0, ..., n-1}.

        Runs in O(1+i) time.
        '''
        if(0<=i<self.size):
            if(i==0):
                temp = self.head
                self.head = temp.front
                self.size-=1
                self.print()
                print(self.size)
                return temp.data
            else:    
                tempPrev = None
                temp = self.head
                count = 0
                while(temp):
                    if(count==i):
                        if(temp.front):
                            tempPrev.front = temp.front
                            self.size-=1
                            self.print()
                            print(self.size)
                            return temp.data
                        else:
                            self.tail = tempPrev
                            self.tail.front = None
                            self.size-=1
                            self.print()
                            print(self.size)
                            return temp.data
                    tempPrev = temp
                    temp = temp.front
                    count+=1
        return False
    
