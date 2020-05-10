from stravaio import strava_oauth2
from stravaio import StravaIO

import json

with open('local-settings.json') as f:
    config = json.load(f)

CLIENT_ID = config['strava_client_id']
CLIENT_SECRET_ID = config['strava_client_secret']
ACCESS_TOKEN = config['strava_access_token']

KILOMETERS = 1000.00


def get_athlete(access_token=ACCESS_TOKEN):
    # If the token is stored as an environment variable it is not necessary
    # to pass it as an input parameters
    client = StravaIO(access_token=access_token)
    athlete = client.get_logged_in_athlete()

    if athlete is None:
        #You need to authorise the app if you have not done so,
        #or your access token has expired.
        oauth2 = strava_oauth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET_ID)
        client = StravaIO(access_token=oauth2['access_token'])
        athlete = client.get_logged_in_athlete()
    return athlete


def shoe_distance(client):
    # Dump athlete stats to a dict
    athlete_dict = client.to_dict()
    shoe_kilometage = athlete_dict["shoes"][0]["distance"] / KILOMETERS
    return shoe_kilometage


def main():
    client = get_athlete(ACCESS_TOKEN)
    kilometrage = shoe_distance(client=client)
    return kilometrage


if __name__=="__main__":
    main()