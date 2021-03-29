import sys
T, N, Q = [ int(x) for x in input().split() ]

def insert(left, right, c, arr):
    while 1:
        middle = (right + left) // 2
        print(arr[middle], c, arr[right])

        response = int(input())
        if response == -1:
            raise "Bad"
            
        if response == arr[middle]:
            right = middle
            if right == left:
                arr.insert(left, c)
                return
        elif response == arr[right]:
            left = right
            if right == left:
                arr.insert(left+1, c)
                return
        elif response == c:
            left = middle + 1
            if left == right:
                arr.insert(left, c)
                return
        else:
            raise "Very bad"

for t in range(T):
    arr = [1, 2]
    candidates = list(range(3, N+1))
    
    for c in candidates:
       insert(0, len(arr)-1, c, arr)
    #    print('-----', *arr, file=sys.stderr)
    
    print(*arr)
    response = int(input())
    if response == 1:
        print('<-------------> OK!', file=sys.stderr)
    else:
        exit(-1)