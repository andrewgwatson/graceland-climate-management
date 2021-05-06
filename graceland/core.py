#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
 
"""
    /|
 .-((--.
( '`^'; )   Graceland Chili House
`;#    |    Micro Controller Climate Management System
 \#    |    https://github.com/andrewgwatson/graceland-climate-management
  \#   \             
   '-.  )   
      \(
       `
""" 
 
# Here comes your imports 
# Here comes your (few) global variables 
# Here comes your class definitions 

class Climate:
    
    def air_temperature(self):
        return '33.23453869203°'
    
    def light_level(self):
        return '1.23 lux'

    def soil_temperature(self, sensor):
        return 'soiltemp'+str(sensor)

# Here comes your function definitions 
 
def main(): 
    c = Climate()
    print(c.air_temperature())
    print(c.light_level())
    print(c.soil_temperature(1))
    print(c.soil_temperature(2))
    print(c.soil_temperature(3))


 
 
if __name__ == "__main__" : main() 