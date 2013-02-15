import unittest

class Foo(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        self.assertEqual(1, 1)

    def tearDown(self):
        pass
        
class Bar(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        self.assertTrue(True)
        
    @unittest.skip("demonstrating skipping")
    def test_skipping(self):
        self.fail("shouldn't happen")

    def tearDown(self):
        pass