import socket
import time
import random
from umqtt.simple import MQTTClient

# Classe para gerenciar o cliente MQTT
class MQTTClientHandler:
    def __init__(self, BROKER_IP, CLIENT_ID, TOPIC):
        """
        Inicializa o cliente MQTT com as informações do broker, ID do cliente e tópico.
        
        :param BROKER_IP: O endereço IP do broker MQTT (servidor).
        :param CLIENT_ID: Identificador único do cliente no broker.
        :param TOPIC: O tópico em que as mensagens serão publicadas.
        """
        self.broker_ip = BROKER_IP  # Endereço IP do broker MQTT
        self.client_id = CLIENT_ID  # ID único para o cliente
        self.topic = TOPIC  # Tópico onde os dados serão enviados
        self.client = MQTTClient(self.client_id, self.broker_ip)  # Criação do objeto cliente MQTT com ID e IP do broker

    def conectar(self):
        """
        Conecta o cliente MQTT ao broker. Caso ocorra um erro, a exceção é tratada e uma mensagem de erro é exibida.
        """
        try:
            print(f"Conectando ao broker MQTT {self.broker_ip}...")
            self.client.connect()  # Conecta ao broker MQTT usando o endereço IP
            print("Conectado ao broker com sucesso!")
        except Exception as e:
            print(f"Erro ao conectar ao broker MQTT: {e}")  # Exibe mensagem de erro caso a conexão falhe

    def publicar_mensagem(self, mensagem):
        """
        Publica uma mensagem no tópico configurado. Se houver erro durante a publicação, a exceção é tratada.

        :param mensagem: A mensagem que será enviada ao broker.
        """
        try:
            print(f"Publicando: {mensagem}")
            self.client.publish(self.topic, mensagem)  # Envia a mensagem para o broker no tópico definido
            print("Mensagem publicada com sucesso!")
        except Exception as e:
            print(f"Erro ao publicar mensagem: {e}")  # Exibe mensagem de erro caso a publicação falhe

    def loop_publicacao(self, tempo):
        """
        Realiza a conexão ao broker e começa a publicar mensagens periodicamente. Caso ocorra erro na conexão ou publicação,
        a exceção é tratada e uma mensagem de erro é exibida.

        :param tempo: O tempo (em segundos) de duração do teste.
        """
        tempo_inicio = time.time()
        try:
            self.conectar()  # Conecta ao broker
            while True:
                tempo_atual = time.time()
                segundos_passados = tempo_atual - tempo_inicio
                distancia = random.uniform(0, 500)
                mensagem = f"Dados do sensor: {distancia} cm"  # Exemplo de dado do sensor (aqui simulado como "20 cm")
                self.publicar_mensagem(mensagem)  # Publica a mensagem
                if segundos_passados >= tempo:
                    print("Fim do tempo de teste")
                    break
                time.sleep(1)  # Aguarda pelo intervalo de 1s antes de publicar novamente
        except Exception as e:
            print(f"Erro no loop de publicação: {e}")  # Exibe mensagem de erro caso ocorra algum erro no loop

# Código principal, responsável por executar o cliente MQTT
if __name__ == "__main__":
    # Configurações do cliente MQTT
    BROKER_IP = "192.168.0.138"  # IP do broker MQTT
    CLIENT_ID = "esp32_mqtt"  # ID único para o cliente
    TOPIC = "sensor/dados"  # Tópico onde as mensagens serão publicadas

    # Instancia o objeto MQTTClientHandler com as configurações fornecidas
    mqtt_client = MQTTClientHandler(BROKER_IP, CLIENT_ID, TOPIC)

    # Inicia o loop de publicação de mensagens a cada intervalo de 5 segundos
    mqtt_client.loop_publicacao(5)  # O intervalo de publicação é de 5 segundos
