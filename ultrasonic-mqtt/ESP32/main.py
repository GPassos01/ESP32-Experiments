import time
import json
from src.WifiConnect import WiFiManager
from src.ultrasonic import UltrasonicSensor
from src.clientMQTT import MQTTClientHandler

def carregar_configuracoes():
    """Carrega as configurações de rede a partir de um arquivo JSON."""
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)  # Carrega o conteúdo JSON
            return config
    except FileNotFoundError:
        print("Arquivo de configurações não encontrado!")
        return None
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON!")
        return None

# Função principal para interação com o usuário
def main():
    """
    Função principal que oferece uma interface interativa no terminal para o usuário,
    permitindo conectar à rede Wi-Fi, medir distância com o sensor ultrassônico e publicar dados via MQTT.
    """
    # Carrega todas as configurações do arquivo JSON
    config = carregar_configuracoes()

    ssid = config['wifi']['ssid']  # Nome da rede Wi-Fi
    senha = config['wifi'] ['password']  # Senha da rede Wi-Fi
    net = WiFiManager(ssid, senha) #instancia objeto de rede

    # Configurar a conexão Wi-Fi
    if not net.conectar():
        return  # Caso a conexão falhe, o programa é interrompido.

    # Definir pinos do sensor ultrassônico (TRIG e ECHO)
    TRIG_PIN = config['ultrasonic_sensor']['trig_pin']  # Pino TRIG
    ECHO_PIN = config['ultrasonic_sensor']['echo_pin']  # Pino ECHO
    sensor = UltrasonicSensor(TRIG_PIN, ECHO_PIN)# Inicializar o sensor ultrassônico com os pinos definidos

    # Definir as informações do cliente MQTT (Broker, ID do cliente e tópico)
    broker_ip = config['mqtt']['broker']  # IP do broker MQTT
    client_id = config['mqtt']['client_id']  # ID do cliente
    topic = config['mqtt']['topic1']  # Tópico onde os dados serão enviados

    # Inicializar o cliente MQTT com os parâmetros configurados
    mqtt_client = MQTTClientHandler(broker_ip, client_id, topic)

    # Interação com o usuário para controle do loop de medição e envio de dados
    while True:
        # Menu de opções para o usuário
        print("\nEscolha uma opção:")
        print("1 - Medir distância")
        print("2 - Enviar ultima medição")
        print("3 - Iniciar teste de comunicação de dados com o Servidor MQTT")
        print("4 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            # Medir e exibir a distância do sensor
            distancia = sensor.measure_distance()
            print(f"Distância medida: {distancia} cm")
        
        elif opcao== "2":
            # Inicia o envio do dado via MQTT
            try:
                mensagem = f"{distancia} cm"
                mqtt_client.publicar_mensagem(mensagem)
            except NameError:
                print('Nenhuma medição foi feita. Selecione a opção "1" para fazer a medição')

        elif opcao == "3":
            # Iniciar loop de envio de dados ficticios via MQTT
            try:
                tempo = int(input("Digite o tempo em segundos de duração do teste: "))
                mqtt_client.loop_publicacao(tempo) #Usando dados ficticios
            except ValueError:
                print("Por favor, insira um número válido para o intervalo de envio.")
        
        elif opcao == "4":
            # Sair do programa
            print("Saindo...")
            break
        
        else:
            # Caso o usuário insira uma opção inválida
            print("Opção inválida. Tente novamente.")

# Rodar a função principal
if __name__ == "__main__":
    main()
