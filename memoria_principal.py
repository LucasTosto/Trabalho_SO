from processo import * 

class MemoriaPrincipal:
 
    def __init__(self, tam):
        self.lista_de_processos = []
        self.fila_de_espera = []
        self.tam = tam
    
    def add_processo(self, processo):
        if processo.tam > tam:
            self.fila_de_espera.append(processo)
            return
        
        self.lista_de_processos.append(processo)
        tam -= processo.tam
        
    def remove_processo(self, processo):
        self.lista_de_processos.remove(processo)
        tam += processo.tam
        
        if len(self.fila_de_espera) > 0:
            if self.fila_de_espera[0].tam <= tam:   
                self.add_processo(self.fila_de_espera.pop(0))