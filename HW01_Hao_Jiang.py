#coding=utf-8
#author:Hao Jiang
#HW01
import unittest
def classifyTraingle(a,b,c):
    if a + b < c or b +c <a: #Judge whether it is a triangle
        return("not a triangle")
    else:             #If the length of three sides conforms to the triangle, continue to judge what type of triangle it is
        if a == b == c:
            return("equilateral triangles")
        elif a == b or a == c or b==c:
            return("isosceles triangles")
        elif (a*a + b*b)==c*c or (b*b + c*c)==a*a:
            return("right triangles")
        else:
            return("scalene triangles")
    

if __name__=='__main__':  
    print("Input lengths of the triangle sides: ")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = classifyTraingle(a,b,c)
    print(d)
   
   