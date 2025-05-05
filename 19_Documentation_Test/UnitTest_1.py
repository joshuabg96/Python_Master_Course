import unittest

def double(a): return a*2
def sum(a,b): return a + b
def even(a): return True if a%2 == 0 else False

class Test(unittest.TestCase):
    def test_double(self):
        self.assertEqual(double(10), 20)
        self.assertEqual(double('Ab'),'AbAb')

    def test_sum(self):
        self.assertEqual(sum(-15,15),0)
        self.assertEqual(sum('Ab','cd'),'Abcd')

    def test_Even(self):
        self.assertEqual(even(11),False)
        self.assertEqual(even(68),True)

class CharTest(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hola'.upper(),'HOLA')

    def test_isupper(self):
        self.assertTrue('HOLA'.isupper())
        self.assertFalse('hola'.isupper())

    def test_split(self):
        s = 'Hola mundo'
        self.assertEqual(s.split(" "), ['Hola','mundo'])



unittest.main()