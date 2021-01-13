def calc(s, t, u):
    def helper(x):
        sx = eval(s)
        y = eval(t)
        x = sx
        return eval(u)

    return helper

F = calc("x", "2*x+1", "x/y")
print(F(100))
print(F(0.1))