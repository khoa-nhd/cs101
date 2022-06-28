def update_stack(stack, actions, books):
    if len(stack) == 0 and actions[0] == "pop":
        print(stack)
        return stack
    for x in actions:
        if x == "push":
            stack.append(books[0])
        elif len(stack) > 0:
            stack.pop()
        books.pop(0)
        print(stack)
    return stack

stack = ['Doraemon', 'Conan', 'Lao Hac']
actions = ['push', 'pop', 'push']
books = ['Truyen Kieu', None, 'Doraemon']
update_stack(stack, actions, books)