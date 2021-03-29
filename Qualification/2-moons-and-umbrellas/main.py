T = int(input())
for t in range(T):
    line = input().split()
    x, y = [ int(x) for x in line[:2] ]
    s = list(line[-1])
    ans = 0
    
    right_neighbor = [ -1 ] * len(s)
    right_letter = None
    for i in range(len(s)-1, -1, -1):
        if s[i] == '?':
            right_neighbor[i] = right_letter
        else:
            right_letter = s[i]
    
    for i in range(len(s)-1):
        if s[i] == '?':
            if i > 0:
                s[i] = s[i-1]
            elif right_neighbor[i]:
                s[i] = right_neighbor[i]
            else:
                s[i] = 'C'
    
        if s[i:i+2] == ['C', 'J']:
            ans += x
        elif s[i:i+2] == ['J', 'C']:
            ans += y

    print(f'Case #{t+1}: {ans}')