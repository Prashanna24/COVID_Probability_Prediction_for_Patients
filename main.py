from flask import Flask,render_template,request
app = Flask(__name__)
import pickle


file = open('clf.pkl','rb')
clf = pickle.load(file)
file.close()

@app.route('/',methods=["GET","POST"])
def hello_world():
	if request.method == "POST":
		mydata = request.form
		bodyTemp = int(mydata['bodyTemp'])
		bodyPain = int(mydata['bodyPain'])	
		runnyNose = int(mydata['runnyNose'])
		diffBreath = int(mydata['diffBreath'])
		o2Saturation = int(mydata['o2Saturation'])
		travelHistory = int(mydata['travelHistory'])
		age = int(mydata['age'])
		LossofTasteSmell = int(mydata['LossofTasteSmell'])
		vomiting = int(mydata['vomiting'])
		Diarrhea = int(mydata['Diarrhea'])
	    
		
	
		
		inputFeatures = [bodyTemp,bodyPain,runnyNose,diffBreath,o2Saturation,travelHistory,age,LossofTasteSmell,vomiting,Diarrhea]
		data_list = [[bodyTemp,bodyPain,runnyNose,diffBreath,o2Saturation,travelHistory,age,LossofTasteSmell,vomiting,Diarrhea]]
		predict_status = clf.predict(data_list)[0]
		print(predict_status)
		if predict_status == 1:
			prediction = "Positive"
		else:
			prediction = "Negative"
		infProb = clf.predict_proba([inputFeatures])[0][1]
		return render_template('show.html',prediction=prediction,inf=round((infProb)*100))
	return render_template('index.html')

@app.route('/contactus')
def contactus():
	return render_template('contactus.html')

if __name__ == '__main__':
	app.run(debug=True)