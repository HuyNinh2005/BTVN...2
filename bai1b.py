n = int(input())

s = 0

for i in range(1, n + 1):
    if n % i == 0:     #Kiểm tra xem n có chia hết cho số hiện tại(i) hay không
        s += i

print(s)



 