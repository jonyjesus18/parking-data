import requests
import json
import pandas as pd
import time
import subprocess

from main import parking_data
first_row = ('Last update','Parking Name','Occupancy','Occupancy %','Status','Hour of sampling',
             'Last update','Parking Name','Occupancy','Occupancy %','Status','Hour of sampling',
             'Last update','Parking Name','Occupancy','Occupancy %','Status','Hour of sampling',
             'Last update','Parking Name','Occupancy','Occupancy %','Status','Hour of sampling',
             'Last update','Parking Name','Occupancy','Occupancy %','Status','Hour of sampling',
             'Last update','Parking Name','Occupancy','Occupancy %','Status','Hour of sampling',
             'Last update','Parking Name','Occupancy','Occupancy %','Status','Hour of sampling',)

# with open('parking.csv', 'a') as f:
#        text = str(first_row)
#        f.write(text + '\n')

start_time = time.time()
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    interval = 10 #in minutes
    if elapsed_time > interval*60:
        start_time = time.time()  # whatever goes uner here gets repeated every interval
        subprocess.call([r'C:\Users\joaom\OneDrive\Desktop\Run_Script.bat'])


