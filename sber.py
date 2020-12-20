import socket 
sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
sock.bind (('',5050))
client = ['Start Server']
while 1 :
         data , addres = sock.recvfrom(1024)
         print (addres[0], addres[1])
         if  addres not in client : 
                 client.append(addres)# Если такого клиента нет, то добавить
         for clients in client :
                 if clients == addres : 
                     continue # Не отправлять данные клиенту обратно
data , addres = sock.recvfrom(1024)  # Адреса клиентов
sock.sendto(data,addres)


import threading
def read_sok(): 
     data = sor.recv(1024)
  
     print(data.decode('utf-8'))
     server= '', 5050  # Данные сервера
     alias = input() # Вводим наш псевдоним
     sor = socket.socket(socet.AF_INET,socket.SOCK_DGRAM)
     sor.bind(('', 0)) # Задаем сокет как клиента
     sor.sendto((alias+' Connect to server').encode('utf-8'), server)# Уведомляем сервер о подключении
     potok = threading.Thread(target= read_sok)
     potok.start()
while 1 :
     mensahe = input()
sor.sendto(('['+alias+']'+mensahe).encode('utf-8'), server)


    
key=519
crypt = ''
for i in  message  :
    crypt += chr(ord(i)^key)
message  = crypt
