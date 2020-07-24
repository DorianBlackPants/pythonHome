# 2. Продолжаем идеализировать fizzbuzz,
# теперь применяем функции и map везде, где можно и нельзя!

def fizz_buzz(n):
    fizz = 3
    buzz = 5
    if not n % fizz and not n % buzz:
        return 'FB'
    elif not n % fizz:
        return 'B'
    elif not n % buzz:
        return 'B'
    else:
        return str(n)


n = 21

for x in map(fizz_buzz, range(1, n + 1)):
    print(x)
