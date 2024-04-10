class Televisao():
    def __init__(self):
        self.ligada = False
        self.volume = 0
        self.canal = 1
        self.volumeSalvo = 0

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def volumeMais(self):
        if self.volume < 100:
            self.volume = self.volume + 1

    def volumeMenos(self):
        if self.volume > 0:
            self.volume = self.volume - 1

    def canalMais(self):
        if self.canal < 300:
            self.canal = self.canal + 1

    def canalMenos(self):
        if self.canal > 1:
            self.canal = self.canal - 1

    def volumeOff(self):
        if self.volume > 0:
            self.volumeSalvo = self.volume
            self.volume = 0

    def volumeOn(self):
        if self.volume < 1:
            self.volume = self.volumeSalvo

    def digitarCanal(self, digitar):
        if  0 < digitar < 301 :
            self.canal = digitar
        else : print("canal invalido")

    def infoCanal(self):
        print("self.canal.infoCanal")
