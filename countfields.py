def fcounter(C, *val):
    LF = list()
    LM = list()
    bufM = list()
    bufF = list()

    for n in dir(C):
        if n[0] != '_':
            if callable(getattr(C,n)):
                LM.append(n)
            else:
                LF.append(n)

    c = C(*val)
    for n in dir(c):
        if n[0] != '_':
            if callable(getattr(c,n)):
                bufM.append(n)
            else:
                bufF.append(n)

    NLF = [i for i in bufF if i not in LF]
    NLM = [i for i in bufM if i not in LM]

    return LM, LF, NLM, NLF