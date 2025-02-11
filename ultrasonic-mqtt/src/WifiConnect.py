import network
import time
import machine

class WiFiManager:
    """
    Classe para gerenciar a conexão Wi-Fi no ESP32.

    A classe permite conectar e desconectar o ESP32 de uma rede Wi-Fi, além de indicar o status da conexão por um LED.

    Atributos:
        ssid (str): Nome da rede Wi-Fi.
        senha (str): Senha da rede Wi-Fi.
        sta_if (network.WLAN): Interface de rede no modo estação.
        led (machine.Pin): Pino do LED indicador de conexão.
    """

    def __init__(self, ssid, senha, led_pin=2):
        """
        Inicializa o gerenciador de Wi-Fi.
        
        led_pin (int, opcional): Pino do LED indicador de conexão. Default é 2.
        """
        self.ssid = ssid
        self.senha = senha
        self.sta_if = network.WLAN(network.STA_IF)  # Cria a interface Wi-Fi no modo estação
        self.led = machine.Pin(led_pin, machine.Pin.OUT)  # Configura o LED como saída
        self.led.off()  # Mantém o LED desligado inicialmente

    def conectar(self, tempo_espera=10):
        """
        Conecta o ESP32 à rede Wi-Fi.

        Args:
            tempo_espera (int, opcional): Tempo máximo de espera para conexão (em segundos). Default é 10.

        Returns:
            bool: Retorna True se a conexão for bem-sucedida, False caso contrário.
        """
        self.sta_if.active(True)  # Ativa o modo Wi-Fi estação

        if not self.sta_if.isconnected():
            print(f"Conectando-se à rede {self.ssid}...")
            self.sta_if.connect(self.ssid, self.senha)  # Tenta conectar à rede

            # Aguarda a conexão ser estabelecida
            while not self.sta_if.isconnected() and tempo_espera > 0:
                time.sleep(1)
                tempo_espera -= 1
                print(f"Aguardando conexão... ({tempo_espera}s restantes)")

        # Verifica se conseguiu conectar
        if self.sta_if.isconnected():
            print("✅ Conectado com sucesso!")
            print("📡 Configurações de rede:", self.sta_if.ifconfig())  # Exibe IP, gateway, máscara e DNS
            self.led.on()  # Liga o LED indicando conexão bem-sucedida
            return True
        else:
            print("❌ Falha ao conectar. Verifique SSID e senha.")
            return False

    def desconectar(self):
        """
        Desconecta o ESP32 da rede Wi-Fi e desativa a interface.

        Returns:
            bool: Retorna True se a desconexão for bem-sucedida, False se já estiver desconectado.
        """
        if self.sta_if.isconnected():
            self.sta_if.disconnect()  # Desconecta da rede
            self.sta_if.active(False)  # Desativa a interface Wi-Fi
            self.led.off()  # Apaga o LED indicando desconexão
            print("📴 Wi-Fi desconectado.")
            return True
        else:
            print("ℹ️ O Wi-Fi já está desconectado.")
            return False


# Exemplo de uso da classe WiFiManager
if __name__ == "__main__":
    ssid = "Racho Floresta"  # Nome da rede Wi-Fi
    senha = "jujumax1969"  # Senha da rede Wi-Fi

    wifi = WiFiManager(ssid, senha)

    if wifi.conectar():
        print("🚀 O ESP32 está pronto para comunicação!")
    else:
        print("⚠️ Não foi possível conectar ao Wi-Fi.")
