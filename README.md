Este é um sistema robusto de cadastro de usuários desenvolvido em Python utilizando o micro-framework **Flask**. O projeto aplica boas práticas de segurança, como criptografia de senhas com `bcrypt`, identificadores únicos globais (`UUID`) para os registros, e validações rigorosas de dados de entrada (E-mail e CPF) antes da persistência no banco de dados **SQLite**.

---

## 🛠️ Tecnologias Utilizadas

O ecossistema do projeto é composto pelas seguintes tecnologias e bibliotecas:

* **[Python 3](https://www.python.org/)**: Linguagem base do projeto.
* **[Flask](https://flask.palletsprojects.com/)**: Micro-framework web ágil e minimalista.
* **[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)**: Abstração ORM para comunicação com o banco de dados.
* **[Bcrypt](https://pypi.org/project/bcrypt/)**: Algoritmo de hash seguro para proteção de senhas.
* **[SQLite](https://www.sqlite.org/)**: Banco de dados relacional leve baseado em arquivo.
* **[Python-dotenv](https://pypi.org/project/python-dotenv/)**: Gerenciamento de variáveis de ambiente.

---

## 📁 Estrutura de Arquivos Recomendada

Para que este script funcione corretamente com o sistema de renderização do Flask, organize seu diretório desta forma:

```text
meu-projeto/
│
├── app.py              # Código principal (o script fornecido)
├── .env                # Arquivo de configuração de variáveis de ambiente
├── .gitignore          # Arquivos e pastas ignorados pelo Git
│
├── instance/           # Gerado automaticamente pelo SQLAlchemy
│   └── usuarios.db     # Banco de dados SQLite
│
└── templates/          # Pasta de arquivos HTML do Flask
    └── index.html      # Interface contendo o formulário de cadastro
