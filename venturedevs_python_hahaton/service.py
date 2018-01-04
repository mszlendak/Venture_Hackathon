import requests
from datetime import datetime
import os
import csv

from .settings import FORECASTS_DIR, API_URL


def get_forecasts_from_api(woeid):
    r = requests.get(API_URL + "/location/" + str(woeid))
    if r.status_code == 404:
        return None
    else:
        return r.json()


def forecast_to_list(forecast):
    return [[y[1] for y in x.items()] for x in forecast["consolidated_weather"]]


def get_forecast_file_path(woeid):
    now = datetime.now()
    return (FORECASTS_DIR + "/" + str(woeid) + "/" + now.strftime('%d-%m-%y'), now.strftime('%H:%M:%S') + ".csv")




def save_forecast(forecast, dir, file_name):


    os.makedirs(dir, exist_ok=True)

    f = forecast_to_list(forecast)

    with open(os.path.join(dir,file_name), 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='\t',
                                quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerows(f)
