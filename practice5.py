N = 5
S = [11,25,7,None,None]
top = 2

# peek algorithm
if top == -1:
    print("stack is full")
else:
    print("top element" , S[top])

print("top index:" , top) 

#isEmpty algorithm

if top == -1:
    print("stack is empty")
else:
    print("stack is not empty")

#isFull algorithm

if top == N - 1:
    print("stack is full")
else:
    print("stack is not full")


N = 5
S = [11, 25, 7, None, None]
top = 2

# size algorithm
size = top + 1

print("Stack size:", size)
