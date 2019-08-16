def max1(L):
    max_so_far = L[0]           # O(1) and executes once
    for v in L:                 # O(1) and executes O(n) times
        if v > max_so_far:      # O(1) and executes O(n) times
            max_so_far = v      # O(1) and executes O(n) times
    return max_so_far           # O(1) and executes once
   

def max2(L):
    max_so_far = L[0]
    while len(L) > 0:
        if L[0] > max_so_far:
            max_so_far = L[0]
        L = L[1:]
    return max_so_far

   
def max3(L):
    return max3_acc(L,L[0],1)   
def max3_acc(L, max_so_far, i):
    #print(L,max_so_far,i)
    if i >= len(L):
        return max_so_far
    else:
        larger = max(max_so_far, L[i])
        return max3_acc(L, larger, i+1)

        
def max4(L):
    if len(L) == 1:
        return L[0]
    elif L[0] > max4(L[1:]):
        return L[0]
    else:
        return max4(L[1:])
                   
                   
def max5(L):
    if len(L) == 1:
        return L[0]
    max_of_rest = max5(L[1:])
    if L[0] > max_of_rest:
        return L[0]
    else:
        return max_of_rest
    #return max(L[0],max5(L[1:]))
    

def max6(L):
    return max6helper(L,0)
def max6helper(L,i):
    if i == len(L)-1:
        return L[i]
    else:
        return max(L[i],max6helper(L,i+1))
    

def max7(L):
    for v in L:
        at_least_all = True
        for w in L:
            if w > v:
                at_least_all = False
        if at_least_all:
            return v


def max8(L):
    if len(L) == 1:
        return L[0]
    else:
        mid = len(L) // 2
        return max(max8(L[:mid]),max8(L[mid:]))     


def max9(L):
    return sorted(L)[-1]


# Yet Other Approaches

def max10(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0], max10(L[1:]))

def max11helper(m, L):
    if len(L)==0:
        return m
    elif m > L[0]:
        return max11helper(m, L[1:])
    else:
        return max11helper(L[0], L[1:])
def max11(L): 
    return max11helper(L[0], L[1:])
    

L1 = list(range(10))   
L2 = list(range(10**3))
L3 = list(range(10**6)) 

import random
random.shuffle(L1)
random.shuffle(L2)
random.shuffle(L3)