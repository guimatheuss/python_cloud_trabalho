from flask import Flask, jsonify

app = Flask(__name__)

alunos = [
    {"nome": "Guilherme", "curso": "ADS"},
    {"nome": "Eduardo", "curso": "ADS"},
    {"nome": "Kleber", "curso": "ADS"}
]

@app.route("/")
def home():
    return "✅ API rodando! Rotas disponíveis: /alunos, /saudacao/<nome>, /curso/<nome_do_curso>"


@app.route("/alunos")
def get_alunos():
    return jsonify(alunos)

@app.route("/saudacao/<nome>")
def saudacao(nome):
    return jsonify({"mensagem": f"Olá, {nome}! Seja bem-vindo à API."})

@app.route("/curso/<nome_do_curso>")
def info_curso(nome_do_curso):
    cursos = {
        "ADS": "Análise e Desenvolvimento de Sistemas. Foco em aplicações web e mobile.",
        "CC": "Ciência da Computação. Foco em teoria, algoritmos e fundamentos de software.",
        "ENGENHARIA": "Engenharia de Software. Foco em processos e qualidade de desenvolvimento em larga escala."
    }

    info = cursos.get(nome_do_curso.upper(), f"Informação sobre o curso '{nome_do_curso}' não encontrada.")

    return jsonify({"curso": nome_do_curso, "descricao": info})


if __name__ == "__main__":
    app.run(debug=True)