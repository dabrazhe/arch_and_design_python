import unittest
from urlparse import urlparse
from inspect import *
# from sets import Set
# import pytest


# core Module
# lets try to write some domain model core classes
# Start from an importer class
# it should take a url, login credentials, and have a run, and credential checks methods.
# Let's start by writing some test we can think of for the methods and properties for several use cases we can thinks of


class SomeDomainServiceBizLogic(object):
    """ I need to verify the data being fed to me and create operations, like intersection of two sets"""
    __locked = True

    setA = set([])
    setB = set([])
    operationResult = frozenset([])
    inits = "Test str"

    # setB = []   # what do you think is better to define an non init set?

    def __init__(self, setA, setB, inits = "Test "):
        """Constructor: Object created as immutable (value for some) object, by using settatr on all the public properties. Yes, python has only public properies.. """

        # Let's validate our input data first. Using the logic, the string cannot be empty.

        if  ((setA == None) ^ (setB == None)):
            raise ValueError(self, "Object Creation Failed." +  str(setA)+ "  " +   str(setB))
        # check if the right type., ie set.
        # isinstance

        object.__setattr__(self, "setA", setA)
        object.__setattr__(self, "setB", setB)
        object.__setattr__(self, "inits", inits)

        # remove this side effect from the actual implementation
        print getdoc(self)
        print getdoc(getattr(self, getframeinfo(currentframe()).function))


    def __setattr___(self, *args, **kw):
         raise Exception('immutable')  # define your own rather than use Exception
         return super(SomeDomainServiceBizLogic).__setattr__(self, *args, **kw)


    def __setattr__(self, *args):
       raise TypeError.message("The value of the object is considered Immutable")

    def __delattr__(self, *args):
       raise ValueError




    # some memory mgmt idea, have not though through it yet -- DA
    def getresult(self):
        """Methods should not change the state of the object to a wrong state """
        # TODO
        # if (self.operationResult <> None) & (self.operationResult.__sizeof__() > 10):
        #     raise ValueError
        # else:
        return self.operationResult

    def intersect(self):
        return self.setA.intersection(self.setB)




class SomeAtomicSetType(object):
    """Example of atomic type. It's using validation """


class TestStringMethods(unittest.TestCase):

    def test_uri(self):


        set1a = set([1, 2, 3, 4, 100, 200, 1000])
        set1b = frozenset ([100, 200, 400, 500])

        print str(set1a)
        print (', '.join(str(e) for e in set1b))

        # create an immutable object Importer
        bizLogic = SomeDomainServiceBizLogic(set1a,set1b)

        #will not work with immutable object
        # bizLogic.init = 500
        # bizLogic.setA = set([111])

        import pprint
        pprint.pprint(str(bizLogic.setB))
        pprint.pprint(bizLogic.intersect())

        #bizLogic.__setattr__(self, "credentials", ["wouou!","\n Override!!"])

        bizLogic.getresult()


        self.assertTrue((bizLogic.getresult()))
        self.assertEqual(bizLogic.intersect(), set1a.intersection(set1b))

        self.assertEqual(bizLogic.intersect(),set([100, 200]))

        self.assertEqual(isinstance(bizLogic.intersect(), set), True)
        self.assertRaises(TypeError)

        self.assertRaises(ValueError)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

# some usefull
# helper code == valid email address

    '''regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        '''


