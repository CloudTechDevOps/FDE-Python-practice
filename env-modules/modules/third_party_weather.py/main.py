import requests #requests is a third-party module that allows you to send HTTP requests easily. It is not included in the standard library, so you need to install it separately using pip.

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)

data = response.json()
current = data["current_condition"][0]
print(current["temp_C"])

current = data["current_condition"][0]

print("City:", city)
print("Temperature:", current["temp_C"], "°C") #Temperature in Celsius, It represents the actual current air temperature of a city.
print("Feels Like:", current["FeelsLikeC"], "°C") #It represents how hot or cold the weather feels to the human body, rather than just the actual air temperature.
print("Weather:", current["weatherDesc"][0]["value"]) #Weather Description.#It tells us the current weather condition in words.
