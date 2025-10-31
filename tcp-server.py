from socket import *
serverPort = 12001

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server hazır.")


while True:
	connectionSocket, addr = serverSocket.accept()
	counter = 0
	while True :
		message = connectionSocket.recv(1024).decode()
		print("Kullanıcıdan gelen mesaj: ", message)
		if message == "Merhaba\n":
			counter += 1
			if counter <5 :
				responce = "Sana da merhaba\n"
				print("Sunucudan cevap: ", responce)
				connectionSocket.send(responce.encode())
			else:
				responce = "Derdin ne senin."
				print("Sunucudan cevap: ", responce)
				connectionSocket.send(responce.encode())
				number = connectionSocket.recv(1024).decode()
				print(f"Öğrenci numarası: {number} ")
				connectionSocket.send("Kaydedildi, görüsürüz".encode())
				break
connectionSocket.close()
print("Bağlantı sonlandı")
			
