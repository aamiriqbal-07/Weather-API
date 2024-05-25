from flask import Flask, jsonify, request
import yaml
from weather_api import WeatherAPI
from constants import JSON_FORMAT, YAML_FORMAT, BAD_REQUEST, INTERNAL_SERVER_ERROR

app = Flask(__name__)
weather_api = WeatherAPI()

@app.route('/api/v1/getCurrentWeather', methods=['POST'])
def get_current_weather():
    data = request.get_json()
    city = data.get('city')
    output_format = data.get('output_format', JSON_FORMAT)

    weather_info = weather_api.get_weather(city)
    if weather_info:
        if output_format == JSON_FORMAT:
            return jsonify(weather_info)
        elif output_format == YAML_FORMAT:
            return yaml.dump(weather_info, default_flow_style=False)
        else:
            return jsonify({"error": f"Invalid output format. Please choose {JSON_FORMAT} or {YAML_FORMAT}."}), BAD_REQUEST 
    else:
        return jsonify({"error": "Failed to fetch weather data for the specified city."}), INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    app.run(debug=True)
