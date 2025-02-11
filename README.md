# 🚀 ESP32 - Projetos e Experimentos

Este repositório contem diversos projetos e experimentos utilizando o ESP32, explorando diferentes sensores, protocolos de comunicação e aplicações. Cada projeto está organizado em uma pasta separada, com seu próprio código e documentação.

## 🎯 Objetivo

Este repositório tem como objetivo armazenar e documentar os experimentos e implementações utilizando o ESP32, organizando-os de forma modular e reutilizável para facilitar a replicação e evolução dos projetos. A ideia é desenvolver projetos para fins de aprendizados.

## 📁 Estrutura do Repositório

```plaintext
ESP32-Projects/
│
├── ultrasonic-mqtt/  # Mede distância e envia via MQTT
│   ├── boot.py
│   ├── main.py
│   ├── src/
|   ├── server/
|   ├── lib/
|   ├── config.json
│   └── README.md
│
├── Projeto2_EM_PRODUÇÃO/
│   ├── boot/
│   ├── main/
│   ├── src/
│   ├── README.md
│
├── Projeto3_EM_PRODUÇÃO/  # Controla um LED via interface web
│   ├── boot/
│   ├── main/
│   ├── src/
│   ├── README.md
│
└── README.md  # Visão geral do repositório
```

## 📌 Projetos Disponíveis

🔹 **Projeto 1: Sensor Ultrassônico com MQTT**

- Mede distâncias com um HC-SR04
- Envia dados via MQTT para um broker

🔹 **Projeto 2: Sensor de Temperatura MQTT**

- Utiliza um sensor DHT11/DHT22
- Envia leituras para um servidor MQTT

🔹 **Projeto 3: Controle de LED via Web**

- Cria um servidor web no ESP32
- Permite controlar um LED remotamente

## 🔧 Como Utilizar

1️⃣ Instalar MicroPython no ESP32

2️⃣ Escolher um projeto e navegar até sua pasta

3️⃣ Conferir o `README.md` do projeto para detalhes sobre sua utilização específica

4️⃣ Enviar os arquivos para a placa (usando Thonny, rshell ou ampy)

5️⃣ Rodar o projeto e monitorar os logs

## 🔜 Melhorias Futuras

- ✅ Adicionar suporte a mais sensores
- ✅ Criar um dashboard para visualização dos dados
- ✅ Melhorar a reconexão automática Wi-Fi e MQTT
