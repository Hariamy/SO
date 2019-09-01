# -*- coding: utf-8 -*-

import socket as sk
import threading as th
import os

os.system('cls' if os.name == 'nt' else 'clear')

ip	  = 'localhost'
porta = 12345

print(" ╔══════════════════════════╗")
print(" ║         SERVIDOR         ║")
print(" ╚══════════════════════════╝")

print("  > Porta:", porta)
print("\n  > Aguardando conexão...\n")

TCP = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
TCP.bind((ip, porta))
TCP.listen(1)

conexoes = []

def conectado():
	conexao, cliente = TCP.accept()
	nome_cliente = conexao.recv(1024).decode()

	if nome_cliente != "exit":	
		print("  > Conexão estabelecida com", nome_cliente)
		conexoes.append(conexao)

		t = th.Thread(target=conectado)
		t.start()

		mensagem = ""
		while mensagem != "exit":
			mensagem = conexao.recv(1024).decode()

			resposta = "[" + nome_cliente + "]: " + mensagem
			
			if len(conexoes) == 1 and mensagem != "exit":
				print("  >", resposta)
				print("  NOTA: Conecte mais clientes para iniciar o chat!\n")

			for con in conexoes:
				if con != conexao:
					con.send(resposta.encode())

		
		print("  > Conexão finalizada com", nome_cliente)
		conexoes.remove(conexao)
		
		if len(conexoes) == 0: mensagem = "exit2"

		conexao.send(mensagem.encode())
		_ = conexao.recv(1024).decode()
		conexao.close()

	else:
		print(" ╔══════════════════════════╗")
		print(" ║   SERVIDOR FORA DO AR    ║")
		print(" ╚══════════════════════════╝")
		conexao.close()

t = th.Thread(target=conectado)
t.start()
