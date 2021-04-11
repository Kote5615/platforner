import socket #импортируем сокет
import threading #просто надо
import pickle #перевод в байты массив
soc = socket.socket() #запустить сокет

history = []#массив


soc.bind(("192.168.71.248", 5000)) #порт и айпи

soc.listen(1) #очередь

#для общения с другими
def chat(con,ip):
    while True:#бесконечный цикл
        data = con.recv(5000) #длина сообщения в байтах(прием сообщения)
        if not data: #выход
            break
        history.append(data)
        con.send(data)  #отправка сообщения
        con.send(pickle.dumps(history))#история
    con.close()  #закрыть сервер

while True:
    con, ip = soc.accept()  #ожидание очереди
    threading.Thread(target=chat, args=(con,ip)).start() #отдельнная программа