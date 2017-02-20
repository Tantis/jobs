


def register(cls, *args, **kwarg):

    print(cls, args, kwarg, 'one')
    def detor(*args, **kw):
        
        print(args, kw, 'two')
    
    return detor



class ooop(object):

    def __init__(self):
        register('123', '2345','2321', l = '2345')(self.fn)

    def fn(self):
        pass
        
if __name__ == '__main__':
    
    p = ooop()

