#Ex12: Тест запроса на метод header

import requests

class Test_Headers:
    def test_headers_cont(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        headers_content = response.headers
        print(headers_content)

        key1 = "Date"
        key2 = "Content-Type"
        key3 = "Content-Length"
        key4 = "Connection"
        key5 = "Keep-Alive"
        key6 = "Server"
        key7 = "x-secret-homework-header"
        key8 = "Cache-Control"
        key9 = "Expires"

        #value1 = "Tue, 21 May 2024 19:12:39 GMT"
        value2 = "application/json"
        value3 = "15"
        value4 = "keep-alive"
        value5 = "timeout=10"
        value6 = "Apache"
        value7 = "Some secret value"
        value8 = "max-age=0"
        #value9 = "Tue, 21 May 2024 19:12:39 GMT"

        assert len(headers_content) == 9, "Count of headers are not equal 9"

        assert key1 in headers_content, "There is no header's key1 in the response"
        assert key2 in headers_content, "There is no header's key2 in the response"
        assert key3 in headers_content, "There is no header's key3 in the response"
        assert key4 in headers_content, "There is no header's key4 in the response"
        assert key5 in headers_content, "There is no header's key5 in the response"
        assert key6 in headers_content, "There is no header's key6 in the response"
        assert key7 in headers_content, "There is no header's key7 in the response"
        assert key8 in headers_content, "There is no header's key8 in the response"
        assert key9 in headers_content, "There is no header's key9 in the response"
        #assert value1 == headers_content.get("Date"), "There is no header's value1 in the response"
        assert value2 == headers_content.get("Content-Type"), "There is no header's value2 in the response"
        assert value3 == headers_content.get("Content-Length"), "There is no header's value3 in the response"
        assert value4 == headers_content.get("Connection"), "There is no header's value4 in the response"
        assert value5 == headers_content.get("Keep-Alive"), "There is no header's value5 in the response"
        assert value6 == headers_content.get("Server"), "There is no header's value6 in the response"
        assert value7 == headers_content.get("x-secret-homework-header"), "There is no header's value7 in the response"
        assert value8 == headers_content.get("Cache-Control"), "There is no header's value8 in the response"
        #assert value9 == headers_content.get("Expires"), "There is no header's value9 in the response"
