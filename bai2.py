a = int(input())
b = int(input())

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a // b = {a // b}")
print(f"a ** b = {a ** b}")
print(f"a % b = {a % b}")

if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a == b")

print(f"a AND b = {a & b}")
print(f"a OR b = {a | b}")
print(f"a XOR b = {a ^ b}")
print(f"NOT a == b = {not a == b}")
print(f"a dịch phải 1 đơn vị = {a >> 1}")
print(f"a dịch trái 1 đơn vị = {a << 1}")