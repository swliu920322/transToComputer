from utils.Request import RequestClient
import os

dict_image = {
    'male': {
        'clear': 'male_clear.png',
        'rain': 'male_rain.png',
        'snow': 'male_snow.png',
        'cloudy': 'male_cloudy.png'
    },
    'female': {
        'clear': 'female_clear.png',
        'rain': 'female_rain.png',
        'snow': 'female_snow.png',
        'cloudy': 'female_cloudy.png'
    }
}

country_list = ['singapore', 'malaysia']
gender_list = ['male', 'female']


def get_weather_by_country(country):
    client = RequestClient.get_instance()
    return client.get_weather(country)

def checkFileExists(filePath):
    return os.path.exists(filePath)

def get_weather_by_response(main):
    main = main.lower()
    if main == 'clear':
        return 'clear'
    elif main == 'snow':
        return 'snow'
    elif main == 'rain' or main == 'thunderstorm' or main == 'drizzle':
        return 'rain'
    else:
        return 'cloudy'


def test_get_weather_by_response():
    # Test case 1: Testing exact matches for main weather types
    assert get_weather_by_response('Clear') == 'clear', "Should return 'clear' for 'Clear'"
    assert get_weather_by_response('Snow') == 'snow', "Should return 'snow' for 'Snow'"
    assert get_weather_by_response('Rain') == 'rain', "Should return 'rain' for 'Rain'"
    assert get_weather_by_response('Thunderstorm') == 'rain', "Should return 'rain' for 'Thunderstorm'"
    assert get_weather_by_response('Drizzle') == 'rain', "Should return 'rain' for 'Drizzle'"
    
    # Test case 2: Testing default cloudy response for other conditions
    assert get_weather_by_response('Clouds') == 'cloudy', "Should return 'cloudy' for 'Clouds'"
    assert get_weather_by_response('Mist') == 'cloudy', "Should return 'cloudy' for 'Mist'"
    assert get_weather_by_response('Fog') == 'cloudy', "Should return 'cloudy' for 'Fog'"
    
    print("All test cases passed!")


if __name__ == '__main__':
    test_get_weather_by_response()
