from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('extra_trees_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Rooms = int(request.form['rooms'])
        People = float(request.form['people'])
        Area = float(request.form["area"])
        AirConditioning = request.form["ac"]
        if(AirConditioning == "ac_yes"):
            AirConditioning = 1
        else:
            AirConditioning = 0
        Television = request.form["television"]
        if(Television == "tv_yes"):
            Television = 1
        else:
            Television = 0
        Apartment = request.form["apartment"]
        if(Apartment == "apartment_yes"):
            Apartment = 1
        else:
            Apartment = 0
        Income = int(request.form["income"])
        Children = int(request.form["children"])
        City = request.form["city"]
        if(City == "city_yes"):
            City = 1
        else:
            City = 0
        prediction=model.predict([[Rooms, People, Area, AirConditioning, Television, Apartment, Income, Children, City]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="Your approximate monthly electricity bill will be ${}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
