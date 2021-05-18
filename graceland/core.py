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
    
    logging.basicConfig(filename='graceland.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)-2s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)-2s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    c = climate.snapshot()
    # Write sensor data to csv as a simple timeseries
    with open(config.db["filename"], 'a', newline='') as csvfile:
        db = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # db.writerow([f"{datetime.now():%Y-%m-%d %H:%M:%S}",c])
        db.writerow([f"{datetime.now():%Y-%m-%d %H:%M:%S}",
                     c['temp'],
                     c['humidity'],
                     c['airpressure'],
                     c['light'],
                     c['moisturesensors'][0],
                     c['moisturesensors'][1],
                     c['moisturesensors'][2],
                     ])
        
if __name__ == "__main__" : main()