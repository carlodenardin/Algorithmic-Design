class MinHeap:

    def __init__(self, maximum_size):
        self.heap = [0] * maximum_size
        self.size = 0
        self.maximum_size = maximum_size

    def parent(self, i):
        return i // 2
    
    def leftChild(self, i):
        return 2 * i + 1
    
    def rightChild(self, i):
        return 2 * i + 2

    def isRoot(self, i):
        return i == 0

    def isLeaf(self, i):
        return 2 * i + 1 > self.size

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Return the minimum of the heap
    def getMinimum(self):
        if (self.size > 0):
            return self.heap[0]
        else:
            print("The heap is empty.")
            return
    
    # Return and extract the minimum
    def extractMinimum(self):
        if (self.size > 0):
            minimum = self.heap[0]
            self.swap(0, self.size)
            heapify(0)
            return minimum
        else:
            print("The heap is empty.")
            return

    # Fix the heap property from the root
    def heapify(self, i):
        if not self.isLeaf(i):
            if (self.heap[i] > self.heap[self.leftChild(i)] or self.heap[i] > self.heap[self.rightChild(i)]):
                if self.heap[self.leftChild(i)] < self.heap[self.rightChild(i)]:
                    self.swap(i, self.leftChild(i))
                    self.heapify(self.leftChild(i))
                else:
                    self.swap(i, self.rightChild(i))
                    self.heapify(self.rightChild(i))
    
    # Build heap
    def buildMinHeap(self):
        for i in range(self.size // 2, -1, -1):
            self.heapify(i)

    # Decrease key of a node
    def decreaseKey(self, i, key):
        self.heap[i] = key

        while self.isRoot(i) or self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i <- self.parent(i)

    # Insert a new node with corresponding key
    def insert(self, key):
        if self.size >= self.maximum_size:
            print("The heap is full.")
            return
        
        self.size += 1
        self.decreaseKey(self.size, key)
    
    # Print heap
    def printHeap(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : "+ str(self.heap[i])+" LEFT CHILD : "+
                                str(self.heap[2 * i])+" RIGHT CHILD : "+
                                str(self.heap[2 * i + 1]))
        
if __name__ == "__main__":
    minHeap = MinHeap(100)

    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)

    minHeap.printHeap()

    minHeap.buildMinHeap()


