from cpu import *
class Processo:
    id : int
    momento_chegada : int
    fase1_cpu : int
    fase_io : int
    fase2_cpu : int
    tam : int
    quant_disco : int 
    estado : str
    cpu_consumida : Cpu
    def __init__(self, id, momento_chegada, fase1_cpu, fase_io, fase2_cpu, tam, quant_disco):
        self.id = id
        self.momento_chegada = momento_chegada
        self.fase1_cpu = fase1_cpu
        self.fase_io = fase_io
        self.fase2_cpu = fase2_cpu
        self.tam = tam
        self.quant_disco = quant_disco
        self.estado = "novo"
        
        