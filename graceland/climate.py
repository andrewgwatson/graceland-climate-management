#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

import logging, sys, config
# LTR559 = Light & Proximity sensor
# BME280 = Temperature, Pressure & Humidity sensor

try:
    from ltr559 import LTR559
except ImportError:
    from stubs import ltr559_STUB
    LTR559 = ltr559_STUB
    
try:
    from bme280 import BME280
except ImportError:
    from stubs import bme280_STUB
    BME280 = bme280_STUB
 
try:
    import GROW
except ImportError:
    from stubs import grow_STUB
    GROW = grow_STUB
 

def current_air_temperature():
        t = BME280.get_temperature()
        logging.info("""Temp: {:06.03f} {:}""".format(t, config.units['temp']))
        return t

def current_humidity():
        h = BME280.get_humidity()
        logging.info("""Humidity: {:06.03f} {:}""".format(h, config.units['humidity']))
        return h

def current_air_pressure():
        p = BME280.get_pressure()
        logging.info("""Pressure: {:06.03f} {:}""".format(p, config.units['airpressure']))
        return p
        
def current_light_level():
        l = LTR559.get_lux()
        logging.info("""Light: {:06.03f} {:}""".format(l, config.units['light']))
        return l
#       prox = ltr559.get_proximity()
        
def current_soil_moisture(sensor):
        m = GROW.moisture()
        logging.info("""Soil Moisture on sensor {:} : {:} {:}""".format(sensor, m, config.units['moisture']))
        return m

#logging.info("""Light: {:05.02f} Lux""".format(current_light_level()))

def headless():
        print('Number of arguments:', len(sys.argv), 'arguments.')
        print('Argument List:', str(sys.argv))

if __name__ == "__main__" : headless()
        
