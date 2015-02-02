#-------------------------------------------------------------------------------
# Name:        BUILDER
# Purpose:
#
# Author:      Amanda
#
# Created:     31/01/2015
# Copyright:   (c) Amanda 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Product(object):
    def __init__(self, type_name):
        self.type = type_name
        self.part = None

    def view(self):
        print(
            "This Product is a " +
            self.type +
            " with; " +
            str(self.part)
            )

class AbstractBuilder(object):
    def BuilPart(self):
        raise NotImplementedError("Classe abstrata")

class ConcreteBuilder(AbstractBuilder):
    def __init__(self):
        self.product = Product("X")
    def buildPart(self):
        self.product.part = "part"

class Director(object):

    def __init__(self):
        self.builder = None

    def create(self):
        if(self.builder == None):
            raise NotImplementedError("No defined builder")
        self.builder.buildPart()
        return self.builder.product

def main():
    director = Director()

    director.builder = ConcreteBuilder()
    product = director.create()
    product.view()

if __name__ == '__main__':
    main()
