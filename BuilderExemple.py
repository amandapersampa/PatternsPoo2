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
class ProductVehicle(object):

    def __init__(self, type_name):
        self.type = type_name
        self.wheels = None
        self.doors = None
        self.seats = None

    def view(self):
        print(
            "This vehicle is a " +
            self.type +
            " with; " +
            str(self.wheels) +
            " wheels, " +
            str(self.doors) +
            " doors, and " +
            str(self.seats) +
            " seats."
            )

#==============================================================================
class AbstractVehicleBuilder(object):
    def build_wheels(self):
        raise

    def build_doors(self):
        raise

    def build_seats(self):
        raise

#==============================================================================
class CarBuilder(AbstractVehicleBuilder):

    def __init__(self):
        self.vehicle = ProductVehicle("Car ")

    def build_wheels(self):
        self.vehicle.wheels = 4

    def build_doors(self):
        self.vehicle.doors = 3

    def build_seats(self):
        self.vehicle.seats = 5

#==============================================================================
class BikeBuilder(AbstractVehicleBuilder):

    def __init__(self):
        self.vehicle = ProductVehicle("Bike")

    def build_wheels(self):
        self.vehicle.wheels = 2

    def build_doors(self):
        self.vehicle.doors = 0

    def build_seats(self):
        self.vehicle.seats = 2

#==============================================================================
class DirectorVehicleManufacturer(object):

    def __init__(self):
        self.builder = None

    def create(self):
        if(self.builder == None):
            raise NotImplementedError("No defined builder")
        self.builder.build_wheels()
        self.builder.build_doors()
        self.builder.build_seats()
        return self.builder.vehicle

#==============================================================================
if (__name__ == "__main__"):
    manufacturer = DirectorVehicleManufacturer()

    manufacturer.builder = CarBuilder()
    car = manufacturer.create()
    car.view()

    manufacturer.builder = BikeBuilder()
    bike = manufacturer.create()
    bike.view()
