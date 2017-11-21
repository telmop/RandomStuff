# Hanoi Tower solver, implemented several years ago

def hanoi(n, origin, destination, tmp):
    if n == 0:  # Base case
        return
    # Move the top n-1 to the tmp tower
    hanoi(n-1, origin, tmp, destination)
    # Move the last element (base)
    destination.append(origin.pop())
    printf()
    # Move the top n-1 to the destination tower
    hanoi(n-1, tmp, destination, origin)

def to_txt(n):
    # Draw towers as text
    q, r = n/2, n%2
    return " "*((N-n+2)/2) + "*"*q + "*"*r + "*"*q + " "*((N-n+2)/2)

def get_element(l, i):
    if len(l) <= i:
        return 0
    return l[i]

c = 0
def printf():
    global orig, dest, temp, c
    print(c)
    c+=1
    for i in range(N-1, -1, -1):
        print to_txt(get_element(orig, i)), to_txt(get_element(temp, i)), \
                     to_txt(get_element(dest, i))
    print "-"*(N+2)*3



N = 5

orig = range(N, 0, -1)
dest, temp = [], []
printf()
hanoi(N, orig, dest, temp)
