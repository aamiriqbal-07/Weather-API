# WeatherAPI

## Overview
WeatherAPI is a Python Flask application that provides current weather information for a given city. It integrates with an external weather API to fetch real-time weather data and returns the information in JSON or YAML format.

## Features
- Fetches current weather data for a specified city.
- Supports output formats: JSON and YAML.
- Easy setup and configuration using environment variables.
- Modular code structure for easy maintenance and extensibility.

## Prerequisites
Before running the WeatherAPI, ensure you have the following installed:
- Python 3.x
- Flask
- Python-dotenv (for handling environment variables)
- Requests (for making HTTP requests)

## Setup
1. Clone the repository to your local machine:
   ```
   git clone <repository-url>
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project directory and add the following environment variables:
   ```
   WEATHER_API_URL=<weather-api-url>
   WEATHER_API_KEY=<weather-api-key>
   WEATHER_API_HOST=<weather-api-host>
   ```
   Replace `<weather-api-url>`, `<weather-api-key>`, and `<weather-api-host>` with the appropriate values from your weather API provider.

## Usage
1. Run the Flask application:
   ```
   python app.py
   ```
2. Make a POST request to the `/api/v1/getCurrentWeather` endpoint with the following payload:
   ```json
   {
       "city": "CityName",
       "output_format": "json"
   }
   ```
   Replace `CityName` with the name of the city for which you want to fetch weather data.
3. Optionally, you can specify the output format as `json` or `yml` in the `output_format` field.

## Example
Here's an example of making a POST request using cURL:
   ```
   curl -X POST http://127.0.0.1:5000/api/v1/getCurrentWeather \
     -H "Content-Type: application/json" \
     -d '{"city": "Bangalore", "output_format": "json"}'
   ```

## License
This project is licensed under the [MIT License](LICENSE).
