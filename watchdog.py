import os
import mysql.connector
from mysql.connector import Error
import schedule
import time
from dotenv import load_dotenv

# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()

# ⚙️ Configurações do banco
config = {
    'host': os.getenv("HOST"),
    'user': os.getenv("USUARIO"),
    'password': os.getenv("SENHA"),
    'database': os.getenv("BANCO_DADOS")
}

# Função de monitoramento
def monitorar_banco():
    try:
        conexao = mysql.connector.connect(**config)
        if conexao.is_connected():
            cursor = conexao.cursor()
            cursor.execute("SELECT COUNT(*) FROM pedidos")  # Exemplo: contar registros
            total = cursor.fetchone()[0]
            print(f"[✓] Banco online | Total de pedidos: {total}")

    except Error as e:
        print(f"[X] Erro ao conectar ou consultar o banco: {e}")

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# ⏰ Rodar a cada 5 minutos
schedule.every(5).minutes.do(monitorar_banco)

print("⏱️ Iniciando monitoramento...")
monitorar_banco()  # Primeira verificação já!

while True:
    schedule.run_pending()
    time.sleep(60)
