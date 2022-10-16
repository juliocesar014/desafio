from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.cliente import Cliente
from utils.db import db


clientes = Blueprint("clientes", __name__)


@clientes.route("/")
def index():
    clientes = Cliente.query.all()
    return render_template("index.html", clientes=clientes)


@clientes.route("/new", methods=["POST"])
def add_cliente():
    nome = request.form["nome"]
    cor1 = request.form["cor1"]
    modelo1 = request.form["modelo1"]
    cor2 = request.form["cor2"]
    modelo2 = request.form["modelo2"]
    cor3 = request.form["cor3"]
    modelo3 = request.form["modelo3"]

    new_cliente = Cliente(nome,cor1,modelo1,cor2,modelo2,cor3,modelo3)

    db.session.add(new_cliente)
    db.session.commit()

    flash("Cliente adicionado com sucesso!")

    return redirect(url_for("clientes.index"))


@clientes.route("/update/<id>", methods=["POST", "GET"])
def update(id):
    cliente = Cliente.query.get(id)

    if request.method == "POST":
        nome = request.form["nome"]
        cor1 = request.form["cor1"]
        modelo1 = request.form["modelo1"]
        cor2 = request.form["cor2"]
        modelo2 = request.form["modelo2"]
        cor3 = request.form["cor3"]
        modelo3 = request.form["modelo3"]

        db.session.commit()

        flash("Cliente atualizado com sucesso!")

        return redirect(url_for("clientes.index"))
    else:
        cliente = Cliente.query.get(id)
        return render_template("update.html", cliente=cliente)


@clientes.route("/delete/<id>")
def delete(id):
    cliente = Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()

    flash("Cliente deletado com sucesso!")

    return redirect(url_for("clientes.index"))


@clientes.route("/about")
def about():
    return render_template("about.html")
