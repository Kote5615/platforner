import socket #импортируем сокет
import pickle
soc = socket.socket() #запустить сокет

soc.connect(("192.168.71.248", 5000)) #порт и айпи

name = input("введите имя: ")

while True:#бесконечный цикл
    txt = input("введите текст: ")
    txt = name + ": " + txt
    soc.send(txt.encode()) #отправка текста, перевод его в байты (сначала байты потои отправка)
    answer = soc.recv(6400000)

    obj = pickle.loads(answer)#байты переводим в текст
    for massage in obj:
        print(massage.decode("utf - 8"))