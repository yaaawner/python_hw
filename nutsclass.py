class Nuts:
    def __str__(self):
        return "Nuts"

    def __getitem__(self, item):
        return item

    def __setitem__(self, key, value):
        return

    def __init__(self, *val):
        return

    def __delitem__(self, key):
        return

    #def __getattr__(self, item):
        #print("bbbbb")
        #return locals()['item']

    def __getattribute__(self, item):
        return locals()['item']

    def __iter__(self):
        return iter(range(0))

    def __delattr__(self, item):
        return

    def __setattr__(self, key, value):
        return