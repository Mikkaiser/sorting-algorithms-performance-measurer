import time
import random
from functions import selection_sort, insertion_sort, bubble_sort, heap_sort, merge_sort, quick_sort, tree_sort
import tracemalloc

def exec():

    num_list = []

    for i in range(70000):
        num_list.append(i)


    funcs = [
        selection_sort, 
        insertion_sort, 
        bubble_sort, 
        heap_sort, 
        merge_sort, 
        quick_sort, 
        tree_sort
    ]

    def apply_memory_and_time(funcs):
        for sort_func in funcs:
            random.shuffle(num_list)
            start_time = time.time()
            tracemalloc.start()
            sort_func(num_list)
            peakMemory = round((tracemalloc.get_traced_memory()[1] / 1024), 2)
            tracemalloc.stop()
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Memory Usage:  {peakMemory} KB")
            print(f"{sort_func.__name__} - execution time: {round(execution_time, 3)} seconds")

    apply_memory_and_time(funcs)

exec()