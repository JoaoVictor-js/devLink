import socket
import os

def send_messages():
    """Solicita ao usuário que digite uma mensagem e a retorna."""
    print("Digite 'END' em uma nova linha para enviar a mensagem.")
    mensagens = []
    while True:
        linha = input("Você (Cliente): ")
        if linha == "END":
            break
        mensagens.append(linha)
    return "\n".join(mensagens)

def get_messages(mensagem):
    """Exibe a mensagem recebida do servidor."""
    print("Servidor:\n", mensagem)

def iniciar_cliente(porta):
    """Inicia o cliente e se conecta ao servidor."""
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(('127.0.0.1', porta))  # Conecta ao servidor local na porta especificada

    print("Conectado ao servidor. Digite 'exit devlink;' para encerrar a conexão.")

    while True:
        try:
            mensagem = send_messages()  # Obtém a mensagem do cliente
            cliente_socket.send(mensagem.encode())  # Envia a mensagem ao servidor
            
            if mensagem.lower() == "exit devlink;":
                print("Cliente encerrando a conexão.")
                break

            resposta = cliente_socket.recv(4096).decode()  # Recebe a resposta do servidor
            get_messages(resposta)  # Exibe a mensagem recebida
        except Exception as e:
            print("Erro:", e)
            break

    cliente_socket.close()

if __name__ == "__main__":
    os.system("clear")  # Limpa a tela ao iniciar
    print("Bem-vindo à DevLink!")  # Mensagem de boas-vindas
    porta = int(input("Qual porta entrar?: "))  # Solicita a porta do servidor
    iniciar_cliente(porta)  # Inicia o cliente
