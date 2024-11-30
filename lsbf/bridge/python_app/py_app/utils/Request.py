import requests


class RequestClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.session = requests.Session()

            cls._instance.session.headers = {
                "x-rapidapi-key": "e3dfcbb108msh824ce8e149e41b1p143745jsn3b1b792821a4",
                "x-rapidapi-host": "open-weather13.p.rapidapi.com"
            }
            cls._instance.session.timeout = 10
        return cls._instance

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def get_weather(self, country):
        url = "https://open-weather13.p.rapidapi.com/city/" + country + '/EN'
        res = self.session.get(url)
        return res.json()['weather'][0]['main']
