# Projeto de Backup e Monitoramento de Banco de Dados

Este projeto realiza o monitoramento contínuo e backups automáticos de um banco de dados MySQL, garantindo segurança e disponibilidade das informações.

## Funcionalidades

- Monitoramento periódico do status do banco de dados
- Backup automático do banco em intervalos configuráveis
- Armazenamento organizado dos arquivos de backup
- Utilização de variáveis de ambiente para configuração
- Logs detalhados das operações realizadas

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Banco de Dados:** MySQL
- **Ferramentas de backup:** [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)
- **Gerenciamento de ambiente:** python-dotenv
- **Agendamento:** schedule

## Como Utilizar

1. Clone este repositório:
    ```sh
    git clone https://github.com/mrcostaalencar/monitoramento-backup-mysql.git
    ```
2. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
3. Configure as variáveis de ambiente no arquivo `.env`:
    ```
    USUARIO=seu_usuario
    SENHA=sua_senha
    BANCO_DADOS=nome_do_banco
    HOST=localhost
    ```
4. Execute o sistema de backup:
    ```sh
    python [backup.py](http://_vscodecontentref_/0)
    ```
5. Execute o sistema de monitoramento:
    ```sh
    python [watchdog.py](http://_vscodecontentref_/1)
    ```

## Estrutura do Projeto

- [`backup.py`](backup.py): Script responsável por realizar backups automáticos do banco de dados.
- [`watchdog.py`](watchdog.py): Script de monitoramento do status do banco de dados.
- [`backups/`](backups/): Diretório onde os arquivos de backup são armazenados.
- [`logs/`](logs/): Diretório para arquivos de log das operações.
- [`requirements.txt`](requirements.txt): Lista de dependências do projeto.
- [`.env`](.env): Arquivo de configuração das variáveis de ambiente.

## Contribuição

Contribuições são bem-vindas! Abra issues ou envie pull requests.

## Licença

Este projeto está licenciado sob a licença MIT.