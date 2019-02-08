'''The next few methods involve performing manipulations on
    DLLists. You should complete them without allocating any new nodes
    or temporary arrays. They can all be done only by changing the
    value of front and back in existing nodes. The exercises are taken from Pat Morins book
    '''
from dl_list import DLList

def is_palindrome(self):
    '''As described in Exercise 3.7.
    '''
    if self.size%2==0:
        n = self.size//2
    else:
        n =(self.size-1)//2

    frontNode = self.dummy.front
    backNode = self.dummy.back
    print("N is: ",n)
    for i in range(n):
        print(i,frontNode.data,backNode.data)
        if frontNode.data != backNode.data:
            return False
        frontNode = frontNode.front
        backNode = backNode.back
    return True

    

def truncate(self,i):
    '''As described in Exercise 3.9.
    '''
    new = None
    if (0<=i<self.size):
        if(i<self.size//2):
            print("//2")
            temp = self.dummy
            for c in range(i):
                temp = temp.front
            new = DLList()
            new.dummy.front = temp.front
            temp.front.back = new.dummy
            
            new.dummy.back = self.dummy.back
            self.dummy.back.front = new.dummy
            
            self.dummy.back = temp
            temp.front = self.dummy
            
            new.size = self.size-i
            self.size = i
            
            print(new)
        else:
            temp = self.dummy
            for c in range(self.size-i+1):
                temp = temp.back
            new = DLList()
            new.dummy.front = temp.front
            temp.front.back = new.dummy
            
            new.dummy.back = self.dummy.back
            self.dummy.back.front = new.dummy
            
            self.dummy.back = temp
            temp.front = self.dummy
           
            new.size = self.size-i
            self.size = i
            
    return new
    

def absorb(self,l2):
    '''As described in Exercise 3.10.

    Your code should run in O(1) time.
    '''
    end1 = self.dummy.back
    start2 = l2.dummy.front

    end1.front = start2
    start2.back = end1

    end2 = l2.dummy.back

    self.dummy.back = end2

    l2.dummy.front  = None
    l2.dummy.back = None

    self.head = self.dummy.front
    self.tail = self.dummy.back

    self.size += l2.size
    l2.size =0        
def reverse(self):
    '''As described in Exercise 3.12.

    Your code should run in O(n) time.
    '''
    if (self.size>1):
        tempNode = self.dummy.front
        nextNode = None
        nextHead = self.dummy.back
        for i in range(self.size):
            nextNode = tempNode.front
            tempNode.front = tempNode.back
            tempNode.back = nextNode
            tempNode = nextNode
       
        self.dummy.back = self.dummy.front
        self.dummy.back.front = self.dummy
        
        self.dummy.front = nextHead
        nextHead.back = self.dummy

        self.head = self.dummy.front
        self.tail = self.dummy.back
    print(self)