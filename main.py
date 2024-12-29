import time
import random
import functions

num_list = []


for i in range(20000):
    num_list.append(i)
random.shuffle(num_list)

start_time = time.time()
print(functions.selection_sort(num_list))
end_time = time.time()


execution_time = end_time - start_time
print(f"execution time: {round(execution_time, 3)} seconds")







