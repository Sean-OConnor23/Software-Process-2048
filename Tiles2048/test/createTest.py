import unittest
import Tiles2048.create as create

class CreateTest(unittest.TestCase):

#  The following is included only for illustrative purposes.  It tests nothing
#  useful.  Please delete and replace with your own test code.        
    def test_create_HappyPathTest010(self):
        userParms = {'op': 'create', 'size': '4'}
        listCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        i = 0
        while (i < 16):
            tempResult = create._create(userParms)
            tempGrid = tempResult.get('grid')
            if (tempGrid == ''):
                self.assertFalse(self)
            count = 0
            for gridVal in tempGrid:
                if (gridVal == '2'):
                    listCount[count] = listCount[count] + 1
                count = count + 1
            i = i + 1
        for count in listCount:
            if (count > 4):
                self.assertFalse(self)
                
        self.assertTrue(self)
            
    def test_create_HappyPathTest020(self):
        userParms = {'op': 'create', 'size': '4'}
        action = create._create(userParms)
        score = action.get('score')
        self.assertEqual(score, '0')
        
    def test_create_HappyPathTest030(self):
        userParms = {'op': 'create', 'size': '4'}
        action = create._create(userParms)
        status = action.get('status')
        expectedResult = 'ok'
        self.assertEqual(status, expectedResult)
    
