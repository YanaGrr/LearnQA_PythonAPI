import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import json


class TestUserDelete(BaseCase):
    def test_delete_user2(self):
        # LOGIN
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id = self.get_json_value(response1, "user_id")

        # DELETE
        response2 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_code_status(response2, 400)
        respJson = json.loads(response2.content)
        resperr = respJson["error"]
        assert resperr == f"Please, do not delete test users with ID 1, 2, 3, 4 or 5.", f"Unexpected response content {response2.content}"

    def test_delete_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        self.user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        self.auth_sid = self.get_cookie(response2, "auth_sid")
        self.token = self.get_header(response2, "x-csrf-token")

        # DELETE
        response3 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_code_status(response3, 200)
        respJson = json.loads(response3.content)
        resperr = respJson["success"]
        assert resperr == f"!", f"Unexpected response content {response3.content}"

        # GET
        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_code_status(response4, 404)
        assert response4.content.decode(
            "utf-8") == f"User not found", f"Unexpected response content {response4.content}"

    def test_delete_other_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        self.user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        self.auth_sid = self.get_cookie(response2, "auth_sid")
        self.token = self.get_header(response2, "x-csrf-token")

        # DELETE
        response3 = requests.delete(
            f"https://playground.learnqa.ru/api/user/97560",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_code_status(response3, 400)
        respJson = json.loads(response3.content)
        resperr = respJson["error"]
        assert resperr == f"This user can only delete their own account.", f"Unexpected response content {response3.content}"
