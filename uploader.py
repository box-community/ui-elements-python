from flask import render_template

def uploader(active_page, token, folder_id,isPopup=False):
    token = token
    folder_id = folder_id

    if isPopup:
        modal = {   
            'buttonLabel': 'Open modal to upload you files',
            'buttonClassName': 'btn-primary',
            'modalClassName': 'upload-modal',
            'overlayClassName': 'upload-overlay',
        }
    else:
        modal = None

    options = {
        'container': '.uploader',
        'fileLimit': 100,

        'modal': modal,
    }

    return render_template('uploader.html', active_page=active_page, token=token, folder_id=folder_id, options=options)
