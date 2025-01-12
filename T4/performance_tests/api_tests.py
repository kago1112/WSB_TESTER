import requests

url = "https://www.interia.pl/"

print("Wysylamy zapytanie GET do:", url)

response = requests.get(url)

print("Otrzymaliśmy odpowiedz o statusie:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("Zawartosc strony to:", data)
else:
    print("Nie udalo sie pobrac danych ze strony/API")