import subprocess

BROKER_IP = "localhost"  # IP do seu broker Mosquitto (substitua se necessário)
TOPIC = "sensor/dados"  # Tópico MQTT a ser escutado

def executar_mosquitto_sub():
    try:
        # Comando para assinar o tópico no Mosquitto
        comando = ["mosquitto_sub", "-h", BROKER_IP, "-t", TOPIC, "-v"]
        
        print(f"Escutando mensagens no tópico '{TOPIC}' do broker '{BROKER_IP}'...")
        subprocess.run(comando, check=True)

    except FileNotFoundError:
        print("Erro: O comando 'mosquitto_sub' não foi encontrado. Certifique-se de que o Mosquitto está instalado e no PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o Mosquitto: {e}")

if __name__ == "__main__":
    executar_mosquitto_sub()