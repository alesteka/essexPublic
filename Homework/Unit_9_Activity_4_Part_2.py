import Uni9Activity4
import unittest

#run program:
#python -m unittest test_assertControl.py

class TestAssertControl(unittest.TestCase):

    def test_equal_strings(self):

        equal_strings = Uni9Activity4.assertControl()
        self.assertEquals(equal_strings.equal_strings(), False)       
        
    def test_concatenation(self):

        assertCheck = Uni9Activity4.assertControl()        
        self.assertEquals(assertCheck.concatenation(), 'HelloWorld!')
        #assert _response == type(str())

    def test_multiply(self):

        assertCheck = Uni9Activity4.assertControl()
        self.assertEquals(assertCheck.multiply(), 'HelloHelloHello')
        