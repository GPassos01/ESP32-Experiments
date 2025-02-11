# ESP32 - Sensor Ultrassônico com Wi-Fi e Protocolo MQTT

Este projeto utiliza um **ESP32** para medir distâncias com um sensor ultrassônico, enviar os dados via **MQTT** para um servidor e exibir essas informações em tempo real.

## 📌 Funcionalidades

- Conecta o ESP32 a uma rede **Wi-Fi**.
- Envia medições de distância via **MQTT**.
- Modularizado para fácil manutenção e expansão.

## 🛠 Componentes Utilizados

- **ESP32**
- **Sensor Ultrassônico HC-SR04**
- **Broker MQTT** (Mosquitto)
- **Micropython**
- **Computador Pessoal** para receber os dados
- **Telefone Celular** para vizualizar os dados (opcional)

## 📁 Estrutura do Projeto

```
ESP32-Experiments/
│
├── boot.py          # Arquivo de inicialização do ESP32
│
├── main.py          # Lógica principal do projeto
│
├── src/
│   ├── WifiConnect.py      # Conexão com Wi-Fi
│   ├── clientMQTT.py       # Cliente MQTT
│   └── ultrasonic.py       # Leitura do sensor ultrassônico
│
├── server/
|   └── mosquitto_sub.py    # Roda o servidor mosquitto
|
├── config.json      # Configurações das variáveis
│
├── README.md           # Documentação do projeto
└── requirements.txt    # Dependências (se necessário)
```

## 🔧 Configuração e Uso

### 1️⃣ Configurar o ESP32

- Instale o **MicroPython** no ESP32, caso ainda não tenha.
- Use **Thonny** ou **rshell** para enviar os **arquivos** da pasta `/ESP32` para a placa.

### 2️⃣ Configurar a Conexão Wi-Fi

Edite o arquivo `config.json` e insira os dados necessários:

```json
{
  "wifi": {
    "ssid": "SEU_WIFI",
    "password": "SUA_SENHA"
  },
  "mqtt": {
    "broker": "BROKER_IP",
    "port": 1883,
    "topic": "esp32/distance"
  }
}
```

### 3️⃣ Rodar o Código

- Envie os arquivos **main.py** e a pasta **/src** para o **ESP32**.
- Importante que os arquivos mantenham a estrutura de diretórios do repositório para devido funcionamento
- Reinicie a placa e acompanhe o terminal para interação com a placa.

## 📡 Testando com MQTT

Nesse projeto foi usado o Broker Mosquitto, disponivel para download em: <https://mosquitto.org/download/>

No seu computador, rode o arquivo `/server/mosquitto_sub.py` com o seguinte comando para verificar os dados recebidos do ESP32:

```cmd
python mosquitto_sub.py
```

## 🚀 Futuras Melhorias

- Integração com um **dashboard web** para visualização dos dados.
