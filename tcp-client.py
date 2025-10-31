from socket import*

serverName = "localhost"
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
	sentence = "Merhaba\n"
	clientSocket.send(sentence.encode())
	print("Kullanıcıdan mesaj: ", sentence)
	responce = clientSocket.recv(1024).decode()
	print("Sunucudan cevap: ", responce)

	if responce == "Derdin ne senin.":
		number = input("öğrenci numaranız: ")
		clientSocket.send(number.encode())
		responce = clientSocket.recv(1024).decode()
		print(responce)
		break
clientSocket.close()
