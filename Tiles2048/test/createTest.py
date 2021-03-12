import unittest
import Tiles2048.create as create

class CreateTest(unittest.TestCase):

#  The following is included only for illustrative purposes.  It tests nothing
#  useful.  Please delete and replace with your own test code.
    def test_create_HappyPathTest010(self):
        userParms = {'op': 'create', 'size': '4'}
        expectedResult = {'grid': '0020000020000000', 'score': '0', 'integrity': 
                            '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5', 'status': 'ok'}
        actualResult = create._create(userParms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test_create_HappyPathTest020(self):
        userParms = {'op': 'create', 'size': '4'}
        listCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        i = 0
        while (i < 16):
            tempResult = create._create(userParms)
            tempGrid = tempResult.get('grid')
            count = 0
            for gridVal in tempGrid:
                if (gridVal == "2"):
                    listCount[count] = listCount[count] + 1
                count = count + 1
            i = i + 1
        for count in listCount:
            if (count > 4):
                self.assertFalse(self)
                
        self.assertTrue(self)
            
    
