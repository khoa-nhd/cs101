def enqueue(queue, value):
    queue.append(value)
    print(queue)
    return queue

value = 0
queue = [1,2,3,4,5,6,7,8,9]
enqueue(queue, value)