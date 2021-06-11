#Import Libraries
from flask import Flask, request, render_template
 
import model # load model.py
 
app = Flask(__name__)
 
# render htmp page
@app.route('/')
def home():
    return render_template('index.html')
 
# get user input and the predict the output and return to user
@app.route('/predict',methods=['POST'])
def predict():
     
    #take data from form and store in each feature    
    input_features = [x for x in request.form.values()]
    BHK = input_features[0]
    Bathroom = input_features[1]
    Parking = input_features[2]
    Area = input_features[3]
    Per_Sqft = input_features[4]
    Furnishing = input_features[5]
    Status = input_features[6]
    Transaction = input_features[7]
    Type = input_features[8]
    Locality = input_features[9]
     
    # predict the price of house by calling model.py     
    predicted_price = model.predict_house_price(BHK,Bathroom,Parking,Area,Per_Sqft,Furnishing,Status, Transaction,Type,Locality) 
 
    # render the html page and show the output
    return render_template('index.html', prediction_text='Predicted Price of the House is {} Lakhs'.format(predicted_price))
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
     
#if __name__ == "__main__":
#  app.run()
    