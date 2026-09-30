"""
Exportador de Relatório de Auditoria
Recebe os alertas gerados pelo analisador de log e salva
num arquivo .txt com data e hora no nome, para uso como evidência.
"""

import datetime
import os
from analisador import analisar, carregar_logs, carregar_colaboradores

#Variável fixa
PASTA_RELATORIO = "relatorio"

#Funções
def exportar(alertas):
    agora = datetime.datetime.now()
    data_hora = agora.strftime("%Y-%m-%d_%H-%M-%S")
    nome = f"{PASTA_RELATORIO}/relatorio_{data_hora}.txt"
    try:
        os.makedirs(PASTA_RELATORIO, exist_ok=True)
        with open(nome, "w", encoding="utf-8") as arquivo:
            for alerta in alertas:
                arquivo.write(alerta + "\n")
    except:
        print("\nOcorreu um erro e não foi possível salvar o arquivo. Tente novamente, por favor.\n")

#Programa principal
if __name__ == "__main__":
    colaboradores = carregar_colaboradores()
    logs = carregar_logs()
    alertas = analisar(logs, colaboradores)
    exportar(alertas)