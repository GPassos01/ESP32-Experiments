import subprocess
import json

def carregar_configuracoes():
    """Carrega as configurações de rede a partir de um arquivo JSON."""
    try:
        with open('../config.json', 'r') as f:
            config = json.load(f)  # Carrega o conteúdo JSON
            return config
    except FileNotFoundError:
        print("Arquivo de configurações não encontrado!")
        return None
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON!")
        return None

def executar_mosquitto_sub():

    config = carregar_configuracoes()

    BROKER_IP = config['mqtt']['broker']  # IP do seu broker Mosquitto (substitua se necessário)
    TOPIC = config['mqtt']['topic1'] # Tópico MQTT a ser escutado

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