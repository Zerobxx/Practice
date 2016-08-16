class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, attr):
        return Chain('%s/%s' %(self._path, attr))

    def __str__(self):
        return self._path

    # __repr__ == __str__

print Chain().api.server.port