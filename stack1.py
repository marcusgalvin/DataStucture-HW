# first: we must creat a function to make an empty stack
# def newStack():
#     stack = []
#     return stack

# # second: we must write a function to find the size of said stack
# # len() will find the length for us


# def size(stack):
#     return len(stack)

# # third: write a function to say the size of the stack is 0 if its empty


# def isEmpty(stack):
#     if size(stack) == 0:
#         return true

# # fourth: write a function to add an item to the top of the stack, increase size by 1
# # append will do this


# def push(stack, item):
#     stack.append(item)

# # fifth: write a function to remove an item from stack using pop


# def pop(stack):
#     if isEmpty(stack):
#         return
#     return stack.pop()

# six: write a reverse string function for the stack


# def reverse(string):
#     n = len(string)


# # now lets initialize and empty stack to start
# stack = newStack()

# # push all of the letters in the string into the new stack
# # n = the length of the string
# for i in range(0, n, 1):
#     push(stack, string[i])

# # making thr string empty since all the letters are saves inside the stack
# string = ""

# # pop all the letter of string and then put them back inside string
# for i in range(0, n, 1):
#     string += pop(stack)


# return string

# # test
# string = "HelloWorld"
# string = reverse(string)

# print("reversed word is " + string)


# Python program to reverse a string using stack

# Function to create an empty stack.
#
# It initializes size of stack as 0


# write a function to create a stack, empty

def newStack():
    stack = []
    return stack

# next, write a function that says the lenght of the stack using len()


def size(stack):
    return len(stack)

# next, write function to declare the Stack is empty if the size is 0


def isEmpty(stack):
    if size(stack) == 0:
        return true

# next, write function to add an item to stack
# use append() to do this


def push(stack, item):
    stack.append(item)

# next write a functio to remove an item from stack
# use .pop() for this


def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()

# next step, write a function to reverse the string inside th stack
# make n = the length of string


def reverse(string):
    n = len(string)

    # now start by declaring an empty stack
    stack = newStack()

    # Push all letters of string into stack
    for i in range(n):
        push(stack, string[i])

    # Making the string empty since letters are now in stack

    string = ""

    # Pop all letters out of the stack  and
    # put them back to string, should now all be reversed
    for i in range(n):
      # string now = what is pop'd from stack
        string += pop(stack)

# return result
    return string


# test
# write a string you want to be reversed
string = "HelloWord"
# call the reverse function
string = reverse(string)
# print result
print("The new reversed word will be " + string)
