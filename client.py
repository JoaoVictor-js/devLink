import socket
import os

def send_messages():
    """Solicita ao usuário que digite uma mensagem e a retorna."""
    return input("Você (Cliente): ")

def get_messages(mensagem):
    """Exibe a mensagem recebida do servidor."""
    print("Servidor:", mensagem)

def iniciar_cliente(porta):
    """Inicia o cliente e se conecta ao servidor."""
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(('127.0.0.1', porta))  # Conecta ao servidor local na porta 12345

    print("Conectado ao servidor. Digite 'exit devlink;' para encerrar a conexão.")

    while True:
        try:
            mensagem = send_messages()  # Obtém a mensagem do cliente
            cliente_socket.send(mensagem.encode())  # Envia a mensagem ao servidor
            
            if mensagem.lower() == "exit devlink;":
                print("Cliente encerrando a conexão.")
                break
            
            resposta = cliente_socket.recv(1024).decode()  # Recebe a resposta do servidor
            get_messages(resposta)  # Exibe a mensagem recebida
        except Exception as e:
            print("Erro:", e)
            break

    cliente_socket.close()

if __name__ == "__main__":
    os.system("clear")
    print("bem vindo à devLink!")
    portaaserescrita = int(input("qual porta entrar?:"))# Limpa a tela ao iniciar
    iniciar_cliente(portaaserescrita)
