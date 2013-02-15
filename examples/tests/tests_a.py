import unittest

class Hello(unittest.TestCase):

    def setUp(self):
        pass

    def test_fail(self):
        print 1 / 0
        
    def test_two(self):
        self.assertTrue(True)

    def tearDown(self):
        pass
        
class World(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        self.assertTrue(True)

    def tearDown(self):
        pass