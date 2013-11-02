#! /usr/bin/python
#Written By Tom Paulus, @tompaulus, www.tompaulus.com

import requests


class WebAPI:
    def __init__(self):
        return

    def getLocation(self, state, city, token):
        """
        get data for the location
        :return: JSON object
        """
        d = requests.get(
            'http://api.wunderground.com/api/' + str(token) + '/forecast/q/' + str(state) + '/' + str(city) + '.json')
        json = d.json()
        return json

    def high(self, json, units):
        """
        extract the High temperature from the JSON Package
        :return: String
        """
        high = str(json['forecast']['simpleforecast']['forecastday'][0]['high'][units])
        return high

    def low(self, json, units):
        """
        extract the Low temperature from the JSON Package
        :return: String
        """
        low = str(json['forecast']['simpleforecast']['forecastday'][0]['low'][units])
        return low

    def windSpeed(self, json, units):
        """
        extract the Wind Speed from the JSON Package
        :return: String
        """
        windSpeed = str(json['forecast']['simpleforecast']['forecastday'][0]['avewind'][units])
        return windSpeed

    def winDir(self, json):
        """
        extract the Wind Direction from the JSON Package
        :return: String
        """
        windDir = str(json['forecast']['simpleforecast']['forecastday'][0]['avewind']['dir'])
        return windDir

    def conditions(self, json):
        """
        extract the Weather Conditions from the JSON Package
        ex. 'Partly Cloudy with a Chance of Meatballs'
        :return: String
        """
        conditions = str(json['forecast']['simpleforecast']['forecastday'][0]['conditions'])
        return conditions

    def rain(self, json):
        """
        extract the chance of rain from the JSON Package
        :return: String
        """
        rain = str(json['forecast']['txt_forecast']['forecastday'][0]['pop'])
        return rain

    def humidity(self, json):
        """
        extract the Humidity from the JSON Package
        :return: String
        """
        humidity = str(json['forecast']['simpleforecast']['forecastday'][0]['avehumidity'])
        return humidity

    def Display1(self, high, low, windSpeed, units_Speed, windDir, lang):
        """
        Concatenate the data for the first display. It contains the High/Low temperature,
        and the wind speed and direction
        :return: String
        """
        if lang == 'eng':
            string = 'Temp H:' + high + ' L:' + low + '\nWind ' + windSpeed + units_Speed + ' ' + windDir
            return string
        else:
            return 0
            #       Not Yet Supported

    def Display2(self, rain, humidity, lang):
        """
        Concatenate the data for the second display. It contains the chance of rain and the relative humidity.
        :return: String
        """
        if lang == 'eng':
            string = rain + '% Rain\n' + humidity + '% Humidity'
            return string
        else:
            return 0
            #        Not Yet Supported

    def Display3(self, text):
    #        Work in Progress!!
        return text

    def USCode(self, short):
        """
        Convert the State short code to the Full name for display purposes.
        :return: String
        """
        states = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
        }
        return states.get(short)

