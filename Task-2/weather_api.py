import requests
import json

print("====================================")
print("       WEATHER API CONSUMER")
print("====================================")

# Get city name from user
name = input("Enter the city name: ").strip()

# -------------------------------
# STEP 1: Find city coordinates
# -------------------------------

geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

geocoding_params = {
    "name": name,
    "count": 1,
    "language": "en",
    "format": "json"
}

try:
    response = requests.get(geocoding_url, params=geocoding_params)
    response.raise_for_status()

    data = response.json()

    # Check whether city was found
    if "results" not in data:
        print("City not found.")
    else:
        city_data = data["results"][0]

        city = city_data["name"]
        country = city_data.get("country", "N/A")
        state = city_data.get("admin1", "N/A")
        latitude = city_data["latitude"]
        longitude = city_data["longitude"]

        print("\n========== LOCATION ==========")
        print("City:", city)
        print("State:", state)
        print("Country:", country)
        print("Latitude:", latitude)
        print("Longitude:", longitude)

        # -------------------------------
        # STEP 2: Get weather information
        # -------------------------------

        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()

        # -------------------------------
        # STEP 3: Extract weather data
        # -------------------------------

        current = weather_data["current"]

        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]

        print("\n========== CURRENT WEATHER ==========")
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Wind Speed:", wind_speed, "km/h")

        # -------------------------------
        # STEP 4: Friendly summary
        # -------------------------------

        print("\n========== WEATHER SUMMARY ==========")
        print(
            f"Current weather in {city}, {country}: "
            f"{temperature}°C, "
            f"Humidity {humidity}%, "
            f"Wind Speed {wind_speed} km/h."
        )

except requests.exceptions.RequestException as e:
    print("Error connecting to the API:", e)

except (KeyError, IndexError):
    print("Unexpected data received from the API.")
