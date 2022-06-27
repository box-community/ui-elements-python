from typing import Collection
from flask import Flask, render_template


def previewer(active_page, token,file_id,file_list=[]):
    token = token
    file_id = file_id

    options = {
        'container': '.previewer',
        'header': 'light',
        'logoUrl':'',

        'collection': file_list,

        'showAnnotations': False,
        'showDownload': True,

    }

    isSingle = True if len(file_list) == 0 else False

    return render_template('previewer.html',active_page=active_page, token=token, file_id=file_id, options=options, isSingle = isSingle)
