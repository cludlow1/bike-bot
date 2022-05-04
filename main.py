from dotenv import load_dotenv
import os
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pandas as pd

load_dotenv()
CLIENT_ID=os.getenv("CLIENT_ID")
CLIENT_SECRET=os.getenv("CLIENT_SECRET")
REFRESH_TOKEN=os.getenv("REFRESH_TOKEN")

payload= {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'refresh_token': REFRESH_TOKEN,
    'grant_type': "refresh_token",
    'f': 'json',
}

auth_url = "https://www.strava.com/oauth/token"
activities_url = "https://www.strava.com/api/v3/athlete/activities"


def getMyData():
    print("Requesting Token...\n")
    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()['access_token']
    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 200, 'page': 1}
    my_dataset = requests.get(activities_url, headers=header,params=param).json()

    #activities = pd.json_normalize(my_dataset)
    print(my_dataset)

    cols = ['name', 'upload_id', 'type', 'distance', 'moving_time',
             'average_speed', 'max_speed','total_elevation_gain',
             'start_date_local'
           ]

    #activities = activities[cols]



if __name__ == "__main__":
    getMyData()
