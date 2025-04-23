import requests

api_key = "750635eec70fd16a4046f77ad926d593"
city = "pune"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

print(response.status_code)
print(response.json())
