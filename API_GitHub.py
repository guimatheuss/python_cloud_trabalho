import requests

url = "https://api.github.com/repos/torvalds/linux"

resp = requests.get(url)

data = resp.json()

print("Repositório:", data["name"])
print("Descrição:", data["description"])
print("Número de estrelas:", data["stargazers_count"])