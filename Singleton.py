#!/usr/bin/python
#coding:utf8
'''
Singleton
'''

class Singleton(object):
    ''''' A python style singleton '''
    '''
    # One singleton for one subclass 
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            org = super(Singleton, cls)
            cls._instance = org.__new__(cls)
        return cls._instance
    '''
    # The only singleton for all subclasses
    def __new__(cls, *args, **kw):
        if not hasattr(Singleton, '_instance'):
            Singleton._instance = object.__new__(cls)
        return Singleton._instance

    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s

if __name__ == '__main__':
    class SingleSpam(Singleton):
        pass


    s1 = SingleSpam('spam')
    print(id(s1), s1)
    s2 = Singleton('spa')
    print(id(s2), s2)
    print(id(s1), s1)