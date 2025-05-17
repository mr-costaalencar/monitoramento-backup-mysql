import os
import datetime
import schedule
import time
from dotenv import load_dotenv

# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()

# ⚙️ Configurações
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
banco = os.getenv("BANCO_DADOS")
diretorio_backup = "./backups"

def fazer_backup():
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    nome_arquivo = f"{diretorio_backup}/backup_{banco}_{data_atual}.sql"
    
    comando = f"mysqldump -u {usuario} -p{senha} {banco} > {nome_arquivo}"
    resultado = os.system(comando)

    if resultado == 0:
        print(f"[✓] Backup feito com sucesso: {nome_arquivo}")
    else:
        print(f"[X] Falha ao fazer backup!")

# ⏰ Exemplo: rodar a cada 6 horas
schedule.every(6).hours.do(fazer_backup)

print("Iniciando agendador de backups...")
fazer_backup()  # Faz um logo no início

while True:
    schedule.run_pending()
    time.sleep(60)
