#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Amanda
#
# Created:     31/01/2015
# Copyright:   (c) Amanda 2015
# Licence:     <your licence>
# COISAS ESTRANHAS NO PYTHON
# 1- Nao existe interface(analogo a java)
# 2- Nao eh nescessário utilizar classe abstrata
#-------------------------------------------------------------------------------

class AbstractFactory(object):
    def getFactory(self, tipoFabrica):
        if tipoFabrica == "X":
            return ConcreteFactory()
    def create(self):
        raise NotImplementedError("Classe abstrata")

class ConcreteFactory(AbstractFactory):
    def create(self):
        return Product()

class AbstractProduct(object):
    def description(self):
        raise NotImplementedError("Classe abstrata")

class Product(AbstractProduct):
    def description(self):
        print("product")

def main():
    factory = AbstractFactory().getFactory("X")
    product = factory.create()
    product.description()

if __name__ == '__main__':
    main()
