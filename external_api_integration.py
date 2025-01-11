import requests

def fetch_weather(city):
    api_key = "your_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Make an API call to get weather data
    params = {"q": city, "appid": api_key}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data['weather'][0]['description']
    else:
        return "Failed to retrieve weather data."

# Example usage
city = "London"
weather = fetch_weather(city)
print(f"Weather in {city}: {weather}")
