import math
a = float(input())
b = float(input())
c = float(input())

delta = b**2 - 4 * a * c

if a != 0:
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x:.2f}")
    else:
        print("Phương trình vô nghiệm")
else:
    x = - b/c
    print(f"Phương trình là phương trình bậc nhất và có nghiệm là {x:.2f}")

