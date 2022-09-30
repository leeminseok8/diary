import requests

import json

from diary.config import API_KEY


class WhetherView:
    def now_whether(self):
        """
        외부 API를 사용하여 현재 도시(서울)의 날씨 호출
        """

        apikey = API_KEY
        api = f"http://api.weatherapi.com/v1/current.json?key={apikey}&q=Seoul&aqi=no"

        res = requests.get(api)
        data = json.loads(res.text)

        return data["current"]["condition"]["text"]
