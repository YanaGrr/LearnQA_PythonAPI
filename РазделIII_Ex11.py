#Ex11: Тест запроса на метод cookie

import requests

class Test_Cookie:
    def test_cookie_cont(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie_content = dict(response.cookies)
        print(cookie_content)
        key = "HomeWork"
        value = "hw_value"
        assert key in cookie_content, "There is no cookie's key in the response"
        assert value == cookie_content.get("HomeWork"), "There is no cookie's value in the response"
