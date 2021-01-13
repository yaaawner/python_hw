def fib(m, n):
    a = 1
    b = 1
    if m == 1:
        yield a
        yield b
    elif m == 2:
        yield b

    for i in range(3, n + 1):
        a, b = b, a+b
        if i >= m:
            yield b

print(*list(fib(1,10)))