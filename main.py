import requests
import json
import pandas as pd
import datetime
def get_time():
    x = datetime.datetime.now().hour
    y = datetime.datetime.now().minute
    if y < 10:
        y= '0'+ str(y)
    r = str(x) + ':' + str(y)
    return r

response = requests.get("https://data.bathhacked.org/api/datasets/8/rows?page=1&per_page=15").json()
content = json.dumps(response, indent=1, sort_keys=True)
df = pd.json_normalize(json.loads(content), "data")
pd.set_option('display.max_columns', None)

parking_data = df.drop(['dateuploaded','description','easting','northing','id', 'location.geojson.type',
       'location.latitude', 'location.longitude', 'location.geojson.coordinates'], axis =1)



row = (parking_data['lastupdate'][0] ,parking_data['name'][0], parking_data['occupancy'][0], parking_data['percentage'][0],parking_data['status'][0],get_time(),
       parking_data['lastupdate'][1] ,parking_data['name'][1], parking_data['occupancy'][1], parking_data['percentage'][1],parking_data['status'][1],get_time(),
       parking_data['lastupdate'][2] ,parking_data['name'][2], parking_data['occupancy'][2], parking_data['percentage'][2],parking_data['status'][2],get_time(),
       parking_data['lastupdate'][3] ,parking_data['name'][3], parking_data['occupancy'][3], parking_data['percentage'][3],parking_data['status'][3],get_time(),
       parking_data['lastupdate'][4] ,parking_data['name'][4], parking_data['occupancy'][4], parking_data['percentage'][4],parking_data['status'][4],get_time(),
       parking_data['lastupdate'][5] ,parking_data['name'][5], parking_data['occupancy'][5], parking_data['percentage'][5],parking_data['status'][5],get_time(),
       parking_data['lastupdate'][6] ,parking_data['name'][6], parking_data['occupancy'][6], parking_data['percentage'][6],parking_data['status'][6],get_time(),
       )

with open('parking.csv', 'a') as f:
       text = str(row)
       f.write(text + '\n')
