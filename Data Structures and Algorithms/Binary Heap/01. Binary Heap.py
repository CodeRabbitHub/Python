class Heap:
    def __init__(self, size):
        """
        Initialize the custom list and properties of the heap.
        """
        self.custom_list = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size + 1


def peek_of_heap(root_node):
    """
    Return the first element of the custom list in the root node.
    """
    if not root_node:
        return
    else:
        return root_node.custom_list[1]


def size_of_heap(root_node):
    """
    Return the size of the heap.
    """
    if not root_node:
        return
    else:
        return root_node.heap_size


def level_order_traversal(root_node):
    """
    Print all elements of the custom list in the root node.
    """
    if not root_node:
        return
    else:
        for i in range(1, root_node.heap_size + 1):
            print(root_node.custom_list[i])


def heapify_tree_insert(root_node, index, heap_type):
    """
    Recursively swap elements in the custom list to maintain the heap property.
    """
    parent_index = int(index / 2)
    if index <= 1:
        return
    if heap_type == "Min":
        if root_node.custom_list[index] < root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)
    elif heap_type == "Max":
        if root_node.custom_list[index] > root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)


def insert_node(root_node, node_value, heap_type):
    """
    Insert a node into the custom list.
    """
    if root_node.heap_size + 1 == root_node.max_size:
        return "The Binary Heap is Full"
    root_node.custom_list[root_node.heap_size + 1] = node_value
    root_node.heap_size += 1
    heapify_tree_insert(root_node, root_node.heap_size, heap_type)
    return "The value has been successfully inserted"


def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return

    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode


def deleteEntireBP(rootNode):
    rootNode.customList = None


newHeap = Heap(5)
inserNode(newHeap, 4, "Max")
inserNode(newHeap, 5, "Max")
inserNode(newHeap, 2, "Max")
inserNode(newHeap, 1, "Max")
deleteEntireBP(newHeap)
levelOrderTraversal(newHeap)
