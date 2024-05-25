class ResponseMapper:
    @staticmethod
    def map_response(current, location):
        mapper = {
            "temp_c": "Weather",
            "lat": "Latitude",
            "lon": "Longitude",
            "name": "City",
        }
        mapped_data = {}
        for key, value in mapper.items():
            if key in current:
                mapped_data[value] = current[key]
            elif key in location:
                if key == "name" and "country" in location:
                    mapped_data[value] = f"{location[key]} {location['country']}"
                else:
                    mapped_data[value] = location[key]
        return mapped_data
