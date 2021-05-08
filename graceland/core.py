#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
 
"""
    /|
 .-((--.
( '`^'; )   Graceland Chilis
`;#    |    Micro Controller Climate Management System
 \#    |    https://github.com/andrewgwatson/graceland-climate-management
  \#   \             
   '-.  )   
      \(
       `
""" 

import config
import climate

# Here comes your (few) global variables

# Here comes your class definitions 

class ClimateX:
    
    def air_temperature(self):
        return '33.23453869203°'
    
    
 
def main(): 
    c = climate
    print(c.current_air_temperature())
    print(c.light_level())
    print(c.soil_temperature(1))
    print(c.soil_temperature(2))
    print(c.soil_temperature(3))
    print(settings.controllers)

 
 
if __name__ == "__main__" : main() 