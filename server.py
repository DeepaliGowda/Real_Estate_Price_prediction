#creating hhtp server

import util


from flask import Flask, request, jsonify
app = Flask(__name__)

# @app.route('/hello')  #obtained server for ex:http://127.0.01:5000/hello you get "Hi"
# def hello():
#     return "Hi"

@app.route('/get_location_names',methods=['GET'])
def  get_location_names(): #returning a reponse which contains all location
    response= jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods=['GET','POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__ == "__main__":
    print("Staring python flask server for home price prediction")
    util.load_saved_artifacts()
    app.run()