import csv
import logging, sys, config
from datetime import datetime
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)-2s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
with open('timeseriesdata.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([f"{datetime.now():%Y-%m-%d %H:%M:%S}",1,2,3,4,5,6,7])
    #logging.debug(f"{datetime.now():%Y-%m-%d %H:%M:%S}")
    #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])