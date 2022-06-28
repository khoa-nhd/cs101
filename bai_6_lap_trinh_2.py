def pop(stack):
    if len(stack) == 0:
        print(stack)
        return stack
    else:
        stack.pop()
        print(stack)
        return stack
    
stack = [1,2,3,4,5,6,7,8,9,0]  
pop(stack)