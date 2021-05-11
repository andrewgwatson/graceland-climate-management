#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
 
"""
    /|
 .-((--.
( '`^'; )   Graceland Chilis
`;#    |    Climate Monitoring & Management System
 \#    |    https://github.com/andrewgwatson/graceland-climate-management
  \#   \             
   '-.  )   
      \(
       `
""" 

import logging, config
import climate

def main():
    logging.basicConfig(filename='graceland.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)-2s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    c = climate
    logging.info("""Core Execution Started""")
    c.current_air_temperature()
    c.current_humidity()
    c.current_air_pressure()
    c.current_light_level()
    print(config.units["temp"])

 
 
if __name__ == "__main__" : main() 