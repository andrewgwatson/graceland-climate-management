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

import logging, csv
from datetime import datetime
import config, climate

def main():
    
    # logging.basicConfig(filename='graceland.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)-2s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)-2s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    c = climate
    logging.info("""Core Execution Started""")
    c.current_air_temperature()
    c.current_humidity()
    c.current_air_pressure()
    c.current_light_level()
    c.current_soil_moisture(1)
    print(config.units["temp"])
    
    # Write sensor data to csv as a simple timeseries
    with open(config.db["filename"], 'a', newline='') as csvfile:
        db = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db.writerow([f"{datetime.now():%Y-%m-%d %H:%M:%S}",1,2,3,4,5,6,7])
        
if __name__ == "__main__" : main()