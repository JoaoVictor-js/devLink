import socket
import os

def send_messages():
    """Solicita ao usuário que digite uma mensagem e a retorna."""
    print("Digite 'END' em uma nova linha para enviar a mensagem.")
    mensagens = []
    while True:
        linha = input("Você (Servidor): ")
        if linha == "END":
            break
        mensagens.append(linha)
    return "\n".join(mensagens)

def get_messages(mensagem):
    """Exibe a mensagem recebida do cliente."""
    print("Cliente:\n", mensagem)

def iniciar_servidor(porta):
    """Inicia o servidor e aguarda a conexão do cliente."""
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(('0.0.0.0', porta))  # Escuta em todas as interfaces na porta especificada
    servidor_socket.listen(1)

    print("Servidor iniciado. Aguardando conexão...")
    conexao, endereco = servidor_socket.accept()
    print(f"Conectado por {endereco}")

    while True:
        try:
            mensagem = conexao.recv(4096).decode()  # Recebe a mensagem do cliente
            if not mensagem:
                print("Conexão encerrada pelo cliente.")
                break
            get_messages(mensagem)  # Exibe a mensagem recebida

            resposta = send_messages()  # Obtém a resposta do servidor
            conexao.send(resposta.encode())  # Envia a resposta ao cliente
            if resposta.lower() == "exit devlink;":
                print("Servidor encerrando a conexão.")
                break
        except Exception as e:
            print("Erro:", e)
            break

    conexao.close()
    servidor_socket.close()

if __name__ == "__main__":
    os.system("clear")  # Limpa a tela ao iniciar
    porta = int(input("Escreva uma porta para ser usada: "))  # Solicita a porta do servidor
    iniciar_servidor(porta)  # Inicia o servidor
