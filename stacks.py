class Stack():
    def __init__(self, stackSize=10):
        # each stack instance will have its array, size of the array
        # and the current pointer
        self.stackSize=stackSize
        self.stack=[None]*stackSize
        self.pointer=-1
    def pop(self):
        # checks whether there is something on the stack, if yes,
        # returns val and moves pointer
        if not self.stackEmpty():
            returnVal = self.stack[self.pointer]
            # the next line can either exist or not, if not then it would just be
            # treated as garbage values which would then be overwritten
            self.stack[self.pointer] = None
            self.pointer -= 1
            return returnVal
        return False
    def peak(self):
        # if stack isnt empty, returns the last value on stack
        # without changing anything
        if not self.stackEmpty():
            return self.stack[self.pointer]
        else:
            return False
    def push(self, value):
        # adds a value to the stack if it isnt yet full, moves pointer
        if not self.stackFull():
            self.pointer+=1
            self.stack[self.pointer]=value
        else:
            return False
    def stackEmpty(self):
        # checks if stack is empty
        if self.pointer == -1:
            return True
        else:
            return False
    def stackFull(self):
        # check if stack is full
        if self.pointer==(self.stackSize-1):
            return True
        else:
            return False

# initializing stack with input stackSize
while True:
    stackSize = input('Enter stack size:')
    if stackSize == '':
        # no input --> default option in class
        stack=Stack()
        break
    else:
        try:
            # integer input --> user-specific stack size
            stackSize = int(stackSize)
            stack = Stack(stackSize)
            break
        except:
            print("Enter stack size:")
