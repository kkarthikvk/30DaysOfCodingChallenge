
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

print(approach1([1,2,3,4]))
