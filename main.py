import requests

#Задание 3: Напишите программу, которая выводит: “Hello from <ваше_имя>”.
print("Hello from Yana")

#Задание 4: Создать скрипт, который отправляет GET-запрос по адресу: https://playground.learnqa.ru/api/get_text
response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)