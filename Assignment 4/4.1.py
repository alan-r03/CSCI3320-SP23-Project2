class ListNode:
    def __init__(self, data = None):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self, inputArray):
        self.headNode = None
        self.createLinkedList(inputArray)

    def insertionSort(self):
        scannedNode = tempNode = ListNode(0)
        currNode = tempNode.nextNode = self.headNode
        while currNode and currNode.nextNode:
            currDataVal = currNode.nextNode.data
            if currNode.data < currDataVal:
                currNode = currNode.nextNode
                continue
            if scannedNode.nextNode.data > currDataVal:
                scannedNode = tempNode
            while scannedNode.nextNode.data < currDataVal:
                scannedNode = scannedNode.nextNode
            newNode = currNode.nextNode
            currNode.nextNode = newNode.nextNode
            newNode.nextNode = scannedNode.nextNode
            scannedNode.nextNode = newNode
        self.headNode = tempNode.nextNode

    def createLinkedList(self, dataArray):
        prevNode = None
        for dataVal in dataArray:
            newNode = ListNode(dataVal)
            if not self.headNode:
                self.headNode = newNode
            else:
                prevNode.nextNode = newNode
            prevNode = newNode

    def printLinkedList(self):
        currNode = self.headNode
        dataArray = []
        while currNode:
            dataArray.append(str(currNode.data))
            currNode = currNode.nextNode
        print('->'.join(dataArray))

if __name__ == '__main__':
    inputArray = [1, 3, 2, 0]

    userLinkedList = LinkedList(inputArray)
    print("Linked list before sorting: ", end='')
    userLinkedList.printLinkedList()
    userLinkedList.insertionSort()
    print("Linked list after sorting:  ", end='')
    userLinkedList.printLinkedList()