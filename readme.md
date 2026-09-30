# 📄 Exportador de Relatório de Auditoria

Script em Python que recebe os alertas gerados pelo analisador de log e salva automaticamente um arquivo `.txt` com data e hora no nome, para uso como evidência de auditoria.

## 🚀 Funcionalidades

* **Exportação automática:** salva o relatório em arquivo `.txt` na pasta `relatorios/`
* **Nome com timestamp:** cada relatório recebe data e hora no nome (ex: `relatorio_2024-09-15_23-47-00.txt`), evitando sobrescrever arquivos anteriores
* **Criação automática de pasta:** se a pasta `relatorios/` não existir, o programa cria sozinho
* **Tratamento de erro:** se algo falhar ao salvar, avisa sem travar o programa (`try/except`)
* **Integração com o analisador:** importa diretamente as funções do `analisador-log-python`

## 🛠️ Tecnologias Utilizadas

* Python 3 (`datetime`, `os`)
* Git & GitHub

## 📂 Arquivos necessários

Copie os seguintes arquivos do repositório `analisador-log-python` para a mesma pasta:

* `analisador.py`
* `auth.log`
* `colaboradores.csv`

## 🏁 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/cah-menezes/exportador-relatorio-python.git
cd exportador-relatorio-python
```

2. Copie os arquivos do analisador (veja seção acima)

3. Execute:

```bash
python3 exportador.py
```

4. O relatório será salvo automaticamente na pasta `relatorios/`

## 🗺️ Próximos Passos

* Integrar diretamente com o analisador sem precisar copiar arquivos
* Adicionar cabeçalho e rodapé no relatório com data, total de alertas e versão