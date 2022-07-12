# Getting started with Box UI Elements using Python & Flask

## Pre-requisites

Follow the instructions on the medium article:

[Getting started with Box UI Elements using Python & Flask (Part 1)](https://medium.com/@barbosa-rmv/getting-started-with-box-ui-elements-using-python-flask-part-1-922f47299fd)

## Installation

> Get the code
```bash
$ git clone git@github.com:barduinor/ui-elements-python.git
$ cd ui-elements-python
```

> Set up your virtual environment
```bash
$ python3.10 -m venv venv
$ source ./venv.bin/activate
```

> Create your application environment
```bash
$ cp .env.example .env
```

> Edit your .env file and fill in the information
```
DEVELOPER_TOKEN=YOUR_DEVELOPER_TOKEN_GOES_HERE
PREVIEWER_FILE_ID= YOUR_PREVIEWER_FILE_ID_GOES_HERE
PREVIEWER_FILE_LIST=Multiple,File,ids,comma,separated,no,spaces
UPLOADER_FOLDER_ID=YOUR_UPLOADS_FOLDER_ID_GOES_HERE
```

> Set up the environment variables and start the server
```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

> Point your browser to the server (e.g http://127.0.0.1:5000)
>Inspect you browser console to see the javascript event.
>Server events will be prited on the terminal.

