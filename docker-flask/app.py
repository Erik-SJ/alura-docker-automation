from flask import Flask, request, jsonify
app = Flask(__name__)
  # Lista em memória para simular o "banco de dados"
cadastros = []

@app.route("/")
def home():
      return "Aplicação Flask de Cadastro Simples!"

@app.route("/cadastro", methods=["POST"])
def criar_cadastro():
      dados = request.json
      if not dados or "nome" not in dados:
          return jsonify({"erro": "Informe o campo 'nome'"}), 400

      novo = {"id": len(cadastros) + 1, "nome": dados["nome"]}
      cadastros.append(novo)
      return jsonify(novo), 201

@app.route("/cadastro", methods=["GET"])
def listar_cadastros():
      return jsonify(cadastros)

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5000)