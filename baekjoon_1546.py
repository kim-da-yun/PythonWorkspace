N = int(input())

M = list(map(int, input().split()))

m = max(M)
 
for i in range(N):
    M[i] = M[i] / m * 100
avg = sum(M) / N
print("%.2f" %avg)