from flask import render_template

def picker(active_page, token, folder_id = 0,isPopup=False):
    token = token
    folder_id = folder_id

    if isPopup:
        modal = {   
            'buttonLabel': 'Open modal to select your files',
            'buttonClassName': 'btn-primary',
            'modalClassName': 'picker-modal',
            'overlayClassName': 'picker-overlay',
        }
    else:
        modal = None

    if active_page=='picker-pdf':
        extensions = ['pdf']
    else:
        extensions = []

    options = {
        'container': '.picker',

        'sortBy': 'name',
        'sortDirection': 'ASC',

        'logoUrl': 'box',
        'defaultView': 'files',

        'chooseButtonLabel': 'Choose',
        'cancleButtonLabel': 'Cancel',


        'extensions': extensions,

        'maxSelectable': 10,

        'canUpload': True,
        'canShareAccess': True,
        'canCreateNewFolder': True,
        
        'modal': modal,
    }

    return render_template('picker.html', active_page=active_page, token=token, folder_id=folder_id, options=options)
