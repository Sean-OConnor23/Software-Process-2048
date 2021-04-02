import unittest
import Tiles2048.shift as shift

class shiftTest(unittest.TestCase):
    #reusing code for calculating hash256 from last assignment. 
    #Thus, we can assume its functionality is correct. 
    def test_shift_HappyPathTest010(self):
        userParms = {'op': 'shift', 'grid':'0020000020000000', 'score': '0', 'direction': 'down', 
                        'integrity': '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        self.assertEqual(actual.get('score'), '0')          
        
    def test_shift_HappyPathTest020(self):
        userParms = {'op': 'shift', 'grid':'0000004024402020', 'score': '4', 'direction': 'up', 
                        'integrity': '2A2EF0D1BEA22B9D6AB67C482BFF954F93F6A3617EF052E11DD8776BFFB7325A'}
        actual = shift._shift(userParms)
        self.assertEqual(actual.get('score'), '16') 
        
    def test_shift_SadPathTest010(self):
       