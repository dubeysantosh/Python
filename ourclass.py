#!/usr/bin/python

class Joe(object):
    def callme(self,args):
        print('calling "callme" methonth with instance: ' + args)
        print (self)

    greeting = 'hello, Santosh'


thisSan = Joe()

thisSan.callme('Santosh')
print thisSan

print thisSan.greeting