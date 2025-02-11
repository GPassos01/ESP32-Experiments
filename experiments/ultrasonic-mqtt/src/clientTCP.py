import socket
from ultrasonic import medir_distancia
import time

def sta_conection(): #conexão via portas (TCP)
    HOST = "192.168.0.138"  # Standard loopback interface address (localhost)
    PORT = 80  # Port to listen on (non-privileged ports are > 1023)

    s = None  # Inicializa a variável do socket

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        mensagem = "Ola do ESP32!" #mensagem a ser enviada
        s.sendall(mensagem.encode()) #envia a mensagem
        print("Mensagem enviada!")
        while True:
            #le os dados do sensor
            dado_sensor = medir_distancia()
            
            mensagem = f"Leitura do sensor: {dado_sensor} cm"
            s.sendall(mensagem.encode()) #envia os dados do sensor como string
            print("Dados enviados!")
            
            #verifica se a conexao existe ainda
            data = s.recv(1024)
            if not data: #se n houver dados n ha conexao
                print("Conexão com servidor foi fechada.")
                break #encerra loop
            
            time.sleep(5) #espera 5 segunndos para ler

    except Exception as e:
        print(f"Erro na comunicação: {e}")

    finally:
        if s:  # Garante que o socket só será fechado se tiver sido criado
            s.close()
            print("Socket fechado")