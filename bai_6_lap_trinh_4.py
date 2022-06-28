def dequeue(queue):
    if len(queue) == 0:
        print(queue)
        return queue
    else:
        queue.pop(0)
        print(queue)
        return queue
 
queue = [0,1,2,3,4,5,6,7,8,9]
dequeue(queue)