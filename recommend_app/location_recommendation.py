from flask import Flask, jsonify
from random import choice

app = Flask(__name__)

def get_truck_gps():
  # Should be from SF data API - https://data.sfgov.org/Permitting/Mobile-Food-Facility-Permit/rqzj-sfat
  possible_gps_locations = [{"Longitude": -122.4041544, "Latitude": 37.70937546},
                            {"Longitude": -122.4714119, "Latitude": 37.71000333},
                            {"Longitude": -122.4552219, "Latitude": 37.71019302},
                            {"Longitude": -122.3961491, "Latitude": 37.71045169},
                            {"Longitude": -122.3996426, "Latitude": 37.71045169},
                            {"Longitude": -122.4027845, "Latitude": 37.71083793},
                            {"Longitude": -122.3900163, "Latitude": 37.71084128},
                            {"Longitude": -122.4316442, "Latitude": 37.71093379},
                            {"Longitude": -122.3899379, "Latitude": 37.71163228},
                            {"Longitude": -122.3899379, "Latitude": 37.7123026},
                            {"Longitude": -122.3895991, "Latitude": 37.716443},
                            {"Longitude": -122.3961491, "Latitude": 37.716443},
                            {"Longitude": -122.3935434, "Latitude": 37.71699129 }]

  return choice(possible_gps_locations)

def get_truck_name():
  # Should be from SF data API - https://data.sfgov.org/Permitting/Mobile-Food-Facility-Permit/rqzj-sfat
  # And wrapped in truck class ;)
  possible_names = ["Grillenium Falcon", "Grill 'Em All", "Burger She Wrote", "Bon Me", "Dogzilla"]
  
  return choice(possible_names)

def get_locations():
  
  weather_options_game = ["Sunny", "Sunny", "Partly Cloudy", "Partly Cloudy", "Cloudy"]
  weather_options_other = ["Sunny", "Partly Cloudy", "Partly Cloudy", "Cloudy", "Rainy"]

  food_trucks = {"Food_Trucks": 
           [{"Food_Truck": {"Position": get_truck_gps(),
                            "Name": get_truck_name()}},
            {"Food_Truck": {"Position": get_truck_gps(),
                            "Name": get_truck_name()}},
            {"Food_Truck": {"Position": get_truck_gps(),
                            "Name": get_truck_name()}},
            {"Food_Truck": {"Position": get_truck_gps(),
                            "Name": get_truck_name()}},
            {"Food_Truck": {"Position": get_truck_gps(),
                            "Name": get_truck_name()}}
            ],
       "Suggestion_Location_Primary": {"Position": {"Longitude": -122.2321, "Latitude": 37.4643},
                                       "Event": {"Name": "SF Gaints Game",
                                                 "Position": {"Longitude": -122.2321, "Latitude": 37.4643}},
                                       "Weather": choice(weather_options_game)},
       "Suggestion_Location_Secondary": {"Position": {"Longitude": -122.4297, "Latitude": 37.8078},
                                       "Event": {"Name": "Off the Grid",
                                                 "Position": {"Longitude": -122.4297, "Latitude": 37.8078,}},
                                       "Weather": choice(weather_options_other)}
          }

  resp = jsonify(food_trucks)
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.route('/date=<int:epoch_date>', methods = ['GET'])
def location_recommendation(epoch_date):
    if len(str(epoch_date)) > 12:
      return get_locations()
    else:
      not_found()

if __name__ == '__main__':
    app.run(debug = True)