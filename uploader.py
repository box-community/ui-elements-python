from flask import render_template

def uploader(active_page, token, folder_id):
    token = token
    folder_id = folder_id

    modal = {
        'buttonLabel': 'Upload',
        'buttonClassName': 'btn-primary',
        'modalClassName': 'upload-modal',
        'overlayClassName': 'upload-overlay',
    }

    options = {
        'container': '.uploader',
        'fileLimit': 100,
    }

    return render_template('uploader.html', active_page=active_page, token=token, folder_id=folder_id, options=options)
