"""
Analisador de Log de Auditoria
Lê registros de acesso (auth.log) e cruza com a base de colaboradores
para identificar comportamentos suspeitos: usuários desligados, sem MFA
e acessos fora do horário comercial.
"""

import csv
import datetime

# Variáveis fixas
ARQUIVO_LOG= "auth.log"
ARQUIVO_COLABORADORES = "colaboradores.csv"

# Funções
def carregar_logs():
    logs = []
    with open(ARQUIVO_LOG, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            logs.append(linha.strip())
    return logs

def carregar_colaboradores():
    colaboradores = {}
    with open(ARQUIVO_COLABORADORES, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            colaboradores[linha["usuario"]] = linha
    return colaboradores

def analisar(logs, colaboradores):
    analisados = []
    for linha in logs:
        partes = linha.split(" | ")
        data_hora = datetime.datetime.strptime(partes[0], "%Y-%m-%d %H:%M:%S")
        hora = data_hora.hour
        usuario = partes[1]
        ficha = colaboradores[usuario]
        if ficha ["status"] == "desligado":
            analisados.append(f"🚨 ALERTA: {usuario} está desligado mas acessou o sistema!")
        if ficha ["mfa"] == "nao":
            analisados.append(f"🚨 ALERTA: {usuario} não tem mfa ativado.")
        if hora < 8 or hora > 18:
            analisados.append(f"🚨 ALERTA: {usuario} acessou o sistema fora do horário comercial.")
    return analisados

def relatorio(alertas):
    print("=" * 40)
    print ("RELATÓRIO DE AUDITORIA DE ACESSO")
    print("=" * 40)
    for alerta in alertas:
        print(alerta)
    print ("=" * 40)
    print (f"Total de alertas: {len(alertas)}")
    print ("=" * 40)

# Programa principal
if __name__ == "__main__":
    colaboradores = carregar_colaboradores()
    logs = carregar_logs()
    alertas = analisar(logs, colaboradores)
    relatorio(alertas)