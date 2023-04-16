import unittest
import Unit10Activity4

class TestMainClass(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Started testing")
    
    @classmethod
    def tearDownClass(cls):
        print("\nFinished testing")
    
    def setUp(self) -> None:
        self.obj = Unit10Activity4.methods()
        
    def tearDown(self) -> None:
        pass

    def test_add(self):
        self.assertEqual(self.obj.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.obj.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.obj.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.obj.divide(6, 3), 2)

        with self.assertRaises(ZeroDivisionError):
            self.obj.divide(6, 0)


