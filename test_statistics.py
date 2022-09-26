import unittest
import getStatistics


class validateStatistics(unittest.TestCase):
    
    def testInputType(self):
        self.assertTrue(getStatistics.getInputTypeOfCurrentSamples([3,3,5,4,10,11,12.0]) == False)
        self.assertFalse(getStatistics.getInputTypeOfCurrentSamples([3,3,5,4,10,11,12]) == True)
                      
    def testArrangeInputAsConsecutiveNumbers(self):
        self.assertNotEqual((getStatistics.getCurrentSampleReadingsAsConsecutiveNumbers([9,3,3,4,5,10,11,12])),[3,3,4,5,10,11,12,9])
        self.assertEqual((getStatistics.getCurrentSampleReadingsAsConsecutiveNumbers([11,3,3,4,5,10,12])),[3,3,4,5,10,11,12])
    
            
    def testArrangeConsecutiveGroupsWithNumberOfReadings(self):
        self.assertNotEqual((getStatistics.getConsecutiveGroupsWithNumberOfReadings([3,3,4,5,10,11,12])),("  [3-4, 2]  [5-12, 4] "))
        self.assertEqual((getStatistics.getConsecutiveGroupsWithNumberOfReadings([3,3,4,5,10,11,12])),("  [3-5, 4]  [10-12, 3] "))
 
if __name__ == '__main__':
    unittest.main()
