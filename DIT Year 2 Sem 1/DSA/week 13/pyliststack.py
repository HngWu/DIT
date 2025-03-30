class Stack:
    # Creates an empty stack.
    def __init__(self):
        self._theItems = list()


    def isEmpty(self):
        # Returns True if the stack is empty or False
        # otherwise.
        return len(self._theItems) == 0

    def __len__(self):
        # Returns the number of items in the stack.
        return len(self._theItems)

    def peek(self):
        # Returns the top item on the stack without
        # removing it.
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._theItems[-1]


    def pop(self):
        # Removes and returns the top item on the stack.
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self._theItems.pop()

    def push(self, item):
        # Push an item onto the top of the stack.
        self._theItems.append(item)


if __name__ == "__main__":
    myStack = Stack()
    myStack.push("1")
    myStack.push("2")
    myStack.push("3")
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())