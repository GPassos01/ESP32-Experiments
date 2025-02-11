import socket

HOST = "192.168.0.138"  # Standard loopback interface address (localhost)
PORT = 80  # Port to listen on (non-privileged ports are > 1023)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor ouvindo em {HOST}:{PORT}")
    
    while True:
        try:
            conn, addr = s.accept()
            print(f"Connected by {addr}")
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Mensagem recebida: {data.decode()}") #Exibe no terminal
                    conn.sendall(b"mensagem recebida")
        except Exception as e:
            print(f"Erro na conexão: {e}")
        finally:
            conn.close()
            
except KeyboardInterrupt:
    print("\nServidor encerrado pelo usuário.")

except Exception as e:
    print(f"Erro no servidor: {e}")

finally:
    s.close()
    print("Socket fechado")
