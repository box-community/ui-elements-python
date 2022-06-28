import json
from flask import Flask,request
from dotenv import load_dotenv
import os

import explorer,previewer,sidebar,uploader

app = Flask(__name__)

load_dotenv()
token = os.getenv('DEVELOPER_TOKEN')
previewer_file_id = os.getenv('PREVIEWER_FILE_ID')
previewer_file_list = os.getenv('PREVIEWER_FILE_LIST').split(',')
uploader_folder_id = os.getenv('UPLOADER_FOLDER_ID')

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

@app.route('/previewer-multi-sidebar/')
def previewer_page_multi_sidebar():
    return previewer.previewer(active_page='previewer-multi-sidebar',token=token,file_id=previewer_file_list[0],file_list=previewer_file_list)     

@app.route('/sidebar/')
def sidebar_page():
    return sidebar.sidebar(active_page='sidebar',token=token,file_id=previewer_file_id)

@app.route('/uploader/')
def uploader_page():
    return uploader.uploader(active_page='uploader',token=token,folder_id=uploader_folder_id)

@app.route('/uploader-popup/')
def uploader_popup_page():
    return uploader.uploader(active_page='uploader-popup',token=token,folder_id=uploader_folder_id,isPopup=True)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)