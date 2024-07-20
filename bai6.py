def shh(n):
    if n <= 1:
        return False
    
    sum = 0
    # Tìm các ước của number
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            sum += i
            # Nếu i không phải là căn bậc hai của number, thêm vào cặp ước đối xứng
            if i != 1 and i != n // i:
                sum += n // i
    
    return sum == n

def hh(n):
    for i in range(1, n + 1):
        if shh(i):
            print(i)

n = int(input())
hh(n)
