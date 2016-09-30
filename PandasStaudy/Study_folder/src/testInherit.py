import math
import numpy
class Animal(object):
    def __init__(self, name):
        self.name = name
        
    def getInfo(self):
        print "This is animal's name: %s" %self.name
        
    def sound(self):
        print "The sound of this animal goes?"
        
class Dog(Animal):
    def __init__(self, name, size):
        super(Dog, self).__init__(name)
        self.__size = size
        
    def getInfo(self):
        print "This dog's name: %s" %self.name
        print "This dog's size: %s" %self.__size

class Cat(Animal):
    def sound(self):
        print "The sound of cat goes meow"

cat = Cat('kaka'); dog = Dog('coco', 'small')

indices = [0,1,2,3,4]
values = [6,7,8,9,0]
def sp(indices,values):
    vec = [indices,values]
    #ind = values.index(numpy.nonzero(values))
    print max(vec[1]).index
    #===========================================================================
    # print indices[ind],values[ind]
    # return ind,max(values)
    #===========================================================================
sp(indices,values)

