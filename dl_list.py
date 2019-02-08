#Made my Moonis Rasheed in the Course Data Strucutres 2
#Follow my Github for more https://github.com/moon18

class DLNode:
    def __init__(self, data):
        self.data = data
        self.front = self.back = None

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        pass

class DLList:
    def __init__(self):
        '''Initializes the dummy node and size.'''
        self.dummy =DLNode(None)
        self.dummy.front = self.dummy
        self.dummy.back = self.dummy
        self.size=0
        self.head = self.dummy.front
        self.tail = self.dummy.back

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        temp = self.dummy
        print(self.size)
        st ="["
        for c in range(self.size+1):
            st+=str(temp.data)+","
            temp = temp.front
        st+=']'
        return st

    def get(self, i):
        '''DL.get(int) -> value

        Returns the value stored at index, i.
        Returns None if i \notin {-n, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if(i<0):
                i =self.size+i
                print(i)
            
        if (0<=i<self.size):
            if(i<self.size//2):
                print("//2")
                temp = self.dummy
                for c in range(i+1):
                    temp = temp.front
                
                return temp.data
            else:
                temp = self.dummy
                for c in range(self.size-i):
                    temp = temp.back
                return temp.data
        return None

    def set(self, i, x):
        '''DL.set(int, value) -> bool

        Sets the element at index, i, to x and returns True.
        Returns False if i \notin {-n, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if(i<0):
                i =self.size+i
                print(i)

        
        if (0<=i<self.size):
            if(i<self.size//2):
                print("//2")
                temp = self.dummy
                for c in range(i+1):
                    temp = temp.front
                temp.data = x
                return True
            else:
                temp = self.dummy
                for c in range(self.size-i):
                    
                    temp = temp.back
                    print(temp.data)
                temp.data = x
                return True
        return False
        
    def add(self, i, x):
        '''DL.add(int, value) -> bool

        Inserts x at index, i, and returns True.
        Returns False if i \notin {-n, ... , n}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if(i<0):
                i +=self.size
                print(i)
        
        if (0<=i<=self.size):
            if(i<self.size//2):
                temp = self.dummy
                for c in range(i):
                    temp = temp.front
                newNode = DLNode(x)
                newNode.front = temp.front
                newNode.back = temp
                newNode.front.back = newNode
                temp.front = newNode
                self.size+=1
                self.head = self.dummy.front
                self.tail = self.dummy.back
                return True
            else:
                temp = self.dummy
                for c in range(self.size-i):
                    temp = temp.back
                newNode = DLNode(x)
                newNode.back = temp.back
                newNode.front = temp
                newNode.back.front =newNode
                temp.back = newNode
                self.size+=1
                self.head = self.dummy.front
                self.tail = self.dummy.back
                return True
                       
        return False

   
                    
    
    def remove(self, i):
        '''DL.remove(int) -> value

        Removes the element at index, i, and returns it.
        Returs None if i \notin {-n, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if(i<0):
                i =self.size+i
                print(i)
                
        if (0<=i<self.size):
            if(i<self.size//2):
                print("//2")
                temp = self.dummy
                for c in range(i+1):
                    temp = temp.front
                temp.back.front = temp.front
                temp.front.back = temp.back
                self.size-=1
                self.head = self.dummy.front
                self.tail = self.dummy.back
                return temp.data
            else:
                temp = self.dummy
                for c in range(self.size-i):
                    temp = temp.back
                temp.back.front = temp.front
                temp.front.back = temp.back
                self.size-=1
                self.head = self.dummy.front
                self.tail = self.dummy.back
                return temp.data
        return None

        

    




