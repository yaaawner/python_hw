def even(seq):
    for s in seq:
        if s % 2 == 0:
            yield s

def slide(seq):
    for i in range(len(seq) - 2):
        yield from even(seq[i:i+3])

test = [3, 4, 6, 8, 11]
print(*list(slide(test)))