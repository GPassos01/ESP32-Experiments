import network
import time
import socket
import machine

ssid = "Racho Floresta" #nome da rede
senha = "jujumax1969" #senha da rede

def configurar_wifi(ssid, senha):
    # Criar objeto para gerenciar a interface Wi-Fi
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True) # Ativa o Wi-Fi no modo estação (STA)

    if not sta_if.isconnected():  # Verifica se já está conectado
        # Reinicia a conexão Wi-Fi antes de conectar
        sta_if.disconnect()
        time.sleep(1)
        
        print(f"Conectando-se a {ssid}...")
        sta_if.connect(ssid, senha)  # Tenta conectar à rede
        
        # Espera a conexão ser estabelecida
        tempo_espera = 10  # Tempo limite (10 segundos)
        while not sta_if.isconnected() and tempo_espera > 0:
            time.sleep(1)
            tempo_espera -= 1
            print("Aguardando conexão...")
        
    #Exibe o status da conexão
    if sta_if.isconnected():
        print("Conectado com sucesso!")
        print("Configurações de rede:", sta_if.ifconfig())  # Exibe IP, gateway, mascara de sub-rede e DNS.
        led = machine.Pin(2, machine.Pin.OUT)
        led.on() #liga o led para sinalizar conexão
    else:
        print("Falha ao conectar. Verifique SSID e senha.")
configurar_wifi(ssid, senha)
