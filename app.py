# from crypt import methods
from flask import Flask, render_template, url_for, request, redirect
import pickle
import pandas as pd



app = Flask(__name__)
# load the model
model = pickle.load(open('Random Forest Regression Model.pkl', 'rb'))


# create default route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buy')
def Buy():
        return render_template('tables.html')

# create predict route
@app.route('/predict', methods=['POST'])
def predict():
    output = 0
   
    if request.method == 'POST':
        Kms=int(request.form['Kms_Driven'])
        ow = int(request.form['Owner'])
        Engine = int(request.form['Engine_CC'])
        Power = int(request.form['Power'])
        Mileage = int(request.form['Mileage'])
        Seats = int(request.form['Seats'])
        fuel = request.form.get('Fuel_Type')
        if (fuel == 'Petrol'):
            Fuel_Type = 1
        elif (fuel == 'Diesel'):
            Fuel_Type = 2
        elif(fuel=='CNG') :
            Fuel_Type = 3
        else:
            Fuel_Type=0
        trans = request.form['Transmission_Mannual']
        if trans == 'Manual':
            Transmission_Manual = 1
        else:
            Transmission_Manual = 0

        age = 2020-int(request.form['Year'])

        output = model.predict([[ Kms, ow, Fuel_Type,Engine,Mileage,Seats,Power,
                                Transmission_Manual, age]])
        output=round(output[0],2)
                      

        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {} lakhs".format(output))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 

   



#    For Future reference
{
# @app.route('/buydata', methods=['POST'])
# def buydata(): 

#     if request.method == 'POST':
       
#         minage = int(request.form['minYear'])
#         maxage = int(request.form['minYear'])
#         Seats = int(request.form['Seats'])  
       
#         minEngine = int(request.form['minEngine_CC'])
#         maxEngine = int(request.form['maxEngine_CC'])

#         minPower = int(request.form['minPower'])
#         maxPower = int(request.form['maxPower'])

#         minMileage = int(request.form['minMileage'])
#         maxMileage = int(request.form['maxMileage'])

#         fuel = request.form.get('Fuel_Type')
#         if (fuel == 'Petrol'):
#             Fuel_Type = 1
#         elif (fuel == 'Diesel'):
#             Fuel_Type = 2
#         elif(fuel=='CNG') :
#             Fuel_Type = 3
#         else:
#             Fuel_Type=0

#         trans = request.form['Transmission_Mannual']
#         if trans == 'Manual':
#             Transmission_Manual = 1
#         else:
#             Transmission_Manual = 0

#         cd=pd.read_csv('data.csv')
#         def resultTable (minage ,maxage ,mineng ,maxeng ,minpow ,maxpow ,minmil ,maxmil ,trans ,seats ,fueltype ):
#             final_dataset=cd[(cd['Year']>=minage)&(cd['Year']<maxage)&(cd['Engine CC']>=mineng)&(cd['Engine CC']<maxeng)&(cd['Power']>minpow)&(cd['Power']<maxpow)&(cd['Mileage Km/L']>minmil)&(cd['Mileage Km/L']<maxmil)&(cd['Transmission']==trans)&(cd['Seats']==seats)&(cd['Fuel_Type']==fueltype)] 
#             df=pd.DataFrame(final_dataset,columns=['Name', 'Manufacturer', 'Owner_Type', 'Price'])
#             # print(df.shape)
#             print(df)

#         resultTable(minage , maxage ,minEngine,maxEngine,minPower,maxPower ,minMileage,maxMileage, Transmission_Manual,Seats ,Fuel_Type)
#         # resultTable( 10 , 20 ,25,600,15,70 ,15,25, "Manual",5 ,"CNG")


#         return render_template('buy.html')
                   
}
