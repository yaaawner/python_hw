import copy

def Stat(*st_args):
    if len(st_args) == 1:
        st_args[0]._stat = dict()
        stat_list = [l[0] for l in vars(st_args[0]).items() if l[0][0] != '_' and not callable(l[1])]
        for l in stat_list:
            st_args[0]._stat[l] = (0, 0)

        def dec_init(init):
            def newinit(self, *args, **kwargs):
                self._stat = copy.deepcopy(st_args[0]._stat)
                init(self, *args, **kwargs)
            return newinit

        def dec_get(self, item):
            if item in st_args[0]._stat.keys():
                buf = list(self._stat[item])
                buf[0] += 1
                self._stat[item] = tuple(buf)
            return super(st_args[0], self).__getattribute__(item)

        def dec_set(self, name, value):
            if name in st_args[0]._stat.keys():
                buf = list(self._stat[name])
                buf[1] += 1
                self._stat[name] = tuple(buf)
            self.__dict__[name] = value

        st_args[0].__getattribute__ = dec_get
        st_args[0].__setattr__ = dec_set
        st_args[0].__init__ = dec_init(st_args[0].__init__)

        return st_args[0]
    else:
        if st_args[1] in st_args[0]._stat.keys():
            return st_args[0]._stat[st_args[1]]
        else:
            return (0, 0)



F.A = 4