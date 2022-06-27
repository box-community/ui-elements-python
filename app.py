import json
from flask import Flask, render_template,request,jsonify
from dotenv import load_dotenv
import os

import explorer,previewer

app = Flask(__name__)

load_dotenv()
token = os.getenv('DEVELOPER_TOKEN')
previewer_file_id = os.getenv('PREVIEWER_FILE_ID')
previewer_file_list = os.getenv('PREVIEWER_FILE_LIST').split(',')
##previewer_file_list = ['962025725719','960391244732','962024331798','962023145830']
print(previewer_file_list)

@app.route('/')
def index_page():
    return explorer.explorer(active_page='explorer',token=token)

@app.route('/event/', methods=['POST'])
def event():
    request_data = request.get_json()
    print('***********************************************************')
    print(request_data)
    print('***********************************************************')
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/explorer/')
def explorer_page():
    return explorer.explorer(active_page='explorer',token=token)

@app.route('/previewer-single/')
def previewer_page_single():
    return previewer.previewer(active_page='previewer-single',token=token,file_id=previewer_file_id)

@app.route('/previewer-multi/')
def previewer_page_multi():
    return previewer.previewer(active_page='previewer-multi',token=token,file_id=previewer_file_list[0],file_list=previewer_file_list)    


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)