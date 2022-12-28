def gcd_extended(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)
a = gcd_extended(100, 101)

print(f'Делитель равен {a[0]}, x = {a[1]}, y = {a[2]}')
