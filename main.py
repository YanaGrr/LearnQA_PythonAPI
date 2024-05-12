import requests

#Задание 3: Напишите программу, которая выводит: “Hello from <ваше_имя>”.
#print("Hello from Yana")

#Задание 4: Создать скрипт, который отправляет GET-запрос по адресу: https://playground.learnqa.ru/api/get_text
#response = requests.get("https://playground.learnqa.ru/api/get_text")
#print(response.text)

#Задание 6: Длинный редирект:  необходимо узнать, сколько редиректов происходит от изначальной точки назначения до итоговой. И какой URL итоговый
response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
response1 = response.history[0]
response2 = response.history[1]
response3 = response

print(response1.url)
print(response2.url)
print(response3.url)