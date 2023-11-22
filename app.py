from flask import Flask, render_template,jsonify,request

app = Flask(__name__)

@app.route("/")

def home():
    return render_template('home.html')
@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method=='POST':
        make=request.form.get("make")
        model=request.form.get("model")
        year=request.form.get("year")
        engine_fuel_type = request.form.get("engine_fuel_type")
        engine_hp=request.form.get("engine_hp")
        engine_cylinders=request.form.get("engine_cylinders")
        transmission_type=request.form.get("transmission_type")
        driven_wheels=request.form.get("driven_wheels")
        number_of_doors=request.form.get("number_of_doors")
        vehicle_size=request.form.get("vehicle_size")
        vehicle_style=request.form.get("vehicle_style")
        highway_mpg=request.form.get("highway_mpg")
        city_mpg=request.form.get("city_mpg")
        popularity=request.form.get("popularity")
        print(make,model,year,engine_fuel_type,engine_hp,engine_cylinders,transmission_type,driven_wheels,number_of_doors,vehicle_size,vehicle_style,highway_mpg,city_mpg,popularity)
        return jsonify({'status':'data fetched successfully'})
    else:
        return render_template("predict.html")
    return render_template('predict.html')


 

if __name__=='__main__':
    app.run()



