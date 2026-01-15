import unittest # for unit testing

class TestTDD(unittest.TestCase):
    def test_tdd(self):
        self.assertEqual(2+2,4)

if __name__ == "__main__":
    unittest.main()