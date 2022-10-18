from flask import Flask,render_template,request
import FeatureExtraction
import pickle

app = Flask(__name__, static_url_path='/static')
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")


model1 = pickle.load(open('XGBoostModel_12000.sav', 'rb'))
model2 = pickle.load(open('RFmodel_12000.sav', 'rb'))


@app.route('/getURL',methods=['GET','POST'])
def getURL():
    if request.method == 'POST':
        url = request.form['url']
        # print(url)
        data = FeatureExtraction.getAttributess(url)
        # print(data)
        model1_predicted_value = model1.predict(data)
        #model2_predicted_value = model2.predict(data)
        print('******************************************************************')
        #print (model2_predicted_value)
        #print(predicted_value)
        
        if model1_predicted_value == 0:    
            value = "This URL is Legitimate"
            return render_template("home.html",error=value)
        else:
            value = "This URL is Phishing"
            return render_template("home.html",error=value)

if __name__ == "__main__":
    app.run(debug=True)