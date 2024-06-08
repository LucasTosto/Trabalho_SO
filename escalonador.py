from processo import Processo
class Escalonador:
    lista_bloqueados : list[Processo]
    lista_q0 : list[Processo]
    lista_q1 : list[Processo]
    lista_q2 : list[Processo]
    lista_q3 : list[Processo]
    quantum = 3

    def escalonar(self, cpu_livre):
        for p in self.lista_q0:
          if p.cpu_consumida == None:
             p.cpu_consumida = cpu_livre
             return
        for p in self.lista_q1:
           if p.cpu_consumida == None:
             p.cpu_consumida = cpu_livre
             return
        for p in self.lista_q2:
           if p.cpu_consumida == None:
             p.cpu_consumida = cpu_livre
             return
        for p in self.lista_q3:
           if p.cpu_consumida == None:
             p.cpu_consumida = cpu_livre
             return
    
    def bloqueia_processo(self, ):
       