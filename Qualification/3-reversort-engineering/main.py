T = int(input())
for t in range(T):
    N, C = [ int(x) for x in input().split() ]
    print(f'Case #{t+1}: ', end='')
    if C > N*(N+1)//2-1 or C < N-1:
        print('IMPOSSIBLE')
        continue
    
    ans = list(range(1, N+1))

    max_c = N * (N + 1) // 2
    cost_left = C
    for i in range(N-2, -1, -1):
        suf_len = N - i
        cost_potential = max_c - suf_len * (suf_len + 1) // 2
        rotation_len = max(1, cost_left - cost_potential)
        cost_left -= rotation_len
        ans = ans[:i] + ans[i:i+rotation_len][::-1] + ans[i+rotation_len:]
    print(*ans)
