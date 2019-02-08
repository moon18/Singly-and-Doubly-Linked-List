#Test cases for Doubly Linked List
#Follow my Github for more https://github.com/moon18
from dl_list import DLList

def test_add_get():
    dllist = DLList()
    assert dllist.add(0, 10) == True
    assert dllist.add(1, 20) == True
    assert dllist.add(1, 15) == True
    assert dllist.add(4, 40) == False
    assert dllist.add(-1, 40) == True
    print(dllist)
    #assert dllist.add(-3, 40) == False
    assert dllist.get(0) == 10
    assert dllist.get(1) == 15
    #assert dllist.get(2) == 20
    assert dllist.get(3) == False

def test_add_front_back():
    dllist = DLList()
    assert dllist.add(0, 100) == True
    assert dllist.add(1, 200) == True
    assert dllist.add(2, 150) == True

    assert dllist.head.data == 100
    assert dllist.tail.data == 150
    assert dllist.add(1, 333) == True
    x=dllist.head.front #here's a problem
    assert x.back.data == 100
    assert x.front.data == 200

    y=dllist.tail.front
    assert y.back.data == 200
    assert y.front == None
    
def test_add_head_tail():
    dllist = DLList()
    assert dllist.add(0, 100) == True
    assert dllist.size == 1
    assert dllist.add(1, 200) == True
    assert dllist.add(2, 150) == True
    assert dllist.head.data == 100
    assert dllist.add(0, 250) == True
    assert dllist.head.data == 250
    assert dllist.tail.data == 150
    assert dllist.size == 4
    assert dllist.get(0) == 250
    assert dllist.get(1) == 100

def test_set():
    dllist= DLList()
    dllist.add(0, 10)
    dllist.add(1, 20)
    dllist.add(2, 10)
    dllist.add(3, 40)
    assert dllist.add(-1, 40) == True
    assert dllist.set(0, 11) == True
    assert dllist.get(0) == 11
    assert dllist.set(2, 22) == True
    assert dllist.get(2)== 22
    assert dllist.set(3, 44) == True
    assert dllist.get(3)== 44
    assert dllist.set(-2, 25) == True
    assert dllist.get(-2) == 25
    assert dllist.tail.data == 40
    
def test_remove():
    dllist= DLList()
    assert dllist.remove(0) == None
    dllist.add(0, 10)
    dllist.add(1, 20)
    dllist.add(2, 100)
    dllist.add(3, 40)
    assert dllist.remove(1) ==20
    assert dllist.size == 3
    assert dllist.head.data == 10
    assert dllist.remove(0) ==10
    assert dllist.head.data == 100
    assert dllist.size == 2
    assert dllist.remove(1) ==40
    assert dllist.tail.data == 100
    assert dllist.size == 1

def test_remove_front_back():
    
    dllist = DLList()
    dllist.add(0, 100)
    print(dllist)
    dllist.remove(0) == 100
    dllist.remove(1) == None
    dllist.add(1, 200)# this will cause a problem
    dllist.add(2, 150)
    dllist.add(3, 300)
    
    assert dllist.remove(1) == 200#problem
    x = dllist.head.front
    assert x.back.data == 100
    assert x.front.data == 300

    y=dllist.tail.back
    assert y.back.data == 100
    assert y.front.data == 300
    
def test_remove_head_tail():
    dllist = DLList()
    dllist.add(0, 10)
    dllist.add(1, 20)
    dllist.add(2, 100)
    dllist.add(3, 40)

    assert dllist.remove(0) == 10
    assert dllist.head.data == 20
    assert dllist.tail.data == 40
    assert dllist.size == 3
    assert dllist.get(0) == 20
    assert dllist.get(1) == 100

