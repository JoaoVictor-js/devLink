# DevLink

DevLink é um aplicativo de chat em tempo real que permite que usuários se comuniquem facilmente através de mensagens de texto. O aplicativo foi desenvolvido em Python e utiliza sockets para estabelecer a comunicação entre um cliente e um servidor.

## Funcionalidades

- **Comunicação em tempo real**: Troca instantânea de mensagens entre o cliente e o servidor.
- **Envio de mensagens multilinha**: Permite que o usuário envie mensagens compostas por várias linhas, ideal para compartilhar códigos e outros textos longos.
- **Saída limpa**: As mensagens recebidas são exibidas de forma clara e organizada.

## Estrutura do Projeto

O projeto consiste em dois arquivos principais:

- `server.py`: Código do servidor que aceita conexões de clientes e processa mensagens recebidas.
- `client.py`: Código do cliente que se conecta ao servidor e permite ao usuário enviar mensagens.

## Como Usar

1. **Instalação**:
   - Certifique-se de ter o Python instalado em seu sistema. Você pode baixar a versão mais recente em [python.org](https://www.python.org/downloads/).

2. **Executando o Servidor**:
   - Abra um terminal e navegue até o diretório do projeto.
   - Execute o servidor com o comando:
     ```bash
     python server.py
     ```
   - Escolha uma porta quando solicitado.

3. **Executando o Cliente**:
   - Em outro terminal, navegue até o mesmo diretório do projeto.
   - Execute o cliente com o comando:
     ```bash
     python client.py
     ```
   - Insira a mesma porta que você usou para o servidor.

4. **Enviando Mensagens**:
   - No cliente, digite mensagens e pressione Enter para enviar. Para enviar mensagens multilinha, digite `END` em uma nova linha para finalizar o envio.

5. **Encerrando a Conexão**:
   - Para encerrar a conexão, digite `exit devlink;` no cliente.

## Exemplo de Uso

```bash
# No terminal do servidor
python server.py
# No terminal do cliente
python client.py
