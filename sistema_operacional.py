from memoria_principal import MemoriaPrincipal
from cpu import Cpu
from disco import Disco

class SistemaOperacional:
  lista_processos_novos = []

  #recursos disponiveis
  memoria = MemoriaPrincipal(tam=32*1024)
  
  cpu1 = Cpu()
  cpu2 = Cpu()
  cpu3 = Cpu()
  cpu4 = Cpu()
  
  disco1 = Disco()
  disco2 = Disco()
  disco3 = Disco()
  disco4 = Disco()
  
  