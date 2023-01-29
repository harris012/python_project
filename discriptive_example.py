# 1. data-descriptors
# 2. self. dict ['d']
# 3. non-data-descriptors

class D:
    def __int__(self):
        print('__int__')
    def __get__(self, inst, owner=None):
        print(f'__get__')
        return 5

class C:
    d = D()
    def __int__(self):
        self.__dict__['d'] = 9

print(C().d)
