"""
Тесты проверяют базовые функции API:

- Регистрация нового пользователя.
- Авторизацию данного пользователя сделайте сами!
"""

import pytest
import requests
from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT,  LOGIN_ENDPOINT
from custom_requester.custom_requester import CustomRequester
from api.api_manager import ApiManager

class TestAuthAPI:
    # def test_register_user(self, api_manager: ApiManager, test_user):
    #     """
    #     Тест на регистрацию пользователя.
    #     """
    #     response = api_manager.auth_api.register_user(test_user)
    #     response_data = response.json()
    #
    #     # Проверки
    #     assert response_data["email"] == test_user["email"], "Email не совпадает"
    #     assert "id" in response_data, "ID пользователя отсутствует в ответе"
    #     assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
    #     assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"

    def test_register_and_login_user(self, api_manager: ApiManager, registered_user):
        """
        Тест на регистрацию и авторизацию пользователя.
        """
        login_data = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }
        response = api_manager.auth_api.login_user(login_data)
        response_data = response.json()

        # Проверки
        assert "accessToken" in response_data, "Токен доступа отсутствует в ответе"
        assert response_data["user"]["email"] == registered_user["email"], "Email не совпадает"

    def test_authorization_user_negativ_password(self, test_user):
        # URL для авторизации
        login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"

        test_user["password"] = 'abc123de'

        # Отправка запроса на авторизацию
        response = requests.post(login_url, json=test_user, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 401, "Пользователь не должен авторизоваться"

        response_data = response.json()
        assert response_data["message"] == "Неверный логин или пароль", "Неверный message"
        assert response_data["error"] == "Unauthorized", "Неверный error"


    def test_authorization_user_negativ_email(self, test_user):
        # URL для авторизации
        login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"

        test_user["email"] = 'abc123de@egor.ru'

        # Отправка запроса на авторизацию
        response = requests.post(login_url, json=test_user, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 401, "Пользователь не должен авторизоваться"

        response_data = response.json()
        assert response_data["message"] == "Неверный логин или пароль", "Неверный message"
        assert response_data["error"] == "Unauthorized", "Неверный error"


    def test_authorization_user_negativ_empty_body(self):
        # URL для авторизации
        login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"

        test_user = {
        "email": '',
        "fullName": '',
        "password": '',
        "passwordRepeat": '',
        "roles": ["USER"]
    }

        # Отправка запроса на авторизацию
        response = requests.post(login_url, json=test_user, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 401, "Пользователь не должен авторизоваться"

        response_data = response.json()
        assert response_data["message"] == "Неверный логин или пароль", "Неверный message"
        assert response_data["error"] == "Unauthorized", "Неверный error"