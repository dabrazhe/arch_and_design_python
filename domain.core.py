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


    setA = frozenset([])
    setB = frozenset([])

    # setB = []   # what do you think is better to define an non init set?

    def __init__(self, setA, setB):
        """Constructor: Object created as immutable (value for some) object, by using settatr on all the public properties. Yes, python has only public properies.. """

        self.setA = setA
        self.setB = setB

        # Let's validate our input data first. Using the logic, the string cannot be empty.
        if not (setA & setB):
            raise ValueError(self, "Object Creation Failed." + str(setA)+ str(setB))

        # object.__setattr__(self, "setA", setA)
       #  object.__setattr__(self, "setB", setB)

        # remove this side effect from the actual implementation
        print getdoc(self)
        print getdoc(getattr(self, getframeinfo(currentframe()).function))


class SomeAtomicSetType(object):
    """Example of atomic type. It's using validation """


class TestStringMethods(unittest.TestCase):

    def test_uri(self):
        #create an immutable object Importer


        set1a = set([1, 2, 3, 4, 100, 200, 1000])
        set1b = frozenset ([100, 200, 400, 500])    
        print str(set1a)
        print (', '.join(str(e) for e in set1a))
        print (', '.join(str(e) for e in set1b))
        # for x in set1b:
        #     x.
        # lambda (x: in set1a print (', '.x))


        bizLogic = SomeDomainServiceBizLogic(set1a,set1b )
        importer = ImporterCore("https://gator3154.hostgator.com:2083/cpsess0910541571/frontend/x3/index.php?login=1&post_login=22462794788126",[1,2])



        #importer.uri = "http://"
        #will not work with immutable object
        #importer.credentials = "TestCreds"
        #importer.__setattr__(self, "credentials", ["wouou!","\n Override!!"])
        print importer.credential_check()

        self.assertTrue(urlparse(importer.uri))

        for r in urlparse(importer.uri):

            print "url\t"+ r
            self.assertTrue(r)
        print self.credentials

        self.assertEqual(isinstance(importer.uri, str), True)
        self.assertRaises(TypeError)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world '
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

class ImporterCore(object):
    __doc = """Guten Tag. A sample Importer Core class here. I'm tres tres simple"""
    # string
    uri = ''
    credentials = None
     # call endpoint with credentials
    def credential_check(self):
        result = "200 OK"
        return result
    def exampleofBuzLogic(self):
        return md5(self.credentials)

    # def __init__
    def __init__(self, url, credentials):
        """Constructor: Object created as immutable (value for some) object, by using settatr on all the public properties. Yes, python has only public properies.. """

        # Let's validate our input data first. Using the logic, the string cannot be empty.



        print getdoc(self)
        print getdoc(getattr(self, getframeinfo(currentframe()).function))

        object.__setattr__(self, "uri", url)
        object.__setattr__(self, "credentials", credentials)


        print self

        for r in urlparse(self.uri):
            print "url\t"+ r

        print self.credentials
        print "_____________\n"

    def __setattr__(self, *args):
        raise TypeError

    def __getattr__(self, *args):
        raise TypeError
