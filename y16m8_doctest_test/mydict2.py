class Dict(dict):
    '''
    A simple dict but also support access as x.y style

    >>> d1 = Dict()
    >>> d1['a'] = 1
    >>> d1.a
    1
    >>> d1.b = 2
    >>> d1['b']
    2
    >>> d2 = Dict(a=100, b=200, c='300')
    >>> d2.c
    '300'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''


    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('\'Dict\' object has no attribute \'%s\'' % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()

