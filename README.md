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

⚙️ Configuração e Instalação
Siga o passo a passo abaixo para rodar o projeto localmente em sua máquina:

1. Clonar ou criar o diretório do projeto
Crie uma pasta para o projeto e salve o código fornecido como app.py.

2. Criar e Ativar o Ambiente Virtual (Venv)
É altamente recomendável isolar as dependências do projeto:
# No Linux/macOS:
python3 -m venv venv
source venv/bin/activate

# No Windows (Prompt de Comando):
python -m venv venv
venv\Scripts\activate

3. Instalar as Dependências
Instale todos os pacotes necessários utilizando o gerenciador pip:

Bash
pip install Flask Flask-SQLAlchemy bcrypt python-dotenv
4. Configurar as Variáveis de Ambiente
Crie um arquivo chamado .env na raiz do projeto e defina uma chave secreta segura para as sessões do Flask:

Snippet de código
SECRET_KEY=uma_chave_secreta_e_complexa_aqui
Nota: Se o arquivo .env não for encontrado, o sistema adotará o valor padrão "dev" configurado no código.

💻 Como Executar o Projeto
Com o ambiente virtual ativo e as dependências instaladas, execute:

Bash
python app.py
O terminal exibirá que o servidor está rodando. Abra o seu navegador e acesse:
👉 http://127.0.0.1:5000/

🧠 Arquitetura do Código e Recursos Técnicos
🔒 Segurança Avançada
Proteção de Senhas: O sistema nunca armazena senhas em texto puro. Utiliza-se a técnica de hashing com bcrypt.hashpw combinado com uma salt (sal) gerada aleatoriamente. Isso impede ataques de dicionário ou consultas em tabelas Rainbow.

UUID v4: Em vez de utilizar IDs sequenciais inteiros (1, 2, 3...) que expõem o volume de usuários cadastrados e facilitam varreduras maliciosas, o sistema utiliza identificadores alfanuméricos universais de 36 caracteres.

📊 Modelo de Dados (ORM)
A tabela Usuario possui restrições de integridade diretamente mapeadas no banco:

email: Único e obrigatório.

cpf: Único e obrigatório (apenas os 11 dígitos numéricos).

🛡️ Camada de Validação Customizada
O sistema intercepta as requisições POST no endpoint /cadastrar e submete os dados a filtros baseados em Expressões Regulares (re):

Validação de E-mail: Verifica a estrutura padrão do endereço de e-mail e barra anomalias como pontos duplicados (..).

Validação de CPF: Garante que a string possua exatamente 11 caracteres e que todos sejam numéricos (.isdigit()).

Checagem de Duplicidade: Antes de realizar o commit, o SQLAlchemy faz uma busca rápida pelos campos unique para evitar falhas críticas de banco de dados e retornar um feedback amigável via mensagens flash.

📨 Estrutura do Formulário HTML (index.html)
Para que o mapeamento dos dados do formulário funcione perfeitamente com os métodos request.form.get() do back-end, certifique-se de que as propriedades name dos inputs coincidam com o esperado pelo código Flask:

HTML
<form action="/cadastrar" method="POST">
    <input type="text" name="username" placeholder="Nome de Usuário" required>
    <input type="email" name="gmail" placeholder="E-mail" required> <input type="text" name="cpf" placeholder="CPF (apenas números)" required>
    <input type="password" name="senha" placeholder="Senha" required>
    <button type="submit">Cadastrar</button>
</form>

{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    {% for category, message in messages %}
      <div class="alert alert-{{ category }}">{{ message }}</div>
    {% endfor %}
  {% endif %}
{% endwith %}
