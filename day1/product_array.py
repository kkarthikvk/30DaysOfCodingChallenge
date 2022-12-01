import math
import time

def approach1(l1):
    l2 = []
    for i,v1 in enumerate(l1):
        prd = 1
        for j,v2 in enumerate(l1):
            if i == j:
                continue
            else:
                prd *= v2
        l2.append(prd)
    return l2

def approach2(l1):
    l2 = []
    if len(l1) == 0:
        return 0
    elif len(l1) == 1:
        return l1[0]

    else:
        for i,v1 in enumerate(l1):
            c = l1[:i] + l1[i+1:]
            l2.append(math.prod(c))
        return l2

def approach3(l1):
    n = len(l1)
    left, right = [1]*len(l1), [1]*len(l1)
    prd = []

    for i in range(1,n):
        left[i] = left[i-1]*l1[i-1]

    for i in range(1,n):
        right[i] = right[i-1]*l1[::-1][i-1]

    for i in range(n):
        prd.append(left[i]*right[::-1][i])

    return prd

start = time.time()
print(approach1([1,2,3,4]))
print("Total time taken by approach1:",time.time()-start)
start = time.time()
print(approach2([1,2,3,4]))
print("Total time taken by approach2:",time.time()-start)
start = time.time()
print(approach3([1,2,3,4]))
print("Total time taken by approach3:",time.time()-start)

print(approach2([]))
print(approach2([4,6]))
print(approach2([-1,-2,-3,4]))
print(approach2([0]))
print(approach2([0,0,0,0]))

