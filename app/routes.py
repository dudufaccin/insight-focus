from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)

registros = {"ganhos": [], "gastos": []}


@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        descricao = request.form["descricao"]
        valor = float(request.form["valor"])
        tipo = request.form["tipo"]

        if tipo == "ganho":
            registros["ganhos"].append({"descricao": descricao, "valor": valor})
        elif tipo == "gasto":
            registros["gastos"].append({"descricao": descricao, "valor": valor})

    return render_template("index.html", registros=registros)
