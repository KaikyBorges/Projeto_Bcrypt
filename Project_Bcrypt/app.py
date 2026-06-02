import os
import re
import uuid
import bcrypt
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Carrega variáveis de ambiente (.env)
load_dotenv()

app = Flask(__name__)

# Segurança
app.secret_key = os.environ.get("SECRET_KEY", "dev")

# Banco SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usuarios.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# =========================
# MODEL (Tabela)
# =========================
class Usuario(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

# =========================
# VALIDAÇÕES
# =========================
def validar_email(email):
    email = email.strip().lower()
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(padrao, email):
        return False, "Formato de email inválido"
    if ".." in email:
        return False, "Email não pode ter '..'"

    return True, email

def validar_cpf(cpf):
    cpf = cpf.strip()

    if not cpf.isdigit():
        return False, "CPF deve conter apenas números"
    if len(cpf) != 11:
        return False, "CPF deve ter 11 dígitos"

    return True, cpf

# =========================
# ROTAS
# =========================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    username = request.form.get("username", "").strip()
    email_raw = request.form.get("gmail", "")
    cpf_raw = request.form.get("cpf", "")
    senha = request.form.get("senha", "")

    # ===== VALIDAÇÕES =====

    if not username:
        flash("Username obrigatório", "error")
        return redirect(url_for("index"))

    if not senha:
        flash("Senha não pode ser vazia", "error")
        return redirect(url_for("index"))

    valido_email, email = validar_email(email_raw)
    if not valido_email:
        flash(email, "error")
        return redirect(url_for("index"))

    valido_cpf, cpf = validar_cpf(cpf_raw)
    if not valido_cpf:
        flash(cpf, "error")
        return redirect(url_for("index"))

    # ===== DUPLICIDADE =====
    if Usuario.query.filter_by(email=email).first():
        flash("Email já cadastrado", "error")
        return redirect(url_for("index"))

    if Usuario.query.filter_by(cpf=cpf).first():
        flash("CPF já cadastrado", "error")
        return redirect(url_for("index"))

    # ===== HASH SENHA =====
    senha_hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    # ===== CRIAR USUÁRIO =====
    novo_usuario = Usuario(
        id=str(uuid.uuid4()),
        username=username,
        email=email,
        cpf=cpf,
        senha=senha_hash
    )

    db.session.add(novo_usuario)
    db.session.commit()

    flash("Usuário cadastrado com sucesso!", "success")
    return redirect(url_for("index"))

# =========================
# INICIALIZAÇÃO
# =========================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # cria banco automaticamente

    app.run(debug=True)