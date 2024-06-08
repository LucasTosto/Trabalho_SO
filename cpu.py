class Cpu:

    #processo alocado = id
    #cpu alocada = bool
    def __init__(self, processo_alocado, alocado:None):
        self.processo_alocado = processo_alocado
        self.alocado = False


    def setAlocado(self, alocado):
        self.alocado = True




