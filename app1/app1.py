import json
from flask import Flask, request
from model_code.main import *
print("flask_log: IMPORTED")

app1 = Flask(__name__)

@app1.route('/')
def hello_world():
   return 'Rohan Lal Kshetry, this is App1 :) '

@app1.route('/test1')
def get_cn():
    if request.method=='GET':
       api_inp=request.args.get('input_txt', '')
       print("flask_log input text: "+api_inp+"\n")
       result = {'status1_25':'success','resp':get_resp(api_inp)}
       result = json.dumps(result, indent=4)
    #    print(result)
       return result
    else:
        return "Wrong url/inp"

# http://192.168.0.114:5000/test1?input_txt=star%20hd%20sport
# http://localhost:8080/test1?input_txt=star%20hd%20sport

if __name__ == '__main__':
   app1.run(debug=True, host='0.0.0.0')