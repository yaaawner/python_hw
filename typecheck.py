from functools import wraps

gen = list()

def TypeCheck(type_in, type_out):
    def decorator(fun):
        @wraps(fun)
        def newfun(*args, **kwargs):
            global gen

            if type_in.__class__.__name__ == "generator":
                t = list(type_in)
                if len(t) == 0:
                    t = gen
                else:
                    gen = t
            else:
                t = type_in

            len_in = len(list(t))
            len_ar = len(args)
            len_kwa = len(kwargs)

            if len_in != len_ar + len_kwa:
                raise TypeError("Function " + fun.__name__ + " must have " + str(len_in) + " arguments")
            else:
                #ret = fun(*args, **kwargs)
                if len_kwa > 0:
                    fun(*args, **kwargs)

                for i in range(len_in):
                    if i < len_ar:
                        if t[i] != type(args[i]):
                            raise TypeError("Type of argument " + str(i+1) + " is not " + str(t[i]))

                    else:
                        if t[i] != type(list(kwargs.values())[i - len_ar]):
                            raise TypeError("Type of argument '" + str(list(kwargs.keys())[i - len_ar])
                                            + "' is not " + str(t[i]))

            ret = fun(*args, **kwargs)
            if type(ret) != type_out:
                raise TypeError("Type of result is not " + str(type_out))
            else:
                return ret
        return newfun
    return decorator
