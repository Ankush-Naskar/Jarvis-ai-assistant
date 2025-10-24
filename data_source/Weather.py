# import asyncio
import python_weather
from datetime import datetime, timedelta
import statistics
import User_info
# from jarvis_system.speak_system import speak

user_location = User_info.LOCATION_FOR_WEATHER

# =======================
# Current weather report
# =======================

async def get_current_weather(location=user_location):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        try:
            weather = await client.get(location)
            Direction =  weather.wind_direction
            
            speech = (f"Currently in {location}, the temperature is {weather.temperature}°C with {weather.description} weather."
                  f" Wind speed is {weather.wind_speed} km/h from the {Direction},"
                  f" visibility is {weather.visibility} km, and atmospheric pressure is {weather.pressure} mb.")
            
            return (speech)

        except Exception as e:
            return(f"Error fetching current weather: {str(e)}")

# =========================
# Date wise weather report
# =========================

async def get_weather_by_date(location, target_date):
    # Convert string to date object if needed
    if isinstance(target_date, str):
        target_date = datetime.strptime(target_date, '%Y-%m-%d').date()
    
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        try:
            weather = await client.get(location)
            
            # Find the matching date in forecasts
            for daily in weather.daily_forecasts:
                if daily.date == target_date:

                    # Extract all hourly wind speeds and pressures
                    wind_speeds = [hour.wind_speed for hour in daily.hourly_forecasts if hour.wind_speed is not None]
                    pressures = [hour.pressure for hour in daily.hourly_forecasts if hour.pressure is not None]

                    # Compute averages
                    avg_wind = statistics.mean(wind_speeds) if wind_speeds else None
                    avg_pressure = statistics.mean(pressures) if pressures else None

                    speech = (f"In {location}, average temperature is expected to be {daily.temperature}°C"
                        f" with a high of {daily.highest_temperature}°C and low of {daily.lowest_temperature}°C."
                        f" The average wind speed is expected to be {avg_wind:.1f} km/h, with average atmospheric pressure of {avg_pressure:.1f} mb. ")
                    
                    
                    
                    
                    
                    # Determine day type
                    conditions = [hourly.description for hourly in daily.hourly_forecasts]
                    if any('rain' in c.lower() for c in conditions):
                        weather_warning = "and rain is expected. Please consider carrying an umbrella just in case."
                    elif any('cloud' in c.lower() for c in conditions):
                        weather_warning = "and skies are expected to remain mostly cloudy, with occasional overcast periods."
                    elif any('thunderstorm' in c.lower() for c in conditions):
                        weather_warning = "and thunderstorms are possible, so staying indoors during storm hours would be safest." 
                    elif any('fog' in c.lower() for c in conditions):
                        weather_warning = "and fog may develop in the early morning or night, which could reduce visibility."  
                    elif any('mist' in c.lower() for c in conditions):
                        weather_warning = "and mist may form in low-lying areas, especially around dawn or dusk." 
                    else:
                        weather_warning = "and it is expected to be sunny with mostly clear skies."  

                    if avg_wind >= 40:
                        weather_warning1 = "and strong winds are expected."  
                    elif avg_wind >= 30:
                        weather_warning1 = "and it may be a windy day with noticeable gusts." 
                    else:
                        weather_warning1 = "" 

                    return speech + " " + weather_warning + " " + weather_warning1

        except Exception as e:
            return(f"Weather data not available for {target_date}"
                f"Note: Weather forecasts are typically available for the next 7-14 days.")

