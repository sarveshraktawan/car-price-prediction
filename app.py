from flask import Flask, render_template,jsonify,request
import pandas as pd
import pickle
app = Flask(__name__)

@app.route("/")

def home():
    return render_template('home.html')
@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method=='POST':
        make=request.form.get("make")
        model=request.form.get("model")
        engine_cylinders=request.form.get("cylinders")
        driven_wheels=request.form.get("wheels")
        print(make,model,engine_cylinders,driven_wheels)
        df=pd.read_json("new.json")
        Make=df["Make_encode"][df['Make']==make].values[0]
        Model=df["Model_encode"][df['Model']==model].values[0]
        Driven_wheels=df["Driven_Wheels_encode"][df['Driven_Wheels']==driven_wheels].values[0]
        with open('model.pkl', 'rb') as mod:
            mlmodel = pickle.load(mod)

        predit = mlmodel.predict([[Model,Make,float(engine_cylinders),Driven_wheels]])

        return render_template('predicted.html',predicted_value=predit[0])
        
    else:
        return render_template("predict.html")
   

 

if __name__=='__main__':
    app.run()



