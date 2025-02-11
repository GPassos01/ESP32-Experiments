import machine
import time

class UltrasonicSensor:
    """
    Classe que representa um sensor ultrassônico.

    O sensor usa dois pinos: um para emitir o pulso (TRIG) e outro para receber o eco (ECHO).
    A distância é medida com base no tempo que leva para o pulso ir e voltar ao sensor.
    """
    
    def __init__(self, trigger_pin, echo_pin):
        """
        Inicializa o sensor ultrassônico com os pinos especificados.

        O pino TRIG é usado para enviar o pulso, e o pino ECHO é usado para medir o tempo
        até o retorno do pulso.

        :param trigger_pin: O pino conectado ao TRIG do sensor.
        :type trigger_pin: int
        :param echo_pin: O pino conectado ao ECHO do sensor.
        :type echo_pin: int
        """
        # Inicializa os pinos do sensor
        self.trig = machine.Pin(trigger_pin, machine.Pin.OUT)
        self.echo = machine.Pin(echo_pin, machine.Pin.IN)

    def measure_distance(self):
        """
        Mede a distância utilizando o sensor ultrassônico.

        O método envia um pulso para o pino TRIG, espera o retorno do pulso no pino ECHO,
        e calcula a distância com base no tempo entre o envio e o recebimento do pulso.

        :return: A distância medida em centímetros, arredondada para 2 casas decimais.
        :rtype: float
        """
        # Envia um pulso de 10µs para o pino TRIG
        self.trig.value(0)  # Garante que o TRIG esteja em baixo inicialmente
        time.sleep_us(2)
        self.trig.value(1)  # Envia o pulso
        time.sleep_us(10)
        self.trig.value(0)  # Finaliza o pulso

        # Espera o sinal de ECHO voltar
        while self.echo.value() == 0:  # Enquanto não começa a resposta do pino ECHO
            pulse_start = time.ticks_us()  # Marca o tempo de início

        while self.echo.value() == 1:  # Enquanto o pino ECHO estiver recebendo o sinal
            pulse_end = time.ticks_us()  # Marca o tempo de fim

        # Calcula a distância com base no tempo de voo do pulso
        pulse_duration = time.ticks_diff(pulse_end, pulse_start)  # Calcula a duração do pulso
        distance = (pulse_duration * 0.0343) / 2  # A velocidade do som é 343 m/s, divide por 2 devido à ida e volta

        return round(distance, 2)  # Retorna a distância arredondada para 2 casas decimais

if __name__ == "__main__":
    # Definindo os pinos do sensor
    TRIG_PIN = 23  # Pino TRIG
    ECHO_PIN = 22  # Pino ECHO

    # Criação do objeto sensor com os pinos definidos
    sensor = UltrasonicSensor(TRIG_PIN, ECHO_PIN)

    # Exibe a distância medida
    print(f"Distância medida: {sensor.measure_distance()} cm")