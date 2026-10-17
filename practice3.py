#creating a stack with empty space
N = 5
s = [None] * N
top = -1
x = 11
#pushing an element into the stack
if top == N-1:
    print("stack overflow")
else:
    top = top + 1
    s[top] = x

x = 7 # pushing 7
if top == N - 1:
    print("stack overflow")
else:
    top = top + 1
    s[top] = x

x = 21 #pushing 21

if top == N-1:
    print("stack overflow")
else:
    top = top + 1
    s[top] = x

print("stack" , s)
print("top" , top)