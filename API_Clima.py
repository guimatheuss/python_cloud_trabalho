import requests
# API CLIMA CURITIBA
url_curitiba = "https://api.open-meteo.com/v1/forecast?latitude=-25.4296&longitude=-49.2713&current_weather=true"
resp_curitiba = requests.get(url_curitiba)
clima_curitiba = resp_curitiba.json()

print("Cidade: Curitiba")
print("Temperatura atual:", clima_curitiba["current_weather"]["temperature"], "°C")
print("Velocidade do vento:", clima_curitiba["current_weather"]["windspeed"], "km/h")
print()

url_sp = "https://api.open-meteo.com/v1/forecast?latitude=-23.5505&longitude=-46.6333&current_weather=true"
resp_sp = requests.get(url_sp)
clima_sp = resp_sp.json()

print("Cidade: São Paulo")
print("Temperatura atual:", clima_sp["current_weather"]["temperature"], "°C")
print("Velocidade do vento:", clima_sp["current_weather"]["windspeed"], "km/h")