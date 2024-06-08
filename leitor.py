from processo import Processo

class Leitor:
    
    def pega_processos(self, arquivo_caminho: str) -> list[Processo]:
        processos = []
        id_atual = 1
        with open(arquivo_caminho, "r") as arquivo:
            for linha in arquivo:
                processos.append(Processo(id_atual, *list(map(int, linha.strip().split(',')))))
                id_atual += 1
        
        return processos
    
    
    def ordena_processos(self, processos: list[Processo]) -> list[Processo]:
        return sorted(processos, key=lambda processo: processo.momento_chegada)
