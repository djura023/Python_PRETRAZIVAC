def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1 #indeks levog i desnog deteta
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i].getBrojRanga() > arr[l].getBrojRanga():
        largest = l     #ovde formiramo min heap

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest].getBrojRanga() > arr[r].getBrojRanga():
        largest = r    #formiramo min heap

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heap_sort(arr):
    n = len(arr)
    # nodes which indices are greater than start are leaves
    start = (n - 1) // 2
    # Build a maxheap. (minheap)
    for i in range(start, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # remove root
        heapify(arr, i, 0)

