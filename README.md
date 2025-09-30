# python-cloud-trabalho
Repositório para trabalho de Python na nuvem

Trabalho: Python + Cloud + GitHub
Disciplina: Cloud Computing - 2º período ADS/CC

n Objetivos
1. Consolidar o aprendizado de Python com APIs, JSON e Flask. 
2. Compreender a relação entre Python e Cloud Computing.
3. Praticar versionamento com Git e GitHub (commit, push, pull). 
4. Desenvolver autonomia na documentação de projetos.

n Tarefas
1. Criar repositório público no GitHub chamado 'python-cloud-trabalho'. 

	https://github.com/kleber-lim/python-cloud-trabalho

2. Adicionar README.md explicando o projeto.



3. Scripts obrigatórios:
   - API GitHub (mostrar nome, descrição e estrelas).
   - API Clima (mostrar temperatura e vento de Curitiba + outra cidade). 
   - JSON Local (salvar e ler dados de alunos).
   - API Flask (rotas /, /alunos, /saudacao/<nome>, /curso/<curso>).
4. Fazer commits separados para cada script.
5. Enviar alterações ao GitHub (push).
6. Testar git pull/clonar em outra máquina.
7. Documentar tudo no README.md com prints de execução.


Git Cheat Sheet – Guia Rápido
Configuração inicial
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@example.com"

Fluxo de Trabalho Básico
git init                      # Inicia repositório local
git status                    # Verifica status
git add .                     # Adiciona todos os arquivos 
git commit -m "mensagem"      # Salva versão
git remote add origin URL     # Conecta ao GitHub 
git push -u origin main       # Envia primeira vez
git push                      # Envia alterações
git pull                      # Atualiza do GitHub
git clone URL                 # Clona repositório existente 
git log --oneline             # Histórico resumido

n Observação Final
Sempre usar mensagens de commit claras e descritivas. 
Exemplo: git commit -m "Adicionei rota /curso no Flask".






---

## 🌤️ Script: API de Clima

O arquivo `02_api_clima.py` realiza uma consulta à API gratuita [Open-Meteo](https://open-meteo.com/) e exibe:

- ✅ Temperatura atual (°C)
- ✅ Velocidade do vento (km/h)
- 🌍 Cidades consultadas: Curitiba e São Paulo

### 🧪 Como executar

1. Instale o pacote necessário:

```bash
pip install requests
Execute o script:

bash
Copiar código
python 02_api_clima.py
💻 Exemplo de saída
text
Copiar código
Temperatura atual: 18.8 °C
Velocidade do vento: 18.6 km/h
📸 Print da execução (PyCharm)

yaml
Copiar código

---

## ✅ Depois de colar o trecho:

1. Clique no botão verde **"Commit changes"** no canto superior direito.
2. Deixe a descrição como `docs: adiciona instruções do script de clima` (ou algo similar).
3. Clique em **Commit directly to the `main` branch**.

---

## 📎 Observações

- Se ainda **não criou a pasta `/prints` com a imagem**, recomendo fazer isso localmente no PyCharm:
  ```bash
  mkdir prints
  # coloque a imagem do print lá dentro
Depois:

bash




 Consulta de Repositório via API do GitHub

Este script em Python utiliza a API pública do GitHub para obter informações de um repositório específico.

---

## 📌 Objetivo

Obter e exibir os seguintes dados do repositório:

- ✅ Nome do repositório
- ✅ Descrição
- ✅ Quantidade de estrelas ⭐

---

## 🧪 Como Funciona

O script faz uma requisição `GET` para o endpoint da API do GitHub:

https://api.github.com/repos/kleber-lim/python-cloud-trabalho

yaml
Copiar código

Se a resposta for bem-sucedida (`status_code == 200`), ele imprime os dados desejados.

---

## 🧠 Tecnologias Usadas

- Python 3.x
- Biblioteca `requests`
- API pública REST do GitHub

---

## 📁 Código-fonte (`github_api.py`)

```python
import requests

# URL da API do GitHub para o repositório
url = "https://api.github.com/repos/kleber-lim/python-cloud-trabalho"

# Faz a requisição GET
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    print(f"Nome do repositório: {data['name']}")
    print(f"Descrição: {data['description']}")
    print(f"Estrelas: {data['stargazers_count']}")
else:
    print(f"Erro ao acessar a API: {response.status_code}")
🚀 Como Executar
Instale a biblioteca requests se ainda não tiver:

bash
Copiar código
pip install requests
Execute o script:

bash
Copiar código
python github_api.py
💻 Exemplo de saída
text
Copiar código
Nome do repositório: python-cloud-trabalho
Descrição: Repositório para trabalho de Python na nuvem
Estrelas: 0
📝 Licença
Distribuído sob a licença MIT.

🙋‍♂️ Autor
Guilherme M Marques Pereira

yaml
Copiar código

---

## ✅ O que fazer agora:

1. Crie o arquivo no PyCharm ou direto no GitHub com o nome:  
   `README.md` (ou edite o existente, se for separado por scripts).
2. Cole esse conteúdo.
3. Faça o commit com a mensagem:

```bash
git add README.md
git commit -m "docs: adiciona documentação da API GitHub (github_api.py)"
git push

Copiar código
git add prints/saida-execucao.png
git commit -m "docs: adiciona print de execução ao README"
git push

