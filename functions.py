def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2

        # See if left child of root exists and is greater than root
        if l < n and arr[largest] < arr[l]:
            largest = l

        # See if right child of root exists and is greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            heapify(arr, n, largest)

    def heap_sort(arr):
        n = len(arr)

        # Build a maxheap.
        for i in range(n//2 - 1, -1, -1):
            heapify(arr, n, i)

        # One by one extract an element from heap
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            heapify(arr, i, 0)
        return arr
    
    heap_sort(arr)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr):
    def partition(arr, low, high):
        i = (low-1)         # index of smaller element
        pivot = arr[high]     # pivot

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def quick_sort(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = partition(arr, low, high)
            quick_sort(arr, low, pi-1)
            quick_sort(arr, pi+1, high)
        return arr
    
    quick_sort(arr, 0, len(arr)-1)


def tree_sort(arr):
    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data

    def insert(root, node):
        if root is None:
            root = node
        else:
            if root.data < node.data:
                if root.right is None:
                    root.right = node
                else:
                    insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    insert(root.left, node)

    def inorder(root):
        if root:
            inorder(root.left)
            inorder(root.right)

    def tree_sort(arr):
        root = Node(arr[0])
        for i in range(1, len(arr)):
            insert(root, Node(arr[i]))
        inorder(root) 
    tree_sort(arr);