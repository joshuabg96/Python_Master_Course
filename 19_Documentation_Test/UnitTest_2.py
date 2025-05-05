import unittest

def double(a): return a*2

class Test_testing(unittest.TestCase):
    def setUp(self):
        print("Configurating context")
        self.numbers = [1,2,3,4,5]

    def Test(self):
        print("Doing test")
        r = [double(n) for n in self.numbers]
        self.assertEqual(r,[2,3,6,5,10])

    def tearDown(self):
        print("Deleting configuration")
        del(self.numbers)

if __name__ == '__main__':
    unittest.main()