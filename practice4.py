
N = 5
S = [None] * N
top = -1


x = 25

if top == N - 1:
    print("STACK OVERFLOW")
else:
    top = top + 1
    S[top] = x

x = 7

if top == N - 1:
    print("STACK OVERFLOW")
else:
    top = top + 1
    S[top] = x

print("Stack after PUSH:", S)
print("Top:", top)


# ---------- POP ----------
print("\nPOP OPERATION")

if top == -1:
    print("STACK UNDERFLOW")
else:
    x = S[top]
    S[top] = None
    top = top - 1
    print("Removed element:", x)

print("Stack after POP:", S)
print("Top:", top)


