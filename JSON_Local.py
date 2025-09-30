import json

alunos = [
    {"nome": "Guilherme", "curso": "ADS"},
    {"nome": "Eduardo", "curso": "ADS"},
    {"nome": "Kleber", "curso": "ADS"}
]

with open("alunos.json", "w") as f:
    json.dump(alunos, f, indent=4)

print("Arquivo 'alunos.json' salvo com sucesso!")
