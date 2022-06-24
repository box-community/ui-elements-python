from flask import Flask, render_template,request,jsonify
from dotenv import load_dotenv
import os

import explorer

app = Flask(__name__)

load_dotenv()
token = os.getenv('DEVELOPER_TOKEN')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/event/', methods=['POST'])
def event():
    request_data = request.get_json()
    print(request_data)
 
    return 'OK'

@app.route('/explorer/')
def explorer_page():
    return explorer.explorer(token=token)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)