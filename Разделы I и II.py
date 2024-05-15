import requests
import time

#Задание 3: Напишите программу, которая выводит: “Hello from <ваше_имя>”.
#print("Hello from Yana")

#Задание 4: Создать скрипт, который отправляет GET-запрос по адресу: https://playground.learnqa.ru/api/get_text
#response = requests.get("https://playground.learnqa.ru/api/get_text")
#print(response.text)

#Задание 6: Необходимо узнать, сколько редиректов происходит от изначальной точки назначения до итоговой. И какой URL итоговый
#response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
#response1 = response.history[0]
#response2 = response.history[1]
#response3 = response

#print(response1.url)
#print(response2.url)
#print(response3.url)

#Задание 7: Надо написать скрипт, который делает следующее:
#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
#response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
#print((f"1. method GET with no parameter has following response: {response.text}"))
#Wrong method provided

#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
#response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"HEAD"})
#print((f"2. method HEAD has following response: {response.text}"))
#пусто

#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
#response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
#print((f"3. method GET with parameter GET has following response: {response.text}"))
#{"success":"!"}

#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

#parameters_methods_list = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]

#for param in parameters_methods_list:
        #response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        #print(f"4. method GET with parameter params={param} has following response: {response.text}")
        #response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        #print(f"4. method GET with parameter data={param} has following response: {response.text}")
        #response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        #print(f"4. method POST with parameter params={param} has following response: {response.text}")
        #response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        #print(f"4. method POST with parameter data={param} has following response: {response.text}")
        #response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        #print(f"4. method PUT with parameter params={param} has following response: {response.text}")
        #response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        #print(f"4. method PUT with parameter data={param} has following response: {response.text}")
        #response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        #print(f"4. method DELETE with parameter params={param} has following response: {response.text}")
        #response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        #print(f"4. method DELETE with parameter data={param} has following response: {response.text}")
#method DELETE with parameter params={'method': 'GET'} has following response: {"success":"!"}
#method DELETE with parameter data={'method': 'GET'} has following response: {"success":"!"}
#method POST with parameter params={'method': 'POST'} has following response: {"success":"!"}
#method PUT with parameter params={'method': 'PUT'} has following response: {"success":"!"}
#method DELETE with parameter params={'method': 'DELETE'} has following response: {"success":"!"}

#Задание 8:  написать скрипт, который делал бы следующее:
#1) создавал задачу
#2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
#3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
#4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
parsed_response_text = response.json()
token = parsed_response_text["token"]
seconds = parsed_response_text["seconds"]

payload={"token": token}

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
parsed_response_text1 = response.json()
status1 = parsed_response_text1["status"]

if status1 == "Job is NOT ready":
    time.sleep(seconds)
    response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
    parsed_response_text2 = response.json()
    status2 = parsed_response_text2["status"]
    result = parsed_response_text2["result"]
    if status2 == "Job is ready" and result is not None:
        print("Good job!")
    else:
        print("Try again")
else:
    print("Try again");

#Задание 9:  написать скрипт, который должен:
#1. Брать очередной пароль и вместе с логином коллеги вызывать первый метод get_secret_password_homework. В ответ метод будет возвращать авторизационную cookie с именем auth_cookie и каким-то значением.
#2. Далее эту cookie мы должна передать во второй метод check_auth_cookie. Если в ответ вернулась фраза "You are NOT authorized", значит пароль неправильный. В этом случае берем следующий пароль и все заново. Если же вернулась другая фраза - нужно, чтобы программа вывела верный пароль и эту фразу.
payload = [{"login": "super_admin", "password": "password"}, {"login": "super_admin", "password": "123456"},
           {"login": "super_admin", "password": "12345678"}, {"login": "super_admin", "password": "qwerty"},
           {"login": "super_admin", "password": "abc123"}, {"login": "super_admin", "password": "monkey"},
           {"login": "super_admin", "password": "1234567"}, {"login": "super_admin", "password": "letmein"},
           {"login": "super_admin", "password": "trustno1"}, {"login": "super_admin", "password": "dragon"},
           {"login": "super_admin", "password": "baseball"}, {"login": "super_admin", "password": "111111"},
           {"login": "super_admin", "password": "iloveyou"}, {"login": "super_admin", "password": "master"},
           {"login": "super_admin", "password": "sunshine"}, {"login": "super_admin", "password": "ashley"},
           {"login": "super_admin", "password": "bailey"}, {"login": "super_admin", "password": "passw0rd"},
           {"login": "super_admin", "password": "shadow"}, {"login": "super_admin", "password": "123123"},
           {"login": "super_admin", "password": "654321"}, {"login": "super_admin", "password": "superman"},
           {"login": "super_admin", "password": "qazwsx"}, {"login": "super_admin", "password": "michael"},
           {"login": "super_admin", "password": "Football"}, {"login": "super_admin", "password": "welcome"},
           {"login": "super_admin", "password": "jesus"}, {"login": "super_admin", "password": "ninja"},
           {"login": "super_admin", "password": "mustang"}, {"login": "super_admin", "password": "password1"},
           {"login": "super_admin", "password": "123456789"}, {"login": "super_admin", "password": "adobe123[a]"},
           {"login": "super_admin", "password": "admin"}, {"login": "super_admin", "password": "1234567890"},
           {"login": "super_admin", "password": "photoshop[a]"}, {"login": "super_admin", "password": "1234"},
           {"login": "super_admin", "password": "12345"}, {"login": "super_admin", "password": "princess"},
           {"login": "super_admin", "password": "azerty"}, {"login": "super_admin", "password": "000000"},
           {"login": "super_admin", "password": "access"}, {"login": "super_admin", "password": "696969"},
           {"login": "super_admin", "password": "batman"}, {"login": "super_admin", "password": "1qaz2wsx"},
           {"login": "super_admin", "password": "login"}, {"login": "super_admin", "password": "qwertyuiop"},
           {"login": "super_admin", "password": "solo"}, {"login": "super_admin", "password": "starwars"},
           {"login": "super_admin", "password": "121212"}, {"login": "super_admin", "password": "flower"},
           {"login": "super_admin", "password": "hottie"}, {"login": "super_admin", "password": "loveme"},
           {"login": "super_admin", "password": "zaq1zaq1"}, {"login": "super_admin", "password": "hello"},
           {"login": "super_admin", "password": "freedom"}, {"login": "super_admin", "password": "whatever"},
           {"login": "super_admin", "password": "666666"}, {"login": "super_admin", "password": "!@#$%^&*"},
           {"login": "super_admin", "password": "charlie"}, {"login": "super_admin", "password": "aa123456"},
           {"login": "super_admin", "password": "donald"}, {"login": "super_admin", "password": "qwerty123"},
           {"login": "super_admin", "password": "1q2w3e4r"}, {"login": "super_admin", "password": "555555"},
           {"login": "super_admin", "password": "lovely"}, {"login": "super_admin", "password": "7777777"},
           {"login": "super_admin", "password": "888888"}, {"login": "super_admin", "password": "123qwe"}]

for i in range(len(payload)):

    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload[i])

    cookie_value = response.cookies.get('auth_cookie')

    cookies = {}
    if cookie_value is not None:
        cookies.update({'auth_cookie':cookie_value})

    response1 = requests.post(" https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)

    if response1.text != 'You are NOT authorized':
        print("Correct password:", payload[i].get("password"), ";", "Response:", response1.text)
        break
    else:
        continue