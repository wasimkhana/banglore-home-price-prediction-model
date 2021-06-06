from flask import jsonify
import util
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
get_location_names()
