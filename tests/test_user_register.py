import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure


@allure.epic("Registration cases")
class TestUserRegister(BaseCase):
    @allure.description("This test successfully registers user")
    @allure.story("Positive test")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("This test checks, that registration with existing email is forbidden")
    @allure.story("Negative test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    # Создание пользователя с некорректным email - без символа @
    @allure.description("This test checks, that registration with wrong email is forbidden")
    @allure.story("Negative test")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_without_simbol(self):
        email = 'vinkotovexample.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Invalid email format", f"Unexpected response content {response.content}"

    # Создание пользователя без указания одного из полей - с помощью @parametrize необходимо проверить, что отсутствие любого параметра не дает зарегистрировать пользователя
    @pytest.mark.parametrize(
        "key, value",
        [
            (
                    "password", {
                        'username': 'learnqa',
                        'firstName': 'learnqa',
                        'lastName': 'learnqa',
                        'email': 'vinkotov@example.com'
                    }
            ),
            (
                    "username", {
                        'password': '123',
                        'firstName': 'learnqa',
                        'lastName': 'learnqa',
                        'email': 'vinkotov@example.com'
                    }
            ),
            (
                    "firstName", {
                        'password': '123',
                        'username': 'learnqa',
                        'lastName': 'learnqa',
                        'email': 'vinkotov@example.com'
                    }
            ),
            (
                    "lastName", {
                        'password': '123',
                        'username': 'learnqa',
                        'firstName': 'learnqa',
                        'email': 'vinkotov@example.com'
                    }
            ),
            (
                    "email", {
                        'password': '123',
                        'username': 'learnqa',
                        'firstName': 'learnqa',
                        'lastName': 'learnqa'
                    }
            )
        ]
    )
    @allure.description("This test checks, that registration without data is forbidden")
    @allure.story("Negative test")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_user_without_data(self, key, value):
        response = MyRequests.post("/user/", data=value)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The following required params are missed: {key}", f"Unexpected response content {response.content}"

    # Создание пользователя с очень коротким именем в один символ
    @allure.description("This test checks, that registration with short username is forbidden")
    @allure.story("Negative test")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_without_simbol(self):
        username = '1'
        data = {
            'password': '123',
            'username': username,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'vinkotovexample.com'
        }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too short", f"Unexpected response content {response.content}"

    # Создание пользователя с очень длинным именем - длиннее 250 символов
    @allure.description("This test checks, that registration with long username is forbidden")
    @allure.story("Negative test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_without_simbol(self):
        username = 'learnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqalearnqa'
        data = {
            'password': '123',
            'username': username,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'vinkotovexample.com'
        }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too long", f"Unexpected response content {response.content}"
