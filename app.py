import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] == 200:
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Description: {desc}")
    else:
        print("Error fetching data.")

def main():
    api_key = "YOUR_API_KEY"
    city = input("Enter city name: ")
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
