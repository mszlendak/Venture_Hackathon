EXAMPLE_FORECAST = {
    "consolidated_weather": [
        {
            "id": 5051757080084480,
            "weather_state_name": "Heavy Cloud",
            "weather_state_abbr": "hc",
            "wind_direction_compass": "WNW",
            "created": "2017-11-06T08:31:54.226710Z",
            "applicable_date": "2017-11-06",
            "min_temp": 4.247999999999999,
            "max_temp": 8.976,
            "the_temp": 7.825,
            "wind_speed": 4.902342398022747,
            "wind_direction": 301.1914683020558,
            "air_pressure": 1024.095,
            "humidity": 88,
            "visibility": 10.127418376680186,
            "predictability": 71
        },
        {
            "id": 6170269643177984,
            "weather_state_name": "Heavy Cloud",
            "weather_state_abbr": "hc",
            "wind_direction_compass": "ENE",
            "created": "2017-11-06T08:31:57.754540Z",
            "applicable_date": "2017-11-07",
            "min_temp": 3.91,
            "max_temp": 8.441999999999998,
            "the_temp": 6.82,
            "wind_speed": 6.009255079630956,
            "wind_direction": 76.31116772318363,
            "air_pressure": 1029.995,
            "humidity": 86,
            "visibility": 13.804382406744612,
            "predictability": 71
        },
        {
            "id": 6622946579709952,
            "weather_state_name": "Heavy Cloud",
            "weather_state_abbr": "hc",
            "wind_direction_compass": "E",
            "created": "2017-11-06T08:32:00.331770Z",
            "applicable_date": "2017-11-08",
            "min_temp": 5.098000000000001,
            "max_temp": 8.441999999999998,
            "the_temp": 7.645,
            "wind_speed": 6.578699405804502,
            "wind_direction": 96.98394027585256,
            "air_pressure": 1020.88,
            "humidity": 88,
            "visibility": 14.50839596754951,
            "predictability": 71
        },
        {
            "id": 5877901287227392,
            "weather_state_name": "Showers",
            "weather_state_abbr": "s",
            "wind_direction_compass": "WSW",
            "created": "2017-11-06T08:32:03.840220Z",
            "applicable_date": "2017-11-09",
            "min_temp": 4.964,
            "max_temp": 7.956,
            "the_temp": 7.35,
            "wind_speed": 4.937034687708582,
            "wind_direction": 256.9335555372414,
            "air_pressure": 1021.25,
            "humidity": 86,
            "visibility": 8.689876123439115,
            "predictability": 73
        },
        {
            "id": 5308185955008512,
            "weather_state_name": "Showers",
            "weather_state_abbr": "s",
            "wind_direction_compass": "WSW",
            "created": "2017-11-06T08:32:06.374360Z",
            "applicable_date": "2017-11-10",
            "min_temp": 6.06,
            "max_temp": 8.738,
            "the_temp": 8.805,
            "wind_speed": 9.258654904751452,
            "wind_direction": 251.25388620941533,
            "air_pressure": 1016.915,
            "humidity": 83,
            "visibility": 16.007764654418196,
            "predictability": 73
        },
        {
            "id": 5607319689756672,
            "weather_state_name": "Light Rain",
            "weather_state_abbr": "lr",
            "wind_direction_compass": "W",
            "created": "2017-11-06T08:32:09.643640Z",
            "applicable_date": "2017-11-11",
            "min_temp": 5.99,
            "max_temp": 9.232,
            "the_temp": 10.64,
            "wind_speed": 11.03448729420186,
            "wind_direction": 259.818149683424,
            "air_pressure": 1012.39,
            "humidity": 81,
            "visibility": None,
            "predictability": 75
        }
    ],
    "time": "2017-11-06T11:00:52.182970+01:00",
    "sun_rise": "2017-11-06T07:12:06.177613+01:00",
    "sun_set": "2017-11-06T16:27:26.674010+01:00",
    "timezone_name": "LMT",
    "parent": {
        "title": "Germany",
        "location_type": "Country",
        "woeid": 23424829,
        "latt_long": "51.164181,10.454150"
    },
    "sources": [
        {
            "title": "BBC",
            "slug": "bbc",
            "url": "http://www.bbc.co.uk/weather/",
            "crawl_rate": 180
        },
        {
            "title": "Forecast.io",
            "slug": "forecast-io",
            "url": "http://forecast.io/",
            "crawl_rate": 480
        },
        {
            "title": "HAMweather",
            "slug": "hamweather",
            "url": "http://www.hamweather.com/",
            "crawl_rate": 360
        },
        {
            "title": "Met Office",
            "slug": "met-office",
            "url": "http://www.metoffice.gov.uk/",
            "crawl_rate": 180
        },
        {
            "title": "OpenWeatherMap",
            "slug": "openweathermap",
            "url": "http://openweathermap.org/",
            "crawl_rate": 360
        },
        {
            "title": "Weather Underground",
            "slug": "wunderground",
            "url": "https://www.wunderground.com/?apiref=fc30dc3cd224e19b",
            "crawl_rate": 720
        },
        {
            "title": "World Weather Online",
            "slug": "world-weather-online",
            "url": "http://www.worldweatheronline.com/",
            "crawl_rate": 360
        },
        {
            "title": "Yahoo",
            "slug": "yahoo",
            "url": "http://weather.yahoo.com/",
            "crawl_rate": 180
        }
    ],
    "title": "Berlin",
    "location_type": "City",
    "woeid": 638242,
    "latt_long": "52.516071,13.376980",
    "timezone": "Europe/Berlin"
}


EXAMPLE_CSV_FILE = '5051757080084480\tHeavy Cloud\thc\tWNW\t2017-11-06T08:31:54.226710Z\t2017-11-06\t4.247999999999999\t8.976\t7.825\t4.902342398022747\t301.1914683020558\t1024.095\t88\t10.127418376680186\t71\n6170269643177984\tHeavy Cloud\thc\tENE\t2017-11-06T08:31:57.754540Z\t2017-11-07\t3.91\t8.441999999999998\t6.82\t6.009255079630956\t76.31116772318363\t1029.995\t86\t13.804382406744612\t71\n6622946579709952\tHeavy Cloud\thc\tE\t2017-11-06T08:32:00.331770Z\t2017-11-08\t5.098000000000001\t8.441999999999998\t7.645\t6.578699405804502\t96.98394027585256\t1020.88\t88\t14.50839596754951\t71\n5877901287227392\tShowers\ts\tWSW\t2017-11-06T08:32:03.840220Z\t2017-11-09\t4.964\t7.956\t7.35\t4.937034687708582\t256.9335555372414\t1021.25\t86\t8.689876123439115\t73\n5308185955008512\tShowers\ts\tWSW\t2017-11-06T08:32:06.374360Z\t2017-11-10\t6.06\t8.738\t8.805\t9.258654904751452\t251.25388620941533\t1016.915\t83\t16.007764654418196\t73\n5607319689756672\tLight Rain\tlr\tW\t2017-11-06T08:32:09.643640Z\t2017-11-11\t5.99\t9.232\t10.64\t11.03448729420186\t259.818149683424\t1012.39\t81\t\t75\n'
