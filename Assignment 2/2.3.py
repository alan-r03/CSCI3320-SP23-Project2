class Node:
    def __init__(self, data = None):
        """
        creates an unallocated node

        :param data: node value
        """
        self.data = data
        self.nextNode = None

class Queue:
    def __init__(self):
        """
        creates an empty queue
        """
        self.header = None
        self.tail = None

    def enqueue(self, data = None):
        """
        adds a node to the
        end of the queue

        :param data: node value
        :return: None
        """
        newNode = Node(data)
        if self.header == None:
            self.header = newNode
        else:
            self.tail.nextNode = newNode
        self.tail = newNode

    def dequeue(self):
        """
        prints and removes the
        head of the queue

        :return: None
        """
        val = None
        if self.header != None:
            val = self.header.data
            self.header = self.header.nextNode
        print(val)

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
queue.enqueue(4)
queue.dequeue()