import unittest
import Tiles2048.shift as shift

class shiftTest(unittest.TestCase):
    #reusing code for calculating hash256 from last assignment. 
    #Thus, we can assume its functionality is correct. 
    def test_shift_HappyPathTest010(self):
        userParms = {'op': 'shift', 'grid':'2000200000000000', 'score': '0', 'direction': 'up', 
                        'integrity': '10469CE866023129A5BFB507A4D641F98C4566747136F24A920AA1C846844320'}
        actual = shift._shift(userParms)
        grid = str(actual.get('grid'))
        val = grid[0]
        self.assertEqual(val, '4')          
        
    def test_shift_HappyPathTest020(self):
        userParms = {'op': 'shift', 'grid':'0000004024402020', 'score': '4', 'direction': 'up', 
                        'integrity': '2A2EF0D1BEA22B9D6AB67C482BFF954F93F6A3617EF052E11DD8776BFFB7325A'}
        actual = shift._shift(userParms)
        self.assertEqual(actual.get('score'), 16) 
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
        expected = {'status': 'error: bad integrity value'}
        self.assertEqual(actual, expected)
    #Tests for an invalid grid value 
    def test_shift_SadPathTest030(self):
        userParms = {'op': 'shift', 'grid':'0020000020000005', 'score': '0', 'direction': 'down', 
                        'integrity': '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        expected = {'status': 'error: bad integrity value'}
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
        userParms = {'op': 'shift', 'grid':'0020000020000000', 'score': '0', 'direction': 'back', 
                        'integrity': '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        expected = {'status': 'error: invalid direction'}
        self.assertEqual(actual, expected)
               
    #Tests for a good integrity value 
    def test_shift_SadPathTest070(self):
        userParms = {'op': 'shift', 'grid':'0020000020000000', 'score': '0', 'direction': 'back', 
                        'integrity': '7CD5E3DEAB0E8F64433DC4AF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        expected = {'status': 'error: invalid direction'}
        self.assertEqual(actual, expected)
        
    def test_shift_HappyPathTest030(self):
        userParms = {'op': 'shift', 'grid':'2222444488881616160', 'score': '9600', 'direction': 'left', 
                    'integrity': '66457746F0596CEE48B4FA4FA9C57A8A56A917F5B42F2600F12CD4266B9098BE'}
        actual = shift._shift(userParms)
        score = str(actual.get('score'))
        self.assertEqual(score, '9688') 
        
    #Start Assgn7
    #Most Testing will be done via local port
    def test_shift_SadPathTest080(self):
        userParms = {'op': 'shift', 'grid':'002000002000', 'score': '-7', 'direction': 'down', 
                        'integrity': '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        expected = {'status': 'error: invalid score'}
        self.assertEqual(actual, expected)
        
    def test_shift_SadPathTest090(self):
        userParms = {'op': 'shift', 'grid':'002000002000', 'score': 'h', 'direction': 'down', 
                        'integrity': '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        expected = {'status': 'error: invalid score'}
        self.assertEqual(actual, expected)
    def test_shift_SadPathTest100(self):
        userParms = {'op': 'shift', 'grid':'002000002000', 'score': '', 'direction': 'down', 
                        'integrity': '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'}
        actual = shift._shift(userParms)
        expected = {'status': 'error: invalid score'}
        self.assertEqual(actual, expected)   
                
    def test_shift_HappyPathTest040(self):
        userParms = {'op': 'shift', 'grid':'2481632641282562481632641280', 'score': '9600', 'direction': 'down', 
                    'integrity': 'CBD6F924B76E41871F106ABDE80AF9BA71350A53B0A148F26F16AF14CA5F6B06'}
        actual = shift._shift(userParms)
        score = str(actual.get('status'))
        self.assertEqual(score, 'lose')
                
    def test_shift_HappyPathTest050(self):
        userParms = {'op': 'shift', 'grid':'2222444488881616160', 'score': '9600', 'direction': 'up', 
                    'integrity': '66457746F0596CEE48B4FA4FA9C57A8A56A917F5B42F2600F12CD4266B9098BE'}
        actual = shift._shift(userParms)
        score = str(actual.get('score'))
        self.assertEqual(score, '9600')
        
        
    def test_shift_HappyPathTest060(self):
        userParms = {'op': 'shift', 'grid':'0000004024402020', 'score': '4', 
                    'integrity': '2A2EF0D1BEA22B9D6AB67C482BFF954F93F6A3617EF052E11DD8776BFFB7325A'}
        actual = shift._shift(userParms)
        score = str(actual.get('score'))
        self.assertEqual(score, '16')  
    
    
    