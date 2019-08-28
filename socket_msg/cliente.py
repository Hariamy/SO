# -*- coding: utf-8 -*-

import socket as sk
import threading as th
import os

os.system('cls' if os.name == 'nt' else 'clear')

def recv_server_msg(sock):
	stop = False
	while not stop:
		mensagem = sock.recv(1024).decode()
		if mensagem == "exit":
			sock.send("".encode())
			sock.close()
			stop = True
		elif mensagem == "exit2":
			sock.close()

			TCP = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
			TCP.connect((ip, porta))
			TCP.send("exit".encode())
			TCP.close()

			stop = True
		elif mensagem.split()[1] != "exit":
			print(mensagem, "\n  > ", end="")

ip	  = '127.0.0.1'
porta = 12345

print(" ╔═════════════════════════════╗")
print(" ║           CLIENTE           ║")
print(" ╚═════════════════════════════╝")

try:
	TCP = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
	TCP.connect((ip, porta))

	t = th.Thread(target=recv_server_msg, args=(TCP,))
	t.start()

	print("\n  > Digite seu nome: ", end="")
	mensagem = input("")

	while mensagem == "exit" or not mensagem:
		print("  > NOME INVÁLIDO!")
		print("  > Digite seu nome: ", end="")
		mensagem = input("")

	print("\n ╔═════════════════════════════╗")
	print(" ║     ENVIE SUA MENSAGEM      ║")
	print(" ║   Para sair digite: exit    ║")
	print(" ╚═════════════════════════════╝")

	while mensagem != "exit":
		TCP.send(mensagem.encode())
		mensagem = input("  > ")


	TCP.send(mensagem.encode())
except ConnectionRefusedError:
	print("\n  > Servidor fora do ar!")


