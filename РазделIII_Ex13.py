#Ex13: User Agent
import pytest
import requests
import json

class TestUserAgent:
    user_agents = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]

    @pytest.mark.parametrize('user_agent', user_agents)

    def test_user_agent(self, user_agent):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        data = {"User-Agent": user_agent}

        resp = requests.get(url, headers=data).text
        response = json.loads(resp)

        platform = response["platform"]
        browser = response["browser"]
        device = response["device"]

        if user_agent == "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30":
            assert platform == "Mobile", "Platform is wrong"
            assert browser == "No", "Browser is wrong"
            assert device == "Android", "Device is wrong"
        if user_agent == "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1":
            assert platform == "Mobile", "Platform is wrong"
            assert browser == "Chrome", "Browser is wrong"
            assert device == "iOS", "Device is wrong"
        if user_agent == "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)":
            assert platform == "Googlebot", "Platform is wrong"
            assert browser == "Unknown", "Browser is wrong"
            assert device == "Unknown", "Device is wrong"
        if user_agent == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0":
            assert platform == "Web", "Platform is wrong"
            assert browser == "Chrome", "Browser is wrong"
            assert device == "No", "Device is wrong"
        if user_agent == "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1":
            assert platform == "Mobile", "Platform is wrong"
            assert browser == "No", "Browser is wrong"
            assert device == "iPhone", "Device is wrong"
