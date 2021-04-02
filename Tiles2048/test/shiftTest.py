import unittest
import Tiles2048.shift as shift

class shiftTest(unittest.TestCase):
    #reusing code for calculating hash256 from last assignment. 
    #Thus, we can assume its functionality is correct. 
    def test_shift_HappyPathTest010(self):
        userParms = {'op': 'shift', 'grid':'20002000000000', 'score': '0', 'direction': 'up', 
                        'integrity': '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        grid = str(actual.get('grid'))
        val = grid[0]
        self.assertEqual(val, '4')          
        
    def test_shift_HappyPathTest020(self):
        userParms = {'op': 'shift', 'grid':'0000004024402020', 'score': '4', 'direction': 'up', 
                        'integrity': '2A2EF0D1BEA22B9D6AB67C482BFF954F93F6A3617EF052E11DD8776BFFB7325A'}
        actual = shift._shift(userParms)
        self.assertEqual(actual.get('score'), '16') 
    #Tests to make sure input contains grid value 
    def test_shift_SadPathTest010(self):
        userParms = {'op': 'shift', 'score': '4', 'direction': 'up', 
                        'integrity': '2A2EF0D1BEA22B9D6AB67C482BFF954F93F6A3617EF052E11DD8776BFFB7325A'}
        actual = shift._shift(userParms)
        expected = {'status': 'error: missing grid'}
        self.assertEqual(actual, expected)
    #Tests for an invalid grid length 
    def test_shift_SadPathTest020(self):
        userParms = {'op': 'shift', 'grid':'002000002000', 'score': '0', 'direction': 'down', 
                        'integrity': '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        expected = {'status': 'error: invalid grid'}
        self.assertEqual(actual, expected)
    #Tests for an invalid grid value 
    def test_shift_SadPathTest030(self):
        userParms = {'op': 'shift', 'grid':'0020000020000005', 'score': '0', 'direction': 'down', 
                        'integrity': '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        expected = {'status': 'error: invalid grid'}
        self.assertEqual(actual, expected)
    #Tests for a valid score 
    def test_shift_SadPathTest040(self):
        userParms = {'op': 'shift', 'grid':'002000002000', 'score': '1', 'direction': 'down', 
                        'integrity': '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        expected = {'status': 'error: invalid score'}
        self.assertEqual(actual, expected)
    #Tests for a valid direction 
    def test_shift_SadPathTest050(self):
        userParms = {'op': 'shift', 'grid':'20002000000000', 'score': '0', 'direction': 'back', 
                        'integrity': '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        expected = {'status': 'error: invalid direction'}
        self.assertEqual(actual, expected)
    #Tests to see if shift is avaliable 
    def test_shift_SadPathTest060(self):
        userParms = {'op': 'shift', 'grid':'2222222222222222', 'score': '0', 'direction': 'down', 
                        'integrity': '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        expected = {'status': 'error: no shift possible'}
        self.assertEqual(actual, expected)
    #Tests for a good integrity value 
    def test_shift_SadPathTest070(self):
        userParms = {'op': 'shift', 'grid':'20002000002000', 'score': '0', 'direction': 'back', 
                        'integrity': '7CD5E3DEAB08FCAE8F64433DC4AF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        expected = {'status': 'error: bad integrity value'}
        self.assertEqual(actual, expected)
        
       