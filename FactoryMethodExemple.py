#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Amanda
#
# Created:     01/02/2015
# Copyright:   (c) Amanda 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# Written by: DGC
#==============================================================================

class AbstractFactory(object):
    def getFactory(self, tipoFabrica):
        if tipoFabrica == "brinquedo":
            return ConcreteFactoryBrinquedo()
        if tipoFabrica == "bola":
            return ConcreteFactoryBola()
    def create(self):
        raise NotImplementedError("Classe abstrata")

class ConcreteFactoryBrinquedo(AbstractFactory):
    def create(self):
        return ProductBrinquedo()

class ConcreteFactoryBola(AbstractFactory):
    def create(self):
        return ProductBola()

class AbstractProduct(object):
    def __init__(self):
        self.nome = None
        self.tempo = None
    def description(self):
        raise NotImplementedError("Classe abstrata")

class ProductBrinquedo(AbstractProduct):
    def __init__(self):
        self.nome = "brinquedo"
        self.tempo = 10
    def description(self):
        print(self.nome)
        print(self.tempo)

class ProductBola(AbstractProduct):
    def __init__(self):
        self.nome = "bola"
        self.tempo = 15
    def description(self):
        print(self.nome)
        print(self.tempo)

def main():
    factory = AbstractFactory().getFactory("brinquedo")
    brinquedo = factory.create()
    brinquedo.description()

    factory = AbstractFactory().getFactory("bola")
    brinquedo = factory.create()
    brinquedo.description()
if __name__ == '__main__':
    main()
