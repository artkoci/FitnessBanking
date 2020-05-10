from stravaio import strava_oauth2
from stravaio import StravaIO

CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET_ID = 'YOUR_CLIENT_SECRET_ID'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

KILOMETERS = 1000.00

def get_athlete(access_token=None):
    # If the token is stored as an environment varible it is not neccessary
    # to pass it as an input parameters
    client = StravaIO(access_token=ACCESS_TOKEN)
    athlete = client.get_logged_in_athlete()

    if athlete is None:
        #You need to authorise the app if you have not done so, or your
        #access token has expired. A pop-up window will open
        oauth2 = strava_oauth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET_ID)
        client = StravaIO(access_token=oauth2['access_token'])
        athlete = client.get_logged_in_athlete()
    return athlete


def shoe_distance(client):
    # Dump athlete into a JSON friendly dict (e.g. all datetimes are converted into iso8601)
    athlete_dict = client.to_dict()
    shoe_kilometage = athlete_dict["shoes"][0]["distance"] / KILOMETERS
    return shoe_kilometage


def main():
    client = get_athlete(access_token=ACCESS_TOKEN)
    kilometrage = shoe_distance(client=client)
    return kilometrage

if __name__=="__main__":
    print("Shoe kilometrage: ", main())