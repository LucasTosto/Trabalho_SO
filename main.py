from leitor import Leitor

leitor = Leitor()
lista = leitor.pega_processos("entrada.txt")

for processo in lista:
    print(
      f'Processo: {processo.id}\n \
          - Chegada: {processo.momento_chegada}\n \
          - Duração CPU 1 \n{processo.fase1_cpu}\n \
          - Duração E/S \n{processo.fase_io}\n \
          - Duração CPU 2 \n{processo.fase2_cpu}\n \
          - Tamanho do processo \n{processo.tam}\n \
          - Quantidade de discos \n{processo.quant_disco}\n\n \
        ')