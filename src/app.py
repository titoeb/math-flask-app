from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from typing import Dict, Tuple

# Build the app
app = Flask(__name__)
api = Api(app)

# Additional helper functions

def parse_data(postedData: Dict, method:str) -> Tuple[int, int, Dict]:
    # No matter which method is called, all need at least x and y.
    if "x" not in postedData or "y" not in postedData:
        return(None, None, {
            "Message": "X or Y is missing from the posted data!", 
            "Status Code": 301})

    if method=="divide":
        if int(postedData["y"]) == 0:
            return(None, None, {
                    "Message": "Y cannot be 0.",
                    "Status Code": 302})

    return(int(postedData["x"]),  int(postedData["y"]), {"Status Code": 200})

# Define the resources
class Add(Resource):
    def post(self):
        # Extract data.
        x, y, retJson = parse_data(request.get_json(), "add")
        
        # Step 4: Add the two numbers
        if (retJson["Status Code"] == 200):
            retJson["Message"]  = x+y
        
        # Step 5: Return the results 
        return jsonify(retJson)

class Subtract(Resource):
    def post(self):
        # Extract data.
        x, y, retJson = parse_data(request.get_json(), "subtract")
        
        # Step 4: Add the two numbers
        if (retJson["Status Code"] == 200):
            retJson["Message"]  = x-y
        
        # Step 5: Return the results 
        return jsonify(retJson)

class Multiply(Resource):
    def post(self):
        # Extract data.
        x, y, retJson = parse_data(request.get_json(), "multiply")
        
        # Step 4: Add the two numbers
        if (retJson["Status Code"] == 200):
            retJson["Message"]  = float(x)*y
        
        # Step 5: Return the results 
        return jsonify(retJson)

class Divide(Resource):
    def post(self):
        # Extract data.
        x, y, retJson = parse_data(request.get_json(), "divide")
        
        # Step 4: Add the two numbers
        if (retJson["Status Code"] == 200):
            retJson["Message"]  = float(x)/y
        
        # Step 5: Return the results 
        return jsonify(retJson)

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

if __name__ == "__main__":
    	app.run(debug=True)
