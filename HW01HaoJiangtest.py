#coding=utf-8
#author:Hao Jiang
#homework01 test
import unittest
from HW01_Hao_Jiang import classifyTraingle

class TestTriangles(unittest.TestCase): #test
    def testSet1(self):
        self.assertEqual(classifyTraingle(3,4,5),"right triangles")

    def testSet2(self):
        self.assertEqual(classifyTraingle(1,1,1),'equilateral triangles')

    def testSet3(self):
        self.assertEqual(classifyTraingle(6,6,7),'isosceles triangles')
    
    def testSet4(self):
        self.assertEqual(classifyTraingle(2,3,4),'scalene triangles')

    def testSet5(self):
        self.assertEqual(classifyTraingle(1,2,7),'not a triangle')



if __name__ == '__main__': 
    unittest.main(exit=False)