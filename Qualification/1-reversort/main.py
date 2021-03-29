T = int(input())
for t in range(T):
    _ = input()
    L = [ int(x) for x in input().split() ]
    ans = 0
    for i in range(len(L) - 1):
        min_l = 1e10
        min_idx = 0
        for j in range(i, len(L)):
            if L[j] < min_l:
                min_l = L[j]
                min_idx = j

        ans += min_idx + 1 - i
        L = L[:i] + L[i:min_idx+1][::-1] + L[min_idx+1:]

    print(f'Case #{t+1}: {ans}')