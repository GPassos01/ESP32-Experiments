import paho.mqtt.client as mqtt

BROKER_IP = "192.168.0.138"  # IP do seu PC
TOPIC = "sensor/dados"

def on_connect(client, userdata, flags, rc):
    print(f"Conectado com o código {rc}")
    # Inscreve-se no tópico após a conexão ser estabelecida
    client.subscribe(TOPIC)
    
def on_message(client, userdata, msg):
    print(f"Recebido: {msg.topic} -> {msg.payload.decode()}")

client = mqtt.Client("pc_mqtt")# Criação do cliente MQTT

# Definindo os callbacks
client.on_connect = on_connect
client.on_message = on_message


client.connect(BROKER_IP, 1883, 60)

client.loop_start()


print("Aguardando mensagens...")
try:
    while True:
        pass  # Aguardando indefinidamente
except KeyboardInterrupt:
    print("Conexão interrompida.")
    client.loop_stop()  # Interrompe o loop quando o usuário pressionar CTRL+C

