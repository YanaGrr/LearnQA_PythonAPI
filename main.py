import requests

#Задание 3: Напишите программу, которая выводит: “Hello from <ваше_имя>”.
#print("Hello from Yana")

#Задание 4: Создать скрипт, который отправляет GET-запрос по адресу: https://playground.learnqa.ru/api/get_text
#response = requests.get("https://playground.learnqa.ru/api/get_text")
#print(response.text)

#Задание 6: Необходимо узнать, сколько редиректов происходит от изначальной точки назначения до итоговой. И какой URL итоговый
response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
response1 = response.history[0]
response2 = response.history[1]
response3 = response

print(response1.url)
print(response2.url)
print(response3.url)

#Задание 7: Надо написать скрипт, который делает следующее:
#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print((f"1. method GET with no parameter has following response: {response.text}"))
#Wrong method provided

#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"HEAD"})
print((f"2. method HEAD has following response: {response.text}"))
#пусто

#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print((f"3. method GET with parameter GET has following response: {response.text}"))
#{"success":"!"}

#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

parameters_methods_list = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]

for param in parameters_methods_list:
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"4. method GET with parameter params={param} has following response: {response.text}")
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"4. method GET with parameter data={param} has following response: {response.text}")
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"4. method POST with parameter params={param} has following response: {response.text}")
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"4. method POST with parameter data={param} has following response: {response.text}")
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"4. method PUT with parameter params={param} has following response: {response.text}")
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"4. method PUT with parameter data={param} has following response: {response.text}")
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"4. method DELETE with parameter params={param} has following response: {response.text}")
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"4. method DELETE with parameter data={param} has following response: {response.text}")
#method DELETE with parameter params={'method': 'GET'} has following response: {"success":"!"}
#method DELETE with parameter data={'method': 'GET'} has following response: {"success":"!"}
#method POST with parameter params={'method': 'POST'} has following response: {"success":"!"}
#method PUT with parameter params={'method': 'PUT'} has following response: {"success":"!"}
#method DELETE with parameter params={'method': 'DELETE'} has following response: {"success":"!"}
