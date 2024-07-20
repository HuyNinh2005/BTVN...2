def bits(a):
  if a == 0:
    return 1  # Số 0 cần 1 bit
  count = 0
  while a > 0:
    a //= 2  # Chia a cho 2
    count += 1
  return count

a = int(input("Nhập số nguyên a: "))
num_bits = bits(a)
print(num_bits)

#3 cách print để cùng đưa ra màn hình “Python is awesome”
print("Python is awesome")

for char in "Python is awesome":
  print(char,end="")
print()

x= "Python is awesome"
print(x)

import sys
print(sys.version)