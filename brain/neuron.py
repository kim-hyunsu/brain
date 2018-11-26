
class Neuron(object):
    def __init__(self, receiver: int, sender: int, length: int):
        self.receiver = receiver
        self.sender = sender
        self.length = length

    def send_to(self, nbr):
        nbr.receive_from(self)

    def receive_from(self, nbr):
        pass


class SensoryNeuron(Neuron):
    pass


class MotorNeuron(Neuron):
    pass


class Interneuron(Neuron):
    pass
