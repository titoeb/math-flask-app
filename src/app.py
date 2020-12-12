from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from typing import Dict

# Build the app
app = Flask(__name__)
api = Api(app)

# Additional helper functions
def check_posted_data(postedData: Dict, method: str):

	# No matter which method is called, all need at least x and y.
	if "x" not in postedData or "y" not in postedData:
		return {
		"Message": "X or Y is missing from the posted data!", 
		"Status Code": 301}
	else:
		return {"Status Code": 200}

# Define the resources
class Add(Resource):
	def post(self):
		# Step 1: Get posted data
		postedData = request.get_json()
		
		# Step 2: Varify validity of posted data	
		retJson = check_posted_data(postedData, "add")
		if (retJson["Status Code"] != 200):
		    return jsonify(retJson)

		# Step 3: Parse posted data
		x = int(postedData["x"])
		y = int(postedData["y"])

		# Step 4: Add the two numbers
		retJson["Message"]  = x+y
		
		# Step 5: Return the results 
		return jsonify(retJson)

# class Subtract(__name__):
#	pass
# class Multipy(__name__):
# 	pass
# class Divide(__name__):
# pass

api.add_resource(Add, "/add")

if __name__ == "__main__":
    	app.run(debug=True)
