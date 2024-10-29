import os

def sendmessages():
    return input("Você:")

def getmessages(mensagem):
    print("other:",mensagem)


def main():
    os.system("clear")
    print("Hello, World!")
    print("bem vindo à DevLink\n")
    while True:
        mens=sendmessages()
        if mens.lower() == "exit devlink;":
            print("goodbye!")
            quit()
        getmessages(mens)





if __name__ == "__main__":
    main()

