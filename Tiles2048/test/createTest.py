import unittest
import Tiles2048.create as create

class CreateTest(unittest.TestCase):
   
#Tests that the grid value is randomly generate with two instances of 2    
    def test_create_HappyPathTest010(self):
        userParms = {'op': 'create', 'size': '4'}
        listCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        i = 0
        while (i < 16):
            tempResult = create._create(userParms)
            tempGrid = tempResult.get('grid')
            if (tempGrid == ''):
                self.assertFalse(self)
            count = 0
            twoCount = 0
            for gridVal in tempGrid:
                if (gridVal == '2'):
                    listCount[count] = listCount[count] + 1
                    twoCount = twoCount + 1
                count = count + 1
            if (twoCount != 2):
                self.assertFalse(self)
            i = i + 1
        for count in listCount:
            if ((count / 16) > 0.4):
                self.assertFalse(self)
              
        self.assertTrue(self)
         
#Tests that the value of score is initialized correctly    
    def test_create_HappyPathTest020(self):
        userParms = {'op': 'create', 'size': '4'}
        action = create._create(userParms)
        score = action.get('score')
        self.assertEqual(score, '0')
        
#Tests that the value of status is initialized correctly 
    def test_create_HappyPathTest030(self):
        userParms = {'op': 'create', 'size': '4'}
        action = create._create(userParms)
        status = action.get('status')
        expectedResult = 'ok'
        self.assertEqual(status, expectedResult)
        
#Tests the value of integrity 
    def test_create_HappyPathTest040(self):
        inputDict = {'grid': '0020000020000000', 'score': '0', 
                        'integrity': '', 'status': 'ok'}        
        expectedResult = "7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5"       
        actualResult = create._calcIntegrity(inputDict)
        self.assertEqual(actualResult, expectedResult)
        
#Tests the value of integrity with different grid value        
    def test_create_HappyPathTest050(self):
        inputDict = {'grid': '2200000000000000', 'score': '0', 
                        'integrity': '', 'status': 'ok'}              
        expectedResult = "0C1E79CDC2D6D5FBA1A31203029C5D951EE92DBC87CB64BA80C41D58A2DE036E"     
        actualResult = create._calcIntegrity(inputDict)
        self.assertEqual(actualResult, expectedResult)
        
    
        
    
