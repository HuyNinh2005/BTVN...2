a = int(input())
b = int(input())
c = int(input())

if a + b <= c or a + c <= b or b + c <= a:
    print("Không phải là tam giác")
else:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 ==a ** 2:
        print("Tam giác vuông ")
    elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
        print("Tam giác nhọn")
    else:
        print("Tam giác tù")
            

