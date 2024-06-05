from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure


@allure.epic("Get user's data cases")
class TestUserGet(BaseCase):
    # неавторизованный запрос на данные - получаем только username
    @allure.description("This test checks getting user's data w/o sending auth cookie or token is forbidden")
    @allure.story("Negative test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    # авторизованный запрос - авторизация пользователем с ID 2 и запрос для получения данных того же пользователя, получаем все поля
    @allure.description("This test successfully getting data")
    @allure.story("Positive test")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(
            f"/user/{self.user_id_from_auth_method}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

    # авторизация под одним пользователем, но получение данных другого (т.е. с другим ID)
    # в этом случае запрос также получает только username, так как не должны видеть остальные данные чужого пользователя
    @allure.description("This test checks, that getting data of another user's account is forbidden")
    @allure.story("Negative test")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_get_user_details_auth_as_other_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #GET
        response3 = MyRequests.get(
            f"/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_has_key(response3, "username")
        Assertions.assert_json_has_not_key(response3, "email")
        Assertions.assert_json_has_not_key(response3, "firstName")
        Assertions.assert_json_has_not_key(response3, "lastName")