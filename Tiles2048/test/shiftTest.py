import unittest
import Tiles2048.shift as shift

class shiftTest(unittest.TestCase):
    
    def test_shift_HappyPathTest010(self):
        userParms = {'op': 'shift', 'grid':'0020000020000000', 'score': '0', 'direction': 'down', 
                        'integrity': '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        self.assertEqual(actual.get('score'), '0')           