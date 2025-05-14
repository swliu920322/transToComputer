import requests


class RequestClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.session = requests.Session()

            cls._instance.session.headers = {
                "x-rapidapi-key": "c6dec742e9msh00962b4203af7e9p1a2fb6jsnaf98c596d800",
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
        url = "https://open-weather13.p.rapidapi.com/city"
        querystring = {"city": country, "lang": "EN"}
        res = self.session.get(url, params=querystring)
        return res.json()['weather'][0]['main']
