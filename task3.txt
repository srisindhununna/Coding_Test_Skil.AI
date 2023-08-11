#from flask import Flask,request,jsonify
#import pandas as pd
#app=Flask(__name__)
#data=pd.read_csv("task1.csv")
#@app.route('/My_City/<city_name>',methods=['GET'])
#def get_city_data(city_name):
#    city_data=[entry for entry in data if entry['My_City']==city_name]
#    return jsonify(city_data)
#if __name__=='__main__':
#    app.run(debug=True)

from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/hello World',methods=['GET'])

def helloworld():
    if(request.method=='GET'):
        data="Hello World"
        return jsonify(data)
if __name__=='__main__':
    app.run(debug=True)
##rjy as input
##prompt as rjy